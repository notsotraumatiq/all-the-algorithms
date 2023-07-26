def common_characters(strings):
    # Write your code here.

    smallestword = "dafafsbsdbsdb"
    for word in strings:
        if len(word) < len(smallestword):
            smallestword = word

    smallestword = set(smallestword)

    for word in strings:
        word = set(word)
        for char in list(smallestword):
            if char not in word:
                smallestword.remove(char)

    return list(smallestword)



print(common_characters(["cool","lock","cook"]))
