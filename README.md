# My Codility solutions

## Lesson 1 Iterations
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

```python
def solution(N):
    gap = max_gap = 0
    start = 0
    while N > 0:
        if start == 0:
            if bin(N & 0b1) == '0b1':
                start = 1
            else:
                N = N >> 1
            continue
        if bin(N & 0b1) == '0b0':
            gap += 1
        else:
            max_gap = max(gap, max_gap)
            gap = 0
        N = N >> 1

    return max_gap
```

## Lesson 2 Arrays

### CyclicRotation
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

```python
def solution(A, K):
    if not A:
        return A

    rotate = K % len(A)
    return A[-rotate:] + A[:-rotate]
```
### OddOccurrencesInArray
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

```python

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
```

## Lesson 3 Time Complexity

### FrogJmp
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

```python
def solution(X, Y, D):
    if D < 0 or X < 0 or Y < 0 or Y < X:
        return 0
    
    dist = Y-X
    steps = dist//D
    if (dist%D) > 0:
        steps += 1
    return steps

'''
Another solution is below to use divmod().

def solution(X, Y, D):
    """Calculate the miminum number of jumps from X to Y.
    :param X: [int] Start position.
    :param Y: [int] End position.
    :param D: [int] Size of the jump.
    :return: Minium number of jumps in O(1) time and space complexity.
    * Integer divide the difference between the start and end position by the jump size.
    * If there is a remainder, froggy needs one more hop to get past the end.
    * Otherwise froggy landed right on it!  Yay for frog.
    """
    quot, rem = divmod(Y - X, D)
    return quot + 1 if rem != 0 else quot
'''
```
### PermMissingElem

```python
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
```