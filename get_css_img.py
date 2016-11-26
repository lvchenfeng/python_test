import urllib.request
import re

#下载图片
def get_img(url,name):
    f = open("./html/"+ name, 'wb')
    f.write(urllib.request.urlopen(url).read())
    f.close()

#下载css文件
url = "http://res8.vmallres.com/20161026/css/notice/main.min.css?20141025"
css_response = urllib.request.urlopen(url)
css_page = css_response.read().decode("gb2312","ignore")
#匹配背景
img_re = re.compile(r"url\(\"([^\)]*)\"\)")
img_list = img_re.findall(css_page)
#计算组合图片网址
dir_list=url.split("/")
dir_list.pop()
# print(dir_list)
img_url_list = []
dian_str = ".."
# print(dian_str)
num = 0
for img in img_list:
    imgs = img.split("/")
    tmp_url = dir_list[:]
    for imgs_l in imgs:
        if imgs_l == dian_str:
            tmp_url.pop()
    result = ""
    for tmp in tmp_url:
        result+=tmp+"/"
    for imgs_l in imgs:
        if imgs_l != dian_str:
            result += imgs_l + "/"
    result = result[:-1]
    names = (imgs[-1]).split("?")
    get_img(result,names[0])
    print("已下载第"+str(num)+"张图片")
    num+=1


