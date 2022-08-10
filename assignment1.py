#write a Python program which accepts the radius of a circle from the user and computes area.
from cmath import pi

radius= float(input("Input the radius of the circle:"))
area= pi*(radius**2)
print(area)

#write a Python program to accept a filename from the user and print the extension of that.
filename= input("Input the filename:")
extn=filename.split(".")
print(filename)
print ("The extension of the file is : ", extn[-1])
