## MicroPython LED Matrix Library - DIYables_MicroPython_LED_Matrix
This MicroPython LED Matrix library is designed for any hardware platform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to work with the Max7219 LED Matrix. It is created by DIYables to work with DIYables LED Matrix, but also work with other brand LED Matrix. Please consider purchasing [LED Matrix 8x8](https://www.amazon.com/dp/B0D2K9ZLW6) and [LED Matrix 32x8](https://www.amazon.com/dp/B0BXKKT72V) from DIYables to support our work.


![LED Matrix](https://diyables.io/images/products/led-matrix.jpg)



Product Link
----------------------------
* [LED Matrix 8x8](https://diyables.io/products/dot-matrix-display-fc16-8x8-led)
* [LED Matrix 32x8](https://diyables.io/products/dot-matrix-display-fc16-4-in-1-32x4-led)



Features  
----------------------------  
* Supports ASCII characters, including the degree (°) symbol  
* Allows custom characters (with a provided custom character generator)  
* Trims each character to its actual width and adds configurable spacing, unlike other libraries that fix characters to 8-pixel width, for a more compact and flexible display  
* Compatible with any MicroPython-supported platform, including Raspberry Pi Pico, ESP32, Micro:bit, and more


Available Functions
----------------------------
* \_\_init\_\_(self,spi, cs, num_matrices=4)
* clear(self)
* show(self)
* set_brightness(self, brightness)
* print_bitmap(self, bitmap, start_col = 0)
* print_char(self, char, start_col = 0)
* print(self, text, spacing=2, col = 0)
* print_custom_char(self, bitmap, col = 0)


Available Examples
----------------------------
`main.py` does:
* display text
* display custom characters
* scroll text.py



Tutorials
----------------------------
* [Arduino MicroPython - LED Matrix](https://newbiely.com/tutorials/arduino-micropython/arduino-micropython-led-matrix)
* [ESP32 MicroPython - LED Matrix](https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-led-matrix)
* [Raspberry Pi Pico - LED Matrix](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-led-matrix)



References
----------------------------
* [MicroPython LED Matrix Library](https://newbiely.com/tutorials/micropython/micropython-led-matrix-library)
