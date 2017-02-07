# from selenium import webdriver as wb
import numpy as np
import webbrowser as wb
from PIL import ImageGrab as ig
from pynput.keyboard import Key as kKey, Listener as kListener

# This dictionary stores the data set.
record = {} # arguments (index : key, press(1)/release(0), image(np.array))

def capture():
    img = ig.grab()
    img_np = np.array(img)
    return img_np

def on_press(key):
    # print('{0} pressed'.format(key))
    # Modification
    length = len(record.items()) + 1
    record.update({length : [key, 1, capture()]})

def on_release(key):
    # print('{0} release'.format(key))
    if key == kKey.esc:
        # Stop listener
        return False

    # Modification
    length = len(record.items()) + 1
    record.update({length: [key, 0, capture()]})

# opening browser
# wb.open("C:\\Python27\\selenium\\chromedriver.exe")
# driver.get("http://www.trex-game.skipser.com/")
# driver.maximize_window()
wb.open("http://www.trex-game.skipser.com/")

# Collect events until released
with kListener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print record.keys()