from datetime import date
from datetime import timedelta
import lxml
import requests
from bs4 import BeautifulSoup

url = 'http://eldoradio.ru/playlist/2021/08/16/17:00'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='title')

for name in quotes:
    print(name)



today = date.today()

# Указываем сколько дней отнять
days_take_away = 2

for i in range(days_take_away):
    new_day = today + timedelta(days=-i)
    url = "http://eldoradio.ru/playlist/" + new_day.strftime('%Y/%m/%d')

    for time in range(0, 24):
        if len(str(time)) == 1:
            url_for_parsing = url + "/0"+str(time) + ":00"
        else:
            url_for_parsing = url + "/"+str(time) + ":00"
        # print(url_for_parsing)
# Генерируем адреса для парсинга
# http://eldoradio.ru/playlist/2021/08/16/17:00

# for month in range(1, 8):
#     text_month = "0"+str(month)
#     for day
