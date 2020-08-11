

def check_anagram(sentence_1,sentence_2):
  sentence_2 = sentence_2.lower()
  sentence_1 = sentence_1.lower()
  #write your code here
  m = len(sentence_1)
  n = len(sentence_2)
  if m==0 or n==0:
    return False
  helper_dict = {}
  for letter in sentence_1:
    if letter in helper_dict:
      helper_dict[letter]+=1 
    else:
      if letter!=" ":
        helper_dict[letter]=1
  for letter in sentence_2:
    if letter in helper_dict:
      helper_dict[letter]-=1 
    else:
      if letter!=" ":
        return False
  for letter in helper_dict.keys():
    if helper_dict[letter]>0:
      return False
  return True
  
  return res
if __name__ == "__main__":
  sentence_1 = "anagram"
  sentence_2 = "anagram"
  print(check_anagram(sentence_1,sentence_2))




