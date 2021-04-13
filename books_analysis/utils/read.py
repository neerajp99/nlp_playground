"""
    Takes a filename and returns the list of lines 
"""
def read(file):
    lines = open (file, "r", encoding="utf8").read().lower()
    lines = lines.replace("\n", " ").replace("."," .").replace('"', '').split(" ")
    return lines 
