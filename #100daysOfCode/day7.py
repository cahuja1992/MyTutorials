def monoArray(array):
    # Write your code here.
    n = len(array)
    if n==1:
      return True
      
    ptr1 = False
    ptr2 = False
    for idx in range(1, n):
      if array[idx]<array[idx-1]:
        ptr1 = True
      elif array[idx]>array[idx-1]:
        ptr2 =True
      if ptr1 and ptr2:
        return False
    return True
      

if __name__ == "__main__":
  array = [1,10,100]
  print(monoArray(array))
