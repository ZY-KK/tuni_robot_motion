#!/usr/bin/env python
import rospy
import sys
sys.path.append('src/moro_ros/filtering_utils/src/')
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from marker_msgs.msg import MarkerDetection
from filtering_utils.ekf import EKF

ekf = EKF(3, 2, 2)


def odom_callback(msg):
    rospy.loginfo("odometry message")
    ekf.print_initials()
    rospy.loginfo(msg.twist.twist.linear.x)
    # pass 
    ekf.predict()
    
    #predict_co_matrix
    pass


def marker_callback(msg):
    rospy.loginfo("Marker message")
    ekf.update()
    pass


def ekf_loc():
    rospy.init_node('ekf_localization', anonymous=True)
    rospy.Subscriber("odom", Odometry, odom_callback)
    rospy.Subscriber("base_marker_detection", MarkerDetection, marker_callback)
    rospy.spin()


if __name__ == '__main__':
    ekf_loc()
