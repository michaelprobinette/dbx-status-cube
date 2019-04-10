from constants import CMD_SET_LED, CMD_SET_TEXT, CMD_PARTY_LEDS, NUM_LED
from get_messenger import get_messenger


def set_led(led_i, red, green, blue, brightness):
    c = get_messenger()
    c.send(CMD_SET_LED, led_i, red, green, blue, brightness)
    return c.receive()


def set_text(line_i, text):
    c = get_messenger()
    c.send(CMD_SET_TEXT, line_i, text)
    return c.receive()


def set_party_leds():
    c = get_messenger()
    c.send(CMD_PARTY_LEDS)
    return c.receive()


def set_solid_color(red, green, blue, brightness):
    return [set_led(i, red, green, blue, brightness) for i in range(0, NUM_LED)]
