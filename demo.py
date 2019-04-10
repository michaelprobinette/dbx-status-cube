# ------------------------------------------------------------------------------
# Python program using the library to interface with the arduino sketch above.
# ------------------------------------------------------------------------------

import PyCmdMessenger

# Initialize an ArduinoBoard instance.  This is where you specify baud rate and
# serial timeout.  If you are using a non ATmega328 board, you might also need
# to set the data sizes (bytes for integers, longs, floats, and doubles).  
arduino = PyCmdMessenger.ArduinoBoard("/dev/ttyACM0", baud_rate=9600)

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.
commands = [["set_led", "IIIII"],
            ["set_text", "Is"]]

# Initialize the messenger
c = PyCmdMessenger.CmdMessenger(arduino, commands)

NUM_LED = 22

# DROPBOX BLUE
# 0 / 97 / 255

print("Ack {}".format(set_text(0, "Oh wow!!!")))
print("Ack {}".format(set_text(1, "This is a test with really long text oh wow I hope this scrolls!")))


# Set all lights to dropbox blue
for i in range(0, NUM_LED - 1):
    ack = set_led(i, 0, 97, 255, 255)
    print("Ack {} - {}".format(i, ack))
