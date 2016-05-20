"""
Library used to parse the type of configuration files associated with crypto currencies.
These files are tipically called ini files.
"""
'''
The MIT License (MIT)

Copyright (c) 2016 Noe De La Cruz, Jr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Created on Apr 16, 2016
@author: Noe De La Cruz


'''
#utils.py python3 
from re import sub
#from ast import literal_eval

def getconf(name):
    """ 
        Pass in the string name of the configuration file to be parsed into your envrionment.
        Returns dict called envars.
    """
    # grab the env from jvim.conf
    cname = name
    cfile = open(cname + '.conf')
    
    envars = {}

   
    for line in cfile:
        

        marker = '#'

        #crline = line.partition(marker)[0].strip().replace('\\', '/')
        crline = line.partition(marker)[0].strip()
        #crline = sub(r'[C|c]:|/$', '', crline)
        
        #print('this is the line: crline ' + crline)

        if not crline:
            continue

        # check to see if the line has a comment. using regular experssions
        
        line = crline.strip()
        #print('this is the line:' + str(line))
        line = line.replace(' = ','=')
        #print('this is the line:' + str(line))

        cdata = line.split('=')
        
        #print('this is the line: cdata[1] ' + str(cdata[1]))
        #print('this is the line:' + str(line))
        #alist = cdata[1].strip().split(',')
        #blist = sub(r'\[|\]|\"', '' , str(cdata[1].strip().split(',')))
        #clist = str(cdata[1].strip().split(',')).replace(r'"', '')
        envars[str(cdata[0].lower())] = cdata[1].strip().split(',')
        
        


    return envars

# envars = getconf('/Users/Noe/workspace/stakenanny/candiapps/test/test')