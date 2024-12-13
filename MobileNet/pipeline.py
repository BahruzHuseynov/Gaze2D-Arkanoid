import cv2
import mediapipe as mp
import torch
from torchvision import transforms
from PIL import Image
import numpy as np

# Load MobileNetV3 model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class MobileNetV3Custom(torch.nn.Module):
    def __init__(self):
        super(MobileNetV3Custom, self).__init__()
        self.base_model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v3_small', weights=None)
        in_features = self.base_model.classifier[0].in_features
        self.base_model.classifier = torch.nn.Identity()  # Remove default classifier
        self.coords_head = torch.nn.Sequential(
            torch.nn.Linear(in_features, 128),
            torch.nn.ReLU(),
            torch.nn.Linear(128, 4)  # Predict 4 coordinates
        )

    def forward(self, x):
        features = self.base_model(x)
        return self.coords_head(features)

# Initialize and load the model
model = MobileNetV3Custom().to(device)
model.load_state_dict(torch.load("MobileNet/mobilenetv3_best50.pth", map_location=device))
model.eval()

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Initialize Mediapipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh

# Start webcam and process frames
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define VideoWriter to save the video
out = cv2.VideoWriter("pupil_detection.avi", cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6) as face_mesh:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Unable to access the webcam")
            break

        # Flip and convert the frame to RGB
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with Mediapipe
        results = face_mesh.process(rgb_frame)

        # If a face is detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape

                # Calculate a single bounding box around both eyes
                left_eye = [face_landmarks.landmark[i] for i in [33, 133]]
                right_eye = [face_landmarks.landmark[i] for i in [362, 263]]
                eye_coords = left_eye + right_eye

                x_coords = [int(landmark.x * w) for landmark in eye_coords]
                y_coords = [int(landmark.y * h) for landmark in eye_coords]

                x_min, x_max = min(x_coords), max(x_coords)
                y_min, y_max = min(y_coords), max(y_coords)

                # Enlarge the bounding box
                padding = 20
                x_min = max(0, x_min - padding)
                x_max = min(w, x_max + padding)
                y_min = max(0, y_min - padding)
                y_max = min(h, y_max + padding)

                # Crop the eye region
                cropped_region = frame[y_min:y_max, x_min:x_max]
                pil_image = Image.fromarray(cv2.cvtColor(cropped_region, cv2.COLOR_BGR2RGB))

                # Preprocess and predict with MobileNetV3
                input_tensor = transform(pil_image).unsqueeze(0).to(device)
                with torch.no_grad():
                    preds = model(input_tensor).cpu().numpy()[0]

                # Denormalize predictions
                preds[0] = preds[0] * cropped_region.shape[1] + x_min
                preds[1] = preds[1] * cropped_region.shape[0] + y_min
                preds[2] = preds[2] * cropped_region.shape[1] + x_min
                preds[3] = preds[3] * cropped_region.shape[0] + y_min

                # Draw pupil centers
                cv2.circle(frame, (int(preds[0]), int(preds[1])), 3, (0, 255, 0), -1)  # Left pupil
                cv2.circle(frame, (int(preds[2]), int(preds[3])), 3, (0, 0, 255), -1)  # Right pupil

        # Write the frame to the video file
        out.write(frame)

        # Display the frame
        cv2.imshow("Pupil Detection", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()