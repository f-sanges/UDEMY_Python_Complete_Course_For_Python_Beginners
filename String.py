# -*- coding: utf-8 -*-
"""
@author: FSanges

"""

# Using enumerate

a = "university"

mylist_enumerate = list(enumerate(a))
print(mylist_enumerate)

print(len(a))


default_order = "{} {} {}".format('Today', 'is', 'Wednesday')
print(default_order)

positional_order = "{1} {0} {2}".format('is', 'Today', 'Wednesday')
print(positional_order)

#find
print(positional_order.find('is'))

