;; Auto-generated. Do not edit!


(when (boundp 'tutorial_msgs::RobotPos)
  (if (not (find-package "TUTORIAL_MSGS"))
    (make-package "TUTORIAL_MSGS"))
  (shadow 'RobotPos (find-package "TUTORIAL_MSGS")))
(unless (find-package "TUTORIAL_MSGS::ROBOTPOS")
  (make-package "TUTORIAL_MSGS::ROBOTPOS"))

(in-package "ROS")
;;//! \htmlinclude RobotPos.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass tutorial_msgs::RobotPos
  :super ros::object
  :slots (_name _pos ))

(defmethod tutorial_msgs::RobotPos
  (:init
   (&key
    ((:name __name) "")
    ((:pos __pos) (instance geometry_msgs::Point :init))
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _pos __pos)
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:pos
   (&rest __pos)
   (if (keywordp (car __pos))
       (send* _pos __pos)
     (progn
       (if __pos (setq _pos (car __pos)))
       _pos)))
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; geometry_msgs/Point _pos
    (send _pos :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; geometry_msgs/Point _pos
       (send _pos :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; geometry_msgs/Point _pos
     (send _pos :deserialize buf ptr-) (incf ptr- (send _pos :serialization-length))
   ;;
   self)
  )

(setf (get tutorial_msgs::RobotPos :md5sum-) "70afeb84f12dd0e4126fdef53df0eb32")
(setf (get tutorial_msgs::RobotPos :datatype-) "tutorial_msgs/RobotPos")
(setf (get tutorial_msgs::RobotPos :definition-)
      "string name 
geometry_msgs/Point pos

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :tutorial_msgs/RobotPos "70afeb84f12dd0e4126fdef53df0eb32")


