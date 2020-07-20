"""
    Write a function that takes in two non-empty arrays of integers,
    find the pair of numbers (one from each array)
    whose absolute difference is closet to zero, and returns an array containing these two numbers, 
    with the numbsers, with the number from the first array in the first position.

    You can assume that there will only be one pair of numbers with the smallest difference.

    **Sample Input**

    ```
        arrayOne = [-1, 5, 10, 20, 28, 3]
        arrayTwo = [26, 134, 135, 15, 17]
    ```

    **Sample Output**
    ```
        [28, 26]
    ```
"""

import unittest
import math

# O(nlog(n)) + O(mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort() 
    arrayTwo.sort()

    idxOne = 0
    idxTwo = 0

    smallest = math.inf
    current = math.inf

    smallestPair = []
    n = len(arrayOne)
    m = len(arrayTwo)

    while idxOne < n and idxTwo < m:
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]
            
    return smallestPair
			

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
        expected_output = [28, 26]
        self.assertEqual(output, expected_output)
        

    def test_case_2(self):
        output = smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17])
        expected_output = [20, 17]
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        output = smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031])
        expected_output = [25, 1005]
        self.assertEqual(output, expected_output)

    def test_case_4(self):
        output = smallestDifference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031])
        expected_output = [25, 1005]
        self.assertEqual(output, expected_output)

    def test_case_5(self):
        output = smallestDifference([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031])
        expected_output = [2000, 1032]
        self.assertEqual(output, expected_output)
        
    def test_case_6(self):
        output = smallestDifference([240, 124, 86, 111, 2, 84, 954, 27, 89],  [1, 3, 954, 19, 8])
        expected_output = [954, 954]
        self.assertEqual(output, expected_output)

    def test_case_7(self):
        output = smallestDifference([0, 20], [21, -2])
        expected_output = [20, 21]
        self.assertEqual(output, expected_output)

    def test_case_8(self):
        output = smallestDifference([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530])
        expected_output = [1000, 1014]
        self.assertEqual(output, expected_output)

    def test_case_9(self):
        output = smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530])
        expected_output = [-123, -124]
        self.assertEqual(output, expected_output)
        
    def test_case_10(self):
        output = smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530])
        expected_output = [530, 530]
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()