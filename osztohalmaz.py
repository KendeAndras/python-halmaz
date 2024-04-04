def dividers(x):
    val = [1]
    for i in range(2,x//2+1):
        if x%i==0: val.append(i)
    val.append(x)
    return val

a=int(input("az elso szam: "))
b=int(input("az masodik szam: "))

dividers_combined=[]
for i in dividers(a):
    if i in dividers(b): dividers_combined.append(i)

print(a,"osztoi: ",dividers(a), b," osztoi: ",dividers(b), " a kozos osztok: ", dividers_combined, " a legnagyobb kozos oszto: ", max(dividers_combined))

print("set-es(halmaz) kozos osztok: ",set(dividers(a)).intersection(dividers(b)))