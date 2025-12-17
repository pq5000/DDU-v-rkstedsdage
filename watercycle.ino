const int IN1_1 = 2;
const int IN1_2 = 3;
const int drainTime = 10000;
const int fillTime = 10000;
const int drainFillDelay = 5000;


const char triggerChar = 'W';

void setPinModes(){
    pinMode(IN1_1, OUTPUT);
    pinMode(IN1_2, OUTPUT);
}
void waterCycle(){
    Serial.println("Beginning draining...");
    digitalWrite(IN1_1, LOW);
    delay(drainTime);
    digitalWrite(IN1_1, HIGH);
    Serial.println("Draining complete!");
    delay(drainFillDelay);
    Serial.println("Beginning filling...");
    digitalWrite(IN1_2, LOW);
    delay(fillTime);
    digitalWrite(IN1_2, HIGH);
    Serial.println("Filling complete!");
}

void resetRelays(){
    Serial.println("Resetting relays...");
    digitalWrite(IN1_1, HIGH);
    digitalWrite(IN1_2, HIGH);
}
void setup() {
    Serial.begin(9600);
    setPinModes();
    resetRelays();
}

void loop() {
    if (Serial.available() > 0) {
        char incomingChar = Serial.read();

        if (incomingChar == triggerChar) {
            waterCycle();
        }
    }
}
