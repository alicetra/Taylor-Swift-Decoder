from lyricsgenius import Genius


genius = Genius("access token")
# while try loop is there so that the time run out error message will be bypassed
while True:
    try:
        artist=(genius.search_artist("Taylor Swift", max_songs=10000))
        break
    except:
        pass

artist.save_lyrics()