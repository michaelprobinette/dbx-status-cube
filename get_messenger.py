# ------------------------------------------------------------------------------
# Python program using the library to interface with the arduino sketch above.
# ------------------------------------------------------------------------------

import PyCmdMessenger
from functools import lru_cache
from constants import DEBUG, COMMANDS, ARDUINO_BAUD_RATE, ARDUINO_DEV_PATH


# Initialize the messenger
@lru_cache(maxsize=1)
def get_messenger():
    if DEBUG:
        return get_debug_messenger()
    # Initialize an ArduinoBoard instance.  This is where you specify baud rate and
    # serial timeout.  If you are using a non ATmega328 board, you might also need
    # to set the data sizes (bytes for integers, longs, floats, and doubles).  
    arduino = PyCmdMessenger.ArduinoBoard(ARDUINO_DEV_PATH, baud_rate=ARDUINO_BAUD_RATE)
    return PyCmdMessenger.CmdMessenger(arduino, COMMANDS)


def get_debug_messenger():
    return FakeMessenger()


class FakeMessenger(object):

    def send(self, cmd, *args, arg_formats=None):
        print("CMD({}) - {}".format(cmd, args))

    def receive(self):
        return "FAKE MESSENGER"
