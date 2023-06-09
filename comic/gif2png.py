import os
from PIL import Image
from datetime import datetime

#今天的日期
today = datetime.now().strftime('%Y%m%d')

gifFileName = '../babyblues.gif'
im = Image.open(gifFileName)
#去除 .gif 取得相同名稱
pngDir = gifFileName[:-4]

if not os.path.exists(pngDir):
    os.mkdir(pngDir)

try:
    while True:
        current = im.tell()
        im.save(pngDir+'/'+str(today)+'.png')
        im.seek(current+1)
except EOFError:
    pass
im2 = Image.open(pngDir+'/'+str(today)+'.png')
im2.show()