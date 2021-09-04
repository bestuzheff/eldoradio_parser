import os
import eyed3

directory_in_str = "E:\\gooDrive\\songs"

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp3"):
        filename = filename.removesuffix('.mp3')
        artist_plus_song_name = filename.split('-')
        artist = artist_plus_song_name[0].strip()
        song_name = artist_plus_song_name[1].strip()

        try:
            audio_file = eyed3.load(directory_in_str + "\\" + filename + ".mp3")
            audio_file.tag.artist = artist
            audio_file.tag.title = song_name
            audio_file.tag.save()
            print("good:" + artist + " - " + song_name)
        except any:
            print("bad: " + filename)
