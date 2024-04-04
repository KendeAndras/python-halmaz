def dividers(x):
    val = [1]
    for i in range(2,x//2+1):
        if x%i==0: val.append(i)
    val.append(x)
    return val



nums=[int(i) for i in input("add meg a szamok: ").split()]

dictionary={}
for i in nums: dictionary[i]=dividers(i)
print(dictionary)
