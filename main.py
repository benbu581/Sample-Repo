#Write your code below this line 👇
import os
import requests

import sys

print(sys.executable)

def greet(who_to_greet):
  greetings = 'Hello, {}'.format(who_to_greet)
  return greetings


print(greet('World'))
print(greet('Benjamin'))
