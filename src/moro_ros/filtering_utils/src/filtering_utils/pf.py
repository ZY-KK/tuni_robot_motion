#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from math import atan2
from numpy.linalg import norm
from numpy.random import randn
from numpy.random import random, uniform
import scipy.stats


class PF:
    def __init__(self, N, landmarks, measure_std_error, control_std_error, state_vector_size):
        self.mean = 0
        self.std = 0
        self.N = N
        self.dt = 0.1
        self.state_vector = np.zeros(state_vector_size)
        self.weights = np.zeros(self.N)
        #self.weights.fill(1./self.N)
        self.particles = np.empty((self.N, 3))
        self.landmarks = landmarks
        #self.R = [measure_std_error, control_std_error]
        self.R = measure_std_error
        # range error
        self.Q = np.diag([0.1])**2
        # input error
        #self.R = np.diag([1.0, np.deg2rad(40.0)])**2 
        

    def create_gaussian_particles(self, mean, std):
        self.particles = np.empty((self.N, 3))
        self.particles[:, 0] = mean[0] + (randn(self.N) * std[0])
        self.particles[:, 1] = mean[1] + (randn(self.N) * std[1])
        self.particles[:, 2] = mean[2] + (randn(self.N) * std[2])
        self.particles[:, 2] %= 2 * np.pi

    def create_uniform_particles(self, x_range, y_range, hdg_range, N):
        self.particles = np.empty((self.N, 3))
        self.particles[:, 0] = uniform(x_range[0], x_range[1], size=N)
        self.particles[:, 1] = uniform(y_range[0], y_range[1], size=N)
        self.particles[:, 2] = uniform(hdg_range[0], hdg_range[1], size=N)
        self.particles[:, 2] %= 2 * np.pi
        
        

    def neff(self, weights):
        return 1. / np.sum(np.square(weights))
        
    def predict(self, u, std, dt=1.):
        #N = len(self.particles)
        self.state_vector[0] += (-u[0]/u[1])*np.sin(self.state_vector[2])+(u[0]/u[1])*np.sin(self.state_vector[2]+u[1]*dt)
        self.state_vector[1] += (u[0]/u[1])*np.cos(self.state_vector[2])-(u[0]/u[1])*np.cos(self.state_vector[2]+u[1]*dt)
        self.state_vector[2] += u[1]*dt

        self.particles[:,0] += (-u[0]/u[1])*np.sin(self.particles[:,2])+(u[0]/u[1])*np.sin(self.particles[:,2]+u[1]*dt)
        self.particles[:,1] += (u[0]/u[1])*np.cos(self.particles[:,2])-(u[0]/u[1])*np.cos(self.particles[:,2]+u[1]*dt)
        self.particles[:,2] += u[1]*dt
        
    def update(self, z, markers):
        self.weights.fill(1.)
        for i, landmark in enumerate(markers):
            distance = np.linalg.norm(self.particles[:, 0:2] - landmark, axis=1)
            self.weights *= scipy.stats.norm(distance, self.R).pdf(z[i])

        self.weights += 1.e-300
        self.weights /= sum(self.weights)
        


    def resample(self):
        
        cumulative_sum = np.cumsum(self.weights)
        cumulative_sum[-1] = 1. # avoid round-off error
        indexes = np.searchsorted(cumulative_sum, random(self.N))

        # resample according to indexes
        self.particles = self.particles[indexes]
        self.weights = self.weights[indexes]
        self.weights /= np.sum(self.weights) # normalize

    def estimate(self):
        """ returns mean and variance """
        
        pos = self.particles[:, 0:3]
        mu = np.average(pos, weights=self.weights, axis=0)
        var = np.average((pos - mu)**2, weights=self.weights, axis=0)
        self.state_vector = mu
        return mu, var