from bs4 import BeautifulSoup
import requests

def get_img():
    target = 'https://www.bing.com/'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    div_bf = bf.find_all('background-image')

    print(div_bf)

get_img()
