from caucaltor import cauc
def pointer(text):
    ret = ""
    if "minus" or "plus" in text:
        ret = cauc(text)

    if ret is not None:
        return ret
    else:
        return ""