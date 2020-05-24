def sample(first, last, **userinfo):
  profile = {}
  profile["firstname"] = first 
  profile["last"] = last
  for key, value in userinfo.items():
    profile[key] = value
  return profile
  

def addNum(b, a,  *nums):
  print(a)
  print(b)
  sum = a + b
  for num in nums:
    sum += num
  print(sum)
  
  
def printComp(d2):
  for i,j in d2.items():
    print("The Keys is {0}, The values is {1}".format(i,j) )
