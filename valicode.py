import os
from PIL import Image
import urllib.request

#img = Image.open('F:/work/python/tmp.jpg')
# 二值化
def binary(img):
    img = img.convert("RGBA")
    pixdata = img.load()

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x,y][0] < 90:
                pixdata[x,y] = (0,0,0,255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img
# img.save("F:/work/python/input_black.gif","GIF")
# im_orig=Image.open("F:/work/python/input_black.gif")
# big=im_orig.resize((120,40),Image.NEAREST)


#批量下载二维码
import re
def download(url,num,dir):
    for i in range(num):
        f = open(dir+"valicate" + str(i) + ".jpg", 'wb')
        f.write(urllib.request.urlopen(url).read())
        f.close()


#图片切割
def division(img):
    font = []
    for i in range(4):
        x = 4 + i*10
        y = 4
        font.append(img.crop((x, y, x+9, y+19)))
    return font

#识别
def recognize(img):
    fontMods = []
    dir = "./num/"
    i=0
    for f in os.listdir(dir):
        fontMods.append((str(i),f[-5],binary(Image.open(dir+f))))
        i+=1

    result = ""
    font = division(img)
    for i in font:
        target = i
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(19):
                for xi in range(9):
                    if mod[2].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                        diffs += 1
                        #print(target.getpixel((xi, yi)))
            points.append((diffs,mod[0],mod[1]))
        points.sort()
        result += points[0][2]
    return result

#
# if __name__ == '__main__':
#     codedir = "./html/"
#     for imgfile in os.listdir(codedir):
#         if imgfile.endswith(".jpg"):
#             dir = "./result/"
#             img = binary(codedir + imgfile)
#             num = recognize(img)
#             dir += (num + ".png")
#             print("save to", dir)
#             img.save(dir)
def getcode(url):
    f = open("./"+ str(1) + ".jpg", 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()
    return "./1.jpg"


if __name__ == '__main__':
    img ="./html/b_valicate1.jpg"
    url = "http://oto.mph88.com/admin.php?c=Login&a=verify&time=1479449308036"
    img=getcode(url)
    img = Image.open(img)
    img1 = urllib.request.urlopen(url).read()
    img = binary(img)
    num=recognize(img)
    print(num)

#字体制作
#download("http://oto.mph88.com/admin.php?c=Login&a=verify&time=1479449308036", 50, "./html/")
# dir = "./html/"
#   for f in os.listdir(dir):
#       binary(dir+f).save(dir+"b_"+f)
# i = 1
# for f in os.listdir(dir):
#     img_list=division(dir+f)
#     for img in img_list:
#         img.save("./num/"+str(i)+".bmp","BMP")
#         i+=1

