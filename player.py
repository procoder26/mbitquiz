from microbit import *
import radio

radio.on()
radio.config(group=156)
player_id = "P1"  # Change to P2, P3, etc.

while True:
    if button_a.was_pressed():
        radio.send(player_id + ":A")
    if button_b.was_pressed():
        radio.send(player_id + ":B")

    msg = radio.receive()
    if msg and msg.startswith(player_id):
        if "CORRECT" in msg:
            display.show("✓")  # ✅ check mark
        elif "WRONG" in msg:
            display.show("X")  # ❌ X mark
        sleep(1000)
        display.clear()
