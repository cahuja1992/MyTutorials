class Solution:
    def isvalid(self,st):
        if len(st)!=1 and st[0]=='0':
            return False
        if 0<=int(st)<=255:
            return True
    def dfs(self, substring, temp):
        if substring == "" and len(temp)==4:
            self.result.append(".".join(temp))
        if len(temp)<4:
            for i in range(1,5):
                if i<=len(substring):
                    if self.isvalid(substring[:i]):
                        self.dfs(substring[i:], temp+[substring[:i]])
    
    def restoreIpAddresses(self,s):
        if s == "":
            return
        self.result = []
        self.dfs(s, [])
        return self.result
def valid_ip(input_string):
  #write your code here
  #return all possible outputs in a list
  res = Solution().restoreIpAddresses(input_string)
  return res
if __name__ == "__main__":
  input_string = "0000"
  print(valid_ip(input_string))
