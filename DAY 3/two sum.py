#method 1[brute force]

def two_sum(num,target):
  for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return[i,j]
  return []

num = [2, 7, 11, 15]
target = 9
print(two_sum(num, target)) 

#time complexity =o(n2)
#space complexity = o(1)



#method 2[hashmap (dict)]

def two_sum(sum,target):
    hashmap={}

    for i ,n in enumerate(num):
        complement=target-n


        if complement in hashmap:
            return [hashmap[complement],i]
        hashmap[n]=i

    return []

num=[2,7,8,9]
target=9
print(two_sum(num,target))

#time complexity =o(n)
#space complexity =o(n) =>uses hashmap


#method 3 (two pointer)

def two_sum(num,target):
    i,j=0,len(num)-1
    while i<j: 
        if num[i]+num[j]==target:
            return[i,j]
        elif num[i]+num[j]<target:
            i+=1
        else:
            j-=1
    return []

num=[2,7,11,8]
target=9
print(two_sum(num,target))

#time complexity =o(n)
#space complexity =o(1) 

