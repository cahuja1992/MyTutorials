def moveElementToEnd(array, toMove):
    # Write your code here.
    
    beg = 0
    end = len(array)-1
    
    while(beg<end):
      if array[beg] == toMove:
        while(beg<end and array[end]==toMove):
          end-=1
        array[beg], array[end] = array[end], array[beg]
        end-=-1
      beg+=1
    return array


if __name__ == "__main__":
  array = [2, 1, 2, 2, 2, 3, 4, 2]
  toMove = 2
  print(moveElementToEnd(array, toMove))
