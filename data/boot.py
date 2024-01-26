import board

from kmk.bootcfg import bootcfg

bootcfg(
    midi=False,
    mouse=False,
    storage=False,
    usb_id=('KMK Keyboard', 'WAKeyboard'),
)