# Might need ros2 launch stretch_core stretch_driver.launch.py in the terminal
import hello_helpers.hello_misc as hm
import time
import numpy as np
# key function of ROS is to use the joint names when sending commands and such. I'll paste them below for convenience.

# joint_arm 
# joint_lift 
# joint_wrist_yaw 
# joint_wrist_pitch 
# joint_wrist_roll 
# joint_gripper_finger_left 
# joint_gripper_finger_right 
# joint_head_pan 
# joint_head_tilt 
# translate_mobile_base 
# rotate_mobile_base

# Create a node class for moving the robot
class MoveNode(hm.HelloNode):
    # Below is from the hello robot tutorial
    def __init__(self):
        hm.HelloNode.__init__(self)
        print("initialized!")
    def main(self):
        print("we tryin")
        hm.HelloNode.main(self, 'my_node', 'my_node', wait_for_first_pointcloud=False)
        print("we ballin")

        # Now we do main movement logic
        self.stow_the_robot() # always stow first
        time.sleep(1.0) # Do we need to sleep between actions? Not sure. Actually, blocking arg should handle this.
        # Recall we need to extend arm and raise the lift SIMULTANEOUSLY
        # self.move_to_pose({'joint_arm': 0.5}, blocking=False) # Setting blocking to False should allow simultaneous movement
        self.move_to_pose({'joint_arm': -0.5, 'joint_lift': 1.1}, blocking=True)
        # self.move_to_pose({'joint_lift': 1.1}, blocking=True)
        # Allow for individual wrist movements
        self.move_to_pose({'joint_wrist_yaw': np.radians(30)}, blocking=True)
        self.move_to_pose({'joint_wrist_pitch': np.radians(30)}, blocking=True)
        self.move_to_pose({'joint_wrist_roll': np.radians(30)}, blocking=True)
        # Now open and close gripper, I'm just going to assume both sides should have the same sign, and 100 to -100 is still valid to start
        self.move_to_pose({'joint_gripper_finger_left': 100.0}, blocking=False)
        self.move_to_pose({'joint_gripper_finger_right': 100.0}, blocking=True) # should be fully good here
        # Now open gripper
        self.move_to_pose({'joint_gripper_finger_left': -100.0}, blocking=False)
        self.move_to_pose({'joint_gripper_finger_right': -100.0}, blocking=True)
        # Now move the robot head
        self.move_to_pose({'joint_head_pan': np.radians(45)}, blocking=True)
        self.move_to_pose({'joint_head_tilt': np.radians(45)}, blocking=True)
        # Stow for base movement
        self.stow_the_robot()
        time.sleep(1.0)
        # Now move the base
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)
        self.move_to_pose({'rotate_mobile_base': np.radians(180)}, blocking=True)
        self.move_to_pose({'translate_mobile_base': 0.5}, blocking=True)

# After defining the class, we still need to create the node and run its main function
node = MoveNode()
node.main()



        