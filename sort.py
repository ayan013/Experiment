arr=[2,9,5,1,56,10]
for i in range(len(arr)):
    for j in range(i):
        if arr[j] > arr[i]:
            s=arr[i]
            arr[i]=arr[j]
            arr[j]=s
print(arr)
length=len(arr)
for i in range(len(arr)):
    if i <= length-2:
     print(i)

