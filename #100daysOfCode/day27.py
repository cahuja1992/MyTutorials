
def return_vertically(s):
  #write your code here
  space_count = 0
  op = []
  
  op_idx = 0
  for idx in range(len(s)):
      if s[idx]==" ":
          while op_idx < len(op):
              op[op_idx] += " "
              op_idx+=1
          op_idx=0
          space_count+=1
          continue
      if op_idx >= len(op):
          op.append(" "*space_count+s[idx])
      else:
          op[op_idx] += s[idx] 
      op_idx+=1
      
  for idx in range(len(op)):
      op[idx] = op[idx].rstrip()
  return op
if __name__ == "__main__":
  input_string = "HOW ARE YOU"
  print(return_vertically(input_string))
