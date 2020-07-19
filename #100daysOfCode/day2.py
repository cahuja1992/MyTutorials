def threeNumberSum(array, targetSum):
    # Write your code here.
    array = sorted(array)
    n = len(array)
    
    result = []
    
    for idx in range(n-2):
      num1 = array[idx]
      start = idx+1
      end = n-1
      temp_target = targetSum - num1
      while start<end:
        if temp_target == array[start]+array[end]:
          result.append(sorted([num1, array[start], array[end]]))
          start+=1
        elif temp_target > array[start]+array[end]:
          start+=1
        else:
          end-=1
    return result
if __name__ == '__main__':
  array =  [12, 2, 1, 3, -6, 5, -8, 6]
  targetSum = 0
  print(threeNumberSum(array, targetSum))
  
