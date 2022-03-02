Mapviz [![Build Status](https://travis-ci.org/swri-robotics/mapviz.svg?branch=master)](https://travis-ci.org/swri-robotics/mapviz)
======

Mapviz is a [ROS](http://www.ros.org/) based visualization tool with a plug-in system similar to [RVIZ](http://wiki.ros.org/rviz) focused on visualizing 2D data.

![](https://github.com/swri-robotics/mapviz/wiki/mapviz.png)

Usage
-----

[View the documentation](https://swri-robotics.github.io/mapviz/) for usage information.

Relevant links / github repos: 

https://github.com/danielsnider/MapViz-Tile-Map-Google-Maps-Satellite

http://docs.ros.org/en/noetic/api/nav_msgs/html/msg/Odometry.html

http://docs.ros.org/en/kinetic/api/gps_common/html/msg/GPSFix.html

http://docs.ros.org/en/melodic/api/inertial_sense/html/msg/GPS.html

To set up the IMU with your Linux: https://github.com/rsx-utoronto/rover/wiki/Connecting-Your-Computer-to-IMU

----


In all separate termials, run:

`cd ~/catkin_ws`

`catkin_make`

`roscore`

Runs the docker and the server

`sudo docker run -p 8080:8080 -d -t -v ~/mapproxy:/mapproxy danielsnider/mapproxy`

Runs the IMU

`rosrun inertial_sense_ros inertial_sense_node`

Run the python / listener file that I created

`rosrun mapviz listener_gps.py`

If it says that it's not an executable, or can't be found, do (in the right file folder):

`chmod +x listener_gps.py`

Echo the topic that I publish to, make sure that messages get sent

`rostopic echo gps_converted`

Run MapViz

`roslaunch mapviz mapviz.launch`

(This may be different for everyone, but for Ellen's computer) Make sure that it's map for Fixed Frame and map for Target Frame

Do all the instructions in the Google Maps Offline capability github mentioned above

Then click 'Add'
Select 'gps' in the pop-up, and click OK.
Then, in the Topic, select 'gps_converted'.
--> Mapviz will only show topics that are compatible to be interpreted (they must be the same message type).
Click OK on selected topic.
There should be no errors when it runs --> should just say status is OK.

Make sure that the gps is below the tile_map, since the order matters. It will draw in order from top to bottom.


--------
For INS

(not necessary, but you can run the ins sub / pub file through) `rosrun mapviz listener_ins.py`

make sure to run it by 
`rosrun mapviz mapviz.launch`

To view frames, do 

`rosrun tf view_frames`

`evince frames.pdf`


Make sure fixed frame is map and target frame is ins_base_link. The arrows appear, but the transforms are messed up. Eg. map coords are 10,000x too big, and lat/lon are also messed up. Fix these later. + if you do this, the tile_map no longer shows up

--------
Future projects:
1. Polish up the IMU simulation python file
2. Create a script that will simultaneously open terminals and run the required commands to streamline process.
3. Make the frames compatible for the GPS and the IMU measurements -- right now, GPS uses a different frame than IMU. This makes it so you will have the location, but not the orientation of the IMU unit, which we need.
4. Create a marker or a more user friendly way of showing an orientation with the IMU measurement units.
