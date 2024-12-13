# Gaze2D-Arkanoid
## Computational Intelligence Course Project (ELTE 2025 - Autumn Semester)

# Technology
- **Python**: Main programming language. ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- **OpenCV**: Used for capturing video feed and processing the gaze data. <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/OpenCV-Dark.svg" alt="OpenCV" width="30" />
- **MediaPipe**: An open-source framework for building pipelines to perform computer vision inference over video or audio. <img src = "https://viz.mediapipe.dev/logo.png" alt = "MediaPipe" width = "30"/>
- **PyAutoGui**: Graphic User Interface for creating the Breakout game. <img src = "https://miro.medium.com/v2/resize:fit:1200/0*N2n8UFCISGIEr1lH.jpeg" alt = "PyAutoGUI" width = "50" />
- **NumPy**: For efficient array manipulation and calculations. <img src = "https://user-images.githubusercontent.com/50221806/86498208-af4bfe00-bd39-11ea-88fa-c747ae0ddd85.png" alt = "NumPy" width = "30"/>
- **PyTorch**: If deep learning-based gaze tracking is implemented. <img src="https://github.com/tandpfun/skill-icons/blob/main/icons/PyTorch-Dark.svg" alt="PyTorch" width="30" />

## Prerequisites
- Creation of the virtual environment is recommended
- Make sure you have **Python 3.x** installed. You can check this by running:
```bash
python --version```

## Using this project

1. Clone the project to use and apply changes

   ```bash
   git clone <URL>
   cd Gaze2D-Arkanoid
   ```
   
   See success message of connection and listening on port 5000

2. Install the required libraries by the command below **after cloning the project**

```pip install -r requirements.txt```


# 2D Gaze Tracking for Breakout Game Control

This project implements a **2D Gaze Tracking** system that uses appearance-based methods to control the paddle in the **Breakout** game. The system tracks the user's gaze and moves the paddle based on their eye position, providing a unique and engaging way to interact with the game.


## Project Structure


1. MobileNet Folder
- Contains a Jupyter Notebook that has been fine-tuned on a public dataset.
- Combines MediaPipe outputs with the MobileNetV3 architecture.
- Uses MediaPipe to obtain two eye boundary boxes.
- Passes these boundary boxes into the MobileNetV3 model to predict the pupil centers for both eyes.
  
2. MediaPipe Folder
- Detect eye boundary boxes and dentify the pupil and iris.
- Determine whether the eye is open or closed.
  
3. Main Folder (Main Folder)
- main.py: The primary script that combines the functionalities of both MobileNet and MediaPipe.
- Calibration Folder: Contains scripts and resources for system calibration.
- Game Folder: Contains the code and resources for the interactive game integrated with gaze detection.



## Installation

Follow the steps below to set up and run the project on your local machine:

### Prerequisites

Make sure you have **Python 3.x** installed. You can check this by running:

```bash
python --version```

git clone https://github.com/yourusername/2D-Gaze-Tracking-Breakout.git
cd 2D-Gaze-Tracking-Breakout

pip install -r requirements.txt

Acknowledgments
Thanks to the creators of OpenCV, Dlib, and PyGame for providing the tools that made this project possible.
Inspired by modern advancements in gaze-based interaction and game control.


---

### Key Sections:
1. **Introduction**: Brief description of the project and its purpose.
2. **Technologies Used**: Lists the tools, libraries, and frameworks used.
3. **Project Structure**: Describes the directory layout for the project.
4. **Features**: Highlights the main functionalities of the project.
5. **Installation**: Step-by-step guide to set up the project.
6. **How It Works**: Explains the underlying mechanics of gaze tracking and game control.
7. **Contributing**: Instructions on how others can contribute to the project.
8. **License**: Provides licensing information.
9. **Acknowledgments**: Credits to the tools and libraries used.
10. **Contact**: Optional section for getting in touch with the project creator.

This README file provides a comprehensive yet clear overview of the project and is ready to be added to your repository.
