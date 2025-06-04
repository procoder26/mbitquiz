from microbit import *
import radio

radio.on()
player_id = "P1"  # Change to P2, P3, etc.

while True:
    if button_a.was_pressed():
        radio.send(player_id + ":A")
    if button_b.was_pressed():
        radio.send(player_id + ":B")
