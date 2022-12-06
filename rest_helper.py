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
             count += 1
             url = (config['Urls']['url' + str(count)])
             print(url[0:8] + username + '@' + url[8:28] + urlpath)
           except:
             exit('\n')
             
  

      print('\n')
             
             
      
        