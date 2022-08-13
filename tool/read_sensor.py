import numpy as np

def read_sensor(filepath):
    txt_data = np.genfromtxt(filepath, dtype=np.object)

    sensor_data = {'odometry':[], 'sensor':[]}
    sensor_info_between_odometry = []

    for line in txt_data:
        if line[0] == b'ODOMETRY':
            if sensor_info_between_odometry:
                sensor_data['sensor'].append(sensor_info_between_odometry)
                sensor_info_between_odometry = []

            sensor_data['odometry'].append({'r1':float(line[1]), 't':float(line[2]), 'r2':float(line[3])})

        elif line[0] == b'SENSOR':
            sensor_info_between_odometry.append({'id':int(line[1]) - 1, 'range':float(line[2]), 'bearing':float(line[3])})

    if sensor_info_between_odometry:
        sensor_data['sensor'].append(sensor_info_between_odometry)

    return sensor_data
