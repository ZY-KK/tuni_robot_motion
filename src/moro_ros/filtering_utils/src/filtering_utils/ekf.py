#!/usr/bin/env python
import numpy as np


class EKF:
    def __init__(self, state_vector_size, control_size, measurement_size):
        self.state_vector = np.zeros((state_vector_size, 1))
        self.cov_matrix = 1000. * np.identity(state_vector_size)
        #self.q = np.zeros((control_size, control_size))
        self.q = np.zeros((control_size, 1))
        self.R = np.zeros((measurement_size, measurement_size))
        self.motion_j_state = np.zeros((state_vector_size, state_vector_size))
        self.motion_j_noise = np.zeros((state_vector_size, control_size))
        self.obs_j_state = np.zeros((measurement_size, state_vector_size))
        self.Q = np.zeros((state_vector_size, state_vector_size))
        self.delta_v = 0
        self.delta_w = 0
        self.t = 0
    def predict(self):
        self.propagate_state()
        self.calculate_cov()

    def update(self):
        
        pass

    def propagate_state(self):
        X = []
        x = self.state_vector[0]
        y = self.state_vector[1]
        theta = self.state_vector[2]
        v = self.q[0]
        w  =self.q[1]
        X[0] = x + (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)
        X[1] = y + (v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)
        X[2] = theta + (w+self.delta_w)*self.t
        pass

    def calculate_cov(self):
        self.Q = self.motion_j_noise * self.q * self.motion_j_noise.transpose()
        self.cov_matrix = self.motion_j_state * self.cov_matrix * \
            self.motion_j_state.transpose() + self.Q

    def motion_jacobian_state_vector(self):
        # TO DO
        x = self.state_vector[0]
        y = self.state_vector[1]
        theta = self.state_vector[2]
        v = self.q[0]
        w  =self.q[1]
        self.motion_j_state = np.array([[1, 0, (v+self.delta_v)*np.cos(theta+(w+self.delta_w)*t)/(w+self.delta_w)],[0, 1, -(v+self.delta_v)*np.sin(theta+(w+self.delta_w)*t)/(w+self.delta_w)], [0, 0, 1]])
        # self.motion_j_state
        pass

    def motion_jacobian_noise_components(self):
        # TO DO
        x = self.state_vector[0]
        y = self.state_vector[1]
        theta = self.state_vector[2]
        v = self.q[0]
        w  =self.q[1]
        self.motion_j_noise = np.array([[np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), -(v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2], [np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2]])
        pass

    def observation_jacobian_state_vector(self):
        # To DO
        x = self.state_vector[0]
        y = self.state_vector[1]
        theta = self.state_vector[2]
        self.obs_j_state = np.array([[x/np.sqrt(x**2+y**2), y/np.sqrt(x**2+y**2), 0], [0, 0, x**2/(x**2+y**2)]])
        pass

    def print_initials(self):
        print("Printing some values")
        print("The initial stated is {}").format(self.state_vector)
        print("The initial cov. matrix is {}").format(self.cov_matrix)
