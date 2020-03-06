#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from marker_msgs.msg import MarkerDetection
from filtering_utils.pf import PF
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('src/moro_ros/filtering_utils/src/')

landmarkers = np.array([[7.30, 3.00], [1.00, 1.00], [
                        9.00, 9.00], [1.00, 8.00], [5.80, 8.00]])
states = []
pf = PF(10000, landmarkers, .2, .2, 3)
pf.state_vector=np.array([5.0, 5.0, 0.0])
#pf.create_gaussian_particles([3, 2, 0], [5, 5, 2])
pf.create_uniform_particles((0,10), (0,10), (0, 2*np.pi), pf.N)
def odom_callback(msg):
    # rospy.loginfo("odometry message")
    v = msg.twist.twist.linear.x
    #v_x = msg.twist.twist.linear.x
    #v_y = msg.twist.twist.linear.y
    w = msg.twist.twist.angular.z
    if w == 0:
        # approximate straight line with huge radius
        w = 1.e-30
    pf.predict([v, w], (.2, .05)) 
    pass


def marker_callback(msg):
    # rospy.loginfo("Marker message")
    markers = []
    zs=[]
    for marker in msg.markers:
        id = marker.ids[0]
        b_x = marker.pose.position.x
        b_y = marker.pose.position.y
        markers.append(landmarkers[id-1])
        zs.append(np.sqrt(b_x**2+b_y**2))
    markers = np.array(markers)
    zs = np.array(zs)
    """
    for landmark in markers:
        d = np.sqrt((landmark[0]-pf.state_vector[0])**2 +  (landmark[1]-pf.state_vector[1])**2)
        zs.append(d)
    """
    """
    for marker in msg.markers:
        id = marker.ids[0]
        b_x = marker.pose.position.x
        b_y = marker.pose.position.y
        zs.append(np.sqrt(b_x**2+b_y**2))
    """
    pf.update(zs, markers)
    if pf.neff(pf.weights) < pf.N/2:    
        pf.resample()
    mu, var = pf.estimate()
    #print(mu.shape)
    
    states.append(mu)
    pass


def pf_loc():
    rospy.init_node('pf_localization', anonymous=True)
    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.Subscriber("base_marker_detection", MarkerDetection, marker_callback)
    rospy.spin()


if __name__ == '__main__':
    pf_loc()
    states = np.array(states)
    plt.scatter(states[:, 0], states[:,1], color='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim([0.,10.])
    plt.ylim([0.,10.])
    plt.show()
    
