#Name: Naina Mogha
#Date:22 July 2024
#Python Tutorial
#Functions_Argument

'''
def average(a,b,c=1):
    print("The average is",(a+b+c)/2)

average(1,2,3)
'''

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        print("Average is: ",sum /len(numbers))
        return 7
        return sum /len(numbers)
 
average(4 ,6)
average(b=9)

c = average(5,6,7,1)
print(c)


'''
def name(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Buchnan",lname="Barnes",fname="James")

'''

            
