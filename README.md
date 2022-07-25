# VisualSlopeDetection

This repository uses the backend OpenCV processing file from PySource which can be downloaded [here](https://pysource.com/2021/03/11/distance-detection-with-depth-camera-intel-realsense-d435i/)

It is also included within ~/python_scripts

## Prerequisites

In order to run the scripts, you need all the dependencies for the Intel RealSense depth cameras. They can be easily installed using pip.

```
sudo apt install pip
pip install realsense2
pip install opencv-python
```

The filtering implementation and array requires Scipy and Numpy, they should be installed in your local machine 

```
pip install numpy
pip install scipy

```

Update and upgrade packages

```
sudo apt update
sudo apt upgrade
```

Clone this repository to your local machine

```
git clone https://github.com/akshatowl/VisualSlopeDetection.git
```
## Running the script

The main file that runs the logic for slope detection is depthcam_slope.py

Make the python file an executable:

```
cd ~/VisualSlopeDetection/python_scripts
chmod +x depthcam_slope.py
chmod +x realsense_depth.py
```
Run depthcam_slope.py

```
./depthcam_slope.py
```

## Expected output
colour frame is just for reference an can be disabled, all depth measurements are from the depth frame.
Angled camera ( ~ 20 degree inclination)

![Screenshot from 2022-07-14 14-58-13](https://user-images.githubusercontent.com/58850654/179061995-10b485b3-ebe7-4ae1-951f-8362853066aa.png)



## Approach for slope detection

### Geometric Approach

This approach dedicates an area and an array of pixel values all a fixed distance apart. Any object detected within this range of pixels will return 4 distances from these pixels

![depthcam1 (1)](https://user-images.githubusercontent.com/58850654/179021620-496e70e2-c66d-405c-b454-0a21960259be.png)

θ is considered to be the angle that is calculated from slopes from distances 
Φ is the actual slope of the obstacle

to calculate angle θ, 3 slopes are calculated which are distance from all the point with reference to one point. The arc tangent of the slopes will give that value of θ.

This can be achieved with just 2 pixel points as well, however using multiple points and averaging slopes results in a more accurate output. It also accounts for the fact if a particular pixel point has a dead-zone due to scratch, relying on those pixels won't yeild in accurate measurements.


### Filtering

To make the data more accurate and less susceptible towards any noise, a simple 3 point moving average filter is used. A basic mean or low pass filter can be explored as well.


# ROS Node based on RosPy

This ros node subcribes to the topic: 
```
/camera/depth/rect_image_raw
```

which is the topic where the camera publishes the frames to via the Intel Realsense ROS drivers.

In order to run the node, you need all the ROS dependencies for the Intel RealSense depth cameras

```
sudo apt-get install ros-<your-ros-distro>-realsense2-camera
sudo apt-get install ros-<your-ros-distro>-realsense2-description
```

If aptitute installation does not work, navigate to the official Intel Realsense git repository [here](https://github.com/IntelRealSense/realsense-ros)




Update and upgrade packages


```
sudo apt update
sudo apt upgrade
```
Make the python node an excutable
```
~/VisualSlopeDetection/src/image_pkg
chmod +x slope_node.py
```
Build the catkin workspace using catkin tools
```
~/VisualSlopeDetection
catkin_make or catkin build
```

Source the workspace, depending on which shell your system has
```
source devel/setup.zsh
or 
source devel/setup.bash
```
Launch the node with the launch file

```
roslaunch image_launcher depthslope.launch
```


In order to run the node with rosrun:

Open a terminal window and run the realsense launch file which starts the camera with the parameters and a roscore instance.

```
roslaunch realsense2_camera rs_camera.launch
```
In the second terminal window
```
~/VisualSlopeDetection
source devel/setup.zsh
rosrun image_pkg slope_node.py
```
