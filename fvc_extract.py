import numpy as np


def extract(image, mask, bd_specs):
    bd_specs = dict(zip(['border_x', 'border_y', 'step_x', 'step_y'], bd_specs))
    # bd_specs is a dictionary with keys:
    # ['border_x', 'border_y', 'step_x', 'step_y']

    ########################################
    # Insert your algorithm here.
    # It should produce an array, called 'angle', whose values are
    # orientation angles in the range [-π/2, π/2). 
    angle = np.random.randn(image.shape)
    ########################################

    # Convert an angle with values in [-π/2, π/2) to the format required by the competition
    angle = np.remainder(angle, np.pi)
    angle *= 255.0 / np.pi
    return np.round(angle).astype('uint8')