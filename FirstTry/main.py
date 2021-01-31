import requests
from bs4 import BeautifulSoup


URL = "https://www.sinoptik.bg/sofia-bulgaria-100727011/hourly"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
#print(soup.prettify())
#results = soup.find("span", id="wfByHourTemp")
results = soup.findAll('span', {'class': 'wfByHourTemp'})

#print(soup.get_text())
#print(soup.find_all('th'))
#print(results)
i = 1
for count, result in enumerate(results):
	if count % 2 != 0:
		for r in result:
			print(f"{i} with {r}C")
			i += 1


