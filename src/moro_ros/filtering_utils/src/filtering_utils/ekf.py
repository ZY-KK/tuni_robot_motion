#!/usr/bin/env python
import numpy as np

R
class EKF:
    def __init__(self, state_vector_size, control_size, measurement_size):
        self.state_vector = np.zeros((state_vector_size, 1))
        self.next_state = np.zeros((state_vector_size, 1))
        self.cov_matrix = 1000. * np.identity(state_vector_size)  #p
        self.q = np.zeros((control_size, control_size))
        #self.r = np.zeros((measurement_size,, measurement_size))
        #self.q = np.zeros((control_size, 1))
        self. = np.zeros((measurement_size, measurement_size))
        self.motion_j_state = np.zeros((state_vector_size, state_vector_size))
        self.motion_j_noise = np.zeros((state_vector_size, control_size))
        self.obs_j_state = np.zeros((measurement_size, state_vector_size))
        self.Q = np.zeros((state_vector_size, state_vector_size))
        self.delta_v = 0
        self.delta_w = 0
        self.t = 0
    def predict(self, x, y, theta, v, w):
        self.motion_jacobian_state_vector(x, y, theta, v, w)
        self.motion_jacobian_noise_components(x, y, theta, v, w)
        # the next state
        self.next_state = self.propagate_state(x, y, theta, v, w)
        self.calculate_cov()

    def update(self, x, y, theta):
        self.observation_jacobian_state_vector(x, y, theta)
        K = (self.calculate_cov*self.obs_j_state.transpose())/(self.obs_j_state*self.calculate_cov*self.obs_j_state.transpose()+self.R)
        m_x, m_y, theta = self.state_vector[0], self.state_vector[1], self.state_vector[2]
        self.state_vector = self.next_state+K*()
        self.Q = (np.eye(self.obs_j_state.shape[0])-K*self.obs_j_state)

        pass
    def h(self, x, y, l_x, l_y, theta):
        Z = []
        Z[0] = np.sqrt((x-l_x)**2+(y-l_y)**2)
        Z[1] = np.arctan((y-l_y)/(x-l_x))-theta
    def propagate_state(self, x, y, theta, v, w):
        state_next = []
        state_next[0] = x + (v)*np.sin(theta+(w)*self.t)/(w)
        state_next[1] = y + (v)*np.cos(theta+(w)*self.t)/(w)
        state_next[2] = theta + (w)*self.t
        return np.asarray(state_next)
        pass

    def calculate_cov(self):
        self.Q = self.motion_j_noise * self.q * self.motion_j_noise.transpose()
        self.cov_matrix = self.motion_j_state * self.cov_matrix * \
            self.motion_j_state.transpose() + self.Q

    def motion_jacobian_state_vector(self, x, y, theta, v, w):
        # TO DO
        self.motion_j_state = np.array([[1, 0, (v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)],[0, 1, (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)], [0, 0, 1]])
        # self.motion_j_state
        pass

    def motion_jacobian_noise_components(self, x, y, theta, v, w):
        # TO DO
        """
        self.motion_j_noise = np.array([[np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), -(v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2], [np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2], [0, self.t]])
        """
        pass

    def observation_jacobian_state_vector(self, x, y, theta):
        # To DO
        self.obs_j_state = np.array([[x/np.sqrt(x**2+y**2), y/np.sqrt(x**2+y**2), 0], [0, 0, x**2/(x**2+y**2)]])
        pass
    
    def print_initials(self):
        print("Printing some values")
        print("The initial stated is {}").format(self.state_vector)
        print("The initial cov. matrix is {}").format(self.cov_matrix)
