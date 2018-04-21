from bs4 import BeautifulSoup
import requests,sys

class Downloader():

    def __init__(self):
        self.server = 'http://www.biqukan.com'
        self.target = 'http://www.biqukan.com/20_20623/'
        self.names = []
        self.urls = []
        self.nums = 0
        
    def get_content(self,target):
        r = requests.get(url=target)
        html = r.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div',class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def get_urls(self):
        r = requests.get(self.target)
        html = r.text
        div_bf = BeautifulSoup(html)
        div_url = div_bf.find_all('div',class_='listmain')
        a_bf = BeautifulSoup(str(div_url[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[12:])
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def writer(self,name,path,text):
        writer_flag = True
        with open(path,'a',encoding = 'utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = Downloader()
    dl.get_urls()
    print('即将开始下载！')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'幻游猎人.txt',dl.get_content(dl.urls[i]))
        sys.stdout.write('已下载.%.3f%%'% float(i/dl.nums)+'\n')
        sys.stdout.flush()
    print('《幻游猎人》下载完成！')
