# Author: Yu  Time:2018/3/9
from bs4 import BeautifulSoup
import requests,sys

class downloader(object):
	def __init__(self):
		self.server = 'http://www.biqukan.com/'
		self.target = 'http://www.biqukan.com/1_1094/'
		self.names = [] #存放章节名
		self.urls = [] #存放章节链接
		self.nums = 0 #起始章节数

	def get_download_url(self):
		r = requests.get(url=self.target)
		html = r.text
		div_bf = BeautifulSoup(html)
		div = div_bf.find_all('div',class_ = 'listmain')
		a_bf = BeautifulSoup(str(div[0]))
		a = a_bf.find_all('a')
		self.nums = len(a[15:])
		for each in a[15:]:
			self.names.append(each.string)
			self.urls.append(self.server+each.get('href'))

	def get_contents(self,target):
		r = requests.get(url=target)
		html = r.text
		bf = BeautifulSoup(html)
		texts = bf.find_all('div',class_= 'showtxt')
		texts = texts[0].text.replace('\xa0'*8,'\n\n')
		return texts

	def writer(self,name,path,text):
		write_flag = True
		with open(path,'a',encoding='utf-8') as f:
			f.write(name+'\n')
			f.writelines(text)
			f.write('\n\n')
			
if __name__ == '__main__':
        dl = downloader()
        dl.get_download_url()
        print('已开始下载：')
        for i in range(dl.nums):
                dl.writer(dl.names[i],'《一念永恒》.txt',dl.get_contents(dl.urls[i]))
                sys.stdout.write(" 已下载.%.3f%%"% float(i/dl.nums)+'\n')
                sys.stdout.flush()
        print('《一念永恒》下载完成！')
