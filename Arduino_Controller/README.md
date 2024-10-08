# Arduino Controller

## Description
This section contains the Arduino sketches used for controlling the smart bulbs in the project. The Arduino interacts with the web server to receive commands and updates the status of the bulbs accordingly.

## Setup Instructions
1. **Dependencies**: Ensure you have the Arduino IDE installed on your computer.
2. **Hardware Requirements**:
   - Arduino board (e.g., Arduino Nano)
   - Relay module (for controlling the bulb)
   - Jumper wires
   - Power supply for the bulb

3. **Installation**:
   - Download and install the Arduino IDE from [the official website](https://www.arduino.cc/en/software).
   - Connect your Arduino board to your computer via USB.

4. **Upload Sketch**:
   - Open the `Arduino_Controller.ino` file in the Arduino IDE.
   - Select the correct board and port from the Tools menu.
   - Click the upload button to upload the sketch to your Arduino board.

## Usage
- Once the sketch is uploaded, the Arduino will connect to the local network (ensure the correct Wi-Fi credentials are set in the code).
- The Arduino listens for commands from the web server to control the bulbs.

## Example
- To turn on a bulb, send a request to the web server with the appropriate parameters.
