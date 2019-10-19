from lxml import html
import requests

url_android_platform = 'https://developer.android.com/reference/packages.html'
url_android_support = 'https://developer.android.com/reference/android/support/packages.html'
url_android_wearable = 'https://developer.android.com/reference/android/support/wearable/packages.html'

# Retrieve android platform packages
page = requests.get(url_android_platform)
tree = html.fromstring(page.content)
td = tree.xpath('//td[@class="jd-linkcol"]/a/text()')
file = open('../Android-API-Files/android_platform_packages.txt', 'w')
for elem in td:
    file.write(elem + "\n")
file.close()

# Retrieve android platform packages
page = requests.get(url_android_support)
tree = html.fromstring(page.content)
td = tree.xpath('//td[@class="jd-linkcol"]/a/text()')
file = open('../Android-API-Files/android_support_packages.txt', 'w')
for elem in td:
    file.write(elem + "\n")
file.close()

# Retrieve android wearable packages
page = requests.get(url_android_wearable)
tree = html.fromstring(page.content)
td = tree.xpath('//td[@class="jd-linkcol"]/a/text()')
file = open('../Android-API-Files/android_wearable_packages.txt', 'w')
for elem in td:
    file.write(elem + "\n")
file.close()
