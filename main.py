import requests
from bs4 import BeautifulSoup

from datetime import datetime

time = datetime.now()
time = str(time.hour) + ":" + str(time.minute)



data = requests.get("https://www.timeanddate.com/moon/phases/netherlands/amsterdam")

soup = BeautifulSoup(data.text, 'html.parser')

moonVisible = soup.find('span', {'id': 'cur-moon-percent'}).text

div = soup.find('div', {'id': 'qlook'})
current_phase = [a.text for a in div.find_all('a')]
current_phase = ''.join(current_phase)

print(f"Good day! It is {time}.")
print(f"The moon is currently visible for {moonVisible} and the current phase is {current_phase}.")
   