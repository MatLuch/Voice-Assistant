from functions.caucaltor import cauc
from functions.weather import weathe
from functions.Ai import ask_ai
def pointer(text):
    ret = ""
    if "+" in text or "-" in text or "*" in text or "/" in text:
        ret = cauc(text)
    elif "weather" in text:
        ret = weathe(text) 
    else: 
        ret = ask_ai(text)
    if ret is not None:
        return ret
    if ret is None:
        return ""