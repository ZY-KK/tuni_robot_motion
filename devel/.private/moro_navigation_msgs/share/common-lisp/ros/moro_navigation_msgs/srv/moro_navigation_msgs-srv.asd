
(cl:in-package :asdf)

(defsystem "moro_navigation_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :trajectory_msgs-msg
)
  :components ((:file "_package")
    (:file "PlanPath" :depends-on ("_package_PlanPath"))
    (:file "_package_PlanPath" :depends-on ("_package"))
  ))