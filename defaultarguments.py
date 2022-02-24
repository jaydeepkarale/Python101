# default arguments are evaluated only once when the def is executed.

import time
def check_time(arg=time.ctime()):
  print(arg)

  
print(check_time())  
print(check_time())
print(check_time())

# output
>>> print(check_time())
Thu Feb 24 22:16:54 2022
None
>>>
>>> print(check_time())
Thu Feb 24 22:16:54 2022
None
>>> print(check_time())
Thu Feb 24 22:16:54 2022
None
>>> print(check_time())
Thu Feb 24 22:16:54 2022
None

# Immutable default values don't cause issues

# Mutable default values however cause trouble

def add_spam(menu=[]):
  menu.append("spam")
  return menu

breakfast = ['bacon','cheese']
add_spam(breakfast)

>>> ['bacon', 'cheese', 'spam']

breakfast2 = ['egg','cheese']
add_spam(breakfast)
>>> ['egg', 'cheese', 'spam']


# The menu list is only created once & subsequent function calls just uses the same list
>>> add_spam()
['spam']
>>> add_spam()
['spam', 'spam']
>>> add_spam()
['spam', 'spam', 'spam']
>>> add_spam()
['spam', 'spam', 'spam', 'spam']

# always use immutable values as default
