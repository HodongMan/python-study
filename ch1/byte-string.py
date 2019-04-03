import os

def toString(string):

    if isinstance(string, bytes):
        return string.decode('utf-8')

    return string

def toBytes(stirng):

    if isinstance(string, str):
        return string.encode('utf-8')
    
    return string

def readRandomToFile(fileName):

    with open(fileName, "wb") as f:
        f.write(os.urandom(10))