from functions.caucaltor import cauc
from functions.weather import tempature, rain
from functions.Ai import ask_ai
def pointer(text):
    ret = ""
    if "+" in text or "-" in text or "*" in text or "/" in text:
        ret = cauc(text)
    elif "temperature" in text:
        ret = tempature(text)
    elif "rain" in text:
        ret = rain(text) 
    else: 
        ret = ask_ai(text)
    if ret is not None:
        return ret
    if ret is None:
        return ""