import numpy as np
import cv2
import pyautogui
import random

# Screen and paddle settings
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
PADDLE_WIDTH, PADDLE_HEIGHT = 400, 50
BALL_RADIUS = 30
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLUMNS
BRICK_HEIGHT = 50

# Initialize bricks and their colors
bricks = np.ones((BRICK_ROWS, BRICK_COLUMNS), dtype=int)
brick_colors = [
    [tuple(random.randint(0, 255) for _ in range(3)) for _ in range(BRICK_COLUMNS)]
    for _ in range(BRICK_ROWS)
]

# Ball settings
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
ball_dx, ball_dy = 5, -5  # Ball velocity

def create_paddle_screen(screen_width, screen_height, paddle_x, paddle_y, video_frame):
    global ball_x, ball_y, ball_dx, ball_dy, bricks
    
    paddle_x = max(0, min(paddle_x, screen_width - PADDLE_WIDTH))
    # Create the full game screen
    full_screen = np.zeros((screen_height, screen_width, 3), dtype=np.uint8)

    # Draw the paddle
    cv2.rectangle(
        full_screen,
        (paddle_x, paddle_y),
        (paddle_x + PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT),
        (255, 0, 0), -1
    )

    # Draw the ball
    cv2.circle(full_screen, (ball_x, ball_y), BALL_RADIUS, (0, 255, 0), -1)

    # Define space between bricks
    BRICK_GAP = 10  # Adjust this value to change the space between bricks

    # Draw the bricks with solid colors and space between them
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            if bricks[row, col] == 1:  # Draw only active bricks
                # Calculate positions with gap between bricks
                top_left = (col * (BRICK_WIDTH + BRICK_GAP), row * (BRICK_HEIGHT + BRICK_GAP))
                bottom_right = (top_left[0] + BRICK_WIDTH, top_left[1] + BRICK_HEIGHT)

                # Draw the solid color brick
                cv2.rectangle(
                    full_screen,
                    top_left,
                    bottom_right,
                    brick_colors[row][col],
                    -1
                )


    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= screen_width:
        ball_dx = -ball_dx
    if ball_y - BALL_RADIUS <= 0:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if paddle_y <= ball_y + BALL_RADIUS <= paddle_y + PADDLE_HEIGHT and \
       paddle_x <= ball_x <= paddle_x + PADDLE_WIDTH:
        ball_dy = -ball_dy

    # Ball collision with bricks
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            if bricks[row, col] == 1:  # Check only active bricks
                brick_top_left = (col * (BRICK_WIDTH + BRICK_GAP), row * (BRICK_HEIGHT + BRICK_GAP))
                brick_bottom_right = (brick_top_left[0] + BRICK_WIDTH, brick_top_left[1] + BRICK_HEIGHT)
                if (brick_top_left[0] <= ball_x <= brick_bottom_right[0] and
                        brick_top_left[1] <= ball_y <= brick_bottom_right[1]):
                    bricks[row, col] = 0  # Destroy the brick
                    ball_dy = -ball_dy  # Reflect the ball
                    break

    # Reset the ball if it goes below the screen
    if ball_y - BALL_RADIUS > screen_height:
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_dx, ball_dy = 5, -5

    # Overlay the webcam feed
    video_width, video_height = video_frame.shape[1], video_frame.shape[0]
    full_screen[:video_height, :video_width] = video_frame

    return full_screen
