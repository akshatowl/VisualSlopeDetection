# ROS Node based on RosPy

This ros node subcribers to the topic: 
```
/camera/depth/rect_image_raw
```

which is the topic where the camera publishes the frames to via the Intel Realsense ROS drivers.

In order to run the node, you need all the dependencies for the Intel RealSense depth cameras

```
sudo apt-get install ros-<your_ros_distro>-realsense2-camera
sudo apt-get install ros-<your-ros-distro>-realsense2-description

```
If aptitute installation does not work, navigate to the official Intel Realsense git repository [here](https://github.com/IntelRealSense/realsense-ros)


```

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

In order to launch the node with rosrun and without the launch file

Open a terminal window and run the realsense launch file which starts the camera with the parameters and a roscore instance.

```
roslaunch realsense2_camera rs_camera.launch
```
In the second terminal 
```
~/VisualSlopeDetection
source devel/setup.zsh
rosrun image_pkg slope_node.py
```

