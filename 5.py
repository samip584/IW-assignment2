# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

my_name = ('Samip', 'Shrestha', 22)

a_list = []

a_list.append(my_name)

more_name = ('john', 'smith', 20)

more_name_2 = ('will', 'johnson', 22)

a_list.append(more_name)
a_list.append(more_name_2)

sort = sorted(a_list, key=lambda tup: tup[2])


print(sort)
