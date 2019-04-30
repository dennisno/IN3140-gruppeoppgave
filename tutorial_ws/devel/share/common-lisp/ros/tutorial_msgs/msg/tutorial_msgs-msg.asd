
(cl:in-package :asdf)

(defsystem "tutorial_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "RobotPos" :depends-on ("_package_RobotPos"))
    (:file "_package_RobotPos" :depends-on ("_package"))
  ))