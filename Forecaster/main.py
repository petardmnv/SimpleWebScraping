import requests
from bs4 import BeautifulSoup
import json
from datetime import date, datetime

URL = "https://www.foreca.bg/Bulgaria/Sofia--Capital/Sofia/10-day-forecast?date=2021-02-01"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
scripts = soup.findAll('script')


def make_string_to_list(text: str) -> list:
	return list(text.split(" ")) 

def find_all(text: list, word: str) -> list:
	index_list = []
	start = 0
	while True:
		try:
			start = text.index(word, start)
			index_list.append(start)
			start += 1
		except:
			return index_list

for script in scripts:
	if "var daily_data" in str(script.string):
		#result = json.loads(script.string)
		# script.string - better
		result = (script.string).replace("}", '')
		result = result.replace(";", '')
		result = result.replace(",", ' ')
		result = result.replace("'", '')
		result = result.replace("{", '')
		result = result.replace(":", '')
		result = result.replace("  ", ' ')

		current_result = make_string_to_list(result)
		current_date = []
		current_date.append(date.today().strftime("%Y%m"))
		current_date.append(datetime.now().strftime("%d"))
		current_date.append(datetime.now().strftime("%H"))
		current_date.append("0000")

		hour = int(datetime.now().strftime("%H"))

		day = date.today().strftime("%A")
		print(f"Weather forecast for {day} is:\n")


		for i in range(hour, 25):
			if i == 24:
				new_day = int(datetime.now().strftime("%d")) + 1
				current_date[1] = str(new_day).rjust(2, '0')
				current_date[2] = "00"
			else:
				current_date[2] = str(i).rjust(2, '0')

			time_index = find_all(current_result, "".join(current_date))
			
			for t in time_index:
				print(f"Time: {current_result[t + 2][0]}{current_result[t + 2][1]}:{current_result[t + 2][2]}{current_result[t + 2][3]}")	
				print(f"Temp: {current_result[t + 4]}")
				print(f"Rain per square meter: {current_result[t + 14]}")
				if current_result[t + 22] == "Ясно":
					print(f"The weather is: {current_result[t + 22]}")
				else:		
					print(f"The weather is: {current_result[t + 22]} {current_result[t + 23]}")		