#Name: Naina Mogha
#Introduction to Lists
#Date: 22 July 2024
#       0  1  2  3  4  5  6    7                         -3  -2 -1
marks =[3,5,6,"Naina",True,"6",7,2,32,345,23]
#marks =[3,5,6,"Naina"]
#print(marks)
#print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])


print(marks[-3])#Negative index
print(marks[len(marks)-3])#Positive index
print(marks[5-3])#positive index
print(marks[2])#positive index

if "6" in marks:
    print("Yes")
else:
    print("No")

#Same thing applies for string as well!
    if"Na" in "Naina":
        print("yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])

lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)



