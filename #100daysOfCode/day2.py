import unittest

def threeNumberSum(array, targetSum):
	array.sort()
	n = len(array)
	triplets = []
	for i in range(n-2):
		left = i + 1
		right = n -1
		
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left +=1
			elif currentSum > targetSum:
				right -=1
	return triplets
  
class TestProgram(unittest.TestCase):
    def assertListEquals(self, l1, l2):
        return sorted(l1) == sorted(l2)

    def test_case_1(self):
      self.assertListEquals(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]])
      
    def test_case_2(self):
        self.assertEquals(threeNumberSum([1, 2, 3], 6), [[1, 2, 3]])

    def test_case_3(self):
        self.assertEquals(threeNumberSum([1, 2, 3], 7), [])

    def test_case_4(self):
        self.assertEquals(threeNumberSum([8, 10, -2, 49, 14], 57), [[-2, 10, 49]])
  
if __name__ == "__main__":
  unittest.main()