import pyautogui
from datetime import datetime
from PIL import ImageGrab
import requests

x = 900
y = 660

width,height = pyautogui.size()
#print(width,height)  # 1920 1080

now = datetime.now().strftime('%Y%m%d %H%M%S')

# 移动到x, y 坐标处，用时0.25s
#收寶
pyautogui.moveTo(x,y,0.25)
pyautogui.doubleClick()
pyautogui.moveTo(x,y+200,2)
pyautogui.click()

#快照
img = ImageGrab.grab()
path = r"C:\Users\FREI\Pictures\Screenshots\{0}.png".format(now)
im = img.crop ( (260, 250, 1540, 950))
im.save(path,quality=1)
#im.show()
pyautogui.moveTo(x,y,2)

#關閉
pyautogui.moveTo(1505,205,2)
pyautogui.click()

# LINE Notify 權杖
token = '2ufcbgqCnVahJPeG8UcH35jGzO6HfckWW5rzl2fj5kM'

# 要發送的訊息
message = '今日禮物'

# HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + token }
data = { 'message': message }

# 要傳送的圖片檔案
image = open(path, 'rb')
files = { 'imageFile': image }

# 以 requests 發送 POST 請求
requests.post("https://notify-api.line.me/api/notify",
    headers = headers, data = data, files = files)