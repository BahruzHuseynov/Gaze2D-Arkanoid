# Gaze2D-Arkanoid

# Balanced Diet Tracker Full-Stack Application
### Advanced Software Technology (ELTE 2024 Spring)

# Technology
- Frontend: ReactJS
- Backend: NodeJS with Express
- Database: MongoDB running on Atlas
- Auth: JWT
- Recommender system: Python & Uvicorn

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB) ![Mongo](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white) ![DigitalOcean](https://img.shields.io/badge/DigitalOcean-%230167ff.svg?style=for-the-badge&logo=digitalOcean&logoColor=white) ![React](https://shields.io/badge/react-black?logo=react&style=for-the-badge) ![!JWT](https://img.shields.io/badge/json%20web%20tokens-323330?style=for-the-badge&logo=json-web-tokens&logoColor=pink) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Prerequisites

- Node.js installed on your system.
- npm (Node Package Manager) installed on your system.

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

## API Base URL

The base URL for all API requests is `localhost:PORT` or `balanced-diet-tracker-uzqit.ondigitalocean.app`

## Authentication

API requests must include a predefined _Authorization_ header with a valid token.

- Key: `x-auth-token`
- Value: `<JWT_TOKEN>` from /login or /register route

## API Routes

### Get Meal

- **Route:** `/get-meal/:id`
- **Method:** GET
- **Description:** Retrieves a meal from the database based on its ID.
- **Parameters:**
  - `id`: The unique identifier of the meal.
- **Middleware:** `auth`
- **Controller:** `getMeal`

### Get Meals

- **Route:** `/get-meals`
- **Method:** GET
- **Description:** Retrieves all meals from the database.
- **Middleware:** `auth`
- **Controller:** `getMeals`

### Add Meal

- **Route:** `/add-meal`
- **Method:** POST
- **Description:** Adds a new meal to the database.
- **Middleware:** `auth`
- **Controller:** `addMeal`

### Delete Meal

- **Route:** `/delete-meal/:id`
- **Method:** DELETE
- **Description:** Deletes a meal from the database based on its ID.
- **Parameters:**
  - `id`: The unique identifier of the meal.
- **Middleware:** `auth`
- **Controller:** `deleteMeal`

### Recommend Meal

- **Route:** `/recommend-meal`
- **Method:** POST
- **Description:** Retrieves several meals from the recommender system based on user daily details.
- **Middleware:** `auth`
- **Controller:** `getRecommendedMeals`

### Get Exercises

- **Route:** `/get-exercises`
- **Method:** GET
- **Description:** Retrieves all Exercises from the database.
- **Middleware:** `auth`
- **Controller:** `getExercises`

### Add Exercise

- **Route:** `/add-exercise`
- **Method:** POST
- **Description:** Adds a new Exercise to the database.
- **Middleware:** `auth`
- **Controller:** `addExercise`

### Delete Exercise

- **Route:** `/delete-exercise/:id`
- **Method:** DELETE
- **Description:** Deletes a Exercise from the database based on its ID.
- **Parameters:**
  - `id`: The unique identifier of the Exercise.
- **Middleware:** `auth`
- **Controller:** `deleteExercise`

### Get Categories

- **Route:** `/get-categories`
- **Method:** GET
- **Description:** Retrieves all static 4 categories from the database.
- **Middleware:** `auth`
- **Controller:** `getCategories`

### Get User

- **Route:** `/get-user`
- **Method:** GET
- **Description:** Retrieves information for the logged in user from the database.
- **Middleware:** `auth`
- **Controller:** `getUser`

### Modify User

- **Route:** `/modify-user`
- **Method:** PUT
- **Description:** Updates logged in user attributes.
- **Middleware:** `auth`
- **Controller:** `modifyUser`

## Auth Routes

### Register

- **Route:** `/register`
- **Method:** POST
- **Description:** Registers a new user.
- **Controller:** `register`

### Login

- **Route:** `/login`
- **Method:** POST
- **Description:** Logs in a user.
- **Controller:** `login`

## DigitalOcean Droplet connection

Continuous deployment is live to a DigitalOcean Droplet, and the app is auto-updating relative to changes to the main branch.

[![DigitalOcean Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg)](https://www.digitalocean.com/?refcode=032964bbbea4)

Made with ❤️ and JavaScript.



# 2D Gaze Tracking for Breakout Game Control

This project implements a **2D Gaze Tracking** system that uses appearance-based methods to control the paddle in the **Breakout** game. The system tracks the user's gaze and moves the paddle based on their eye position, providing a unique and engaging way to interact with the game.

## Technologies Used

- **Python**: Main programming language.
- **OpenCV**: Used for capturing video feed and processing the gaze data.
- **Dlib**: Facial landmark detection for gaze tracking.
- **PyGame**: Framework for creating the Breakout game.
- **NumPy**: For efficient array manipulation and calculations.
- **TensorFlow/PyTorch (optional)**: If deep learning-based gaze tracking is implemented.

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
