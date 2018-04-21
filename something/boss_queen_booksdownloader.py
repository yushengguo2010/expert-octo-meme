from bs4 import BeautifulSoup
import requests , sys

class Downloader():

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/43_43060/'
        self.names = []
        self.urls = []
        self.nums = 0
        
    def get_download_url(self):
        r = requests.get(self.target)
        html = r.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div',class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[12:])   #剔除不必要的章节，并统计章节数
        for i in a[12:]:
            self.names.append(i.string)
            self.urls.append(self.server + i.get('href'))

    def get_content(self,target):
        r= requests.get(url=target)
        html=r.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div',class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n').replace('&1t;/p>','')
        return texts

    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    dl = Downloader()  #实例化类
    dl.get_download_url()  #调用类中的获取目录链接的方法
    print('即将开始下载： ')
    for i in range(dl.nums):
        dl.writer(dl.names[i],'极品女总裁.txt',dl.get_content(dl.urls[i])) # 调用writer方法
        sys.stdout.write("已下载.%.3f%%"% float(i/dl.nums)+'\n')
        sys.stdout.flush()
    print('《极品女总裁》下载完成！')
