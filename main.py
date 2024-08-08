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

