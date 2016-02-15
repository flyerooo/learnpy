#!/usr/bin/env python
#coding:utf-8

import urllib2
import re
import os

#声明一个爬虫类
class Spider(object):
    # 构造方法
    def __init__(self):
        self.num = 0
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
    # 获取网页源代码
    def get_page(self, page_index):
        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url = self.url % str(page_index), headers = headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
            exit()
        except urllib2.URLError as e:
            print e
            exit()
    # 分析网页源代码
    def analysis(self, content):
        pattern = re.compile('<p class="font20 color00 marginB14 t3out p">(.*?)<a href="/group/common/course/.*?/" class="go font12">.*?</a></p>.*?<p class="color66 marginB14"><span class="color99">(.*?)</span></p>.*?<p class="color66"><span class="color99">(.*?)</span>(.*?)</p>', re.S)
        items = re.findall(pattern, content)
        return items
    # 保存抓取的内容
    def save(self,items, path):
        for item in items:
            self.num += 1
            item_new = "%d %s %s\n%s%s\n\n" %(self.num,item[0],item[1],item[2],item[3])
            path = 'teachersOfMaizi'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'infoOfTeachers' + '.txt'
            f = open(file_path, 'a')
            f.write(item_new)
            f.close
    # 运行
    def run(self):
        print '开始抓取内容了。。。'
        for i in range(1, 21):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items, 'teachersOfMaizi')
        print '内容抓取完了'

if __name__ == '__main__':
    spider = Spider()
    spider.run()