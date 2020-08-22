def recursive_call(n, num, temp):
  if n==0:
    res.append(temp)
    return
  for i in range(num, 10):
    recursive_call(n-1, i+1, temp+str(i))
def strictly_increasing(input_number):
  #write your code here
  #return all possible outputs in a list
      
  global res
  res = []
  if input_number==1:
    for i in range(1,10):
      res.append("0"+str(i))
    return res
  recursive_call(input_number, 0, "")
  return res
if __name__ == "__main__":
  input_number = 1
  print(strictly_increasing(input_number))
