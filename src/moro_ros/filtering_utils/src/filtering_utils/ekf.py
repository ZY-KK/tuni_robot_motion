#!/usr/bin/env python
import numpy as np
from math import atan2
from numpy.random import randn


class EKF:
    def __init__(self, state_vector_size, control_size, measurement_size):
        #self.state_vector = np.zeros(state_vector_size)
        self.state_vector = np.zeros(state_vector_size)
        #self.next_state = np.zeros((state_vector_size, 1))
        
        self.cov_matrix = 1000. * np.identity(state_vector_size)
        self.q = np.zeros((control_size, control_size))
        self.R = np.zeros((measurement_size, measurement_size))
        self.motion_j_state = np.zeros((state_vector_size, state_vector_size))
        self.motion_j_noise = np.zeros((state_vector_size, control_size))
        self.obs_j_state = np.zeros((measurement_size, state_vector_size))
        self.Q = np.zeros((state_vector_size, state_vector_size))
        self.t = 0

    def predict(self, control_vector):
        # X_next
        self.propagate_state(
            self.state_vector[0], self.state_vector[1], self.state_vector[2], control_vector[0], control_vector[1])
        # F
        self.motion_jacobian_state_vector(
            self.state_vector[0], self.state_vector[1], self.state_vector[2], control_vector[0], control_vector[1])
        # V
        self.motion_jacobian_noise_components(
            self.state_vector[0], self.state_vector[1], self.state_vector[2], control_vector[0], control_vector[1])
        
        
        
        self.calculate_cov()
        

    def update(self, lmark, m_x, m_y, a):
        # H
        self.observation_jacobian_state_vector(
            self.state_vector[0], self.state_vector[1], self.state_vector[2], lmark[0], lmark[1])
        
        PHT = np.dot(self.cov_matrix, self.obs_j_state.T)
        S = np.dot(np.dot(self.obs_j_state, self.cov_matrix), self.obs_j_state.T) +self.R
        K = PHT.dot(np.linalg.inv(S))
        z = np.array([np.sqrt(m_x**2+m_y**2), a])
        hx = self.hx(self.state_vector[0], self.state_vector[1], self.state_vector[2], lmark[0], lmark[1])
        #y = self.residual(z, hx)
        y = z-hx
        self.state_vector = self.state_vector+np.dot(K, y)
        self.cov_matrix = np.dot(
            (np.eye(self.obs_j_state.shape[1])-np.dot(K, self.obs_j_state)), self.cov_matrix)
        pass

    def hx(self, x, y, theta, m_x, m_y):
        dist = np.sqrt((m_x-x)**2+(m_y-y)**2)
        Hx = np.array([dist, atan2(m_y-y, m_x-x)-theta])
        return Hx

    def propagate_state(self, x, y, theta, v, w):
        
        self.state_vector[0] = x + (-v/w)*np.sin(theta)+(v/w)*np.sin(theta+w*self.t)
        self.state_vector[1] = y + (v/w)*np.cos(theta)-(v/w)*np.cos(theta+w*self.t)
        self.state_vector[2] = theta + w*self.t
        
        
    def residual(self, a, b):
        y = a - b
        y[1] = y[1] % (2 * np.pi)
        if y[1] > np.pi:
            y[1] -= 2 * np.pi
        return y

    def calculate_cov(self):
        # P = FPF.T+VMV.T
        self.Q = np.dot(np.dot(self.motion_j_noise, self.q), self.motion_j_noise.T)
        self.cov_matrix = np.dot(np.dot(self.motion_j_state, self.cov_matrix), self.motion_j_state.T)+ self.Q #P

    def motion_jacobian_state_vector(self, x, y, theta, v, w):
        # F
        self.motion_j_state[0,:] = np.array(
            [1, 0, (-v/w)*np.cos(theta)+(v/w)*np.cos(theta+w*self.t)])
        self.motion_j_state[1,:] = np.array(
            [0, 1, (-v/w)*np.sin(theta)+(v/w)*np.cos(theta+w*self.t)])
        self.motion_j_state[2,:] = np.array([0, 0, 1])
        pass

    def motion_jacobian_noise_components(self, x, y, theta, v, w):
        # TO DO
        # V
        self.motion_j_noise[0,:] = np.array([(-1/w)*np.sin(theta)+(1/w)*np.sin(theta+w*self.t), (v/w**2)*np.sin(
            theta)-(v/w**2)*np.sin(theta+w*self.t)+(v/w)*np.cos(theta+w*self.t)*self.t])
        self.motion_j_noise[1,:] = np.array([(1/w)*np.cos(theta)-(1/w)*np.cos(theta+w*self.t), (-v/w**2)*np.cos(
            theta)+(v/w**2)*np.cos(theta+w*self.t)+(v/w)*np.sin(theta+w*self.t)*self.t])
        self.motion_j_noise[2,:] = np.array([0, self.t])
        pass

    def observation_jacobian_state_vector(self, x, y, theta, m_x, m_y):
        # To DO
        # H
        self.obs_j_state[0,:] = np.array(
            [(x-m_x)/(np.sqrt((m_x-x)**2+(m_y-y)**2)), (y-m_y)/(np.sqrt((m_x-x)**2+(m_y-y)**2)), 0])
        self.obs_j_state[1,:] = np.array(
            [(m_y-y)/((m_x-x)**2+(m_y-y)**2), -(m_x-x)**2/((m_x-x)**2+(m_y-y)**2), -1])
        pass

    def print_initials(self):
        print("Printing some values")
        print("The initial stated is {}").format(self.state_vector)
        print("The initial cov. matrix is {}").format(self.cov_matrix)
