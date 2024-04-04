nums = [int(n) for n in input("add meg a szamok: ").split(",")]

#hagyomanyos
square1=[]
for i in nums: square1.append(i**2)

print(square1)

#sajat fv
def square(x):
    return(x**2)
square2=list(map(square,nums))
print(square2)

#lambda fv
square3=list(map(lambda x: x**2,nums))
print(square3)


