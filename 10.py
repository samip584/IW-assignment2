# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def convert(str, separator):
    temp = [str[0].lower()]
    for i in str[1:]:
        if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            temp.append(separator)
            temp.append(i.lower())
        else:
            temp.append(i)

    return ''.join(temp)


str = "ThisIsCamelCased"
print(convert(str, '_'))
