
def groupAnagrams(strs):
    groups = {}

    for s in strs:
        key = ''.join(sorted(s))

        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]

    result = []
    for value in groups.values():
        result.append(value)

    return result
            



print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))