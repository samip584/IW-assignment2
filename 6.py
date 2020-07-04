# Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

name_list = ['Samip', 'Will', 'John', 'Masey']


def find_John(x):
    found = ''
    for i in x:

        if i == 'John':
            found = 'John'
            break
        else:
            found = 'not found'
    print(found)


find_John(name_list)
