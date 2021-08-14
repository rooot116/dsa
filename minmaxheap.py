# max heap function
def maxheap(arr,n,i):
    max = i
    left = 2*i+1
    right = 2*i+2
    if(right<n and arr[right]>arr[max]):
        max = right
    if(left<n and arr[left]>arr[max]):
        max = left
    if(max!=i):
        arr[i],arr[max] = arr[max],arr[i]
        maxheap(arr,n,max)
# min heap function
def minheap(arr,n,j):
    min = j
    left = 2*j+1
    right = 2*j+2
    if(right<n and arr[right]<arr[min]):
        min = right
    if(left<n and arr[left]<arr[min]):
        min = left
    if(min!=j):
        arr[j],arr[min] = arr[min],arr[j]
        minheap(arr,n,min)

num = int(input("enter your choice \n 1.maxheap \n 2.minheap")) #input
alist = list(map(int,input("Enter the elements : ").split())) #input
n=len(alist)
if num==1:
    for p in range(n//2,-1,-1):
        maxheap(alist, n, p)
    print("maxheap")
    print(alist)
else:
    for q in range(n//2,-1,-1):
        minheap(alist, n, q)
    print("minheap")
    print(alist)