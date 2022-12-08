'''
Below is my idea, but it fails on "self.assertEqual(700, Q.odd_occurrences_in_array.solution(arr))"

import collections

def solution(A):
    found = 0
    if not A:
        return A
    B = collections.Counter(A)
    for k, v in B.items():
        if v == 1:
            found = k

    return found
'''

# https://github.com/johnmee/codility/blob/master/L2_OddOccurencesInArray.py
def solution(A):
    """Find the value that does not have a match in an odd sized array.
    :param A: [[int]] an array of integers with an odd number of elements.
    :param N: [int] length of the array.
    :return: The value which does not have a duplicate.
    * With a collection to accumlate unmatched values, step through the array.
    * Remove the value from the unmatched collection.
    * If that fails, add it to the unmatched collection.
    * At the end of the list, there should be one unmatched value in the collection.
    * The 'collection' can be either a set, or a dictionary (with the value as the key and a boolean as the value).
      The dictionary is slightly faster; I guess finding a value in a set is more work than indexed dict keys,
      but imho the set is faintly more elegant.
    """
    unmatched = set()
    for element in A:
        try:
            unmatched.remove(element)
        except KeyError:
            unmatched.add(element)
    return unmatched.pop()