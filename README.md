# VisionBallGame

##  Description
"HandBallGame is a real-time interactive game using Python, OpenCV, and MediaPipe. Players use their hands to catch moving enemies on the screen. The game tracks hand movements via webcam and updates the score when an enemy is caught, providing an engaging experience through advanced hand-tracking and computer vision technologies."


## Table of Contents


1. [Features](#features)
2. [Usage](#usage)
3. [Code Overview](#code-overview)
4. [Concepts Used](#concepts-used)
5. [Challenges Faced](#challenges-faced)
6. [Images and Videos](#images-and-videos)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)


# Features

- Real-time hand tracking using a webcam
- Interactive gameplay with score tracking
- Dynamic enemy movement
- Easy-to-use interface

# Usage

1.Run the game:

  Open a terminal or command prompt, navigate to the project directory, and execute:

2.Gameplay Instructions:

 - Objective: Use your index finger to catch the moving enemies on the screen.

 - Scoring: The score increases each time an enemy is caught.
   
 - Exit the Game: Press 'q' to quit the game at any time.

3.Controls:

 - Hand Movement: Move your hand in front of the webcam to control the game.
   
 - Enemy Interaction: Position your index finger close to the moving enemy to score points.
   
 - Troubleshooting:
   

4.Webcam Issues:

 - Ensure your webcam is properly connected.
   
 - Performance: Close other applications if you experience lag.
   
 - Detection Accuracy: Ensure good lighting for accurate hand tracking.
   

## Code Overview

```
import mediapipe as mp
import cv2
import numpy as np
import random
import time  

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
score = 0

x_enemy = random.randint(50, 600)
y_enemy = random.randint(50, 400)

def enemy():
    global x_enemy, y_enemy
    cv2.circle(image, (x_enemy, y_enemy), 25, (255, 0, 0), 5)  

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 255, 0)  
        cv2.putText(image, "Score", (480, 30), font, 1, color, 4, cv2.LINE_AA)
        cv2.putText(image, str(score), (590, 30), font, 1, color, 4, cv2.LINE_AA)

        enemy()

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2)
                )

                for point in mp_hands.HandLandmark:
                    normalized_landmark = hand_landmarks.landmark[point]
                    pixel_coordinates = mp_drawing._normalized_to_pixel_coordinates(
                        normalized_landmark.x, normalized_landmark.y, imageWidth, imageHeight
                    )

                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP and pixel_coordinates:
                        cv2.circle(image, (pixel_coordinates[0], pixel_coordinates[1]), 25, (255, 0, 0), 5)  
                        distance = np.sqrt((pixel_coordinates[0] - x_enemy) ** 2 + (pixel_coordinates[1] - y_enemy) ** 2)
                        if distance < 25:
                            print("found")
                            x_enemy = random.randint(50, 600)
                            y_enemy = random.randint(50, 400)
                            score += 1
                            enemy()

        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print(score)
            break

video.release()
cv2.destroyAllWindows()


```



## Libraries Used:

 -OpenCV: For video capture and image processing.
 
 -MediaPipe: For hand tracking and landmark detection.
 
 -NumPy: For mathematical operations.




## Main Components:

 -Video Capture: Captures video from the webcam.
 
 -Hand Detection: Detects and tracks hand landmarks using MediaPipe.
 
 -Enemy Movement: Randomly positions the enemy on the screen.
 
 -Collision Detection: Checks for proximity between the player's finger and enemy to update the score.




## Game Logic:

 -Continuously captures and processes video frames.
 
 -Updates score when the player's finger touches an enemy.
 
 -Moves enemies to new positions when caught.



# Concepts Used

 -Computer Vision: Real-time processing with OpenCV.
 
 -Hand Tracking: MediaPipe for detecting hand landmarks.
 
 -Game Mechanics: Score tracking and interaction through gesture recognition



# Challenges Faced

 -Real-time Processing: Optimizing performance for smooth gameplay.
 
 -Lighting Conditions: Ensuring accurate tracking in different lighting environments.
 
 -Coordinate Mapping: Mapping hand positions to screen coordinates accurately.
 


# Images and Videos


Images

![Screenshot 2024-08-08 183706](https://github.com/user-attachments/assets/ac56695e-47b1-44ff-b14b-bfcef9a84e2e)

"Displays real-time hand recognition with detected hand landmarks and a blue circle indicating tracked positions in the webcam feed."

![Screenshot 2024-08-08 183626](https://github.com/user-attachments/assets/95d003bf-2b2e-49dc-9c3a-4af77a5e3480)

"Displays real-time hand recognition with a blue circle on the index finger and another blue circle representing the enemy target in the webcam feed."


Videos


https://github.com/user-attachments/assets/f5c33444-377b-4e6d-8a51-6ba9c1ae0b68

G-Drive Link

https://drive.google.com/file/d/1z71S2z2AnT5i7tsJWebQKhzyeNONLhoL/view?usp=sharing


# Future Enhancements

-Add more levels with increasing difficulty.

-Include additional gestures for diverse interactions.

-Enhance UI design and add sound effects for better user experience.





