from pynput.keyboard import Key as kKey, Listener as kListener

def on_press(key):
    print('{0} pressed'.format(key))

def on_release(key):
    print('{0} release'.format(key))
    if key == kKey.esc:
        # Stop listener
        return False

# Collect events until released
with kListener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


