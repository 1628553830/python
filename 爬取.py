import urllib
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档可能的编码
        res.encoding = res.apparent_encoding
        #返回网页HTML代码
        return res.text
    except:
        return 'Error!'
def download(url,name):
    f=requests.get(url)
    with open(name,"wb") as code:
       code.write(f.content)
def check(c):
    for f in c.find_all("a"):
        link=f.get("href")
        return link  
def main():
    #附加BeautifulSoup函数教程：http://www.jsphp.net/python/show-24-214-1.html
    url = 'https://bing.lylares.com/detail/r3yVKRAI.html'#第一个子网页
    k=1
    for i in range(0,339):
       print("----------------- PROCESSING ",k," ----------------------")
       print("Present Url Is ",url)
       k=k+1
       soup = BeautifulSoup(getHTMLText(url), 'html.parser')#获取网页源代码并传输，缩进格式
       if soup.find_all("a")==None:
           print("Error!")
           break
       # 这一段用来提取图片名字
       for b in soup.find_all("a"):
           name=b.get('download')
           if name!= None:
               if name[28:34]=='4k.jpg':
                 break
       #
       # 这一段用来提取图片链接
       for a in soup.find_all("a"):
          link=a.get('href')
          if link!=None:
             if link[0:36]=='https://bing.lylares.com/download/4k':
                print("Imagedownloadlink Is ",link)
                download(link,name)
                break
       #
       #这一段用来提取上一篇的链接，方便跳转
       for c in soup.find_all("div"):
           Class=c.get('class')
           if Class==['post-navigation-with-image','my-2']:
                url=check(c)
       #
main()

