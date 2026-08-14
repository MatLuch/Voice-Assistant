from functions.caucaltor import cauc
from functions.weather import weathe

def pointer(text):
    ret = ""
    if "+" in text or "-" in text:
        ret = cauc(text)
    if "weather" in text:
        ret = weathe(text) 
    if ret is not None:
        return ret
    else:
        return ""