#coding=utf-8
import urllib.request
from headers import Headers
import random
from lxml import etree
import time

class Pics():
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def get_xml(self, url):
        uas = Headers('user_agent.txt')
        ua = random.choice(uas.headers())
        self.headers = {
            'User-Agent': ua
        }
        try:
            requests = urllib.request.Request(url=url, headers=self.headers)
            html = urllib.request.urlopen(requests,timeout=30).read()
            xml = etree.HTML(html)
            return xml
        except:
            requests = urllib.request.Request(url=url, headers=self.headers)
            html = urllib.request.urlopen(requests,timeout = 100).read()
            xml = etree.HTML(html)
            return xml

    def get_picture_url(self, page_url, filename):
        xml = self.get_xml(page_url)
        picture_urls = xml.xpath('//div[@class="boxgrid caption"]/a/@href')
        # 获得每一页里面图片的链接url
        for i in range(0, len(picture_urls) + 1):
            try:
                picture_xml = self.get_xml(picture_urls[i])
                picture = picture_xml.xpath('//img[@onclick="resize();"]/@src')
                with open(self.filename + '//' + picture[0][-10:-4] + '.jpg', 'wb') as f:
                    request = urllib.request.Request(url=picture[0], headers=self.headers)
                    image = urllib.request.urlopen(request, timeout=10).read()
                    f.write(image)
                    print(picture[0][-10:-4] + '.jpg' + '已经下载完毕')
            except:
                print('error')
    def get_page_url(self):
        xml = self.get_xml(self.url)
        max_page = int(xml.xpath('//*[@id="page_container"]/div[10]/div[1]/ul/li/a/text()')[-2])
        for i in range(1, max_page + 1):
            page_url = self.url + '?page=' + str(i)
            self.get_picture_url(page_url, self.filename)