#傳送line notify
from datetime import datetime
import requests

today = datetime.now().strftime('%Y%m%d')
nameList = ["babyblues","peanuts","onebighappy"]

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