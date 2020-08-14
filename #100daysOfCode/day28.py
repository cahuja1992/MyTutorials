def islands(grid, r, c):
  if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]!='1':
      return
  grid[r][c]="-1"
  islands(grid, r-1, c)
  islands(grid, r, c-1)
  islands(grid, r+1, c)
  islands(grid, r, c+1)
def count_island(grid):
  if grid == [] or grid ==[[]]:
    return 0 
  
  count=0
  for r in range(len(grid)):
      for c in range(len(grid[0])):
          if grid[r][c]=='1':
              islands(grid, r, c)
              count+=1
  return count
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))
