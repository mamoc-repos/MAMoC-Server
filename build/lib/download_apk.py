#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   File name: download_apk.py
   Author: Dawand Sulaiman

   Download APK_files files from Google Play Store with Python
   This script scraps https://apkpure.com to get the apk download link

   Required libraries: BeautifulSoup and urllib
"""
import os
from os import path

from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests

useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 ' \
            'Safari/601.7.5 '


def search(query):
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
        'User-Agent': useragent
    }).text
    soup = BeautifulSoup(res, "html.parser")
    search_result = soup.find('div', {'id': 'search-res'}).find('dl', {'class': 'search-dl'})
    app_tag = search_result.find('p', {'class': 'search-title'}).find('a')
    download_link = 'https://apkpure.com' + app_tag['href']
    return download_link


def download(link):
    res = requests.get(link + '/download?from=details', headers={
        'User-Agent': useragent
    }).text
    soup = BeautifulSoup(res, "html.parser").find('a', {'id': 'download_link'})
    if soup['href']:
        r = requests.get(soup['href'], stream=True, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                          'Version/9.1.2 Safari/601.7.5 '
        })
        apk_file = os.path.join("./APK_files", link.split('/')[-1] + '.apk')
        with open(apk_file, 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)


def download_apk(app_id):
    print("searching for ", app_id)
    if path.exists("APK_files/{}.apk".format(app_id)):
        print("Found the APK locally")
        return

    download_link = search(app_id)

    if download_link is not None:
        print('Downloading {}.apk ...'.format(download_link))
        download(download_link)
        print('Download completed!')
    else:
        print('No results')
