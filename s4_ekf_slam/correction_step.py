import sys

import numpy as np

sys.path.append('../tool')
from normalize_angle import *


def normalize_all_bearings(z):
    z[1::2, 0] = normalize_angle(z[1::2, 0])
    return z


def landmark_state_index(landmark_id):
    return 3 + 2 * landmark_id


def correction_step(mu, sigma, z, observed_landmarks):
    measurement_count = len(z)
    dim = mu.shape[0]

    if measurement_count == 0:
        return mu, sigma, observed_landmarks

    Z = np.zeros((2 * measurement_count, 1))
    expected_Z = np.zeros((2 * measurement_count, 1))
    H = np.zeros((2 * measurement_count, dim))

    for i, measurement in enumerate(z):
        landmark_id = measurement['id']
        landmark_index = landmark_state_index(landmark_id)

        if not observed_landmarks[landmark_id]:
            bearing = measurement['bearing'] + mu[2, 0]
            mu[landmark_index, 0] = mu[0, 0] + measurement['range'] * np.cos(bearing)
            mu[landmark_index + 1, 0] = mu[1, 0] + measurement['range'] * np.sin(bearing)
            observed_landmarks[landmark_id] = True

        Z[2 * i:2 * i + 2, 0] = [measurement['range'], measurement['bearing']]

        delta = mu[landmark_index:landmark_index + 2] - mu[0:2]
        dx = delta[0, 0]
        dy = delta[1, 0]
        q = dx * dx + dy * dy
        sqrt_q = np.sqrt(q)

        expected_Z[2 * i, 0] = sqrt_q
        expected_Z[2 * i + 1, 0] = normalize_angle(np.arctan2(dy, dx) - mu[2, 0])

        Hi_low = np.array([
            [-sqrt_q * dx, -sqrt_q * dy, 0, sqrt_q * dx, sqrt_q * dy],
            [dy, -dx, -q, -dy, dx],
        ]) / q

        Fxj = np.zeros((5, dim))
        Fxj[0:3, 0:3] = np.eye(3)
        Fxj[3, landmark_index] = 1
        Fxj[4, landmark_index + 1] = 1

        H[2 * i:2 * i + 2] = Hi_low @ Fxj

    Q = 0.01 * np.eye(2 * measurement_count)
    S = H @ sigma @ H.T + Q
    K = np.linalg.solve(S.T, (sigma @ H.T).T).T

    diff_Z = normalize_all_bearings(Z - expected_Z)

    mu = mu + K @ diff_Z
    mu[2, 0] = normalize_angle(mu[2, 0])
    sigma = (np.eye(dim) - K @ H) @ sigma
    sigma = 0.5 * (sigma + sigma.T)

    return mu, sigma, observed_landmarks
