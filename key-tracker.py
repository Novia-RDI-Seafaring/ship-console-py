import hid
import json
# based on intructions from https://blog.thea.codes/talking-to-gamepads-without-pygame/

def save_key_map(key_map, file):
    '''save a new keymap dictionary as json'''
    with open(file, 'w') as f:
        json.dump(key_map, f)

def load_key_map(file):
    '''load a keymap from json'''
    with open(file, 'r') as f:
        data = json.load(f)
        return data

def get_key(my_dict, val):
    '''find key from dictionary'''
    for key, value in my_dict.items():
        if val == value:
            return key
    return "key doesn't exist"

class ConsoleState:
    '''Class for keeping track of the state of a console'''
    # default constructor
    def __init__(self):
        self.key = "none"
        self.slider = ""
        self.thruster = ""
        self.zrot = ""

def get_console_action(my_console, report):
    '''retrieve keypresses and updates the state of the console'''
    if report[0]==1:
        # slider change
        slider = report[1]
        thruster = report[2]
        zrot = report[3]
        # check if slider value has changed
        if my_console.slider != slider:
            my_console.slider = slider
            print('slider: ' + 's' + str(slider))
        #check if thruster value has changed
        if my_console.thruster != thruster:
            my_console.thruster = thruster
            print('thruster: ' + 't' + str(thruster))
        # check if zrot calue has changed
        if my_console.zrot != zrot:
            my_console.zrot = zrot
            print('zrot: ' + 'z' + str(zrot))
    elif report[0]==2:
        # button press
        my_console.key = get_key(key_map, report)
        print('key: ' + my_console.key)
    return my_console

# ==== GET ID FOR A SPECIFIC CONSOLE ====
# find ID of ship console. # The ship console name can be found (in Windows) from System Settings -> Devices -> Other devices
console_name = 'usb pad'
def get_console_id(console_name):
    for device in hid.enumerate():
        if device['product_string'] == console_name:
            print('Device found!')
            #save vendor and product ids as hex
            vendor_id = eval(f"0x{device['vendor_id']:04x}")
            product_id = eval(f"0x{device['product_id']:04x}")
            break
    return vendor_id, product_id

vendor_id, product_id = get_console_id(console_name)
print('Ship Console name: ' + console_name)
print('Console id: ' + str(vendor_id) + ":" + str(product_id))

# talk to the device
console = hid.device()
console.open(vendor_id, product_id)
#Enabling non-blocking means that the program won't hang when trying to read from the device if it isn't ready, it'll just return None.
console.set_nonblocking(True) 

# ===== TRACK ACTIONS ====
#load key map
key_map = load_key_map('consoles/aboa_mare_console.json')
#initialze console states
my_console = ConsoleState()

#listen to the device
print('Press Ctrl+c to exit')
while True:
    report = console.read(64)
    if report:
        #key = get_console_action(report, key_map)
        my_console = get_console_action(my_console, report)