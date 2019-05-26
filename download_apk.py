
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def get_apk_url(package_name): 
    response = Request('http://apk-dl.com/' + package_name,headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(response).read(), 'html.parser')
    temp_link = soup.find("div",{'class': 'download-btn'}).find("a")["href"]
    response = Request('http://apk-dl.com/' + temp_link, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(response).read(), 'html.parser')
    temp_link2 = soup.find("section",{'class': 'detail'}).find("a")["href"]

    response = Request(temp_link2, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(response).read(), 'html.parser')
    temp_link3 = soup.find("div",{'class': 'contents'}).find("a")["href"]
    
    return "http:" + temp_link3

print(get_apk_url('com.facebook.katana'))
