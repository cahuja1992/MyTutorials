def apartmentHunting(blocks, reqs):
    # Write your code here.
    
    req_block_scores = [[float("inf") for _ in range(len(blocks))] for i in range(len(reqs))]
    
    for r in range(len(reqs)):
      for b in range(len(blocks)):
        
        if blocks[b][reqs[r]]:
          req_block_scores[r][b]=0
        elif b>0 and req_block_scores[r][b-1]!=float("inf"):
          req_block_scores[r][b]=req_block_scores[r][b-1]+1
    
    for r in range(len(reqs)):
      for b in range(len(blocks)-2, -1, -1):
        if req_block_scores[r][b+1]!=float("inf"):
          req_block_scores[r][b]=min(req_block_scores[r][b], req_block_scores[r][b+1]+1)
          
    best_block = None
    b_max = float("inf")
    
    for b in range(len(blocks)):
      t_max = -1
      for r in range(len(reqs)):
        t_max = max(req_block_scores[r][b], t_max)
      if t_max < b_max:
        b_max = t_max
        best_block = b
    #print(best_block)
    return best_block

false = False 
true = True 
blocks = [
 {"gym": false, "school": true, "store": false},
 {"gym": true, "school": false, "store": false},
 {"gym": true, "school": true, "store": false},
 {"gym": false, "school": true, "store": false},
 {"gym": false, "school": true, "store": true}
]
reqs = ["gym", "school", "store"]

apartmentHunting(blocks, reqs)
