#  參考 https://www.youtube.com/watch?v=9Z9xKWfNo7k&t=72s  基本教學
# install beautifulsoup4 using "pip install beautifulsoup4" 以解析網頁
import urllib.request as req
import bs4
import csv
import re

verb = 'etre'
category = 'Indicatif'
tense = 'Plus-que-parfait'

url=f'https://www.the-conjugation.com/french/verb/{verb}.php'
#一header讓Crawler看起來像是一般人的Request
Request=req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
with req.urlopen(Request) as response:
    data = response.read().decode("utf-8")

root = bs4.BeautifulSoup(data, "html.parser")
element = root.find('h2', text = re.compile(category), attrs = {'class' : 'mode'})
while re.search(tense, str(element)) == None:
	element = element.next_element

word = element.find('div', attrs = {'class' : 'tempscorps'})
x = str(word).replace('<br/>', '\n')

word = bs4.BeautifulSoup(x, "html.parser")

data = [verb, '', '0', category, tense]
data += word.text.split('\n')
data.pop()
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(data)

