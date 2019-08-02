# Q10.2

def group_anagrams(strings):
    # Created sorted version
    strings = [(''.join(sorted(s)), s) for s in strings]

    # Sort by first entry
    strings.sort(key=lambda x: x[0])

    # Remove sorted versions
    strings = [s for _, s in strings]

    return strings

"""
Note on solution

Don't need to do the sort on the sorted strings. Just insert into a dictionary!

This improves runtime complexity.

"""

strings = ['cat', 'dog', 'monkey', 'god', 'tac']

print(group_anagrams(strings))