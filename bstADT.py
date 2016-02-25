"""
Binary search tree implementation
Copyright (C) 2015 Vasantha Ganesh K <vasanthaganesh.k@tuta.io>.

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

# Cool inplementation of binary search tree in python3
class Node(object):
	def __init__(self, data = 0):
		self.data = data
		self.parent = None

		self.left =  None
		self.right = None

class bst(object):
	def __init__(self):
		self.head = None

	def insert(self, data):
		temp = Node(data)
		if self.head == None:
			self.head = temp
		else:
			cur = self.head
			while True:
				if cur.data > data:
					if cur.left == None:
						temp.parent = cur
						cur.left = temp
						break
					cur = cur.left
				else:
					if cur.right == None:
						temp.parent = cur
						cur.right = temp
						break
					cur = cur.right
	
	def inorder(self, temp):
		if temp != None:
			self.inorder(temp.left)
			print(temp.data)
			self.inorder(temp.right)
	def inorder2(self):
		# inorder traversal with stacks
		s = []
		cur = self.head
		while not (cur == None and s == []):
			if cur == None:
				temp = s.pop()
				print(temp.data)
				cur = temp.right
			else:
				s.append(cur)
				cur = cur.left

#inorder traversal without recusion and without stack
	def inorder3(self):
		cur = self.head
		while cur != None:
			if cur.left == None:
				print(cur.data)
				cur = cur.right
			else:
				lstree = cur.left # left subtree
				while lstree.right != None and lstree.right != cur:
					lstree = lstree.right
				if lstree.right == None:
					lstree.right = cur
					cur = cur.left
				else:
					lstree.right = None
					print(cur.data)
					cur = cur.right

	def __find(self, data):
		"""Returns the Node object that is found"""
		cur = self.head
		while cur != None:
			if cur.data == data:
				break
			cur = (cur.left if data < cur.data else cur.right)
		return cur
	def find(self, data):
		"""returns true if data is in bst else returns False (try to replace with in operator)"""
		if self.__find(data) == None:
			return False
		else:
			return True
	
	def remove(self, data):
		"""using smallest element in right subtree the element is removed if found"""
		# this method doesn't work
		cur = self.__find(data)
		dup = cur
		if self.find(data):
			while True:
				if dup.left == None:
					cur.data = dup.data
					cur.parent = None
					break
				else:
					dup = dup.left
		else:
			print("Element to be removed is not found!")
# driver program
a = bst()
temp = map(int, input().split(' '))
for i in temp:
	a.insert(i)
a.inorder(a.head)
a.remove(0)
print("Inorder after deletion")
a.inorder(a.head)
print("Inorder2's call")
a.inorder2()

#inorder without stack and without recursion
print("Inorder3's call:")
a.inorder3()