


def recursive_sum(input_matrix):
  #write your code here
  sum = 0
  for idx in range(len(input_matrix)):
    if type(input_matrix[idx])==list:
      sum += recursive_sum(input_matrix[idx])
    else:
      sum+=input_matrix[idx]
  return sum
if __name__ == "__main__":
  input_matrix = [1, 2, [3,4],[5,6]]
  print(recursive_sum(input_matrix))
