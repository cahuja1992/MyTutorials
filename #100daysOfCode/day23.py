

def find_target(input_matrix,target):
  if len(input_matrix)==0:
    return False
  if len(input_matrix[0])==0:
    return False
  n = len(input_matrix)
  m = len(input_matrix[0])
  start = 0 
  end = m*n -1
  
  while start <= end:
    mid = (start+end)//2
    if input_matrix[mid//m][mid%m]<target:
      start = mid+1
    elif input_matrix[mid//m][mid%m]>target:
      end = mid-1
    else:
      return True
  return False
if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  target = 3
  print(find_target(input_matrix,target))
