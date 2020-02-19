#!/usr/bin/env python
import rospy
import sys
import numpy as np
sys.path.append('src/moro_ros/filtering_utils/src/')
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from marker_msgs.msg import MarkerDetection
from filtering_utils.ekf import EKF

ekf = EKF(3, 2, 2)
# initialize 
ekf.t = 1/50
ekf.q = np.diag([1.5, 0.01])
ekf.R = np.diag([1.5, 0.01])
ekf.state_vector=np.array([0, 0, 0])

def odom_callback(msg):
    rospy.loginfo("odometry message")
    ekf.print_initials()
    rospy.loginfo(msg.twist.twist.linear.x)
    v_x = msg.twist.twist.linear.x
    v_y = msg.twist.twist.linear.y
    w = msg.twist.twist.angular.z
    v = np.sqrt(v_x**2+v_y**2)
    theta = np.arctan(v_y/v_x)
    ekf.predict(ekf.state_vector[0], ekf.state_vector[1], ekf.state_vector[2], v, theta)
    
    #predict_co_matrix
    pass


def marker_callback(msg):
    rospy.loginfo("Marker message")

    #ekf.update(ekf.state_vector[0], ekf.state_vector[1], ekf.state_vector[2], m_x, m_y)
    pass


def ekf_loc():
    rospy.init_node('ekf_localization', anonymous=True)
    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.Subscriber("base_marker_detection", MarkerDetection, marker_callback)
    rospy.spin()


if __name__ == '__main__':
    ekf_loc()
