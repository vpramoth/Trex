import gtk.gdk
import time
import webbrowser
from pynput.keyboard import Key, Listener
import threading
from threading import Thread

webbrowser.open('http://www.trex-game.skipser.com/')
time.sleep(3)
gkey = ''
def on_press(key):
    gkey = key
    print('{0} pressed'.format(
        key))

def on_release(key):
    gkey = key
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()



t_begin = time.time()
t_end = time.time() + 10
di={}
while time.time() < t_end:

    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])

    ts = time.time()
    filename = "screenshot"
    filename += str(ts)
    filename += ".png"
    print(pb)
    if (pb != None):
        pb.save('/home/pramoth/PycharmProjects/nn/images/%s'%filename,"png")
        print "Screenshot saved to "+filename
    else:
        print "Unable to get the screenshot."
    # print ('%f'%(time.time()-t_begin))
    # print(gkey)
    # print ('*****************')
    time.sleep(1)
