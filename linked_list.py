"""
Linked list implementaion as stack.
Copyright (C) 2016 Vasantha Ganesh K <vasanthaganesh.k@tuta.io>.

This file is part of data-structures.

data-structures is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

data-structures is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with data-structures.  If not, see <http://www.gnu.org/licenses/>.
"""


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
