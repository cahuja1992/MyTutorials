class Solution:
    def ispalin(self, st):
        return st == st[::-1]
    def dfs(self, substring, temp):
        if substring=="":
            self.res.append(" ".join(temp))
        else:
            for i in range(1,len(substring)+1):
                if self.ispalin(substring[:i]):
                    self.dfs(substring[i:], temp+[substring[:i]])
    def partition(self, s):
        if len(s)==0:
            return
        
        self.res = []
        
        self.dfs(s, [])
        
        return self.res



def recursive_palindrome(input_string):
  #write your code here
  #return all possible outputs in a list
  #res = ["n i t i n","n iti n","nitin"]
  res = Solution().partition(input_string)
  return res
if __name__ == "__main__":
  input_string = "nitin"
  print(recursive_palindrome(input_string))




