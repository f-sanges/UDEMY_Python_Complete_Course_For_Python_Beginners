class MyComplexNumber:
    # Constructor methods
    def __init__(self,real = 0,imag = 0):
        print("MyComplexNumber constructor executing...")
        self.real_part = real
        self.imag_part = imag
        
    def displayComplex(self):
        print("{0} + {1}j".format(self.real_part,self.imag_part))
        
     
# Create a new object against MyComplexNumber class
cmplx1 = MyComplexNumber(40,50)
# call the function
cmplx1.displayComplex()

# Create a new object
cmplx2 = MyComplexNumber(40,50)
# Specify a new attribute only for the new object
cmplx2.new_attribute = 60
print(cmplx2.real_part, cmplx2.imag_part, cmplx2.new_attribute)

print(cmplx1)
# Delete the object 
del cmplx1
# The cmplx1 object is not present so you will see NameError: name 'cmplx1' is not defined
print(cmplx1)