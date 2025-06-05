radio.setGroup(17)
serial.redirectToUSB()

radio.onReceivedString(function (msg) {
    serial.writeLine(msg)
})

input.onButtonPressed(Button.B, function () {
    serial.writeLine("NEXT")
})
