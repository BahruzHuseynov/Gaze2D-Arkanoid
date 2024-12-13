import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True, max_num_faces=1)

# Function to calculate Euclidean distance
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Webcam feed
cap = cv2.VideoCapture(0)

# Get frame width, height, and FPS
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Initialize VideoWriter
out = cv2.VideoWriter('eye_status_detection.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Eyelid, canthus, and iris landmark indices
            left_eye_landmarks = [159, 145, 33, 133]  # Upper, lower, left, right (left eye)
            right_eye_landmarks = [386, 374, 362, 263]  # Upper, lower, left, right (right eye)
            left_iris_indices = [469, 470, 471, 472]
            right_iris_indices = [474, 475, 476, 477]

            def get_coordinates(index):
                """Get (x, y) coordinates for a landmark."""
                x = int(face_landmarks.landmark[index].x * frame.shape[1])
                y = int(face_landmarks.landmark[index].y * frame.shape[0])
                return x, y

            def calculate_bounding_box(landmarks):
                """Calculate the bounding box for a set of landmarks."""
                coords = [get_coordinates(i) for i in landmarks]
                min_x = min([p[0] for p in coords])
                min_y = min([p[1] for p in coords])
                max_x = max([p[0] for p in coords])
                max_y = max([p[1] for p in coords])
                return (min_x, min_y), (max_x, max_y)

            # Calculate bounding boxes for eyes
            left_eye_box = calculate_bounding_box(left_eye_landmarks)
            right_eye_box = calculate_bounding_box(right_eye_landmarks)

            # Draw bounding boxes for both eyes
            cv2.rectangle(frame, left_eye_box[0], left_eye_box[1], (0, 255, 0), 1)  # Green for left eye
            cv2.rectangle(frame, right_eye_box[0], right_eye_box[1], (255, 0, 0), 1)  # Blue for right eye

            # Always draw eyelid middle points
            cv2.circle(frame, get_coordinates(left_eye_landmarks[0]), 2, (0, 255, 255), -1)  # Yellow for left upper
            cv2.circle(frame, get_coordinates(left_eye_landmarks[1]), 2, (0, 255, 255), -1)  # Yellow for left lower
            cv2.circle(frame, get_coordinates(right_eye_landmarks[0]), 2, (255, 255, 0), -1)  # Cyan for right upper
            cv2.circle(frame, get_coordinates(right_eye_landmarks[1]), 2, (255, 255, 0), -1)  # Cyan for right lower

            # Draw iris landmarks and pupil center only if the respective eye is open
            left_eye_height = calculate_distance(
                get_coordinates(left_eye_landmarks[0]), get_coordinates(left_eye_landmarks[1])
            )
            right_eye_height = calculate_distance(
                get_coordinates(right_eye_landmarks[0]), get_coordinates(right_eye_landmarks[1])
            )
            threshold = 4  # Adjust based on resolution and application
            left_eye_open = left_eye_height > threshold
            right_eye_open = right_eye_height > threshold

            if left_eye_open:
                left_coords = [get_coordinates(i) for i in left_iris_indices]
                left_center_x = (left_coords[0][0] + left_coords[2][0]) // 2
                left_center_y = (left_coords[1][1] + left_coords[3][1]) // 2
                left_pupil_center = (left_center_x, left_center_y)

                # Draw landmarks and pupil center for left eye
                for x, y in left_coords:
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)  # Green for left iris
                cv2.circle(frame, left_pupil_center, 1, (0, 255, 0), -1)  # Green for left pupil

            if right_eye_open:
                right_coords = [get_coordinates(i) for i in right_iris_indices]
                right_center_x = (right_coords[0][0] + right_coords[2][0]) // 2
                right_center_y = (right_coords[1][1] + right_coords[3][1]) // 2
                right_pupil_center = (right_center_x, right_center_y)

                # Draw landmarks and pupil center for right eye
                for x, y in right_coords:
                    cv2.circle(frame, (x, y), 1, (255, 0, 0), -1)  # Blue for right iris
                cv2.circle(frame, right_pupil_center, 1, (255, 0, 0), -1)  # Blue for right pupil

            # Display eye status
            cv2.putText(frame, f"Left Eye: {'Open' if left_eye_open else 'Closed'}", 
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) if left_eye_open else (0, 0, 255), 1)
            cv2.putText(frame, f"Right Eye: {'Open' if right_eye_open else 'Closed'}", 
                        (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0) if right_eye_open else (0, 0, 255), 1)

    # Write the frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow('Eye Status and Bounding Boxes', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()