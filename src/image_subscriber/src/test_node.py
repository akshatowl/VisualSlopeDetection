#!/usr/bin/env python

import cv2
from matplotlib import image
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import pyrealsense2 as rs

#realsense_depth.py starts
# class DepthCamera:
#     def __init__(self):
#         # Configure depth and color streams
#         self.pipeline = rs.pipeline()
#         config = rs.config()

#         # Get device product line for setting a supporting resolution
#         pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
#         pipeline_profile = config.resolve(pipeline_wrapper)
#         device = pipeline_profile.get_device()
#         device_product_line = str(device.get_info(rs.camera_info.product_line))

#         config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
#         config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)



#         # Start streaming
#         self.pipeline.start(config)

#     def get_frame(self):
#         frames = self.pipeline.wait_for_frames()
#         depth_frame = frames.get_depth_frame()
#         color_frame = frames.get_color_frame()

#         depth_image = np.asanyarray(depth_frame.get_data())
#         color_image = np.asanyarray(color_frame.get_data())
#         if not depth_frame or not color_frame:
#             return False, None, None
#         return True, depth_image, color_image

#     def release(self):
#         self.pipeline.stop()
#ends


#setup cv bridge
bridge=CvBridge()

#Moving average filter function
def moving_average(x,n):
    return np.convolve(x,np.ones(n),'valid')/n


#Image callback function
def image_callback(image_msg):

    rospy.loginfo(image_msg.header)
    rospy.loginfo("got frames!")

    try:
        cv2_image_msg=bridge.imgmsg_to_cv2(image_msg,'passthrough')
        cv_image_array = np.array(cv2_image_msg, dtype = np.dtype('f8'))
        cv_image_norm = cv2.normalize(cv_image_array, cv_image_array, 0, 1, cv2.NORM_MINMAX)         
        cv2.imshow("camera", cv_image_norm)
        cv2.waitKey(1)

        print(cv_image_norm.shape)

    except CvBridgeError as e:
        print(e)
    else:
        # cv2.imwrite('camera_to_rosimage',cv2_image_msg)
        print("successful frames")
        
# img_sub=rospy.Subscriber("/camesra/depth/image_rect_raw",Image,image_callback)

def main():
    rospy.init_node('image_subscriber')
    image_topic="/camera/depth/image_rect_raw"
    rospy.Subscriber(image_topic,Image,image_callback)
    rospy.spin()
    


if __name__=='__main__':
    main()
