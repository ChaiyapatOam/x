list1=[]
list2=[]
x= int(input("Input Number : "))
for i in range(1,x+1):
    list1.append(i)
#print(list1)

for a in range(len(list1)):
    list2.append(list1[a]**4)
print(list2)
print("ผลรวมคือ "+ str(sum(list2)))
