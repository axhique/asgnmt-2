# to take multiple tuples in list as input :

im=input("enter the no of tuples in list :")
result=[]
container=[]

for i in range(int(im)):
    tup=input("enter the tuple : ").split(',')

    for k in tup:
        container.append(int(k))

    result.append(tuple(container))
    container.clear()

#to sort list in acending order of last value of tuples

lis=[]
as_ord = []

for i in result:
    lis.append(i[-1])

set1 = set(lis)
list1 = list(set1)

list1.sort()

for j in list1:
    for k in result:
        if j == int(k[-1]) :
            as_ord.append(k)

print (as_ord)
  


""" example:
 enter the no of tuples :3
 enter the tuple ;5,6
 enter the tuple ;9,1
 enter the tuple ;8,5 
 
 input list will be  [(5, 6), (9, 1), (8, 5)]
 output list [(9, 1), (8, 5) ,(5, 6)] """