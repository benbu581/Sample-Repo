#Write your code below this line 👇
import os
import requests

import sys
from jnpr.junos 
import Devicefrom jnpr.junos.utils.config 
import Configfrom jnpr.junos.exception 
import *if __name__ == '__main            __':
    try:        
      dev = Device(host='172.25.11.1', user='lab', pass       wd='lab123')        
      dev.open()        
      conf = Config(dev)        conf            .lock()        conf.load(path="bgp-config.conf", merge=True)        c       onf.commit()        conf.unlock()        print("Configuration applied      !")    except ConnectAuthError:
    print("Authentication error!")              
    except ConnectTimeoutError:        
    print("NETCONF connection time   d out!")    
    except ConnectError as error:        print("Other connect        error: %s" % str(error))    
    except ConfigLoadError:        print("Fa      ilure when loading a configuration!")    
    except Exception as error:               
      print("Some other exception happened: %s" % str(error))    
      finally:        
      dev.close()

print(sys.executable)

def greet(who_to_greet):
  greetings = 'Hello, {}'.format(who_to_greet)
  return greetings


print(greet('World'))
print(greet('Benjamin'))
