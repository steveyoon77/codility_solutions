import unittest
import random
import Q


class Test(unittest.TestCase):

    @staticmethod
    def gen_array(L, odd):
        """Generate a list of sample data: random integers in pairs.
        :param L: the length of the list is double this int
        :param odd: the odd integer out
        * Generate a list of random ints half the size required.
        * Join it to a duplicate of itself.
        * Append the odd value.
        * Shuffle the array and return.
        """
        arr = []
        for _ in range((L - 1) // 2):
            val = random.randint(1, 100000)
            arr.extend((val, val))
        arr.append(odd)
        random.shuffle(arr)
        return arr

    def test_binary_gap(self):
        max_int = 2147483647
        self.assertEqual(Q.binary_gap.solution(9), 2)
        self.assertEqual(Q.binary_gap.solution(529), 4)
        self.assertEqual(Q.binary_gap.solution(20), 1)
        self.assertEqual(Q.binary_gap.solution(15), 0)
        self.assertEqual(Q.binary_gap.solution(32), 0)
        self.assertEqual(Q.binary_gap.solution(1041), 5)
        self.assertEqual(Q.binary_gap.solution(max_int), 0)
        self.assertEqual(Q.binary_gap.solution(6), 0)
        self.assertEqual(Q.binary_gap.solution(328), 2)
        self.assertEqual(Q.binary_gap.solution(9), 2)
        self.assertEqual(Q.binary_gap.solution(11), 1)
        self.assertEqual(Q.binary_gap.solution(19), 2)
        self.assertEqual(Q.binary_gap.solution(42), 1)
        self.assertEqual(Q.binary_gap.solution(1162), 3)
        self.assertEqual(Q.binary_gap.solution(5), 1)
        self.assertEqual(Q.binary_gap.solution(51712), 2)
        self.assertEqual(Q.binary_gap.solution(561892), 3)
        self.assertEqual(Q.binary_gap.solution(1073741825), 29)
        self.assertEqual(Q.binary_gap.solution(1610612737), 28)

    def test_cyclic_rotation(self):
        self.assertEqual(Q.cyclic_rotation.solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(Q.cyclic_rotation.solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(Q.cyclic_rotation.solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(Q.cyclic_rotation.solution([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])
        self.assertEqual(Q.cyclic_rotation.solution([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])
        self.assertEqual(Q.cyclic_rotation.solution([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])
        self.assertEqual(Q.cyclic_rotation.solution([], 5), [])

    def test_odd_occurrences_in_array(self):
        self.assertEqual(7, Q.odd_occurrences_in_array.solution([9, 3, 9, 3, 9, 7, 9]))
        arr = self.gen_array(5, 4)
        self.assertEqual(4, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(11, 4)
        self.assertEqual(4, Q.odd_occurrences_in_array.solution(arr))
        self.assertEqual(42, Q.odd_occurrences_in_array.solution([42]))
        arr = self.gen_array(201, 42)
        self.assertEqual(42, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(601, 4242)
        self.assertEqual(4242, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(2001, 100)
        self.assertEqual(100, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(100003, 500000)
        self.assertEqual(500000, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(100003, 700)
        self.assertEqual(700, Q.odd_occurrences_in_array.solution(arr))
        arr = self.gen_array(999999, 5000111222)
        self.assertEqual(5000111222, Q.odd_occurrences_in_array.solution(arr))

if __name__ == '__main__':
    unittest.main()