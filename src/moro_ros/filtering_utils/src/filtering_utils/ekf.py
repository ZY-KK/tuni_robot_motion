#!/usr/bin/env python
import numpy as np

R
class EKF:
    def __init__(self, state_vector_size, control_size, measurement_size):
        self.state_vector = np.zeros((state_vector_size, 1))
        self.next_state = np.zeros((state_vector_size, 1))
        self.cov_matrix = 1000. * np.identity(state_vector_size)
        self.q = np.zeros((control_size, control_size))
        self.R = np.zeros((measurement_size, measurement_size))
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
        self.state_vector = self.propagate_state(x, y, theta, v, w)
        self.calculate_cov()

    def update(self, x, y, theta, m_x, m_y):
        self.observation_jacobian_state_vector(x, y, theta, m_x, m_y)
        K = (self.calculate_cov*self.obs_j_state.transpose())/(self.obs_j_state*self.calculate_cov*self.obs_j_state.transpose()+self.R)
        z = self.z_function(x, y, theta, m_x, m_y)
        self.state_vector = self.next_state+K*()
        self.Q =np.dot((np.eye(self.obs_j_state.shape[0])-K*self.obs_j_state), self.Q)

        pass

    def z_function(self, x, y, theta, m_x, m_y):
        z = np.zeros((2,1))
        z[0] = np.sqrt((x-m_x)**2+(y-m_y)**2)
        z[1] = np.sqrt(np.arctan((m_y-y)/(m_x-x))-theta)
        return z
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
        """
        self.motion_j_state = np.array([[1, 0, (v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)],[0, 1, (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w)], [0, 0, 1]])
        """
        #self.motion_j_state = np.array([[1, 0, v*np.cos(theta+w*self.t)/w],[0, 1, v*np.sin(theta+w*self.t)/w], [0, 0, 1]])
        self.motion_j_state[0] = np.array([1, 0, v*np.cos(theta+w*self.t)/w])
        self.motion_j_state[1] = np.array([0, 1, v*np.sin(theta+w*self.t)/w])
        self.motion_j_state[2] = np.array([0, 0, 1])
        pass

    def motion_jacobian_noise_components(self, x, y, theta, v, w):
        # TO DO
        """
        self.motion_j_noise = np.array([[np.sin(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), -(v+self.delta_v)*np.cos(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2], [np.cos(theta+(w+self.delta_w)*self.t)/(w+self.delta_w), (v+self.delta_v)*np.sin(theta+(w+self.delta_w)*self.t)*self.t/(w+self.delta_w)**2], [0, self.t]])
        """
        self.motion_j_noise[0] = np.array([(np.sin(theta+w*self.t))/w, -v*np.sin(theta+w*self.t)/(w**2)+v*np.cos(theta+w*self.t)*self.t/w, v*np.cos(theta+w*self.t)/w])
        self.motion_j_noise[1] = np.array([-np.cos(theta+w*self.t)/w, v*np.cos(theta+w*self.t)/(w**2)+v*np.sin(theta+w*self.t)*self.t/w, v*np.sin(theta+w*self.t)/w])
        self.motion_j_noise[2] = np.array([0, self.t, 1])
        pass

    def observation_jacobian_state_vector(self, x, y, theta, m_x, m_y):
        # To DO
        self.obs_j_state[0] = np.array([x/(np.sqrt((x-m_x)**2+(y-m_y)**2)), y/(np.sqrt((x-m_x)**2+(y-m_y)**2)), 0])
        self.obs_j_state[1] = np.array([(y-m_y)/((m_x-x)**2+(m_y-y)**2), (m_x-x)**2/((m_x-x)**2+(m_y-y)**2), 1])
        pass
    
    def print_initials(self):
        print("Printing some values")
        print("The initial stated is {}").format(self.state_vector)
        print("The initial cov. matrix is {}").format(self.cov_matrix)
