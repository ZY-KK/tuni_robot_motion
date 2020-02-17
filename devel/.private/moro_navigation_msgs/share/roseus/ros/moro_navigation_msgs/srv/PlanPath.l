;; Auto-generated. Do not edit!


(when (boundp 'moro_navigation_msgs::PlanPath)
  (if (not (find-package "MORO_NAVIGATION_MSGS"))
    (make-package "MORO_NAVIGATION_MSGS"))
  (shadow 'PlanPath (find-package "MORO_NAVIGATION_MSGS")))
(unless (find-package "MORO_NAVIGATION_MSGS::PLANPATH")
  (make-package "MORO_NAVIGATION_MSGS::PLANPATH"))
(unless (find-package "MORO_NAVIGATION_MSGS::PLANPATHREQUEST")
  (make-package "MORO_NAVIGATION_MSGS::PLANPATHREQUEST"))
(unless (find-package "MORO_NAVIGATION_MSGS::PLANPATHRESPONSE")
  (make-package "MORO_NAVIGATION_MSGS::PLANPATHRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(if (not (find-package "TRAJECTORY_MSGS"))
  (ros::roseus-add-msgs "trajectory_msgs"))


(defclass moro_navigation_msgs::PlanPathRequest
  :super ros::object
  :slots (_start _goal ))

(defmethod moro_navigation_msgs::PlanPathRequest
  (:init
   (&key
    ((:start __start) (instance geometry_msgs::Point :init))
    ((:goal __goal) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _start __start)
   (setq _goal __goal)
   self)
  (:start
   (&rest __start)
   (if (keywordp (car __start))
       (send* _start __start)
     (progn
       (if __start (setq _start (car __start)))
       _start)))
  (:goal
   (&rest __goal)
   (if (keywordp (car __goal))
       (send* _goal __goal)
     (progn
       (if __goal (setq _goal (car __goal)))
       _goal)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point _start
    (send _start :serialization-length)
    ;; geometry_msgs/Point _goal
    (send _goal :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point _start
       (send _start :serialize s)
     ;; geometry_msgs/Point _goal
       (send _goal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point _start
     (send _start :deserialize buf ptr-) (incf ptr- (send _start :serialization-length))
   ;; geometry_msgs/Point _goal
     (send _goal :deserialize buf ptr-) (incf ptr- (send _goal :serialization-length))
   ;;
   self)
  )

(defclass moro_navigation_msgs::PlanPathResponse
  :super ros::object
  :slots (_trajectory ))

(defmethod moro_navigation_msgs::PlanPathResponse
  (:init
   (&key
    ((:trajectory __trajectory) (instance trajectory_msgs::JointTrajectory :init))
    )
   (send-super :init)
   (setq _trajectory __trajectory)
   self)
  (:trajectory
   (&rest __trajectory)
   (if (keywordp (car __trajectory))
       (send* _trajectory __trajectory)
     (progn
       (if __trajectory (setq _trajectory (car __trajectory)))
       _trajectory)))
  (:serialization-length
   ()
   (+
    ;; trajectory_msgs/JointTrajectory _trajectory
    (send _trajectory :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; trajectory_msgs/JointTrajectory _trajectory
       (send _trajectory :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; trajectory_msgs/JointTrajectory _trajectory
     (send _trajectory :deserialize buf ptr-) (incf ptr- (send _trajectory :serialization-length))
   ;;
   self)
  )

(defclass moro_navigation_msgs::PlanPath
  :super ros::object
  :slots ())

(setf (get moro_navigation_msgs::PlanPath :md5sum-) "098f7f8b063d412adcf0fd12d1459840")
(setf (get moro_navigation_msgs::PlanPath :datatype-) "moro_navigation_msgs/PlanPath")
(setf (get moro_navigation_msgs::PlanPath :request) moro_navigation_msgs::PlanPathRequest)
(setf (get moro_navigation_msgs::PlanPath :response) moro_navigation_msgs::PlanPathResponse)

(defmethod moro_navigation_msgs::PlanPathRequest
  (:response () (instance moro_navigation_msgs::PlanPathResponse :init)))

(setf (get moro_navigation_msgs::PlanPathRequest :md5sum-) "098f7f8b063d412adcf0fd12d1459840")
(setf (get moro_navigation_msgs::PlanPathRequest :datatype-) "moro_navigation_msgs/PlanPathRequest")
(setf (get moro_navigation_msgs::PlanPathRequest :definition-)
      "geometry_msgs/Point start
geometry_msgs/Point goal

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
trajectory_msgs/JointTrajectory trajectory

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start
")

(setf (get moro_navigation_msgs::PlanPathResponse :md5sum-) "098f7f8b063d412adcf0fd12d1459840")
(setf (get moro_navigation_msgs::PlanPathResponse :datatype-) "moro_navigation_msgs/PlanPathResponse")
(setf (get moro_navigation_msgs::PlanPathResponse :definition-)
      "geometry_msgs/Point start
geometry_msgs/Point goal

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
---
trajectory_msgs/JointTrajectory trajectory

================================================================================
MSG: trajectory_msgs/JointTrajectory
Header header
string[] joint_names
JointTrajectoryPoint[] points
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: trajectory_msgs/JointTrajectoryPoint
# Each trajectory point specifies either positions[, velocities[, accelerations]]
# or positions[, effort] for the trajectory to be executed.
# All specified values are in the same order as the joint names in JointTrajectory.msg

float64[] positions
float64[] velocities
float64[] accelerations
float64[] effort
duration time_from_start
")



(provide :moro_navigation_msgs/PlanPath "098f7f8b063d412adcf0fd12d1459840")


