#爬蟲下載漫畫+轉檔
import os
import pyautogui
from datetime import datetime
from win32 import win32clipboard
import requests
from PIL import Image
#漫畫名稱
nameList = ["babyblues","peanuts","onebighappy"]

uri = r"https://www.arcamax.com/thefunnies/"

#日期
today = datetime.now().strftime('%Y%m%d')

#開網頁瀏覽器
os.system("start firefox.exe")

for name in nameList:

    pyautogui.moveTo(290, 64, 2)
    pyautogui.leftClick()
    pyautogui.typewrite(uri + name, interval=0.05)
    pyautogui.press("enter")

    # 按右鍵 複製鏈結
    pyautogui.moveTo(610, 864, duration=3.5)
    pyautogui.rightClick()
    pyautogui.press("o")
    # get clipboard data
    win32clipboard.OpenClipboard()
    picLink = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print(picLink)

    #下載圖片
    r = requests.get(picLink)
    open(r"C:\Users\FREI\Pictures\comic\{0}.gif".format(name), 'wb').write(r.content)

    #gif2png

    gifFileName = r"C:\Users\FREI\Pictures\comic\{0}.gif".format(name)
    im = Image.open(gifFileName)
    # 去除 .gif 取得相同名稱
    pngDir = gifFileName[:-4]

    if not os.path.exists(pngDir):
        os.mkdir(pngDir)

    try:
        while True:
            current = im.tell()
            im.save(pngDir + '\\' + str(today) + '.png')
            im.seek(current + 1)
    except EOFError:
        pass
#關閉進程
im.close()

for name in nameList:
    # LINE Notify 權杖
    token = '2ufcbgqCnVahJPeG8UcH35jGzO6HfckWW5rzl2fj5kM'

    # 要發送的訊息
    message = '今日漫畫{0}'.format(name)

    # HTTP 標頭參數與資料
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}

    path = r"C:\Users\FREI\Pictures\comic\{}\{}.png".format(name, today)

    # 要傳送的圖片檔案
    image = open(path, 'rb')
    files = {'imageFile': image}

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, data=data, files=files)