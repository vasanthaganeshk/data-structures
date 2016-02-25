# Cool inplementation of linked list
class Node(object):
	def __init__(self, data = 0):
		self.data = data
		self.next = None

class lnk_list(object):
	def __init__(self):
		self.head = None
		self.size = 0
	def __len__(self):
		return self.size
	def append(self, data):
		temp = Node(data)
		temp.next = self.head
		self.head = temp
		self.size += 1	

# driver program

# Recieving input
a = lnk_list()
inp = map(int, input().split(' '))
#inp = [1, 2, 3]
for i in inp:
	a.append(i)

# Displaying output
cur = a.head
for i in range(len(a)):
	print(cur.data)
	cur = cur.next
