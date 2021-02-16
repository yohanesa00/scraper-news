import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler/finance', params={'tag_from':'wp_cb_mostPopular_more'})
soup = BeautifulSoup(html_doc.text,'html.parser')
popular_area = soup.find(attrs={'class':'grid-row list-content'})
#print(popular_area)

titles = popular_area.findAll(attrs={'class':'media__title'})
substitles = popular_area.findAll(attrs={'class':'media__subtitle'})
images = popular_area.findAll(attrs={'class':'media__image'})
for image in images:
    print(image.find('a').find('img')['title'])
