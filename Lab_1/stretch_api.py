# For operating Stretch using its given API
import time
import stretch_body.robot
import numpy as np
# Create and start our robot object
robot = stretch_body.robot.Robot()
robot.startup()
print("this is running")
# First, stow the robot
robot.stow()
robot.push_command()

# Next, move the arm all the way out and the lift all the way up
robot.arm.move_to(0.5)
robot.lift.move_to(0.4)
robot.push_command()
robot.arm.wait_until_at_setpoint() # Wait for things to move
robot.lift.wait_until_at_setpoint()

# Move all three wrist motors
robot.end_of_arm.move_to('wrist_yaw', np.radians(30))
robot.push_command()
time.sleep(2.0) # move each wrist motor independently
robot.end_of_arm.move_to('wrist_roll', np.radians(30))
robot.push_command()
time.sleep(2.0)
robot.end_of_arm.move_to('wrist_pitch', np.radians(30))
robot.push_command(0)
time.sleep(2.0)

# Move the head
robot.head.move_by('head_pan', np.radians(45))
robot.push_command()
time.sleep(1.0)
robot.head.move_by('head_tilt', np.radians(45))
robot.push_command()
time.sleep(1.0)

# Stow the robot
robot.stow()
robot.push_command()

# Move the base
robot.base.translate_by(0.5)
robot.push_command()
robot.base.rotate_by(np.radians(180))
robot.push_command()
robot.base.translate_by(0.5)
# Stop the robot
robot.stop()