import random
import timeit
import matplotlib.pyplot as plt
import math

def MergeSort(array):
	if len(array)>1:
		mid=int(len(array)/2)
		Left=array[:mid] 
		Right=array[mid:]
		MergeSort(Left)
		MergeSort(Right)
		merge(array,Left,Right)
def merge(array,Left,Right):
	i = j = k = 0	
	while i < len(Left) and j < len(Right):
		global com
		if Left[i] < Right[j]:
			com=com+1
			array[k] = Left[i]
			i += 1
		else:
			com=com+1
			array[k] = Right[j]
			j += 1
		k += 1
		
	while i < len(Left):
		array[k] = Left[i]
		i += 1
		k += 1
	while j < len(Right):
		array[k] = Right[j]
		j += 1
		k += 1	
timeList=[]
comList=[]

start = timeit.default_timer()
for p in range(200):
	com=1 
	array = []
	for i in range(0,p):
		n = random.randint(1,100)
		array.append(n)
	MergeSort(array);
	comList.append(com)
end = timeit.default_timer()	
n = [*range(1, 201, 1)]
nn=[]
for x in n:
		nn.append(x*math.log(x,2))
total=end-start
print(f"the total time taken is {total}")
plt.plot(comList,n,color='green', linewidth=3,label='Mergesort time')
plt.plot(nn,n,color='red', linewidth=3,label='nlogn')
plt.title('Merge Sort Running ime')
plt.xlabel('value of time')
plt.ylabel('value of n')
plt.legend()
plt.show()	

