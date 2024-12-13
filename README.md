# Gaze2D-Arkanoid
## Computational Intelligence Course Project (ELTE 2025 - Autumn Semester)

This project implements a **2D Gaze Tracking** system that uses appearance-based methods to control the paddle in the **Breakout** game. The system tracks the user's gaze and moves the paddle based on their eye position, providing a unique and engaging way to interact with the game.

# Technology
- **Python**: Main programming language. ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **OpenCV**: Used for capturing video feed and processing the gaze data. <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/OpenCV-Dark.svg" alt="OpenCV" width="30" />
- **MediaPipe**: Open-source framework for building pipelines to apply computer vision inference over video. <img src = "https://viz.mediapipe.dev/logo.png" alt = "MediaPipe" width = "30"/>
- **PyAutoGui**: Graphic User Interface for creating the Breakout game. <img src = "https://miro.medium.com/v2/resize:fit:1200/0*N2n8UFCISGIEr1lH.jpeg" alt = "PyAutoGUI" width = "50" />
- **NumPy**: For efficient array manipulation and calculations. <img src = "https://user-images.githubusercontent.com/50221806/86498208-af4bfe00-bd39-11ea-88fa-c747ae0ddd85.png" alt = "NumPy" width = "30"/>
- **PyTorch**: If deep learning-based gaze tracking is implemented. <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/PyTorch-Dark.svg" alt="PyTorch" width="30" />

## Prerequisites
- Creation of the virtual environment is recommended
- Make sure you have **Python 3.x** installed. You can check this by running:
```bash python --version```

## Using this project

1. Clone the project to use and apply changes

   ```bash
   git clone <URL>
   cd Gaze2D-Arkanoid
   ```
   
   See success message of connection and listening on port 5000

2. Install the required libraries by the command below **after cloning the project**

```pip install -r requirements.txt```

## Project Structure


1. MobileNet Folder
- Contains a Jupyter Notebook that has been fine-tuned on a public dataset.
- Combines MediaPipe outputs with the MobileNetV3 architecture.
- Uses MediaPipe to obtain two eye boundary boxes.
- Passes these boundary boxes into the MobileNetV3 model to predict the pupil centers for both eyes.
  
2. MediaPipe Folder
- Detect eye boundary boxes and dentify the pupil and iris.
- Determine whether the eye is open or closed.
  
3. Main Folder
- main.py: The primary script that combines the functionalities of both MobileNet and MediaPipe.
- Calibration Folder: Contains scripts and resources for system calibration.
- Game Folder: Contains the code and resources for the interactive game integrated with gaze detection.


### Acknowledgments
This project leverages the following tools and frameworks:

- MediaPipe by Facebook
- MobileNetV3: A lightweight deep learning architecture used for fine-tuned model inference.

We thank the developers and maintainers of these tools for their valuable contributions to the open-source community.
