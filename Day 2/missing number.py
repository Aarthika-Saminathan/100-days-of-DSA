#method 1 (using normal method)

def missing_number(arr):
    n=len(arr)+1
    total=sum(arr)
    actual_val=n*(n+1) //2

    missing_number=actual_val-total
    return missing_number

arr=[1,2,4,5]
print(missing_number(arr))


#method 2  (using sorting)

def missing_number(num):
    num.sort()

    for i in range(len(num)):
        if num[i]!=i+1:
            return i+1
    return len(num)+1

num=[1,2,3,4]
print(missing_number(num))

#method 3 (dsa)



def missing_number(arr):
    n=len(arr)+1

    xor_total = 0
    xor_arr = 0

   # to find xor for the numbers n=len(arr)+1=>5  so (1,6):=>[1,2,3,4,5] 1^2=3 3^3=0 0 ^4=4 4^5=1 so xor_total=1    [total sum]
    for i in range(1,n+1):
        xor_total ^=i

   # to find xor for the actual arr[1,2,4,5] 1^2=3 3^4=7 7^5=2  so xor_arr=2    [actual sum]
    for j in arr:
        xor_arr ^=j
    
    return xor_total^xor_arr   #total sum-actual sum

arr=[1,2,3,5]

print(missing_number(arr))

