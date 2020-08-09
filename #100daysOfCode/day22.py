

def get_key(input_dict,key):
  #write your code here
  res=[]
  for k in input_dict:
    if key in input_dict[k]:
      res.append(input_dict[k][key])
  return res
if __name__ == "__main__":
  input_dict = {
    'sup' : {"a" : 7, "b" : 9, "c" : 12}, 
			'is' : {"a" : 15, "b" : 19, "c" : 20}, 
			'best' :{"a" : 5, "b" : 10, "c" : 2}
    
  }
  key = "c"
  print(get_key(input_dict,key))




