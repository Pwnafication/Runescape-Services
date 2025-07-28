def groupAnagrams(strs):
    groups = {}  # use normal dict

    for word in strs:
        count = [0] * 26  # letter frequency for a-z

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)  # use immutable key

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())