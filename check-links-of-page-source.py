import requests
from bs4 import BeautifulSoup
import urllib.request
import re

page = 'http://trendyol.com'

urls = []

html_page = urllib.request.urlopen(page)
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    urls.append(link.get('href'))

url_responses = {}

for url in urls:
    temp_r = requests.get(url)
    url_responses[url] = temp_r.status_code

print(url_responses)