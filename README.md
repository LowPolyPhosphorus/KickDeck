# KickDeck
using a KickPi K2B v1.1 to make a Cyberdeck inside of a mini pelican case (from aliexpress or i would have to pay $50+) 7" HDMI screen and a full keyboard and more.

## What is it?
Im uisng a KickPi K2B which is almost nothing like a RPi as its an Allwinner H618 board that ships with Android TV on it and as far as I can tell is made to be used as an Anrdoid TV box with its IR sensor onboard and of course the OS that comes with it but it supports Ubuntu and Android according to the docs! Im trying to turn this into a cyberdeck inside of a Pelican case or similar 

## Status
Currently this is only in the design phase so most of my hardware is not purchased yet, nothing is wired or flashed and no software or hardware changes have been made other than plugging the display into the board so at the moment im just confirming the specs and docs.

### Confirmed/Working parts 
- K2B V1.1 + 7" display both power on and work
- touch input works
- display's mounting holes are good

### Current Issues
- stock android TV has no back button and the operating system has almost nothing on it, so its kinda useless as a cyberdeck
- KickPi's own PDF on the website contradicts its self a couple tiems where it says it runs on 12V in one table and Type-C 5V in the power supply row, 5v is correct since it only has a USB c port no 12V barrel input onboard, its raw GPIO pin name table also doesn't match the actual pinout diagram????

## The current build/concept
**brain:** KickPi K2B V1.1
**screen:** 7" 1024x600 HDMI touchscreen (2 micro USB cables, one's power, one's touch data)
**power:** Waveshare UPS HAT (E), 4x 21700 Li-ion cells, 6A output
**input:** mini keyboard w/ built-in touchpad 
**extras:** SSD1306 OLED, EC11 rotary encoder, panel-mount LED indicators, 16mm self-locking power button, small 5V fan
**case:** mini pelican-style, ~9.84" external width

full parts list with prices/links/status is going to be in the BOM soon to be added to the repo, the pinout already has all of the pin assignments but some are TBD 

