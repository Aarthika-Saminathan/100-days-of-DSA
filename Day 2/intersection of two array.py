#method 1

def intersection_of_array(arr1,arr2):
    result=[]

    for i in arr1:
        for j in arr2:
            if i==j:
                result.append(i)

    return result

arr1=[1,2,3,4]
arr2=[2,3,6,8]

print("Intersection of two array: ",intersection_of_array(arr1,arr2))

#method 2

def intersection_of_array(arr1,arr2):
    i,j=0,0
    result=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j-=1
        else:
            result.append(arr1[i])
            i+=1
            j+=1


    return result

arr1=[1,2,3,4]
arr2=[3,4,5,6]
print(intersection_of_array(arr1,arr2))


#method 3

def intersection_of_array(arr1,arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6]

print(intersection_of_array(arr1,arr2))