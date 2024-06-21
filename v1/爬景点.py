# auchor JCC

import requests
import random
import time
import csv
from lxml import etree
from bs4 import BeautifulSoup
f=open('携程游记_青岛.csv','w',encoding='utf-8')
wr=csv.writer(f)
wr.writerow(['标题','内容'])
class Spider():
    def __init__(self):
        self.num = 1
        self.oper = requests.session()
        self.page=1
        self.first_url = 'https://you.ctrip.com/travels/qingdao5/t3'
    def Main_spiders(self):
        for i in range(1, 9):
            print("")
            mUrl=""
            if i==1:
                mUrl=self.first_url+'.html'
            else:
                mUrl=self.first_url+'-p'+str(i)+'.html'
            main_headers = {
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'authority': 'you.ctrip.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'referer': mUrl,
                'upgrade-insecure-requests': "1",
            }
            #print(mUrl)
            req = self.oper.get(mUrl, headers=main_headers)
            html = etree.HTML(req.text)

            title_url = html.xpath('//div[@class="journalslist cf"]/a[@class="journal-item cf"]/@href')
            for i in range(0, len(title_url)):
                title_url[i] = 'https://you.ctrip.com' + title_url[i]
            title = html.xpath('//div[@class="iteminner"]/dl/dt/text()')
            #print(title_url)
            #print(title)
            # 爬取游记内容
            self.content_spider(title_url,title)

    def content_spider(self, url_list,title):
        #print(len(url_list))
        index=0
        content_headers = {
            'authority':'you.ctrip.com',
            'method':'GET',
            'path':'/travels/qingdao5/3968139.html',
            'scheme':'https',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Cache-Control':'max-age=0',
            'Cookie':'ASP.NET_SessionSvc=MTAuNjAuMzUuMTQ2fDkwOTB8amlucWlhb3xkZWZhdWx0fDE2NTY0NjYwMTYzODQ; Hm_lvt_e4211314613fcf074540918eb10eeecb=1716255153; Hm_lpvt_e4211314613fcf074540918eb10eeecb=1716255153; MKT_CKID=1716255153398.dq7vp.lygk; GUID=09031067216193750444; _bfa=1.1716255153684.47ceth.1.1716255153684.1716255153684.1.1.0; _ubtstatus=%7B%22vid%22%3A%221716255153684.47ceth%22%2C%22sid%22%3A1%2C%22pvid%22%3A1%2C%22pid%22%3A0%7D; _jzqco=%7C%7C%7C%7C1716255153702%7C1.961006120.1716255153346.1716255153346.1716255153346.1716255153346.1716255153346.undefined.0.0.1.1; _RF1=153.3.21.147; _RSG=nHa7qpuwCZ8ngoZqjuwWX9; _RDG=28e78c5e5900db2e54081c0b3c6d68e496; _RGUID=88cceb8c-f41e-4471-9860-eb8b748f2ab1; _bfaStatusPVSend=1; _bfaStatus=send',
            'Priority':'u=0, i',
            'Sec-Ch-Ua':'"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        }
        for url in url_list:
            #print(url)
            req = self.oper.get(url, headers=content_headers)
            soup=BeautifulSoup(req.text,'lxml')
            c=soup.find("div","ctd_content")#"journalslist cf")#
            #print("\n"*8)
            if c!=None:
                content=c.get_text(strip=True)
                #print(content)
                row=[]
                #f.write(title[index]+"\n")
                #f.write(content + '\n')
                row.append(title[index])
                row.append(content)
                wr.writerow(row)
            #f.write('\n' * 6+'\n')

            

            print('\n' + '第' + str(self.num) + '篇爬取完成！' + '\n')
            print("-" * 80)
            self.num += 1
            index+=1
            t = random.choice(range(2, 7))
            print("延迟" + str(t) + "秒钟!")
            time.sleep(t)

if __name__ == '__main__':
    spider = Spider()
    spider.Main_spiders()
    f.close()
    
                                              
        

        
        
        




