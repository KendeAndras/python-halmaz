l1=input('elso lista: ').split()
l2=input('masodik lista: ').split()

h1=set(l1)
h2=set(l2)

h=h1.intersection(h2)
u=h1.union(h2)

print("az elso lista: ",l1)
print("az masodik lista: ",l2)
print("az elso halmaz: ",h1)
print("az masodik halmaz: ",h2)
print("a metszet halmaz: ",h)
print("a unio halmaz: ",u)