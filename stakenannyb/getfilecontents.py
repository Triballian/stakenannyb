def getfilecontents(func):
    def openfile(file): 
        with open(file, 'r') as f:
            d = f.read()
            return func()
    return openfile

@getfilecontents
def readsncmd(file):          
        return d

@getfilecontents
def readdatfile(file):
        if not 'PID' in d:
            return "{'PID': ''}"
        return d