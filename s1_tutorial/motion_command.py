import sys
import numpy as np

sys.path.append('../tool')
from normalize_angle import *

def motion_command(x, u):
    x[0, 0] = x[0, 0] + u['t'] * np.cos(normalize_angle(x[2, 0] + u['r1']))
    x[1, 0] = x[1, 0] + u['t'] * np.sin(normalize_angle(x[2, 0] + u['r1']))
    x[2, 0] = normalize_angle(x[2, 0] + u['r1'] + u['r2'])
    return x
