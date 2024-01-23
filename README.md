# WAK!

Whilst waiting for a replacement for a beautiful split keyboard, the Sofle v2, i jumped into the rabbit hole of Mechanical Keyboards. It didn't help that my daughter now wants her own, so here I am.

## The Board
This will be a handwired, wired (for now) build using an RP2040 board (specifically this one [Waveshare RP2040 Plus](https://thepihut.com/products/rp2040-plus?variant=42405935612099), however if that doesn't work out then I have a Pi Pico WH in waiting--which I need to figure out how to hook up to a LiPo) programmed with KMK. For me this makes sense as i'm primarily a Python developer and KMK is built for the RP2040 ecosystem.

## Inspiration
### My Daughter (actual daughter, not a keyboard)
Wanted a "One piece" keyboard, apparently my split board was toooo space ship like... pfft.

### Lumberjack keyboard
I found this very early on in my search across the web, the one piece "split" with the controller in the middle looks pretty cool.

### Sofle v2
Of course, it's cool. I've tried to keep a similar-ish column stagger (more aggresive pinky, and no ring finger stagger). However, i've moved the clusters into the centre of the board ( something I may live to regret, but hey ho ).

## Design

I've designed this board using [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/), writing it all in their raw data json field _before_ realising that there was GUI the whole time. This produces the contents of this file: [layout.json](data/layout.json).
![WAK](Images/what-a-keyboard-(wak).png)

Copy Pasting this into [KBFirmware](https://kbfirmware.com/), which I know is EOL but it's great for getting a quick and easy wiring diagram.
![Wiring](Images/WAKwiring.png)

Pasting it into [swillkb's builder app](http://builder.swillkb.com/) will generate some CAD output too. Saved in the cad folder. This looks something like this:
![Switch Layer](Images/SwitchLayer.png)

I went to [laserboost](https://www.laserboost.com/en/create) to get the switch and bottom plate cut in Aluminium (This is only a prototype, and I feel like I should have found a 3d printer service too... lessons for the future)

I then thought, hmm... what would make this look very professional? People on the Reddit and the YouTube seem to like KiCad, so I gave it a go and came up with this:
![KiCad Drawing](Images/KiCad.png)

I also used this and the ScottoKeebs KiCad repo to generate a PCB, which I will not be getting printed as it is not completed (Some of the lines couldn't route to their pin so I temporarily gave up) and looks trash (from my currently uneducated gaze). It's more here to show it's easy to do after a 3rd viewing of Joe Scotto's tutorial. Look's cool though right?
![WAK_PCB](Images/WAK_pcb.png)

## Bill Of Materials

| Item | Cost | Use | Site |
|---|---|---|---|
| Diodes | £3.00 | For Dioding | Mechboards.co.uk |
