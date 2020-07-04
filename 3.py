# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

paragraph = "dog cat god haat ate eat"

x = paragraph.split()


def findAnagram(x):

    dict = {}

    for word in x:
        key = ''.join(sorted(word))

        if key in dict.keys():
            dict[key].append(word)
        else:
            dict[key] = []
            dict[key].append(word)
        output = ""
        for key, value in dict.items():
            if len(value) > 1:
                output = output + ' '.join(value) + ' '

    return output


print(findAnagram(x))
