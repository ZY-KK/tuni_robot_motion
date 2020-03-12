# -*- coding: utf-8 -*-
import numpy as np
from math import atan2
from numpy.linalg import norm
from numpy.random import randn
from numpy.random import random, uniform
import scipy.stats
class EKF_SLAM:
    def __init__(self, state_vector_size, control_size, measurement_size, landmarkers_n):
        # F
        self.F = np.hstack((np.eye(state_vector_size), np.zeros((state_vector_size, 3*landmarkers_n))))
        self.P = 1.0 * np.identity(state_vector_size+3*landmarkers_n)
        self.Q = np.zeros((state_vector_size, state_vector_size))
        self.R = np.zeros((state_vector_size, state_vector_size))
        self.j_state = np.zeros((state_vector_size, state_vector_size))
        self.control_vector = np.zeros(control_size)
        self.state_vector = np.zeros(state_vector_size+3*landmarkers_n).T
        self.t = 0
        self.I = np.hstack((1.0*np.eye(state_vector_size), np.zeros((state_vector_size, 3*landmarkers_n))))
        self.z = np.zeros(measurement_size+1)
        self.checked_land = []
        self.N = landmarkers_n
        self.h = np.zeros((state_vector_size, 2*state_vector_size))
    def propagate_state(self, control_vector):
        v = control_vector[0]
        w = control_vector[1]
        theta = self.state_vector[2]
        #print(v, w, theta)
        state_vector_f = np.array([(-v/w)*np.sin(theta)+(v/w)*np.sin(theta+w*self.t), (v/w)*np.cos(theta)-(v/w)*np.cos(theta+w*self.t), w*self.t])
        #print(state_vector_f)
        self.state_vector = self.state_vector+np.dot(self.F.T, state_vector_f.T)
        #print(self.state_vector)

    def predict(self, control_vector):
        self.propagate_state(control_vector)
        v = control_vector[0]
        w = control_vector[1]
        theta = self.state_vector[2]
        j_state = np.array([[0, 0, (v/w)*np.cos(theta)-(v/w)*np.cos(theta+w*self.t)], [0, 0, (v/w)*np.sin(theta)-(v/w)*np.sin(theta+w*self.t)], [0, 0, 0]])
        G = 1.0*np.identity(self.F.shape[1]) + np.dot(np.dot(self.F.T, j_state), self.F)
        #print(G.shape,self.P.shape,  self.F.shape, self.R.shape)
        self.P = np.dot(np.dot(G, self.P), G.T)+np.dot(np.dot(self.F.T, self.Q), self.F)
        
    def update(self, j, m_x, m_y,l_x, l_y, a, s):
        #print(self.state_vector)
        x = self.state_vector[0]
        y = self.state_vector[1]
        theta = self.state_vector[2]
        r = np.sqrt(m_x**2+m_y**2)
        
        if(s not in self.checked_land):
            l_x = x + r*np.cos(a+theta)
            l_y = y = r*np.sin(a+theta)
            s = s
        
    
        q = (l_x-x)**2+(l_y-y)**2
        
        self.z = np.array([np.sqrt(q), np.arctan2((l_y-self.state_vector[1]), (l_x-self.state_vector[0]))-self.state_vector[2], s])
        #print(self.z)
        F_j_part_1 = np.vstack((1.0*np.eye(3), 1.0*np.zeros((3, 3))))
        F_j_part_2 = np.zeros((6, 3*j-3))
        F_j_part_3 = np.vstack((np.zeros((3, 3)), 1.0*np.eye(3)))
        F_j_part_4 = np.zeros((6, 3*self.N-3*j))
        
        F_j = np.hstack((np.hstack((F_j_part_1, F_j_part_2)), np.hstack((F_j_part_3, F_j_part_4))))
        #print(F_j.shape)
        q = (l_x-x)**2+(l_y-y)**2
        self.h_j(x, y, l_x, l_y, q)
        H = np.dot(self.h, F_j)
        #print(H.shape, self.P.shape)
        PHT = np.dot(self.P, H.T)
        #print(self.P.shape)
        S = np.dot(np.dot(H, self.P), H.T)+self.R
        
        K = np.dot(PHT, np.linalg.inv(S))
        #print(K.shape, H.shape)
        return K, H
    def h_j(self,x,y,l_x, l_y, q):
        self.h[0,:] = np.array([(l_x-x)/np.sqrt(q), -(l_y-y)/np.sqrt(q), 0, -(l_x-x)/np.sqrt(q), (l_y-y)/np.sqrt(q), 0])
        self.h[1,:] = np.array([(l_y-y)/q, (l_x-x)/q, -1, -(l_y-y)/q, -(l_x-x)/q, 0])
        self.h[2, :] = np.array([0, 0, 0, 0, 0, 1])    