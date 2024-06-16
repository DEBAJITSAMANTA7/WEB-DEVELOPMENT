# mylist =[1,2,3]
mylist=[1,2,3,4,"HelloWorld","Nato",[6,9,1333]]
# nested List
print(len(mylist))
print(mylist[0::+2])
# Sliceing 

mylist[0]="Debajit"
print(mylist)

mylist2=[]
init =5
for i in range(5,0,-1):
    mylist2.append(init)
    init-=1
print(mylist2)
mylist2.sort
print(mylist2)


# pop remove from it and return it 
it = mylist2.pop(0)
print(it,mylist2)

mylist3=[12,42,4,2,4,99,12,67,2]
mylist4=['a','b','c']
mylist5=[1,2,3]
mylist4.reverse()
mylist5.reverse()
mylist5.remove(2)
print(mylist5,mylist4)

# Nested List  -> list under it list
lis=[1,2,3,4,4,['a','b','c']]
print(lis)
# now this nested list is considered as a single index element then 
# with in it their are indexing over it 
# [5]--> nested index no [5][0] 1st elemet of index element 
print(lis[5][1])


# list comprehension

matix =[[1,2,3],[4,5,6],[7,8,9]]
print(matix[0][2])

# using loop
first_column=[i[0] for i in matix] 
print(first_column)