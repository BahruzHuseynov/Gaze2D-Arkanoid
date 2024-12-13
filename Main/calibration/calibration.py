import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)

def get_iris_center(face_landmarks, frame):
    left_iris_indices = [469, 470, 471, 472]

    def get_coordinates(index):
        x = int(face_landmarks.landmark[index].x * frame.shape[1])
        y = int(face_landmarks.landmark[index].y * frame.shape[0])
        return x, y

    left_coords = [get_coordinates(i) for i in left_iris_indices]
    left_center_x = (left_coords[0][0] + left_coords[2][0]) // 2
    left_center_y = (left_coords[1][1] + left_coords[3][1]) // 2
    return left_center_x, left_center_y

def normalize_coordinates(pupil_center, frame_shape):
    normalized_x = pupil_center[0] / frame_shape[1]
    normalized_y = pupil_center[1] / frame_shape[0]
    return normalized_x, normalized_y
