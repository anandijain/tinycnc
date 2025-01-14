# tinycnc


this has all the designs:
https://cad.onshape.com/documents/f0edc675ec6e7dd579a916ba/w/8ae7a773a962de3b1e73e6d8/e/a93e4edb635fdcd076b4d8c3 


bom
---

* rpi 5
* rpi level shifter
* rpi lcnc gpio <-> parallel port
* cnc breakout board https://www.amazon.com/dp/B07S5JSWC6
* 3 nema 17 steppers https://www.amazon.com/dp/B0B93J9QZY
* 3 a4988 stepper drivers https://www.amazon.com/gp/product/B07BND65C8/
* 6 guide rods https://www.amazon.com/gp/product/B09VDHKQLB/
* gt2 timing belts https://www.amazon.com/dp/B08R93QQ8Z
* gt2 pulley wheel

* linear rail mgn15h https://www.amazon.com/dp/B07QZ25F53


grbl stuff

C:\Users\anand\AppData\Local\Arduino15\packages\arduino\tools\avrdude\6.3.0-arduino17\etc\avrdude.conf

 avrdude -p m328p -D -PCOM4 -c arduino -b 115200 -U flash:w:grbl_v1.1h.20190825.hex -C C:\Users\anand\AppData\Local\Arduino15\packages\arduino\tools\avrdude\6.3.0-arduino17\etc\avrdude.conf
or use xloader2

grbl settings 
https://github-wiki-see.page/m/gnea/grbl/wiki/Grbl-v1.1-Configuration


todo:
* microstepping and try the quieter drivers
* redesign the rail holder parts so stepperx is on other side, the screws can actually be put in, and the rail actually gets fully surrounded, on the idler side, make a slotted section to more precisely control belt tension, also surround rail and make more rigid and so screws can actually be installed 
* try 2 sets of linear bearings on Y see if deflection improves 
* try to take a short video of it drawing using a rpi camera, I'm down to just hold it cuz I don't have a long enough cable
* far out but could use the z axis to control rolling paper across  
* use a 775 spindle

done:
* add little clamps to hold paper down instead of using tape 
* make the pen holder even longer (closer to ground to improve deflection)