"""
Tutorials
- Arduino MicroPython - LED Matrix 8x8: https://newbiely.com/tutorials/arduino-micropython/arduino-micropython-led-matrix
- ESP32 MicroPython - LED Matrix 8x8: https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-led-matrix
- Raspberry Pi Pico - LED Matrix 8x8: https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-led-matrix
"""

from machine import Pin, SPI
from time import sleep
from DIYables_MicroPython_LED_Matrix import Max7219

# Example usage:
# Initialize SPI and CS pin
spi = SPI(0, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
cs = Pin(21, Pin.OUT)

# Initialize the Max7219 class
display = Max7219(spi, cs, num_matrices=4)
display.set_brightness(15)  # Adjust brightness from 0 to 15

# Clear the display
display.clear()
# Render text on the display
display.print("11°C", col = 2)
display.show()
sleep(3)

# Clear the display
display.clear()
display.show()

custom_char_1 = [
    0b00000000,
    0b00000000,
    0b00000000,
    0b11110000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000
]

custom_char_2 = [
    0b00000000,
    0b01101100,
    0b10010010,
    0b10000010,
    0b10000010,
    0b01000100,
    0b00101000,
    0b00010000
]

custom_char_3 = [
    0b00000000,
    0b00100000,
    0b00010000,
    0b11111000,
    0b00010000,
    0b00100000,
    0b00000000,
    0b00000000
]


# Clear the display
display.clear()
display.print_custom_char(custom_char_1, col = 0)
display.print_custom_char(custom_char_2, col = 4)
display.print_custom_char(custom_char_3, col = 11)
display.show()
sleep(3)

def scroll_text(message):
    # Scroll the message from right to left
    display.print(message, col = 32)  # Text starts from the right (x=32) and moves left
    for i in range(len(message) * 8 + 32):  # Scroll through the entire message
        display.clear()
        display.print(message, col = 32 - i)  # Move text from right to left
        display.show()
        sleep(0.05) # change speed here

while True:
    scroll_text("Hello, DIYables")  # Change text as needed


