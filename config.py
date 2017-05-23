"""
For each module, put its config variables / constants in its own respective 
"""

class WorldConfig():
    NAME = "CarRacing-v0"

    # POSSIBLE ACTIONS 
    GAS = [0.0, 1.0, 0.0]
    BRAKE = [0.0, 0.0, 0.9]
    LEFT = [-1.0, 0.0, 0.0]
    RIGHT = [1.0, 0.0, 0.0]

    ACTIONS = [GAS, BRAKE, LEFT, RIGHT]

    NUM_ACTIONS = len(ACTIONS)

    # Each state is 3rd dimensional stack of consecutive frames
    NUM_FRAMES_IN_STATE = 5
    WORLD_SIZE = 84


class A3CConfig():
    NUM_THREADS = 1

class ACNetworkConfig():
    LR = 0.001

    FEATURE_DIM = 256