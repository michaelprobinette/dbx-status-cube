from os import environ
DEBUG = environ.get('DEBUG', False)

ARDUINO_DEV_PATH = environ.get('DBX_ARDUINO_DEV', "/dev/ttyACM0")
ARDUINO_BAUD_RATE = environ.get('DBX_ARDUINO_BAUD', 9600)

CMD_SET_LED = "set_led"
CMD_SET_TEXT = "set_text"
CMD_PARTY_LEDS = "party_leds"

# List of command names (and formats for their associated arguments). These must
# be in the same order as in the sketch.
COMMANDS = [[CMD_SET_LED, "IIIII"],
            [CMD_SET_TEXT, "Is"],
            [CMD_PARTY_LEDS, ""]]


WHITE_RGB = [255, 255, 255]
BLACK_RGB = [0, 0, 0]
DBX_BLUE_RGB = [0, 97, 255]
AVAILABLE_RGB = [0, 128, 0]
FLOW_RGB = DBX_BLUE_RGB
MAX_BRIGHTNESS = 255

NUM_LED = 22
