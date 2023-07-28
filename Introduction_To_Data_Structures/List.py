
name_lst = ["Ramehs", "Kamlesh", "Rajesh", "Mukesh", "Abdul"]

#print(name_lst[0]) # first name
#print(name_lst[-1])
#print(name_lst[1:3])

#for i in range(len(name_lst)):
 #   print(name_lst[i])

for name in name_lst:
    print(name)


name_lst.append("Raja")


name_lst.insert(1,"Pooja")


#print(name_lst)

lst2 = ["apple", "orange"]
lst3 = ["Guava", "Banana"]

lst2.extend(lst3)
#print(lst2)


name_lst.remove("Raja")

name_lst.append("Pooja")

#print(name_lst)

print(name_lst)
print(name_lst.index("Pooja",2))

#print(name_lst.index("Pooja",2,4))


print(name_lst.count("Pooja"))

name_lst.reverse()
print(name_lst)

name_lst.sort()

print(name_lst)


name_lst.sort(reverse=True)

print(name_lst)

name_lst.pop()

print(name_lst)


name_lst.pop(4)

print(name_lst)

name_lst_copy = name_lst.copy()

print(name_lst_copy)

name_lst.clear()
print(name_lst)

