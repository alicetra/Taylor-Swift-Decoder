import re

def text_formatting(text):
    text = re.sub(r"\(.*?\)|\[.*?\]|/|,|\"|'|(\.\.\.)|\.", "", text)
    text = re.sub(r"-"," ",text)
    # Remove unicode from utf-8 files by converting to ascii and then back to its original form 
    text = text.encode("ascii", "ignore").decode()
    return text