from microbit import *
import radio

radio.on()
uart.init(baudrate=115200)

while True:
    msg = radio.receive()
    if msg:
        uart.write(msg + "\n")
    if button_b.was_pressed():
        uart.write("NEXT\n")
