#method 1
def union_brute_force(arr1,arr2):
    unique_val=[]

        
    for i in arr1:
        if i not  in unique_val:
            unique_val.append(i)

    for i in arr2:
        if i not in unique_val:
            unique_val.append(i)

    return unique_val

arr1=[1,6,7,8]
arr2=[7,9,6,5]
print(union_brute_force(arr1,arr2))


#method 2

def union_of_array(arr1,arr2):

    return list(set(arr1) | set(arr2))

arr1=[1,6,7,8]
arr2=[7,9,6,5]
print(union_of_array(arr1,arr2))


#method 3

def union_of_array(arr1, arr2):
    new_arr1 = set(arr1)  # Convert arr1 to a set
    new_arr2 = set(arr2)  # Convert arr2 to a set
    result = new_arr1 | new_arr2  # Union operation
    return list(result)  # Convert set to list before returning

# Example Usage
arr1 = [1, 2, 3, 5]
arr2 = [2, 3, 5, 4]
print("Union of Arrays:", union_of_array(arr1, arr2))


#method 4 (dsa)



#method 4 (dsa)

def union_of_array(arr1,arr2):
    i,j=0,0
    result=[]

    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i+=1
        elif arr1[i]>arr2[j]:
            result.append(arr2[j])
            j+=1
        else:
            result.append(arr1[j])
            i+=1
            j+=1

    while i<len(arr1):
        result.append(arr1[i])
        i+=1

    while j<len(arr2):
        result.append(arr2[j])
        j+=1
    return result

arr1=[1,3,4]
arr2=[2,8,9,3]
print(union_of_array(arr1,arr2))


