from controller import Robot
from math import sin, cos
import random

# Define robot parameters
TIME_STEP = 64
WHEEL_RADIUS = 0.0205
AXLE_LENGTH = 0.057
NOISE_STD_DEV = 0.05

# Create the Robot
robot = Robot()

# Get robot's devices
accelerometer = robot.getDevice('accelerometer')
accelerometer.enable(TIME_STEP)

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_position_sensor = robot.getDevice('left wheel sensor')
right_position_sensor = robot.getDevice('right wheel sensor')

# Set up  devices properties
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

left_position_sensor.enable(TIME_STEP)
right_position_sensor.enable(TIME_STEP)

# Initial values of robot position and orientation
x = 0.0
y = 0.0
theta = 0.0

# Initial values of wheels ticks
old_left_wheel_ticks = 0.0
old_right_wheel_ticks = 0.0
# Initial values fo robot speed
previous_velocity = 0.0
current_velocity = 0.0
# Single robot step (to get initial value of position sensors)
robot.step(TIME_STEP)
initial_left_wheel_ticks = left_position_sensor.getValue()
initial_right_wheel_ticks = right_position_sensor.getValue()

# Clear file with data
open('dane.txt', 'w').close()

# Main loop
while robot.step(TIME_STEP) != -1:
    #   Robot speed based on accelerometer values
    # Accelerometer values
    ax, ay, _ = accelerometer.getValues()
    # Robot actuall acceleration (in little time stamp we assume robot move on straight line)
    a_magnitude = (ax**2 + ay**2) ** 0.5
    # Update current robot speed
    current_velocity = a_magnitude * (TIME_STEP / 1000.0) + previous_velocity
    # Store current speed for the next time step
    previous_velocity = current_velocity

    #   Robot estimated position based on odometry
    # Get value of corruption from the begining (- initial offset)
    left_wheel_ticks = left_position_sensor.getValue() - initial_left_wheel_ticks
    right_wheel_ticks = right_position_sensor.getValue() - initial_right_wheel_ticks

    # Each time add random white noise on sensors output
    left_wheel_ticks += random.gauss(0, NOISE_STD_DEV)
    right_wheel_ticks += random.gauss(0, NOISE_STD_DEV)

    # Get wheel rotations in radians in this time stamp
    left_wheel_rotation = left_wheel_ticks - old_left_wheel_ticks
    right_wheel_rotation = right_wheel_ticks - old_right_wheel_ticks

    # Compute distance covered by each wheel in this time stamp
    left_wheel_distance = left_wheel_rotation * WHEEL_RADIUS
    right_wheel_distance = right_wheel_rotation * WHEEL_RADIUS

    # Compute the average distance covered by wheels
    distance = (left_wheel_distance + right_wheel_distance) / 2.0

    # Compute the change in orientation of robot in this time stamp
    delta_theta = (right_wheel_distance - left_wheel_distance) / AXLE_LENGTH

    # Update robot position and orientation
    x += distance * cos(theta + delta_theta / 2.0)
    y += distance * sin(theta + delta_theta / 2.0)
    theta += delta_theta

    # Save wheel rotation to next time step
    old_left_wheel_ticks = left_wheel_ticks
    old_right_wheel_ticks = right_wheel_ticks
    #print(f"Position: x={x}, y={y}, theta={theta}")

    # Set motors velicity so robot move in a circle
    left_motor.setVelocity(2)
    right_motor.setVelocity(1)

    # Write robot estimated position to file
    with open('dane.txt', 'a') as f:
        f.write(
            f"{x},{y}, {current_velocity}\n")
