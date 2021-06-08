# -*- coding: utf-8 -*-
"""
@author: Fsanges
"""

import os
print(os.getcwd())

#r in front of the path means raw
os.chdir(r'D:\GitHub\PYTHON\UDEMY_Python_Complete_Course_For_Python_Beginners')
print(os.getcwd())


print(os.listdir(r'D:\GitHub\PYTHON\UDEMY_Python_Complete_Course_For_Python_Beginners'))

# mkdir e rmdir
try:
    os.mkdir(r'D:\GitHub\PYTHON\UDEMY_Python_Complete_Course_For_Python_Beginners\testDir')
except IOError:
    print("File already present")
finally:
    os.rmdir(r'D:\GitHub\PYTHON\UDEMY_Python_Complete_Course_For_Python_Beginners\testDir')
     



