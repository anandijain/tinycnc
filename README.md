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

1/21/25

* gopro mount on z 
* redesign z to be rack and pinion + spring 
* cloudflare site setup

todo:
* fix bom (30 mins)
* try to take a short video of it drawing using a rpi camera or gopro, I'm down to just hold it cuz I don't have a long enough cable
* replace xidler with the new tensioner
* microstepping
* load cell on pen, have control over force applied to page
* for the supported gantry, do the physics to see how much longer the y axis can be made 
* look at how bed leveling works on a 3d printer, it would be cool to do that, but it would mainly be measuring deflection since that is way more of a change than how flat the wood board is
* find out what it would take to do closed loop with angular encoders
* improve the testing situation- it would be nice to log information on the page printed about what type of pen- what grbl settings and what cad settings were used to produce an image
* have some actual gcode written tests, like a bunch of lines spaced 1mm apart, and a big circle, stuff like that
* art- try a really thick pen (requires cad change) and try to draw some cool graffiti 
* CAD tool changer
* far out but could use the z axis to control rolling paper across 
* redesign to use 3 rails (2 500mm ones) increases the print area  
* download all the timelapses on the SD card of printer. good for the video 
* finally make a pcb to wire this  thing, basically take 12v 5a barrel with a pretty good 5v regulator. then give power to shield but return the servo data pin.
    - then to unplug, just remove the barrel. no more 2 wall wart nonsense
* use a 775 spindle


shelved: 
* try the quieter drivers (the pinout is different :/ )
* mount a time of flight on the z axis and do bed leveling or rather more a measurement of deflection 
    - the precision of the TOF is 1mm so the picture wouldnt look that cool not worth 

done:
* add little clamps to hold paper down instead of using tape 
* make the pen holder even longer (closer to ground to improve deflection)
* finish assembly and hardware for the whole design in onshape 
* fix tensioner to not limit travel in x 
* minimize threaded insert usage and opt for tapping (particularly for thru holes, threaded inserts in blind is ok)
* instead of slotted nut put a cbore under rail, because the support removal for slot is a nightmare
* also for the cbore on the bolt that goes thru rail need to increase diam
* cbore on the bottom nuts for x axis motor and currently they are super inaccessible 
* pegs for belt holder are too weak and can easily break (3mm to 4mm)
* slot for belt tensioning is UX nightmare terrible mechanism 
* try 2 sets of linear bearings on Y see if deflection improves 
* redesign the rail holder parts so stepperx is on other side, the screws can actually be put in, and the rail actually gets fully surrounded, on the idler side, make a slotted section to more precisely control belt tension, also surround rail and make more rigid and so screws can actually be installed 
* cad changes for pen to be removable from the top 
* tof mount on z 
* redesign it to be a supported gantry
* beam bending physics, work out the expected deflection given the mass of the z axis 
* make the pen holder way longer - requires making the z wider so that the pen can be taken out upwards
