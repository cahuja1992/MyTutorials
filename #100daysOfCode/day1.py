"""
    Two Number Sum:
    
    Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. 
    If any two numbers in the input array sum upto the target sum, the function should return them in an array, in any order. 
    If no two numbers sum up to the target sum, the function should return an empty array. 
    Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
    You can assume that there will be at most one pair of numbers summing up to the target sum.
    
    There are 3 possible solutions for the question as follow.
"""
import unittest

"""
# O(n^2,) time | O(1) space
def twoNumberSum(array, targetSum):
    for i in range(0, len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []
# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    complements = {}
    n  = len(array)
    for i in range(0, n):
        temp = targetSum - array[i]
        if temp in complements:
            return sorted([temp, array[i]])
        else:
            complements[array[i]] = temp
    return []
"""

# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort() #inplace sort 
    left  = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

    
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)

    def test_case_2(self):
        output = twoNumberSum([4, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(4 in output)
        self.assertTrue(6 in output)

    def test_case_3(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 15)
        self.assertTrue(len(output) == 0)

    def test_case_4(self):
        output = twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163)
        self.assertTrue(len(output) == 2)
        self.assertTrue(210 in output)
        self.assertTrue(-47 in output)

    def test_case_5(self):
        output = twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
        self.assertTrue(len(output) == 0)


if __name__ == '__main__':
    unittest.main()