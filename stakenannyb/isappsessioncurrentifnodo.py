def isappsessioncurrentifnodo():
    finddirmakeifno(appdirpath)
    filemakeifno(appdatfile)
    appdatfilecontents = {}
    #PID 3

    appdatfilecontents = literal_eval(str(readdatfile()))
    print ("This is appdatfilecontents" + str(appdatfilecontents))
    apppidstr['PID'] = apppid()
    if not sessionsdatintegrety(appdatfilecontents):
        print ('writting current pid to disk')
        with open(appdatfile, 'w+') as f:
            f.write(str(apppidstr))
    print("this is appdatfilecontents[\'PID\'] " + str(appdatfilecontents['PID']))
    print("this is apppidstr[\'PID\'] " + str(apppidstr['PID']))

    appdatfilecontents = literal_eval(str(readdatfile()))

    print (str(appdatfilecontents['PID']) + '\=\=' + str(apppidstr['PID']))
    return True