# tinycnc

ITS A PEN PLOTTER NOW 

tiniest cnc. starting off 3 axis no spindle - manually attach a dremel

eventually use a 775 


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
* add little metal clamps to hold paper down instead of using tape 
* make the pen holder even longer (closer to ground to improve deflection)