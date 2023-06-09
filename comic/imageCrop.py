import pyautogui
from PIL import ImageGrab
from datetime import datetime
now = datetime.now().strftime('%Y%m%d %H%M%S')

x = 900
y = 660
path = r"C:\Users\FREI\Pictures\Screenshots\{0}.png".format(now)
width,height = pyautogui.size()
print(width,height)  # 1920 1080

#快照
img = ImageGrab.grab()
im = img.crop ( (265, 250, 1540, 950))
#im.show()
im.save(path,quality=1)