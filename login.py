from html.parser import HTMLParser
import urllib
import http.cookiejar
import string
import re
import io
import json

hosturl = 'http://oto.mph88.com/index.php?c=account&a=login'
posturl = 'http://oto.mph88.com/index.php?c=account&a=login'

cj = http.cookiejar.CookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(hosturl)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36',
    'Referer': 'http://oto.mph88.com/index.php?c=account&a=login'}
postData = {
    'login_type': 'P-N',
    'phone': '13642989720',
    'password': '123456',
    'referer': 'http://oto.mph88.com/',
    'web_site': 'http://oto.mph88.com/',
    'current_login_url': '',
    'submit_login': '登录',
}
postData = urllib.parse.urlencode(postData, encoding='gb2312').encode('gb2312')
# 因为post里面有中文，因此需要先把url经过gb2312编码处理，然后再把请求编码为gb2312字节码（post必须是字节码）。

request = urllib.request.Request(posturl, postData, headers)
response = urllib.request.urlopen(request)
text = response.read()
html = text.decode('gb2312')
#hgjj_last_data = re.findall('', html)
ret_dic = json.loads(html)
url=ret_dic['data']['nexturl']

#{"status":true,"msg":"\u767b\u5f55\u6210\u529f","data":{"nexturl":"http:\/\/oto.mph88.com\/index.php?c=store&a=index&id=1211184742"}}



# 模拟登录结束
# 模拟跳转开始



'''列出网址
url2 = 'http://oto.mph88.com/index.php?c=store&a=index&id=1211184662'
request = urllib.request.Request(url2)
data2 = urllib.request.urlopen(request).read()
data2 = data2.decode('UTF-8', 'ignore')
file = open("F://work/python/html/1.html", 'a', encoding='utf-8')
reObj2 = re.compile(r'http:\/\/oto\.mph88\.com\/[^\"\']*')
data2 = reObj2.findall(data2)
for value in data2:
    file.write(value + "<br/>")
'''