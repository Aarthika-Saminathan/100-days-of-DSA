#By using two pointer technique

def move_zeros(arr):
    n=len(arr)
    j=0

    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]  #swap helps to move the zeros to end
            j+=1

arr=[0,1,0,3,12]
move_zeros(arr)
print("Array after moving zeros: ",arr)