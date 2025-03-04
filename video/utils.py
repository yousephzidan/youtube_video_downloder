from time import gmtime
from time import strftime

def duration(seconds):
    return strftime("%H:%M:%S",gmtime(seconds))


