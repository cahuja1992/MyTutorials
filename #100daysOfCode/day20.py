import re

def remZero(ip_addr):
  #write your code here
  result = re.sub("\.0+", ".", ip_addr)
  
  return result
if __name__ == "__main__":
  ip = "016.08.0904.96"
  print(remZero(ip))
