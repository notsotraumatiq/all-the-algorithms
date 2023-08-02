
def longest_unique_substring(string):

    i, j = 0, 0
    h = {}
    curcount = 0
    maxcount = 0
    longest = [i, j]
    while j < len(string):

        if string[j] in h:
            i = max(i, h[string[j]] + 1)

        h[string[j]] = j

        if j - i + 1 > maxcount:
            longest = [i, j]
            maxcount = j - i + 1
        j += 1

    return string[longest[0]:longest[1] + 1]







print(longest_unique_substring('abcbdefghiabcbb'))
