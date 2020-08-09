import itertools 

def max_col(test_list):
  #write your code here
  n=len(test_list[0])
  res = test_list[0]
  
  for i in range(1, len(test_list)):
    for j in range(len(test_list[i])):
      if j < n:
        if test_list[i][j]>res[j]:
          res[j]=test_list[i][j]
      else:
        res.append(test_list[i][j])
        n+=1
  
  return res
if __name__ == "__main__":
  input_list = [[1, 8, 1], [1,21], [9]]
  print(max_col(input_list))
