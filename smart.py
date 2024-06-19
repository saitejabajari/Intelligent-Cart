#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// Define OLED display parameters
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
#define OLED_ADDRESS  0x3C  // I2C address for the OLED display
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Define global variables
float totalBill = 0.0;  // Variable to store the total bill amount
bool touchHeld = false;  // Flag to track touch sensor state

// Counters for each item
int milkCount = 0;
int juiceCount = 0;
int breadCount = 0;
int jamCount = 0;

// Pin definitions
const int touchPin = 2;  // Pin for the touch sensor (example: connected to digital pin 2)

void setup() {
  Serial.begin(9600);     // Initialize serial communication with the PC
  Serial2.begin(9600, SERIAL_8N1, 16, 17);  // Initialize serial communication with the RFID reader on pins 16 (RX) and 17 (TX)
  
  pinMode(touchPin, INPUT);  // Set touch sensor pin as input
  
  // Initialize OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }
  display.clearDisplay();
  display.display();

  // Print initial message
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Welcome to Smart Shopping!");
  display.println("Scan RFID tags to add");
  display.println("or remove items from your cart.");
  display.display();
}

void loop() {
  // Check for touch sensor activation
  if (digitalRead(touchPin) == HIGH) {
    touchHeld = true;
  } else {
    touchHeld = false;  // Reset touch sensor state
  }
  
  // RFID tag scanning
  if (Serial2.available()) {
    String rfidNumber = "";  // String to store RFID card number
    
    // Read the data from the RFID reader
    while (Serial2.available()) {
      char c = Serial2.read();
      rfidNumber += c;
      delay(10); // Delay to allow buffer to fill with next character
    }
    
    // Perform action based on touch sensor state and RFID card number
    if (rfidNumber.equals("150026F45D9A")) {
      handleItem("milk", 40.0, milkCount);
    } else if (rfidNumber.equals("090031EB2AF9")) {
      handleItem("juice", 30.0, juiceCount);
    } else if (rfidNumber.equals("180045AF00F2")) {
      handleItem("bread", 50.0, breadCount);
    } else if (rfidNumber.equals("19007EBFA27A")) {
      handleItem("jam", 20.0, jamCount);
    } else {
      // Handle unknown or unhandled cards if needed
      displayMessage("Unknown item or card");
    }
    
    // Display current total bill
    displayTotalBill();
  }
}

// Function to handle item addition or removal based on touch sensor state
void handleItem(String item, float price, int &count) {
  if (touchHeld) {
    // If touch sensor is held, remove item if count is greater than 0
    if (count > 0) {
      reduceTotalBill(item, price, count);
    } else {
      displayMessage("Cannot remove more of item: " + item);
    }
  } else {
    // If touch sensor is not held, add item
    addItemToCart(item, price, count);
  }
}

// Function to add item to the total bill
void addItemToCart(String item, float price, int &count) {
  count++;  // Increment the count for the item
  totalBill += price;
  displayMessage("Item scanned: " + item + " - Price: $" + String(price) + " - Count: " + String(count));
}

// Function to reduce total bill when holding the touch sensor
void reduceTotalBill(String item, float price, int &count) {
  count--;  // Decrement the count for the item
  totalBill -= price;
  displayMessage("Item removed from cart: " + item + " - Price: $" + String(price) + " - Updated Count: " + String(count));
}

// Function to display a message on the OLED display
void displayMessage(String message) {
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println(message);
  display.display();
}

// Function to display the total bill on the OLED display
void displayTotalBill() {
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Total Bill: $");
  display.println(totalBill);
  display.display();
}