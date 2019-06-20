# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:09:31 2019

@author: Administrator
"""

import requests,useragent
import csv,time
from lxml import etree
import re
class Douban(object):
    def __init__(self):
        self.headers = useragent.headers
        self.baseurl = 'http://s.tuniu.com/search_complex/whole-cd-0-%E4%BA%91%E5%8D%97/list-h1/'

    def getPage(self,url,params):
        res = requests.get(url,params=params,headers = self.headers)
        res.encoding = 'utf-8'
        html = res.text
        
        self.parsePage(html)
    def parsePage(self,html):
        #把json格式的响应内容转为Python数据类型
        parseHtml = etree.HTML(html)
        title = parseHtml.xpath('//p[@class="title"]/span/@name')            
        money = parseHtml.xpath('//ul/li/div/a/div/div/em/text()')        
        manyidu = parseHtml.xpath('//ul/li/div/a/div/div/div/span/i/text()')
        p= re.compile(r'<div class="trav-person">.*?<i>(.*?)</i>',re.S)
        people = p.findall(html)
        if not people:
            people = '0'
       
        self.writeMysql(title,money,manyidu,people)
    def writeMysql(self,title,money,manyidu,people):
        with open('途牛2.csv','a',newline='') as f:
            writer = csv.writer(f)
#            writer.writerow(['云南'])
            for r in range(0,len(title)):
                
                info=[title[r],money[r]+'起',manyidu[r]+'%',people[r]]
#                print(info)
                writer.writerow(info)
    def main(self):
#        s = ['%E5%9B%9B%E5%B7%9D','%E4%B8%89%E4%BA%9A','%E4%BA%91%E5%8D%97','%E6%B5%99%E6%B1%9F','%E5%B9%BF%E4%B8%9C']
        s = ['%E6%B1%9F%E8%8B%8','%E6%B2%B3%E5%8D%97','%E8%B4%B5%E5%B7%9E','%E5%8C%97%E4%BA%AC','%E5%AE%89%E5%BE%BD']
        for x in s:
            self.baseurl = 'http://s.tuniu.com/search_complex/whole-cd-0-'+x+'/list-h1/'
            for x in range(1,3):
                url = self.baseurl+str(x)
                print(url)
                params = {
                        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.9',
                        'Connection': 'keep-alive',
                        'Cookie': 'tuniuuser_citycode=MjgwMg==; tuniu_partner=MTAwLDAsLDI2OWJhMjJhNDAxOWQyNDRjYzNkMGU4ODZkMjQ1NGFk; isHaveShowPriceTips=1; Hm_lvt_51d49a7cda10d5dd86537755f081cc02=1560821970; OLBSESSID=s7cb84u3ictlo828rmud8lai83; tuniuuser_ip_citycode=MjgwMg==; p_phone_400=4007-999-999; p_phone_level=0; p_global_phone=%2B0086-25-8685-9999; _tacau=MCxkOGU4MjEyNi0yY2Q1LWQyYjYtMjY5MC02ZTA3Mzk4ZjY5NWEs; _tact=MDkyZjViZmYtODEwNi1kMDkxLTdjZjYtMTA0YTUwOGQ0Y2U1; _tacz2=taccsr%3D%28direct%29%7Ctacccn%3D%28none%29%7Ctaccmd%3D%28none%29%7Ctaccct%3D%28none%29%7Ctaccrt%3D%28none%29; _taca=1560821969805.1560821969805.1560821969805.1; _tacb=OGRlYzQ2YTItZTFmZC01ZDBmLWIyZTctZjgwZDE0MGY4OTVl; _tacc=1; tuniu_searched=a%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A6%3A%22%E5%9B%9B%E5%B7%9D%22%3Bs%3A4%3A%22link%22%3Bs%3A52%3A%22http%3A%2F%2Fs.tuniu.com%2Fsearch_complex%2Fwhole-cd-0-%E5%9B%9B%E5%B7%9D%2F%22%3B%7D%7D; connect.sid=s%3AlXy0fzEkExf95OrRCG_mxD_mP6DnGj27.zi%2Fr03vovTs%2FLg5ZYFtgh27phsJl2dtfYtPpI2qbSKA; Hm_lpvt_51d49a7cda10d5dd86537755f081cc02=1560822847',
                        'Host': 's.tuniu.com',
                        'Referer': url,
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest',
                        }
                
                
                self.getPage(url,params)

if __name__=='__main__':
    start = time.time()
    douban = Douban()
    douban.main()
    end = time.time()
    print('执行时间:%.2f秒'%(end-start))
s = ['%E6%B1%9F%E8%8B%8','%E6%B2%B3%E5%8D%97','%E8%B4%B5%E5%B7%9E','%E5%8C%97%E4%BA%AC','%E5%AE%89%E5%BE%BD']


















