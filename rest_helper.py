Usage = '''
  Usage:
  rest_helper.py [-n] <number> [-c] <filename>
  rest_helper.py [--num] <number> [--config] <filename>
  '''


from configparser import ConfigParser
from docopt import docopt


config = ConfigParser()
comparser = docopt(Usage)


num = int(comparser['<number>'])
if  ['-c']: file = comparser['<filename>'] 


if  num > 0 :
      print('\n')
      count=0
      config.read(file)
      username = (config['Data']['username'])
      urlpath  = (config['Data']['urlpath'])
      
      
      while count < num:
           try:
             string=''
             count += 1
             urlcount = 0
             url = (config['Urls']['url' + str(count)])
             while url[urlcount] != '/':
                   urlcount += 1
             urlcount += 2    
             string = url[0:urlcount]
             print(string + username + '@' + url[urlcount:(len(url))] + urlpath)
           except:
             exit('\n')
             
  
      print('\n')
      
             
             
      
        