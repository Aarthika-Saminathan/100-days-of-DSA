def reverse(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=-1

def left_rotate(arr,d):
    n=len(arr)
    d=d%n


    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)

arr=[1,2,3,4,5]
d=2
left_rotate(arr,d)
print("left rotate array: ",arr)