

# Terrain_Navigation

This project demonstrates terrain-aware navigation for a simulated robot using ROS 2, Gazebo, and RViz. The robot uses a depth camera to measure ditch depths and stops in front of ditches it cannot traverse.

## Features

- Simulated mobile robot with a tilted depth camera
- Detects and measures ditch depth
- Robot stops before ditches using real sensor data
- Visualization in both Gazebo and RViz

## Requirements

- ROS 2 Jazzy (or compatible distribution)
- Gazebo Harmonic
- Python and C++ build tools

## Project Structure

- `terrain_robot_ws/`  
  ROS 2 workspace containing code, launch files, and configuration

***

## Getting Started

1. **Clone the repository**
    ```
    git clone https://github.com/Megha-ldce/Terrain_Navigation.git
    ```

2. **Build the workspace**
    ```
    cd Terrain_Navigation/terrain_robot_ws
    colcon build
    ```

3. **Source the workspace**
    ```
    source install/setup.bash
    ```

4. **Launch the simulation in Gazebo**
    ```
    ros2 launch terrain_aware_robot terrain_robot_launch.py
    ```

5. **Open RViz for visualization (optional)**  
   Open a new terminal, source the workspace, and start RViz:
    ```
    cd Terrain_Navigation/terrain_robot_ws
    source install/setup.bash
    rviz
    ```
   *Or, launch with your configuration file:*
    ```
    rviz -d src/terrain_aware_robot/rviz/config.rviz
    ```

***

## How It Works

- The robot uses a depth camera to detect ditches ahead on the terrain.
- If the ditch is not traversable, the robot automatically stops.
- All sensor and navigation data can be visualized live in RViz.

***

## Contact

For issues or contributions, please open an issue or pull request on this repository.


