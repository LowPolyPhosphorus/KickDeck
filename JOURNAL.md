# LOG 1
54m 29s logged
## BOM Research 

did some BOM research
so far I did the following:
- confirmed K2B (V1.1) and 7" display both work; touch input functional, mounting holes good
- identified Android TV navigation issue (no back button, requires restart, so any hopes of using the stock OS are gone)
- built out the BOM on Notion
- resolved KickPi PDF voltage contradiction confirmed K2B runs 5V (Type-C), not 12V as one table mistakenly stated
- currently i decided on the Waveshare UPS HAT (B) 5V output, dual 18650, I2C monitoring as a UPS module 
- found keyboard+touchpad combo, eliminating need for separate trackpad/trackball
- worked out full USB port budget: touch data + keyboard combo fit K2B's 2 native ports with no hub; hub only needed once OLED is added later
- picked power button: 16mm, self-locking, LED ring, 3-6V, 3A, aluminum alloy

<img width="1600" height="629" alt="image" src="https://github.com/user-attachments/assets/c4a169ab-818c-424b-a779-587c08304c64" />

# LOG 2
1h 1m 29s logged
## BOM Finalization (mostly)

### UPS Module

continuing from the last journal, I started off with the Waveshare UPS HAT (B) designed for dual 18650 Li-ion batteries since it has usb output and i2c battery monitoring but it used pogo pins to clip into the RPi for power delivery which wouldn't work with the K2B, then i switched to the (D) model briefly it used a single 21700 cell but it only outputs ~4A while charging actively and would drop as the battery depletes which would cause problems with my estimated power draw. I settled on the UPS HAT (E) running on 4 21700 Li-ions and had 6A output clearing the draw estimate with a margin so its my final pick. I also realized that all the boards only have one shared USB output port which means I will have to use a USB hub since I cant use that USB port.

### Battery sourcing

I literally couldn't find any listings on Amazon for the right 21700 battery or on AliExpress either... the only place I could find one has them at $9.00 a piece but if I can get this done on time it will still be on sale for ~$6.00 on the 18650 Battery Store (which has more than just 18650s) 

### OLED wiring (not published/done)

I originally planned to get a USB I2C adapter since the GPIO is unconfirmed :/ but I found the official pinout on their info PDF also confirmed there were the right pins for the OLED I already have (ideaspark SSD1306) that accepts 3.3-5V so no mismatch risk!

### Budget
so far the price I have is at about $120 in unpurchased parts ($200 if i didnt own alot of the parts)

### Fan

I was going to use a fan I already have but the fan uses 12V which would run horribly on the 5V rail

#### unresolved stuffs

- mounting material?? ( like plastic PLA boards i have already or 3D printing)
- cable management (idk if its going to be enough of a problem?)
- thats about it 

<img width="1195" height="619" alt="image" src="https://github.com/user-attachments/assets/0e0cabc4-f836-4de1-b665-183b61925395" />

# LOG 3
2h 9m 34s logged
## another devlog!

### UPS HAT
- onboard power switch is a tiny physical switch and there is NO seperate gpio header for it :( so the panel power button will have to wire in parallel (or cut off the switch) 

### Power button 
- turns out its an RGB pushbutton (im blind) and not single color, but I have decided to keep it since it looks good and I will be only wiring the green led line

### OLED + GPIO resolved !
- I got the real KickPi 20 pin diagram with correct pins
- OLED: i2C4 on pins 9/13, no adapter needed
- rotary encoder: assigned CLK/DT/SW/VCC/GND to free pins
-2 indicator LEDs: one PWM-driven (dim HDD activity light, pin 10) and one plain GPIO (battery/low-battery warning, pin 12), found by confirming actually has 2 real PWM channels broken (Pin 8/10)

### Docs
- finalized README, finalized BOM, finalized pinout.txt

### Paper sketch thing
- I documented my planned organization and placement for all the parts on paper 

### everything else
- I made some updates to the BOM to use 2 usb hubs also added a rotary encoder and some other stuff
- the rest of the stuff thats still open is what material to use for the case mounting stuff and cable management

Stardance doesn't seem to support markdown CSV ??? so here's a screenshot, its also on the repo [here](https://github.com/LowPolyPhosphorus/KickDeck/blob/main/docs/BOM.csv)
<img width="1066" height="590" alt="image" src="https://github.com/user-attachments/assets/1e7924bb-a71d-4385-8a5c-1ac1a2f892e3" />

# LOG 4
