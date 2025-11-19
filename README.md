Terrain_Navigation
This project demonstrates simulated terrain-aware robot navigation using ROS 2, Gazebo, and RViz. The robot uses a depth camera to measure the depth of ditches and automatically stops when it encounters untraversable terrain.

Features
Simulated mobile robot with a depth camera in a tilted position

Terrain awareness and obstacle detection using depth data

Automatic stopping at ditches that the robot cannot negotiate

Visualization support in both Gazebo and RViz

Project Structure
terrain_robot_ws/: ROS 2 workspace containing source code, launch files, and configuration

Source code includes depth camera processing, robot description, and navigation logic

Getting Started
Clone this repository:

bash
git clone https://github.com/Megha-ldce/Terrain_Navigation.git
Build the workspace:

bash
cd Terrain_Navigation/terrain_robot_ws
colcon build
Source the setup file:

bash
source install/setup.bash
Launch the simulation in Gazebo:

bash
ros2 launch terrain_aware_robot terrain_robot_launch.py
Start RViz (in a new terminal, after sourcing your workspace):

bash
rviz
Or load the provided configuration:

bash
rviz -d src/terrain_aware_robot/rviz/config.rviz
How It Works
The robot uses depth camera data to evaluate the terrain ahead.

If a ditch or gap is detected that cannot be crossed, the robot stops automatically.

All navigation data and robot state can be visualized in real time in RViz.

Requirements
ROS 2 (Jazzy or compatible version)

Gazebo Harmonic (or supported simulator for ROS 2 Jazzy)

Python and C++ build tools

Contact
For questions or contributions, please open an issue or pull request on this repository.
