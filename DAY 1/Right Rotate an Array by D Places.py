def reverse(arr,i,j):
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1

def right_rotate(arr,d):
    n=len(arr)
    d=d%n

    reverse(arr,n-d,n-1)

    reverse(arr,0,n-d-1)

    reverse(arr,0,n-1)

arr=[1,2,3,4,5]
d=2
right_rotate(arr,d)
print("Array after right rotate", arr)