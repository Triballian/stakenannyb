from os import path
def finddirmakeifno(dirpath):
    # PID 1
    print('this is dirpath: ' + dirpath)
    if not (path.isdir(dirpath)):
        mkdir(dirpath)
    if not (path.isdir(appdatadirpath)):
        mkdir(appdatadirpath)
    return True