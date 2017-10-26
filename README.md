# wallpaper
爬取wallpaper的小爬虫  

壁纸爬取来自于 WALLPAPER ABYSS URL:https://wall.alphacoders.com/?lang=chinese  

通过首页中的内链获取分类下的各部分的URL地址  

判断网址属于分类并进行本地创建文件夹后进行爬取

因为爬取中 games，movies,gifs不便保存直接pass掉

每个分类的保存写一个类来进行处理，方法都基本一致但是在解析url时响应时间没有很好的处理 希望能得到提示
