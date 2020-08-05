len1 = int(input())
nums1 = sorted(list(map(int, input().split())))
len2 = int(input())
nums2 = sorted(list(map(int, input().split())))

p1 = 0
p2 = 0

while p1<len1 and p2<len2:
  if nums1[p1]>nums2[p2]:
    print(nums2[p2])
    p2+=1 
  elif nums1[p1]<nums2[p2]:
    print(nums1[p1])
    p1+=1
  else:
    p1+=1 
    p2+=1 
while p1<len1:
  print(nums1[p1])
  p1+=1
while p2<len2:
  print(nums2[p2])
  p2+=1
