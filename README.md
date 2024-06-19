# Intelligent Trolly with automatic invoice system

This project is a prototype of a smart shopping trolley equipped with an automatic billing system. The system uses an RFID reader to scan items, a touch sensor to handle item addition or removal, and an OLED display to show the current total bill and other messages.

## Features
- RFID Scanning: Scan RFID tags to add or remove items from the cart.
- Touch Sensor: Use the touch sensor to indicate item removal.
- OLED Display: Display current total bill, scanned items, and messages.
## Components
- Arduino (compatible) board
- RFID reader (e.g., MFRC522)
- Touch sensor
- OLED display (e.g., Adafruit SSD1306)
- Various items with RFID tags
## How It Works
### Initialization:

The OLED display initializes and shows a welcome message.
### RFID Tag Scanning:

- The system reads the RFID tags of items to add or remove them from the cart.
- If the touch sensor is not held, scanning an RFID tag adds the item to the cart.
- If the touch sensor is held, scanning an RFID tag removes the item from the cart, if it exists.
### Display:

- The current total bill is displayed on the OLED screen after each action.
- Messages such as item scanned, item removed, or unknown item are displayed accordingly.
## Setup
### Hardware Setup:

- Connect the RFID reader to the Arduino.
- Connect the touch sensor to a digital pin on the Arduino.
- Connect the OLED display to the Arduino using I2C.
