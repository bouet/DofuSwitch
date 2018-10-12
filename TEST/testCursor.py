import win32gui
import time

i = 1

while i > 0 :
    time.sleep(5)
    x, y = win32gui.GetCursorPos()
    print x, y