# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

tup_list = [('Samip', 'Shrestha', 22), ('john', 'smith', 20),
            ('will', 'johnson', 18), ('witney', 'son', 19), ('amy', 'jeny', None)]

age = []
full_name = ''

for i in range(len(tup_list)):
    if tup_list[i][2]:
        age.append(tup_list[i][2])

avg_age = sum(age) / len(age)

for i in range(len(tup_list)):
    full_name = tup_list[i][0] + ' ' + tup_list[i][1]
    if tup_list[i][2]:
        if tup_list[i][2] < avg_age:
            print(full_name + ' is young')
        else:
            print(full_name + ' is old')
    else:
        print(full_name)
