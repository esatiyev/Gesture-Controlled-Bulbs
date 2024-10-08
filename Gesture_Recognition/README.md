# Gesture Recognition

## Description
This section contains the Python scripts used for detecting hand gestures to control the smart bulbs. The script processes video input and recognizes gestures to send commands to the web server.

## Setup Instructions
1. **Dependencies**: Ensure you have Python installed on your computer.
2. **Required Libraries**: Install the following libraries using pip:
   ```bash
   pip install opencv-python mediapipe requests


### Modify
Before running the Gesture Detection component, please ensure to update the necessary configuration settings in the gesture_detection.py file:
Locate the following line (line 20) of code where the port value is defined:
PORT = <your_port_value_here>
Change <your_port_value_here> to the appropriate port number for your setup.


