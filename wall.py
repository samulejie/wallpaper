#coding = utf-8
import urllib.request
from headers import Headers
import random
from lxml import etree
import time
class Wall():
    '''
        解析传递的url  获取到该页面的所有图片的链接地址并获取到页数和页的url地址
        https://wall.alphacoders.com/by_collection.php?id=597&lang=Chinese&page=2
        设置自增函数 并从网站中获取的url地址 判断最大的数字
        //div[@class="thumb-container-big"]/div/div/a/@href  每个图片的url地址后半部分
        //ul[@class="pagination"]/li/a/text()  获取到页数信息后[-2]
    '''
    def __init__(self,url,filename):
        self.filename = filename
        self.url = url
    def get_xml(self,url):
        '''
            返回xml文件的方法
        :return:
        '''
        uas = Headers('user_agent.txt')
        ua = random.choice(uas.headers())
        self.headers = {
            'User-Agent': ua
        }
        try:
            requests = urllib.request.Request(url = url,headers = self.headers)
            html = urllib.request.urlopen(requests,timeout = 50).read()
            xml = etree.HTML(html)
            return xml
        except:
            requests = urllib.request.Request(url=url, headers=self.headers)
            html = urllib.request.urlopen(requests, timeout=100).read()
            xml = etree.HTML(html)
            return xml


    def get_picture_url(self,page_url,filename):
        '''
            获得大图的url并保存下来
        :return:
        '''
        xml = self.get_xml(page_url)
        picture_urls = xml.xpath('//div[@class="thumb-container-big "]/div/div/a/@href')
        print(picture_urls)
        j = 1
        for i in range(0,len(picture_urls)):
            try:
                full_picture_url = 'https://wall.alphacoders.com/' + picture_urls[i]
                picture_xml = self.get_xml(full_picture_url)
                picture = picture_xml.xpath('//*[@id="container_page"]/div[4]/a/img/@src')
                with open(self.filename +'\\'+ picture[0][-10:-4] + '.jpg','wb') as f:
                    request = urllib.request.Request(url = picture[0],headers = self.headers)
                    image = urllib.request.urlopen(request,timeout=10).read()
                    print(full_picture_url)
                    f.write(image)
                    print(str(j) +'.'+picture[0][-10:-4] + '.jpg' + '已经下载完毕')
                    j+=1
            except:
                print('error')
    def get_page_url(self):
        '''
            判断页数并自增
        :return:
        '''
        xml = self.get_xml(self.url)
        max_page = int(xml.xpath('//ul[@class="pagination"]/li/a/text()')[-2])
        for i in range(1,max_page+1):
            print(max_page)
            page_url = self.url + '&page=' + str(i)
            print(page_url)
            self.get_picture_url(page_url,self.filename)










