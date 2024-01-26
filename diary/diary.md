# 24th January 2024
My PiHut order arrived!

I plugged my Waveshare RP2040 Plus and Raspberry Pi Pico into a mounting board and then into my computer, whilst pressing the bootslct button.

Now follow [this link](https://kmkfw.io/docs/Getting_Started/#tldr-quick-start-guide) on KMK to get started or if your too lazy...

- Downloaded the latest circuit python UF2 file and dropped it into the Pi's. Reboot by pressing the reset button or just re-plugging the device.

- Now download the kmk repo and drop the `kmk` folder and `boot.py` into the the Pi.

- Create a `code.py` or `main.py` in the top level directoy (where boot.py is) and add the following code:

```python
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,]
]

if __name__ == '__main__':
    keyboard.go()
```

You may have to addapt the GP0 and GP1 to your board, these are the General Programmable pins, so don't assume they just mean pin and include ground pins.

_Viola_ 

Reset/boot your pi and use something to bridge GP0 and GP01, I had a jumper wire but you can use a paperclip too. Don't worry if the pi still comes up as an accessible drive, it will still work as a keyboard. Scratched my head for a while before just trying the pins and figuring I had done it right.

Once I got that work, I wrote the first version of my keymap ([found here](data/code_v1.py)) which only took some minor debugging before I found that KC.9 should have been KC.N9, any error will cause it to straight up not work.

And now I wait for everything else to turn up...

# 26th January 2024

The switch and bottom plates, switches, diodes and wire have arrived!

The plates look great, and I have immediately populated it with _some_ help from my daughter (6 switches rushed into place) before realising I was 6 switches short, so off to mechboards again...

It's a good thing this is a handwired board because those switches wouldn't be coming out even if they wanted to.

Apologies for the shody photots.
![SwitchPlate](../Images/SwitchPlate.jpg)

![PopSwitchPlate](../Images/PopulatedSwitchPlate.jpg)

6 switches off though...

I then spent the next half hour using these sausage finger to bend all my diodes in preparation for soldering day.