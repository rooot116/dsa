import random
import timeit
import matplotlib.pyplot as plt
import math
comList=[]
com = 1
def quicksort(arr, start , stop):
	if(start < stop):
		pivotindex = pivotfun(arr,start, stop)
		quicksort(arr , start , pivotindex-1)
		quicksort(arr, pivotindex + 1, stop)

def pivotfun(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)

def partition(arr,start,stop):
    global com
    pivot = start 
    i = start + 1
    for j in range(start + 1, stop + 1):
		com +=1        
		if arr[j] <= arr[pivot]:
			com +=1
			arr[i] , arr[j] = arr[j] , arr[i]
            
            i +=1
    arr[pivot] , arr[i-1] = arr[i-1] , arr[pivot]
    pivot = i-1
    return pivot
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
plt.title('Quick Sort Running ime')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()		