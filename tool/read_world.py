import numpy as np

def read_world(filepath):
    txt_data = np.loadtxt(filepath)

    world_data = {'id':txt_data[:, 0], 'x':txt_data[:, 1], 'y':txt_data[:, 2]}
    return world_data
