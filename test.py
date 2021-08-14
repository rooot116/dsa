import random
import timeit
import matplotlib.pyplot as plt
import math
comList=[]
com = 0
def quicksort(arr, start , stop):
	if(start < stop):
		pivotindex = pivotfun(arr,start,stop)
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)
def pivotfun(arr,start,stop):
    randpivot = random.randrange(start,stop)
    pivot = arr[randpivot]
    arr[start] , arr[randpivot] = arr[randpivot] , arr[start]
    return partition(arr,start,stop)

def partition(arr,start,stop):
    randpivot = start
    pivot = arr[randpivot]
    while start<stop:
        global com
        while start < len(arr) and arr[start] <= pivot:
            com += 1
            start += 1
        while arr[stop] > pivot:
            com +=1
            stop -= 1
        if start < stop:
            arr[start] , arr[stop] = arr[stop] , arr[start]
            com +=1
    arr[randpivot] , arr[stop] = arr[stop] , arr[randpivot]
    return stop
start = timeit.default_timer()
for r in range(200):
	com = 1
	A=[]
	for i in range(0,r):
		n = random.randint(1,100)
		A.append(n)
	quicksort(A,0,len(A)-1)
	comList.append(com)
	
end = timeit.default_timer()
total = end-start

print(f"the total time taken is {total}")
n = [*range(1, 201, 1)]
nn=[]
nm=[]
for x in n:
		nn.append(x*math.log(x,2))
for y in n:
    nm.append(y*y)

plt.plot(comList,n,color='green', linewidth=3,label='Quicksort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.plot(nm,n,color='blue', linewidth=3,label='n^2')
plt.title('Quick Sort running time graph')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()	