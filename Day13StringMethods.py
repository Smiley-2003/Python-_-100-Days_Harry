#Author : Naina Mogha
#Date: 28 June 2024
#STRING METHODS
print("STRING METHODS:")


#Strings are immutable
a = "Naina"
print(len(a))
print(a)
#Print all letter of string a in upper case
print(a.upper())#Upper method

#Print all letter of string a in lower case
print(a.lower())#Lower method

#print(a)
print(a.rstrip("!"))

#replace all string of Naina with Sadhna
print(a.replace("Naina","Sadhna"))


a= "!!Naina!!!!!!!!!!!!Naina"
#split the string into a list
print(a.split(" "))

blogHeading = "ïntroduction to js"
print(blogHeading)

#Captilize make first character captial of string
print(blogHeading.capitalize())

str1 = "Naina Mogha is my Name"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Naina"))


str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))


str1 = "He's name is Dan . He is an honest man."
print(a.count("Naina"))

print(str1.find("ishh"))
#print(str1.index("ishh"))

str2 = "WelcomeToTheConsole"
print(str2.isalnum())
str1 = "Welcome00"
print(str2.isalpha())

str3 = "hello world"
print(str3.islower())
