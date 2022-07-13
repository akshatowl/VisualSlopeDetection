from cmath import pi
from turtle import distance
import cv2
import pyrealsense2
from realsense_depth import *
import math
import numpy as np

#-- The logic towards depth calculation is a basic geometric approach, in order to make the 
#    slope data less susceptible towards noise a basic 3-point moving average filter is being used.

#Defining depth cam

depthcam=DepthCamera()


#N-point Moving Average Filter
def moving_average(x, n):
        return np.convolve(x, np.ones(n), 'valid') / n


while True:
    ret,depth_frame,clr_frame=depthcam.get_frame()

    #5 coordinates 50mm pixels apart
    coordinate=(300,250)
    coordinate_2=(300,300)
    coordinate_3=(300,350)
    coordinate_4=(300,400)
    coordinate_5=(300,450) #For reference , not used in computation

    #Display for reference in the coloured frame
    cv2.circle(clr_frame,coordinate,4,(0,255,0))
    cv2.circle(clr_frame,coordinate_2,4,(0,255,0))
    cv2.circle(clr_frame,coordinate_3,4,(0,255,0))
    cv2.circle(clr_frame,coordinate_4,4,(0,255,0))
    cv2.circle(clr_frame,coordinate_5,4,(0,255,0))


    #distances of interactables/objects from pixel values
    dist1=depth_frame[coordinate[1],coordinate[0]]
    dist2=depth_frame[coordinate_2[1],coordinate_2[0]]
    dist3=depth_frame[coordinate_3[1],coordinate_3[0]]
    dist4=depth_frame[coordinate_4[1],coordinate_4[0]]

    x=np.array([dist1,dist2,dist3,dist4], dtype=np.float64)
    

    #calculating angles wrt slope
    angle_1=math.degrees(math.atan((x[0]-x[1])/50.0))
    angle_2=math.degrees(math.atan((x[0]-x[2])/100.0))
    angle_3=math.degrees(math.atan((x[0]-x[3])/150.0))

    slopes=np.array([angle_1,angle_2,angle_3], dtype=np.float64)
    rectified_slopes=moving_average(slopes,3)

    slope_mean=(rectified_slopes)
    

    if slope_mean<90:
        print(90-slope_mean)
    else:    
        print(90+slope_mean) #180-(90-slope_mean)

    #Display coloured and depth frame
    cv2.imshow("Depth Frame", depth_frame)
    cv2.imshow("Coloured Frame", clr_frame)

    #Wait 2ms for the frame
    key=cv2.waitKey(2)

    