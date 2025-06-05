let player_id = "P1"
radio.setGroup(17)

input.onButtonPressed(Button.A, function () {
    radio.sendString(player_id + ":A")
})
input.onButtonPressed(Button.B, function () {
    radio.sendString(player_id + ":B")
})

radio.onReceivedString(function (msg) {
    if (msg.substr(0, player_id.length) == player_id) {
        if (msg.includes("CORRECT")) {
            basic.showString("✓")
        } else if (msg.includes("WRONG")) {
            basic.showString("X")
        }
        basic.pause(1000)
        basic.clearScreen()
    }
})
