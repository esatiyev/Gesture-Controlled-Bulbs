import cv2
import mediapipe as mp

import serial
import time

import requests

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)  # Detect only one hand
drawing_styles = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)

# Initialize webcam
cap = cv2.VideoCapture(0)


# # Set up serial communication with Arduino
PORT = 'COM5' # Change this to the port where your Arduino is connected
arduino = serial.Serial(port=PORT, baudrate=115200, timeout=.1) 

def send_http_request(bulbNumber: int, state: str):
    url = "http://intern.agarmen.com:8080/bulb_project/bulb.php"

    data = {
        "bulb_number": bulbNumber,
        "status": state
    }

    try:
        response = requests.post(url, json=data)
        print(f"Response from server: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error sending HTTP request: {e}")



def write_read(num_fingers): 
    arduino.write(bytes(num_fingers, 'utf-8')) 
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').strip()

    if(data != "-1"):  # -1 is the value returned by Arduino if no bulb changed its state
        send_http_request(int(data), "OFF")
        send_http_request(int(num_fingers), "ON")
    

def count_fingers(hand_landmarks):
    if not hand_landmarks:
        return 0

    # Indices of finger tips
    finger_tips = [4, 8, 12, 16, 20]  
    fingers_up = 0

    # Separate thumb detection
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[3]  # Joint before the tip
    if thumb_tip.y < thumb_ip.y - 0.05:
        fingers_up += 1

    # Check other fingers
    for i in range(1, len(finger_tips)):  # Start from index 1 to skip the thumb
        tip = hand_landmarks.landmark[finger_tips[i]]
        pip = hand_landmarks.landmark[finger_tips[i] - 2]  # The joint before the tip
        if tip.y < pip.y - 0.05:  # Adjust the threshold value if necessary
            fingers_up += 1

    return fingers_up


last_sent_time = time.time()
send_interval = 1  # Interval in seconds

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Create a copy of the image to draw hand landmarks
    image_with_annotations = image.copy()

    # Draw hand annotations on the copied image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image_with_annotations, hand_landmarks, mp_hands.HAND_CONNECTIONS, drawing_styles, drawing_styles)
            # num_fingers = count_fingers(hand_landmarks)
            # cv2.putText(image_with_annotations, f'Fingers: {num_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Flip the image horizontally to create a mirror effect
    image_mirrored = cv2.flip(image_with_annotations, 1)

###
    # Convert the mirrored image to RGB for text drawing
    image_mirrored_rgb = cv2.cvtColor(image_mirrored, cv2.COLOR_BGR2RGB)

    # Draw the text on the mirrored image
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            num_fingers = count_fingers(hand_landmarks)
            # Convert the image to RGB for text drawing
            image_mirrored_rgb = cv2.cvtColor(image_mirrored, cv2.COLOR_BGR2RGB)
            cv2.putText(image_mirrored_rgb, f'Fingers: {num_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            write_read(str(num_fingers))
            # Send the number of fingers to Arduino if the interval has passed
            # if time.time() - last_sent_time > send_interval:
            #     arduino.write(f"{num_fingers}\n".encode())  # Send data as a string with newline
            #     last_sent_time = time.time()

    # Convert back to BGR for display
    image_mirrored = cv2.cvtColor(image_mirrored_rgb, cv2.COLOR_RGB2BGR)

###

    # Display the mirrored image
    cv2.imshow('Hand Gesture Detection', image_mirrored)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()