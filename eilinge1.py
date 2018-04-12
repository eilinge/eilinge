import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_img(html):
    p = r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    imglist = re.findall(p,html)
    for each in imglist:
        print(each)

if __name__ == '__main__':
    url = 'http://cn-proxy.com'
    get_img(open_url(url))
