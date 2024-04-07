; Auto-generated. Do not edit!


(cl:in-package p_robot_learning_demo-msg)


;//! \htmlinclude UrDemoGoal.msg.html

(cl:defclass <UrDemoGoal> (roslisp-msg-protocol:ros-message)
  ((action_id
    :reader action_id
    :initarg :action_id
    :type cl:integer
    :initform 0)
   (mode_id
    :reader mode_id
    :initarg :mode_id
    :type cl:integer
    :initform 0)
   (urpos
    :reader urpos
    :initarg :urpos
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (gripper_val
    :reader gripper_val
    :initarg :gripper_val
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass UrDemoGoal (<UrDemoGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UrDemoGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UrDemoGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name p_robot_learning_demo-msg:<UrDemoGoal> is deprecated: use p_robot_learning_demo-msg:UrDemoGoal instead.")))

(cl:ensure-generic-function 'action_id-val :lambda-list '(m))
(cl:defmethod action_id-val ((m <UrDemoGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:action_id-val is deprecated.  Use p_robot_learning_demo-msg:action_id instead.")
  (action_id m))

(cl:ensure-generic-function 'mode_id-val :lambda-list '(m))
(cl:defmethod mode_id-val ((m <UrDemoGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:mode_id-val is deprecated.  Use p_robot_learning_demo-msg:mode_id instead.")
  (mode_id m))

(cl:ensure-generic-function 'urpos-val :lambda-list '(m))
(cl:defmethod urpos-val ((m <UrDemoGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:urpos-val is deprecated.  Use p_robot_learning_demo-msg:urpos instead.")
  (urpos m))

(cl:ensure-generic-function 'gripper_val-val :lambda-list '(m))
(cl:defmethod gripper_val-val ((m <UrDemoGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:gripper_val-val is deprecated.  Use p_robot_learning_demo-msg:gripper_val instead.")
  (gripper_val m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UrDemoGoal>) ostream)
  "Serializes a message object of type '<UrDemoGoal>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'mode_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'mode_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'mode_id)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'urpos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'urpos))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'gripper_val))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'gripper_val))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UrDemoGoal>) istream)
  "Deserializes a message object of type '<UrDemoGoal>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'mode_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'mode_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'mode_id)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'urpos) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'urpos)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'gripper_val) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'gripper_val)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UrDemoGoal>)))
  "Returns string type for a message object of type '<UrDemoGoal>"
  "p_robot_learning_demo/UrDemoGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UrDemoGoal)))
  "Returns string type for a message object of type 'UrDemoGoal"
  "p_robot_learning_demo/UrDemoGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UrDemoGoal>)))
  "Returns md5sum for a message object of type '<UrDemoGoal>"
  "3e2e647b480d85b93a63fd7219d610b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UrDemoGoal)))
  "Returns md5sum for a message object of type 'UrDemoGoal"
  "3e2e647b480d85b93a63fd7219d610b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UrDemoGoal>)))
  "Returns full string definition for message of type '<UrDemoGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%uint32 action_id  # Specify which dishwasher we want to use~%uint32 mode_id~%float64[] urpos~%float64[] gripper_val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UrDemoGoal)))
  "Returns full string definition for message of type 'UrDemoGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the goal~%uint32 action_id  # Specify which dishwasher we want to use~%uint32 mode_id~%float64[] urpos~%float64[] gripper_val~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UrDemoGoal>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'urpos) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'gripper_val) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UrDemoGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'UrDemoGoal
    (cl:cons ':action_id (action_id msg))
    (cl:cons ':mode_id (mode_id msg))
    (cl:cons ':urpos (urpos msg))
    (cl:cons ':gripper_val (gripper_val msg))
))
