import sys
from getpass import getuser
from cmd_helpers import set_text, set_solid_color, set_party_leds
from constants import FLOW_RGB, AVAILABLE_RGB, MAX_BRIGHTNESS


def init():
    set_text(0, "@{}".format(getuser()))
    set_available_state()


def set_flow_state():
    # Set everything to DBX blue
    set_solid_color(FLOW_RGB[0], FLOW_RGB[1], FLOW_RGB[2], MAX_BRIGHTNESS)
    set_text(1, "Currently Flowing, check back later!")


def set_available_state():
    # Set everything to Green
    set_solid_color(AVAILABLE_RGB[0], AVAILABLE_RGB[1], AVAILABLE_RGB[2], MAX_BRIGHTNESS)
    set_text(1, "Available, talk to me!")


def set_party_state():
    # PARTY ON GARTH
    set_party_leds()
    set_text(1, "PAAAAAAAAAAAARTY")


state_to_fn = {
    'init': init,
    'flow': set_flow_state,
    'available': set_available_state,
    'party': set_party_state,
}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Missing required state parameter. Expected one of: {}".format(state_to_fn.keys()))
        sys.exit(1)

    state = sys.argv[1]
    handler = state_to_fn.get(state)

    if handler is None:
        print("Unknown state. Expected one of: {}".format(state_to_fn.keys()))
        sys.exit(1)

    print("Setting state: {}".format(state))
    handler()
