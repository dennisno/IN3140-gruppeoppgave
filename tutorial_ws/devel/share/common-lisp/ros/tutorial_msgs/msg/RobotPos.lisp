; Auto-generated. Do not edit!


(cl:in-package tutorial_msgs-msg)


;//! \htmlinclude RobotPos.msg.html

(cl:defclass <RobotPos> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (pos
    :reader pos
    :initarg :pos
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point)))
)

(cl:defclass RobotPos (<RobotPos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RobotPos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RobotPos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tutorial_msgs-msg:<RobotPos> is deprecated: use tutorial_msgs-msg:RobotPos instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <RobotPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:name-val is deprecated.  Use tutorial_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'pos-val :lambda-list '(m))
(cl:defmethod pos-val ((m <RobotPos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tutorial_msgs-msg:pos-val is deprecated.  Use tutorial_msgs-msg:pos instead.")
  (pos m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RobotPos>) ostream)
  "Serializes a message object of type '<RobotPos>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pos) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RobotPos>) istream)
  "Deserializes a message object of type '<RobotPos>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pos) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RobotPos>)))
  "Returns string type for a message object of type '<RobotPos>"
  "tutorial_msgs/RobotPos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RobotPos)))
  "Returns string type for a message object of type 'RobotPos"
  "tutorial_msgs/RobotPos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RobotPos>)))
  "Returns md5sum for a message object of type '<RobotPos>"
  "70afeb84f12dd0e4126fdef53df0eb32")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RobotPos)))
  "Returns md5sum for a message object of type 'RobotPos"
  "70afeb84f12dd0e4126fdef53df0eb32")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RobotPos>)))
  "Returns full string definition for message of type '<RobotPos>"
  (cl:format cl:nil "string name ~%geometry_msgs/Point pos~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RobotPos)))
  "Returns full string definition for message of type 'RobotPos"
  (cl:format cl:nil "string name ~%geometry_msgs/Point pos~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RobotPos>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pos))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RobotPos>))
  "Converts a ROS message object to a list"
  (cl:list 'RobotPos
    (cl:cons ':name (name msg))
    (cl:cons ':pos (pos msg))
))
