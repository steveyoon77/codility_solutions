# https://github.com/johnmee/codility/blob/master/L3_PermMissingElem.py
# I couldn't find better than below idea

def solution(A):
    """Find the missing element in a given permutation.
    :param A: [[int]] List of integers.
    :return: [int] The integer that is missing.
    Requires: O(n) time and O(1) space complexity.
    * Add up all the numbers between 1 and the length of the list + 1.
    * Add up all the numbers in the list.
    * Subtract one from the other.
    * That is your missing number.
    """
    # Why 2? Add 1 because the length of the given array is missing a number.
    # Add another 1 because the range function stops one before the max number.
    full_array = range(1, len(A) + 2)
    return sum(full_array) - sum(A)