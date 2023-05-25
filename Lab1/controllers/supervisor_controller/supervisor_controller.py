from controller import Supervisor
import numpy as np

# Initial time step in miliseconds (should be the same as controller time step)
TIME_STEP = 64

# Create Supervisor
robot = Supervisor()

# Connect supervisor to e-puck robot
e_puck = robot.getFromDef('E-PUCK')

# Clear data file
open('dane_z_supervisora.txt', 'w').close()

# Main loop
while robot.step(TIME_STEP) != -1:
    try:
        # Get field of robot
        translation_field = e_puck.getField('translation')

        # Get robot actuall position
        x, y, z = translation_field.getSFVec3f()
        #print(f'x: {x} y:{y}')

        # Write robot position to file
        with open("dane_z_supervisora.txt", "a") as f:
            f.write(f"{x},{y}\n")
    except Exception as e:
        print(e)
