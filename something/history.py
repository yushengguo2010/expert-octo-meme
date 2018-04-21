from bs4 import BeautifulSoup
import requests,sys,time

class Downloader():
    def __init__(self):
        self.server = 'http://www.shumilou.org'
        self.target = 'http://www.shumilou.org/88_88768/'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_contents(self,target):
        req = requests.get(url = target)
        req.encoding = 'gb2312'
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div',class_='chapter-content')
        texts = texts[0].text.strip().replace('\xa0'*4,'\n').replace('一秒记住【书迷楼小说网 www.shumilou.org】，精彩小说无弹窗免费阅读！','')
        return texts

    def get_urls(self):
        req = requests.get(self.target)
        req.encoding = 'gb2312'
        html = req.text
        bf = BeautifulSoup(html)
        bf_url = bf.find_all('div',class_ = 'fd-list')
        a_bf = BeautifulSoup(str(bf_url))
        a = a_bf.find_all('a')
        self.nums = len(a[2:])
        for i in a[2:]:
            self.names.append(i.string)
            self.urls.append(self.target+i.get('href'))

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = Downloader()
    dl.get_urls()
    print('Downloading starts in minutes: ')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'时间简史.txt',dl.get_contents(dl.urls[i]))
        time.sleep(2)
        sys.stdout.write('已下载.%.3f%%'% float(i/dl.nums)+'\n')
        sys.stdout.flush()
    print('Downloading completed.')
