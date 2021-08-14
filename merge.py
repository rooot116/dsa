class Node:
	def __init__(self, data,next=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
	def printList(self):
		temp = self.head
		while temp :
			print(temp.data, end=" ")
			temp = temp.next
	def append(self, new_data):
		new_node = Node(new_data)
		
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		
		while last.next:
			last = last.next
		last.next = new_node

def mergeLists(head1, head2):
	temp = None
	if head1 is None:
		return head2
	if head2 is None:
		return head1
	if head1.data >= head2.data:
		temp = head2
		temp.next = mergeLists(head1, head2.next)
	else:
		temp = head1
		temp.next = mergeLists(head1.next, head2)
	return temp
if __name__ == '__main__':
	list1 = LinkedList()
	list2 = LinkedList()
	m= input("enter list1 size")
	n= input("enter list2 size")
	print("enter list1 elements")
	for i in range(m):
    		x=int(input())
    		list1.append(x)
	print("enter list2 elements")
	for i in range(n):
    		x=int(input())
    		list2.append(x)
	list3 = LinkedList()
	list3.head = mergeLists(list1.head, list2.head)
	print("Merged List is : ", end="")
	list3.printList()	
'''
Time Complexity:  Since we are traversing through the two lists fully. So, the time complexity is O(m+n) where m and n are the lengths of the two lists to be merged. 


'''