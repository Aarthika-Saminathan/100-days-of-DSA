# method 1

def sorted_arr(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    
arr=[1,2,3,4]
print(sorted_arr(arr))

#t(c)=>o(n)  s(c)=<0[1]


#method 2

def sorted_arr(arr):
    result=sorted(arr)

    if arr==result:
        return True
    return False

arr=[1,2,3,2]
print(sorted_arr(arr))

#t(c)=<o(nlogn)



#method 3


def sorted_arr(arr,index=0):

    if index==len(arr)-1:   
       return True
    if arr[index]>arr[index+1]:
        return False
    
    return sorted_arr(arr,index+1)
arr=[1,2,3,4]
print(sorted_arr(arr))





