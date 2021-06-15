list=[]
print("Enter the size of the list")
n= int(input())

for i in range(0,n):
    print("Enter a number in list")
    num=int(input())
    list.append(num)

print("The list is")
for x in list:
    if x>=0:
        print(x)
