

def num_conversion(input_number):
  #write your code here
  mapping = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
  result = ""
  num = input_number
  rem = 0
  factor = 1
  while num>0:
    rem = num%10
    num = num//10
    if rem <= 3:
      result = mapping[factor]*rem + result 
    elif rem == 4:
      result = mapping[factor]+mapping[factor*5]+result
    elif rem == 5:
      result = mapping[factor*5]+result
    elif rem <= 8:
      result = mapping[factor*5]+mapping[factor]*(rem%5)+result
    elif rem == 9:
      result = mapping[factor]+mapping[10*factor]+result
    factor=factor*10
  return result
if __name__ == "__main__":
  input_number = 58
  print(num_conversion(input_number))

