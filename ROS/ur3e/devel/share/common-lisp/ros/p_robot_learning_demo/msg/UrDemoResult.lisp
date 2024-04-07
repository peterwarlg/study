; Auto-generated. Do not edit!


(cl:in-package p_robot_learning_demo-msg)


;//! \htmlinclude UrDemoResult.msg.html

(cl:defclass <UrDemoResult> (roslisp-msg-protocol:ros-message)
  ((action_done
    :reader action_done
    :initarg :action_done
    :type cl:integer
    :initform 0)
   (rurpos
    :reader rurpos
    :initarg :rurpos
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (rf1
    :reader rf1
    :initarg :rf1
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass UrDemoResult (<UrDemoResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UrDemoResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UrDemoResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name p_robot_learning_demo-msg:<UrDemoResult> is deprecated: use p_robot_learning_demo-msg:UrDemoResult instead.")))

(cl:ensure-generic-function 'action_done-val :lambda-list '(m))
(cl:defmethod action_done-val ((m <UrDemoResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:action_done-val is deprecated.  Use p_robot_learning_demo-msg:action_done instead.")
  (action_done m))

(cl:ensure-generic-function 'rurpos-val :lambda-list '(m))
(cl:defmethod rurpos-val ((m <UrDemoResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:rurpos-val is deprecated.  Use p_robot_learning_demo-msg:rurpos instead.")
  (rurpos m))

(cl:ensure-generic-function 'rf1-val :lambda-list '(m))
(cl:defmethod rf1-val ((m <UrDemoResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader p_robot_learning_demo-msg:rf1-val is deprecated.  Use p_robot_learning_demo-msg:rf1 instead.")
  (rf1 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UrDemoResult>) ostream)
  "Serializes a message object of type '<UrDemoResult>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action_done)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action_done)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action_done)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action_done)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'rurpos))))
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
   (cl:slot-value msg 'rurpos))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'rf1))))
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
   (cl:slot-value msg 'rf1))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UrDemoResult>) istream)
  "Deserializes a message object of type '<UrDemoResult>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action_done)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action_done)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action_done)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action_done)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'rurpos) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'rurpos)))
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
  (cl:setf (cl:slot-value msg 'rf1) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'rf1)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UrDemoResult>)))
  "Returns string type for a message object of type '<UrDemoResult>"
  "p_robot_learning_demo/UrDemoResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UrDemoResult)))
  "Returns string type for a message object of type 'UrDemoResult"
  "p_robot_learning_demo/UrDemoResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UrDemoResult>)))
  "Returns md5sum for a message object of type '<UrDemoResult>"
  "3444c2c0ad381ffdf4a9aeaec324987c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UrDemoResult)))
  "Returns md5sum for a message object of type 'UrDemoResult"
  "3444c2c0ad381ffdf4a9aeaec324987c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UrDemoResult>)))
  "Returns full string definition for message of type '<UrDemoResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the result~%uint32 action_done~%float64[] rurpos~%float64[] rf1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UrDemoResult)))
  "Returns full string definition for message of type 'UrDemoResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define the result~%uint32 action_done~%float64[] rurpos~%float64[] rf1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UrDemoResult>))
  (cl:+ 0
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'rurpos) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'rf1) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UrDemoResult>))
  "Converts a ROS message object to a list"
  (cl:list 'UrDemoResult
    (cl:cons ':action_done (action_done msg))
    (cl:cons ':rurpos (rurpos msg))
    (cl:cons ':rf1 (rf1 msg))
))
