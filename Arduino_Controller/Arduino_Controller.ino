const int ledPins[] = {2, 3, 4, 5, 6};
const int numLeds = 5;
int previousNum = -1;

void setup() {
  Serial.begin(115200); // Start serial communication at 9600 baud rate
  Serial.setTimeout(1); 
  
  for(int i = 0; i < numLeds; i++){
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW); // Turn off all LEDs initially
  }
}

void loop() {
	while (!Serial.available()); 

  int numFingers = Serial.readString().toInt();
  
  if(numFingers > 0 && numFingers < 6  && previousNum != numFingers) {
    for(int i = 0; i < numLeds; i++){
      digitalWrite(ledPins[i], LOW); // Turn off all LEDs initially
    }

    digitalWrite(ledPins[numFingers - 1], HIGH);

    Serial.print(previousNum);
    previousNum = numFingers;
  } else {
    Serial.print(-1);
  }

  // delay(500);
}