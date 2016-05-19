from filemakeifno import filemakeifno
from getfilecontents import readsncmd
from os import getcwd
from subprocess import check_output
from re import search



def sncmdintegraty(contents, searchstrng):
        
    return search('searchstrng', str(contents))

    


def issncmdfileinstartupifnodo(appdata, appdatfile, snpy):
        startupfolder = appdata + r'/Microsoft/Windows/Start Menu/Programs/Startup'
        sncmd = startupfolder + '/stakenammy.cmd'

        currentwd = getcwd()
        pydir = check_output(['where', 'python']).decode('unicode_escape').split()
        sncommandln = pydir[0] + ' "' + currentwd + '\\' + snpy +  '" start'
         
        
        filemakeifno(sncmd)
        snmdcontents = readsncmd(appdatfile)
        filecontents=sncmdintegraty(snmdcontents, sncommandln)
        if not filecontents == snpy:
            isappstartup=input('\t Stakenanny start script is not detected in windws startup directory. \n\tWould you like stakenanny to run when windows starts up?[y/n]')
            if isappstartup.lower()=='y':
                 with open(sncmd, 'w+') as f:
                    f.write(str(sncommandln))
        
        return True