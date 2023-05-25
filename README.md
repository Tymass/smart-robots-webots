# smart-robots-webots

Projects implemented on the Webots platform in the Python language

## Table of Contents
- [smart-robots-webots](#smart-robots-webots)
  - [Table of Contents](#table-of-contents)
  - [Robot position estimation](#robot-position-estimation)
    - [Set up the envoirnment](#set-up-the-envoirnment)
    - [Calculating the robot's position](#calculating-the-robots-position)
  - [Useful links](#useful-links)

## Robot position estimation
    
   This project involves estimating the position of a robot based on motion sensor data calculated using odometry
    
### Set up the envoirnment

   We will use an e-puck robot to complete this task. When creating a world from scratch, you should create a new world in 
   the Webots environment and add the e-puck robot to it. Then set the DEF of the e-puck robot to "E-PUCK". 
   Now add a standard robot from the base nodes path to the world. Set the "supervisor" variable on the robot to True. 
   Now you should create a controller for the robot and for the supervisor and then set the corresponding controllers in the robot's properties.
   Your envoirnment should look like this:
   
   ![image](https://github.com/Tymass/smart-robots-webots/assets/83314524/9083db84-0059-4740-9322-22b6db1f1dad)
    
### Calculating the robot's position

   **e-puck_controller.py**
    
   The defined time step is 64 milliseconds, in such a small time interval we can assume that the robot is moving in a rectilinear motion. 
   To calculate the robot's displacement, we need to set the value of its initial position and orientation to 0.

   Then, in each time stamp, we take the value of the rotation of the motor from the beginning of its movement. 
   In fact, the sensors do not give accurate values so we additionally add white noise to the output of these sensors. 
   We calculate the turning of the wheels, the distance traveled by them, and the change in the robot's orientation for the current time step.
   The coordinates are then saved in a .txt file
    
   **supervisor_controller.py**
    
   Supervisor controller is conected to e-puck robot. It has access to the plane on which it moves and on the exact values of its position. Those values are saved in file.
    
   **vis.py**
    
   The visualization script takes data from files and plots them on a graph.
    
   ![image](https://github.com/Tymass/smart-robots-webots/assets/83314524/0581a71b-54a2-4ebb-aa5d-872fab80dc2f)


## Useful links
 
   - [Mathematic behind differential drive robots](https://www.cs.columbia.edu/~allen/F19/NOTES/icckinematics.pdf)
   - [E-puck robot documentation](https://cyberbotics.com/doc/guide/epuck)
   - [Webots supervisor tutorial](https://cyberbotics.com/doc/guide/tutorial-8-the-supervisor)
