def dfs(string, temp, idx):
  if idx == len(string):
    if temp!= "":
      result.append(temp)
    return
  temp += string[idx]
  dfs(string, temp, idx+1)
  temp = temp[:-1]
  dfs(string, temp, idx+1)
def power_set(input_string):
  #write your code here
  #return all possible outputs in a list
  #res = ["a","ab","abc","ac","b","bc","c"]
  

  
  global result
  result = []
  input_string = ''.join(sorted(input_string)) 
  dfs(input_string, "", 0)
  return sorted(list(set(result)))
if __name__ == "__main__":
  input_string = "abc"
  print(power_set(input_string))




