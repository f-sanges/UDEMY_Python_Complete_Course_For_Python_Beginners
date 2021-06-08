
#None
print(None)
print(None == None)


import math as mymath #alias
print(mymath.pi)


#assert(5>5) #assertion error
assert(5==5)    # no output when it is true


#break
for i in range(1, 10):
    print(i)
    if i == 5:
        break   #break
    
    
# continue    
for i in range(1, 10):
    print(i)
    if i == 5:
        continue   #continue
    
  
# class
class ExampleClass:
    def function1(parameters):
        print("called function1")
    def function2(parameters):
        print("called function2")

obj1 = ExampleClass()
obj1.function1()
obj1.function2()


# def
def function3():
    pass            #pass
    print("called function3")
function3()


# try raise except finally
try:
    x = 9
    raise ZeroDivisionError
except ZeroDivisionError:
    print("Division cannot be performed")
finally:
    print("Operation completed")
    
    
# global
globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar  #global
    globvar = 5
def write2():
    globvar = 15
read1()
write1()
read1()
write2()
read1()


# in
a = [1,2,3,4]
print(4 in a)
print(4 not in a)

# lambda (anonymous function)
a = lambda x:x*2
for i in range(0,5):
    print(i, a(i))
    
    
# nonlocal
def outer_func():
    a = 5
    def inner_func():
        nonlocal a
        a = 10
        print("inner_func a: ", a)
    inner_func()
    print("outer_func a: ", a)
outer_func()


# return
def func_return():
    a = 6
    return a
print("Value returned: ", func_return())


# while
i = 1
while(i<5):
    print(i)
    i += 1
    
# with
import os
cwd = os.getcwd()
print(cwd)  # to check the current directory and find the file created
with open('example.txt', 'w') as myfile:
    myfile.write("Hello W")
    
# yield
def generator():
    for i in range(6):
        yield i*i
g = generator()
for j in g:
    print(j)