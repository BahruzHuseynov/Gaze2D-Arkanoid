# Gaze2D-Arkanoid
### Computational Intelligence Course Project (ELTE 2025 - Autumn Semester)

# Technology
- **Python**: Main programming language.
- **OpenCV**: Used for capturing video feed and processing the gaze data.
- **Dlib**: Facial landmark detection for gaze tracking.
- **PyGame**: Framework for creating the Breakout game.
- **NumPy**: For efficient array manipulation and calculations.
- **TensorFlow/PyTorch (optional)**: If deep learning-based gaze tracking is implemented.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Prerequisites

- 

## Using this project


1. Clone the project, change into the directory and install the dependencies for server. Create a `.env` file for environment variables in your server and start it.

   ```bash
   git clone <URL>
   cd balanced_diet_tracker/backend
   touch .env
   npm install
   npm start
   ```
   
   See success message of connection and listening on port 5000

2. Install dependencies for cliens and start it. Open a different terminal parallel:

   ```bash
   cd balanced_diet_tracker/frontend
   npm install
   ```

   Run the React application on its own with the command:

   ```bash
   npm start 
   ```

    See browser opening up on port 3000


# 2D Gaze Tracking for Breakout Game Control

This project implements a **2D Gaze Tracking** system that uses appearance-based methods to control the paddle in the **Breakout** game. The system tracks the user's gaze and moves the paddle based on their eye position, providing a unique and engaging way to interact with the game.

## Technologies Used



## Project Structure


## Features

- **Real-Time Eye Gaze Tracking**: Tracks the user’s eye position using their webcam.
- **Breakout Game Control**: The paddle moves based on the user's gaze in the game.
- **Appearance-Based Gaze Detection**: The system uses computer vision techniques to detect and interpret gaze direction.

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
