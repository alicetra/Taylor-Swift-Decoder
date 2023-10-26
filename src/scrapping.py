from lyricsgenius import Genius

genius = Genius("access token")

# The 'try' loop is present to bypass the timeout error message.
while True:
    try:
        artist = genius.search_artist("Taylor Swift", max_songs=10000)
        break
    except:
        pass

artist.save_lyrics()