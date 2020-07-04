# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

insert = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]


def insert_in_file(data):
    file = open("file.csv", "w+")
    file.write('name,address,age \n')
    for i in range(len(data)):
        value = tuple(map(str, data[i]))
        single = ','.join(value)
        file.write(single + '\n')

    file.close()


insert_in_file(insert)
