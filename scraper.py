import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.morewords.com/ends-with/ism/")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

f = open("words.txt", 'w')
for word in soup.find_all('a'):
	f.write(word.get_text() + '\n')
f.close()