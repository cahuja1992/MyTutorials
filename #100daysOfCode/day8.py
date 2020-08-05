def LongestPeak(a): 
  # Write your code here
  result=0
  
  up = 0
  down = 0
  
  for idx in range(1, len(a)):
    
    if a[idx]==a[idx-1] or (down>0 and a[idx]>a[idx-1]):
      up = 0
      down = 0
    
    if a[idx]>a[idx-1]:
      up+=1 
    elif a[idx]<a[idx-1]:
      down+=1 
    if up+down!=0:
      result=max(result, up+down+1)
  
  return result
  


if __name__ == "__main__":
  d = [ 1, 3, 1, 4, 5, 6,  
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d)) 
      
