from datetime import date
from datetime import timedelta
import lxml
import requests
from bs4 import BeautifulSoup


today = date.today()

song_list = dict()

songs_file = open('songs.csv', 'w')

# Указываем сколько дней отнять
days_take_away = 10

for i in range(days_take_away):
    new_day = today + timedelta(days=-i)
    url = "http://eldoradio.ru/playlist/" + new_day.strftime('%Y/%m/%d')

    for time in range(0, 24):
        if len(str(time)) == 1:
            url_for_parsing = url + "/0"+str(time) + ":00"
        else:
            url_for_parsing = url + "/"+str(time) + ":00"

        response = requests.get(url_for_parsing)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('span', class_='title')

        for song_name in quotes:
            if song_name.string is not None:
                if song_name.string in song_list:
                    song_list[song_name.string] += 1
                else:
                    song_list[song_name.string] = 1


for song in song_list:
    songs_file.write(song + " ; " + str(song_list[song]) + "\n")

songs_file.close()
print("Конец парсинга!")
