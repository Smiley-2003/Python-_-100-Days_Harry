#author: Naina Mogha
#Date: 24 July 2024
#List methods
l = [1,2,4,6]
print(l)

#append method
l.append(7)
print(l)

#sort method
l = [11,45,1,2,4,6,1,1]
l.sort()
print(l)

#reverse method
l.sort(reverse=True)
print(l)

l.reverse()
print(l)

#index method
print(l.index(1))

#print count
print(l.count(1))


m =l
m[0]=0
print(l)

#insert method
l.insert(1,899)
print(l)

#extend method -> extend l and m
m=[900,1000,1100]
l.extend(m)
print(l)

#and l and m
k=l+m
print(k)
print(l)
