my_list = [10, 20, 30, 40, 50]

print(my_list[2])
print(my_list[1:4])
print(my_list[-1])

my_list[3] = 45
my_list[3:] = [45, 55]

A = my_list[:2]
B = A.copy()
B.append("Bilangan")
B.extend([70, 80, 90])

combined_list = A + B
print(combined_list)