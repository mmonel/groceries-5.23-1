
my_numbers = [1, 2, 3, 4, 5, 6, 7]
my_numbers2 = []
my_numbers3 = []
k = 4
j = 8
l = 3

for i in my_numbers:
    my_numbers2.append (i * 100)

filter_list = [n for n in my_numbers if ((n > k) & (n < j))] 
filter_list2 = [n for n in my_numbers if n > j]
filter_list3 = [n for n in my_numbers2 if n > l] 

for i in filter_list3:
    my_numbers3.append (i * 100)




print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION:", my_numbers2)

print("--------------")
print("numbers filtered:", filter_list)

print("--------------")
print("numbers filtered > 8:", filter_list2)

print("--------------")
print("numbers filtered > 300:", my_numbers3)

print("--------------")
