def bool2str(m_bool):
  if m_bool:
    return 'true'
  else:
    return 'false'
    
def isValidSubsequence(array, sequence):
    is_valid = False
    
    # Write your code here.
    i = 0 
    j = 0 
    while i < len(array) and j<len(sequence):
      if sequence[j] == array[i]:
        j+=1
        i+=1
      else:
        i+=1
    if j==len(sequence):
      return True 
    else:
      return False
      
    
    return bool2str(is_valid)
  
  
if __name__ == "__main__":
  array = [ 5, 1, 22, 5, 6, -1, 8, 10]
  subsequence = [1, 6, -1, 10]
  print(isValidSubsequence(array, subsequence))
  
