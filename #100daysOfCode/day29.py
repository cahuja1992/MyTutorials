
def return_diag(matrix):
  #write your code here
  if matrix ==[] or matrix == [[]]:
      return
  
  output = []
  
  rows = len(matrix)
  cols = len(matrix[0])
  
  r = 0
  c = 0
  
  while r<rows and c<cols:
      output.append(matrix[r][c])
      if (r+c) % 2 == 0:
          if c == cols-1:
              r+=1
          elif r == 0:
              c+=1
          else:
              r-=1
              c+=1
              
      else:
          if r==rows-1:
              c+=1 
          elif c==0:
              r+=1
          else:
              r+=1
              c-=1
  return output
if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))
