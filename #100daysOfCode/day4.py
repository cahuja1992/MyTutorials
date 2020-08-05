def fourNumberSum(array, targetSum):
    # # Write your code here.
    # pairsum_dict = {}
    # n = len(array)
    # for idx1 in range(n-1):
    #   for idx2 in range(idx1+1, n):
    #     pairsum = array[idx1]+array[idx2]
    #     if pairsum in pairsum_dict:
    #       pairsum_dict[pairsum].append([array[idx1], array[idx2]])
    #     else:
    #       pairsum_dict[pairsum] = [[array[idx1], array[idx2]]]
    
    # result = set()
    # for key in pairsum_dict.keys():
    #   target = targetSum - key
    #   if target in pairsum_dict:
    #     for candiadate1 in pairsum_dict[target]:
    #       v1 = candiadate1[0]
    #       v2 = candiadate1[1]
    #       for candiadate2 in pairsum_dict[key]:
    #         v3 = candiadate2[0]
    #         v4 = candiadate2[1]
    #         if v1!=v4 and v1!=v3 and v2!=v3 and v2!=v4:
    #           result.add(tuple(sorted([v1, v2, v3, v4])))
    # return list(result)
    
    result = []
    array = sorted(array)
    n = len(array)
    for i in range(n-3):
      for j in range(i+1, n-2):
        start = j+1
        end = n-1
        while start<end:
          tsum = array[start]+array[end]+array[i]+array[j]
          if tsum < targetSum:
            start+=1
          elif tsum>targetSum:
            end-=1
          else:
            result.append([array[start],array[end],array[i],array[j]])
            start+=1
            end-=1
    return result
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
