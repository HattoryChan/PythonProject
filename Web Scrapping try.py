from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup 
'''
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')

except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('1')
'''
'''
def getTitle(url):
    try:
        html = urlopen(url)
    except  HTTPError as e:
        print(None)
    try:
        bs = BeautifulSoup(html.read(), 'lxml')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

'''
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'lxml')
nameList = bs.findAll('span',{'class':'green'})
for name in nameList:
    print(name.get_text())

nameList = bs.find(text='the prince')
print(len(nameList))
print(nameList)

title = bs.find_all(id='title', class_='text')
print(title)

