# ship-console-py
This repo is for mapping [Ship Console](http://www.vrinsightshop.com/shop/step1.php?number=24&b_code=B20111116050346) buttons.

*key-tracker.py* is used to find a ship-console USB device given the device name. The ship console device name can be found (in Windows) from System Settings -> Devices -> Other devices.

The key tracker detects button presses and returns the state of the console. An action gets mapped to a letter-number combination according to the following scheme:

![console](https://github.com/Novia-RDI-Seafaring/ship-console-py/blob/main/console.png?raw=true)

The key mapping can be change by defining a new *key_map* dictionary, cf. *consoles/aboa_mare_console.json*.
