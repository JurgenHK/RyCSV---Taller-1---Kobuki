# RyCSV-Taller-1-KobukiSim
## Workshop #1 - RyCSV 2020-II

This is the ROS package solution for the Workshop #1 from the RyCSV course at UNAL

![KOBUKI RVIZ](https://i.ibb.co/60BQPDV/rviz-kobuki.png)

## Usage

**NOTE** 
Tested on:
* **Ubuntu 20.04** with **ROS Noetic** full desktop installation
* **Ubuntu 16.04** with **ROS Kinetic** full desktop installation

For URDF model RViz visualization, use:

```bash
roslaunch kobuki_sim kobuki_rviz.launch 
```
For Gazebo simulation, use:

```bash
roslaunch kobuki_sim kobuki_gazebo.launch 
```
For keyboard logger node, use:

```bash
rosrun kobuki_sim keyboard_node.py 
```

## Team 
* **Jurgen Krejci** - [JurgenHK](https://github.com/JurgenHK) - _jhkrejcim@unal.edu.co
* **David Fonseca** - _daafonsecato@unal.edu.co_
* **Alejandro Marin** - _almarinca@unal.edu.co_