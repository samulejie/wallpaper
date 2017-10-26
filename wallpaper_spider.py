#coding = utf-8
import urllib.request
from lxml import etree
import random
import os
from wall import Wall
from art import Art
from photos import Photos
from pics import Pics
from avatars import Avatars
from gifs import Gifs
from games import Games
from movies import Movies
from headers import Headers

#解析完网站获得 源码解析后通过xpath方法来的到所需要的数据


#大类的名字
def makedir(xml):
    '''
        解析首页的url地址
        并解析出每个小类的url
    '''
    all_genres = xml.xpath('//*[@id="popular_collections"]/fieldset/legend/a/text()')
    all_genres_urls = xml.xpath('//*[@id="popular_collections"]/fieldset/legend/a/@href')
    genres_urls = xml.xpath('//*[@id="popular_collections"]/fieldset[i]/ul/li/a/@href')
    #通过for循环获取名字 并创建名字
    for i in range(0,len(all_genres)):
        page_filename = r'C:\python_project\wallpaper\\' + all_genres[i]
        if (not os.path.exists(page_filename)):
            os.makedirs(page_filename)
        genres_urls = xml.xpath('//*[@id="popular_collections"]/fieldset['+str(i+1)+']/ul/li/a/@href')
        genres = xml.xpath('//*[@id="popular_collections"]/fieldset[' + str(i+1) + ']/ul/li/a/text()')
        for j in range(0,len(genres)):
            filename = page_filename + '\\' + genres[j]
            if (not os.path.exists(filename)):
                os.makedirs(filename)
            judge(genres_urls[j],filename)
def judge(genres_url,filename):
    '''
        获得每一个小类的url地址后进行判断为什么类型在进行解析
    '''
    if "wall" in genres_url:
        wall = Wall(genres_url,filename)
        wall.get_page_url()
    elif "art" in genres_url:
        art = Art(genres_url,filename)
        art.get_page_url()

    elif "photos" in genres_url:
        photos = Photos(genres_url,filename)
        photos.get_page_url()

    elif "pics" in genres_url:
        pics = Pics(genres_url,filename)
        pics.get_page_url()
    elif "avatars" in genres_url:
        avatars = Avatars(genres_url,filename)
        avatars.get_page_url()
    elif "gifs" in genres_url:
        gifs = Gifs()

    elif "games" in genres_url:
        games = Games()
    elif "movies" in genres_url:
        movies = Movies()


#使用urllin.request 解析网址
if __name__ == '__main__':
    url = 'https://wall.alphacoders.com/?lang=chinese'
    proxies = [
        {'http': '218.3.75.149:9000'},
        {'http': '121.232.147.94:9000'},
        {'http': '211.159.171.58:80'},
        {'http': '182.246.207.192:80'},
        {'http': '182.43.198.112:808'},
        {'http': '163.125.222.240:8118'},
        {'http': '121.232.147.94:9000'},
    ]
    uas = Headers('user_agent.txt').headers()
    ua = random.choice(uas)
    proxie = random.choice(proxies)
    proxy_support = urllib.request.ProxyHandler(proxie)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    headers = {
        'User-Agent': ua

    }
    requests = urllib.request.Request(url = url,headers = headers)
    html = urllib.request.urlopen(requests).read()
    xml = etree.HTML(html)
    makedir(xml)









