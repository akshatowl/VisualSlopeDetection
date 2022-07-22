#!/usr/bin/env python

import cv2
from matplotlib import image
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import pyrealsense2 as rs
import math

#setup cv bridge
bridge=CvBridge()

#Moving average filter function
def moving_average(x,n):
    return np.convolve(x,np.ones(n),'valid')/n


#Image callback function
def image_callback(image_msg):

    # rospy.loginfo(image_msg.header)
    rospy.loginfo("got frames!")

    try:
        cv2_image_msg=bridge.imgmsg_to_cv2(image_msg,'passthrough')
        cv_image_array = np.array(cv2_image_msg, dtype = np.dtype('f8'))
        cv_image_norm = cv2.normalize(cv_image_array, cv_image_array, 0, 255, cv2.NORM_MINMAX)         
        cv2.imshow("camera", cv_image_array)
        cv2.waitKey(1)

        # print(cv_image_norm)


    except CvBridgeError as e:
        print(e)
    else:
        # cv2.imwrite('camera_to_rosimage',cv2_image_msg)
        print("successful frames")
    
    dist1=cv_image_norm[180][390]
    dist2=cv_image_norm[180][340]
    dist3=cv_image_norm[180][290]
    dist4=cv_image_norm[180][240]
    dist5=cv_image_norm[180][190]
    dist6=cv_image_norm[180][140]
    dist7=cv_image_norm[180][90]
 

    x=np.array([dist1,dist2,dist3,dist4,dist5,dist6,dist7])

    angle_1=math.degrees(math.atan((x[0]-x[1])/5.0))
    angle_2=math.degrees(math.atan((x[0]-x[2])/10.0))
    angle_3=math.degrees(math.atan((x[0]-x[3])/15.0))
    angle_4=math.degrees(math.atan((x[0]-x[4])/25.0))
    angle_5=math.degrees(math.atan((x[0]-x[5])/25.0))
    angle_6=math.degrees(math.atan((x[0]-x[6])/30.0))

    slopes=np.array([angle_1,angle_2,angle_3,angle_4,angle_5,angle_6])
    rectified_slopes=moving_average(slopes,6)
    slope_mean=(rectified_slopes)

    # print(angle_1,angle_2,angle_3)
    if slope_mean<90.0:
        print(90.0-slope_mean)
    else:
        print(90.0+slope_mean)


def main():
    rospy.init_node('image_pkg')
    image_topic="/camera/depth/image_rect_raw"
    rospy.Subscriber(image_topic,Image,image_callback)
    rospy.spin()
    


if __name__=='__main__':
    main()
