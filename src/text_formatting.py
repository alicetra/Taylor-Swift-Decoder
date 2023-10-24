import re

def text_formatting(text):
    text = re.sub(r"\(.*?\)|\[.*?\]|/|,|\"|'|(\.\.\.)|\.", "", text)
    text = re.sub(r"-"," ",text)
    return text