# OxMinesweepers_navigation

## Dependancies

Catkin Tools: https://catkin-tools.readthedocs.io/en/latest/installing.html

Jackal_simulator: 

[Source Code](https://github.com/jackal/jackal_simulator)

To install the jackal simulator: 

`sudo apt install ros-melodic-jackal-viz ros-melodic-jackal-navigation ros-melodic-position-controllers`

Here is the [documentation] (https://www.clearpathrobotics.com/assets/guides/melodic/jackal/simulation.html) on Clear Sense's website.

## Building

**Create Catkin Workspace**
`mkdir -p <your own workspace>/src`

`cd <your own workspace>`

`catkin init`

`cd src`

<--clone this repo here-->

**Build**
`catkin build`

`cd <your own workspace>/src`

`source ../devel/setup.bash`

Note: To be able to run the packages, you need to run the last command on every terminal, it is recommended that this line is added to you ~/.bashrc file to simplify testing.

## Run
**Simulator**

To test whether jackal simulator is working properly, run `./OXMS_demo.sh`

**Testing**
The package serves to ensure that everything is running properly.

`rosrun robot monitor_py.py`
The linear and angular speed of the robot will be printed in the terminal

`rosrun robot move_py.py`
Under gazebo, you should see the robot moving in a circle.

Legacy C++ Version
`rosrun robot monitor`

`rosrun robot move`

**Goal Setting**
This allow us to hijack the ROS Navigation Stack and set a custom target for the odometry to reach.

So this will only work if you are already running `roslaunch jackal_navigation odom_navigation_demo.launch`

1)
`rosrun goal set_goal.py`
This allows you to inject a specific x,y,orientation for the jackal to move to

2)
`rosrun goal parser.py`
This allows you to put all the destination you want your robot to reach in a list and it will move the robot to each location oen by one

Note: Currently to change which text document you want the parser to parse, you must go edit the file path in the python script directly

**Test World**

`./nav_test.sh`
`roslaunch launch test_world.launch`
This put jackal in the temporary test world I have made.


**Known Issues**
If you encounter an error that says you dont have permission to run these script or it tells you that `Couldn't find executable named <file_name>`

Go to the folder where the python scripts are found

chmod 777 <filename>

WARNING: This is the nuclear option, it is not a good idea to give everyone permission to access the files. I need to come up with a way to fix this

