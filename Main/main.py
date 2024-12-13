import cv2
from calibration.calibration import face_mesh, get_iris_center, normalize_coordinates
from calibration.homography import calculate_homography, map_coordinates
from game.game import create_paddle_screen
import numpy as np

# Define calibration points
calibration_points = [
    (100, 100), (960, 100), (1820, 100),
    (100, 540), (960, 540), (1820, 540),
    (100, 980), (960, 980), (1820, 980),
]

# Initialize calibration variables
calibration_data = []
mapping_function = None
calibrated = False
calibration_index = 0
# Define a buffer for smoothing the paddle movement
SMOOTHING_BUFFER_SIZE = 5
paddle_positions = []

# Add paddle smoothing logic
def smooth_paddle_position(new_x):
    global paddle_positions
    # Append the new position
    paddle_positions.append(new_x)
    # Keep the buffer size limited
    if len(paddle_positions) > SMOOTHING_BUFFER_SIZE:
        paddle_positions.pop(0)
    # Return the average position
    return int(np.mean(paddle_positions))

# Screen and paddle settings
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
VIDEO_WIDTH, VIDEO_HEIGHT = 200, 154  # Smaller camera feed dimensions
VIDEO_POSITION_X, VIDEO_POSITION_Y = 50, 50  # Position for camera feed
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 30
paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 50  # Position just above the bottom

# Initialize video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    # Resize the camera feed for a smaller window
    resized_frame = cv2.resize(frame, (VIDEO_WIDTH, VIDEO_HEIGHT))

    # Create the main calibration/game frame
    main_frame = np.zeros((SCREEN_HEIGHT, SCREEN_WIDTH, 3), dtype=np.uint8)

    # Overlay the camera feed in the smaller section
    main_frame[VIDEO_POSITION_Y:VIDEO_POSITION_Y + VIDEO_HEIGHT, VIDEO_POSITION_X:VIDEO_POSITION_X + VIDEO_WIDTH] = resized_frame

    # Check if face landmarks are detected
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            pupil_center = get_iris_center(face_landmarks, frame)
            normalized_x, normalized_y = normalize_coordinates(pupil_center, frame.shape)

            if not calibrated:
                # Display calibration points on the screen
                for i, point in enumerate(calibration_points):
                    if i < calibration_index:
                        continue
                    # Draw the calibration point as a circle
                    cv2.circle(main_frame, point, 15, (0, 255, 0), -1)
                    # Add the point number near the circle
                    cv2.putText(
                        main_frame,
                        str(i + 1),  # Convert the index to a user-friendly 1-based number
                        (point[0] - 10, point[1] - 20),  # Position the number slightly above the circle
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,  # Font size
                        (255, 255, 255),  # White text color
                        2,  # Thickness
                    )
                cv2.putText(
                    main_frame,
                    f"Look at point {calibration_index + 1} and press 'C'",
                    (VIDEO_POSITION_X, VIDEO_POSITION_Y - 20),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 255),
                    2,
                )

                # Check for calibration key press
                if cv2.waitKey(1) & 0xFF == ord('c'):
                    calibration_data.append([normalized_x, normalized_y])
                    calibration_index += 1
                    if calibration_index == len(calibration_points):
                        mapping_function = calculate_homography(calibration_points, calibration_data)
                        calibrated = True
            else:
        
                mapped_coords = map_coordinates(mapping_function, (normalized_x, normalized_y))
                #apply smoothing to the paddle's x-coor
                paddle_x = smooth_paddle_position(max(0, min(mapped_coords[0] - PADDLE_WIDTH // 2, SCREEN_WIDTH - PADDLE_WIDTH)))

    #add paddle and game logic after calibration
    if calibrated:
        main_frame = create_paddle_screen(SCREEN_WIDTH, SCREEN_HEIGHT, paddle_x, paddle_y, resized_frame)

    # Display the result
    cv2.imshow("Gaze Paddle Game", main_frame)

    # Handle quit event
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()