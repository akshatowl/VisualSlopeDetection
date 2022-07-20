#! /usr/bin/env python

import rospy
from cmath import pi
from turtle import distance
import cv2
import pyrealsense2
import sys
from realsense_depth import *
from sensor_msgs.msg import Image
from std_msgs import String 
import math
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

class image_node:

    def _init_(self):
        self.image_publish=rospy.Publisher("camera/realsense2_camera_manager",Image,queue_size=10)
        self.bridge=CvBridge()
        self.image_subscriber=rospy.Subscriber("camera/depth/image_rect_raw",Image,self.image_callback)

    
    def image_callback(self, data):
        try:
            cv_image=self.bridge.imgmsg_to_cv2(data,"bgr8")
        except CvBridgeError as error:
            print(error)

        (rows,cols,channels)=cv_image.shape

        if cols>60 and rows>60:
            cv2.circle(cv_image,(50,50,),10,255)
        
        cv2.imshow("Image Window", cv_image)
        cv2.waitKey(1)

def main(args):
    ic=image_node()
    rospy.init_node('image_node',anonymous=True)

    try:
            rospy.spin()
    except KeyboardInterrupt:
        print("Bye bye depth cam ;-;")
    cv2.destroyAllWindows()

if __name__=='__main__':
    main(sys.argv)





