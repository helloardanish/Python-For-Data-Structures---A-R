#immutable

tuple1 = (23,34,565,75,43)

print(tuple1[0])

for val in tuple1:
    print(val)


my_info = ("A R", "India", "Bihar")


print(my_info.index("India"))

my_info_list = list(my_info)

my_info_list.append("Bihar2")

my_info_list[0] = "Admin"

my_info_fin = tuple(my_info_list)


print(my_info_fin)