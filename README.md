# ship-console-py
This repo is for mapping [Ship Console](http://www.vrinsightshop.com/shop/step1.php?number=24&b_code=B20111116050346) buttons.

*key-tracker.py* is used to find the console USB device given the device name. The ship console device name can be found (in Windows) from System Settings -> Devices -> Other devices.

The key tracker detects button presses and returns the state of the console. An action gets mappet to a letter-number combination according to the following scheme:

![console](https://github.com/Novia-RDI-Seafaring/ship-console-py/blob/main/console.png?raw=true)

A key mapping is defined by a dictionary, cf. *consoles/aboa_mare_console.json*.
