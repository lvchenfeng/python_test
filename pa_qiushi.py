import urllib.request
import re

def pa_qiubai(pages):
    i=1
    for page in range(pages):
        url = 'http://www.qiushibaike.com/hot/page/' + str(pages)
        try:
            #request = urllib.request.Request(url)

            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            request = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            #pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                  #               'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
            pattern = re.compile('class="content">[\s\S]*?<span>([\s\S]*?)</span>')
            items = re.findall(pattern, content)
            for item in items:
                duan="第"+str(i)+"个段子：\n"
                item_data=item.replace("<br/>","\n")
                xian="\n\n\n-----------------------------------------\n"
                open("./qiubai.txt","a").write(duan+item_data+xian)
                i+=1
        except Exception as e:
            # if hasattr(e, "code"):
            #     print(e.code)
            # if hasattr(e, "reason"):
            #     print(e.reason)
            continue
pa_qiubai(35)