pyteven=[]
odd=[]
char=[]
x=[1,3,4,2,7,9,10,12]
for i in x:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
    # elif i%2==0 and i%2!=0:
    #     char.append(i)    
print(even)
print(odd)
# print(char)