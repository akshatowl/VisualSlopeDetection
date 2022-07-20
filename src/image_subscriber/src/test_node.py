#!/usr/bin/env python

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


#setup cv bridge
bridge=CvBridge()

#Image callback function
def image_callback(image_msg):

    rospy.loginfo(image_msg.header)

    try:
        cv2_image_msg=bridge.imgmsg_to_cv2(image_msg,"brg8")
    except CvBridgeError as e:
        print(e)
    else:
        cv2.imwrite('camera_to_rosimage',cv2_image_msg)

img_sub=rospy.Subscriber("/camera/depth/image_rect_raw",Image,image_callback)

def main():
    rospy.init_node('image_subscriber')
    image_topic="/camera/depth/"

    rospy.Subscriber(image_topic,Image,image_callback)

    rospy.spin()

if __name__=='__main__':
    main()
