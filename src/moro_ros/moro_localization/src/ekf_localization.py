#!/usr/bin/env python
from filtering_utils.ekf import EKF
from marker_msgs.msg import MarkerDetection
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import rospy
import sys
import numpy as np
import math
import matplotlib.pyplot as plt
from tf.transformations import euler_from_quaternion, quaternion_from_euler
sys.path.append('src/moro_ros/filtering_utils/src/')

ekf = EKF(3, 2, 2)
    # initialize

landmarkers = np.array([[7.30, 3.00], [1.00, 1.00], [
                        9.00, 9.00], [1.00, 8.00], [5.80, 8.00]])
states = []
true_state = []    
ekf.t = 0.01
ekf.q = np.diag([0.01, 0.01])
ekf.R = np.diag([0.01, 0.01])
ekf.P = np.diag([.1, .1, .1])
ekf.state_vector = np.array([5.0, 5.0, math.pi])
states.append(ekf.state_vector)
ekf.print_initials()


def odom_callback(msg):
    #rospy.loginfo("odometry message")
    # rospy.loginfo(msg.twist.twist.linear.x)
    v = msg.twist.twist.linear.x
    #v_x = msg.twist.twist.linear.x
    #v_y = msg.twist.twist.linear.y

    #w = msg.pose.pose.orientation.w
    w = msg.twist.twist.angular.z
    # convert
    if w == 0:
        # approximate straight line with huge radius
        w = 1.e-30
    #v = np.sqrt(v_x**2+v_y**2)
    '''
    o_x = msg.pose.pose.orientation.x
    o_y = msg.pose.pose.orientation.y
    o_z = msg.pose.pose.orientation.z
    o_w = msg.pose.pose.orientation.w
    theta = quat2euler(o_x, o_y, o_z, o_w)
    '''
    #theta = np.arctan2(v_y, v_x)
    control_vector = np.array([v, w])
    ekf.predict(control_vector)
    pass
def quat2euler(x, y, z , w):
    r = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    r = r / math.pi * 180
    p = math.asin(2 * (w * y - z * x))
    p = p / math.pi * 180
    y = math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
    #y = y / math.pi * 180
    return r, p, y


def marker_callback(msg):
    #rospy.loginfo("Marker message")
    
    for marker in msg.markers:
        id = marker.ids[0]
        b_x = marker.pose.position.x
        b_y = marker.pose.position.y
        o_x = marker.pose.orientation.x
        o_y = marker.pose.orientation.y
        o_z = marker.pose.orientation.z
        o_w = marker.pose.orientation.w
        #z_a = quat2euler(o_x, o_y, o_z, o_w)
        z_a = euler_from_quaternion([o_x, o_y, o_z, o_w])
        #print(z_a)
        ekf.update(landmarkers[id-1], b_x, b_y, z_a[2])
    
    states.append(ekf.state_vector)
    #print(ekf.state_vector)
    

    #ekf.update(ekf.state_vector[0], ekf.state_vector[1], ekf.state_vector[2], m_x, m_y)
    #states.append(ekf.state_vector)
    pass
def ground_tru_callback(msg):
    t_x = msg.pose.pose.position.x
    t_y = msg.pose.pose.position.y
    true_state.append([t_x, t_y])


def ekf_loc():
    rospy.init_node('ekf_localization', anonymous=True)

    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.Subscriber("base_marker_detection", MarkerDetection, marker_callback)
    rospy.Subscriber("base_pose_ground_truth", Odometry, ground_tru_callback)

    rospy.spin()


if __name__ == '__main__':
    
    ekf_loc()
    states = np.array(states)
    true_state = np.array(true_state)

    
    plt.scatter(true_state[:, 0], true_state[:,1], marker='+', color='r', s=180, lw=1)
    plt.scatter(states[:, 0], states[:,1], color='k')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0.,10.])
    plt.ylim([0.,10.])
    plt.show()
    
    
