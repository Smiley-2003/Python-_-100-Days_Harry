# Enter your code here
a = "1"
#a = 1
b = "2"
#b = 2
print(int(a)+int(b))

#Implicit Typecasting
c = 1.9
d = 8
print(c + d)

#Typecasting in python
print("Typecasting in python")
#Explicit Conversion
string = "15"
number = 7
string_number = int(string) #throws an error if the string
#string not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ",sum)

#Implicit
#python automatically converts
#a to integer
a = 7
print(type(a))

#Python automatically converts b to float
b = 3.0
print(type(b))

#Pyhton automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))