print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.hid import HIDModes
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.modules = [Layers, MediaKeys]

keyboard.debug_enabled = False

WAK_W = send_string("What A Keyboard!!")
WAK_A = send_string("Amazing Keyboard!!")
WAK_K = send_string("Killer Keeb!!")
SMILE = send_string(":)")

keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,
    board.GP21
)
keyboard.row_pins = (
    board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [   KC.NO, KC.NO, KC.N2, KC.N3, KC.N4, KC.N5,           KC.NO, KC.NO, KC.NO,        KC.N6, KC.N7, KC.N8, KC.N9, KC.NO, KC.NO,
        KC.ESC, KC.N1, KC.W, KC.E, KC.R, KC.T,              KC.NO, KC.NO, KC.NO,        KC.Y, KC.U, KC.I, KC.O, KC.N0, KC.TILD,
        KC.TAB, KC.Q, KC.S, KC.D, KC.F, KC.G,               KC.NO, KC.NO, KC.NO,        KC.H, KC.J, KC.K, KC.L, KC.P, KC.QUOT,
        KC.LSHIFT, KC.A, KC.X, KC.C, KC.V, KC.B,            KC.NO, KC.NO, KC.NO,        KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.GRV,
        KC.LCTRL, KC.Z, KC.LGUI, KC.LALT, KC.ENT, KC.SPACE, WAK_W, WAK_A, WAK_K,        KC.SPACE, KC.ENT, KC.RALT, KC.MUTE,
        KC.ESC, KC.RLD, KC.NO, KC.NO, KC.NO, KC.NO,         KC.MO(1), SMILE, KC.MO(2),  KC.NO, KC.NO, KC.NO, KC.NO, KC.VOLU, KC.VOLD,
    ],
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.USB, secondary_hid_type=HIDModes.BLE, ble_name='WAKeyboard')
