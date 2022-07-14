# VisualSlopeDetection

This repository uses the backend openCV processing file from PySource which can be downloaded from: https://pysource.com/2021/03/11/distance-detection-with-depth-camera-intel-realsense-d435i/

It is also included within ~/python_scripts

In order to run the scripts, you need all the dependencies for the Intel RealSense depth cameras

```
sudo apt install pip
pip install realsense2
pip install opencv-python

```

Update and upgrade packages

```

sudo apt update
sudo apt upgrade
```


## Approach for slope detection

### Geometric Approach

This approach dedicated an area and an array of pixel values all a fixed distance apart. Any object detected within this range of pixels will return 4 distances from these pixels

![depthcam1 (1)](https://user-images.githubusercontent.com/58850654/179021620-496e70e2-c66d-405c-b454-0a21960259be.png)

θ is considered to be the angle that is calculated from slopes from distances 
Φ is the actual slope of the obstacle

to calculate angle θ, 3 slopes are calculated which are distance from all the point with reference to one point. The arc tangent of the slopes will give that value of θ.

This can be achieved with just 2 pixel points as well, however using multiple points and averaging slopes results in a more accurate output. It also accounts for the fact if a particular pixel point has a dead-zone due to scratch, relying on those pixels won't yeild in accurate measurements.


### Filtering

To make the data more accurate and less susceptible towards any noise, a simple 3 point moving average filter is used.




