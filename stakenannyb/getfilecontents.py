def getfilecontents(func):
    def openfile(file, d=''): 
        with open(file, 'r') as f:
            d = f.read()
            return func(file, d)
    return openfile

@getfilecontents
def readsncmd(file):          
        return d

@getfilecontents
def readdatfile(file, d=''):
        if not 'PID' in d:
            return "{'PID': ''}"
        return d