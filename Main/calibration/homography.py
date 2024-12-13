import cv2
import numpy as np

def calculate_homography(calibration_points, normalized_points):
    screen_coords = np.array(calibration_points, dtype=np.float32)
    webcam_coords = np.array(normalized_points, dtype=np.float32)
    if len(webcam_coords) == len(screen_coords):
        return cv2.findHomography(webcam_coords, screen_coords)[0]  # Homography matrix
    return None

def map_coordinates(homography_matrix, normalized_coords):
    input_coords = np.array([[normalized_coords[0], normalized_coords[1], 1]], dtype=np.float32).T
    screen_coords = np.dot(homography_matrix, input_coords)
    screen_coords /= screen_coords[2]  # Normalize homogeneous coordinates
    return int(screen_coords[0]), int(screen_coords[1])
