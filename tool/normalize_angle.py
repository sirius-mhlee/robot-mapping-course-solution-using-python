import numpy as np

def normalize_angle(value):
    return (((value + np.pi) % (2 * np.pi)) - np.pi)
