"""
Avl tree implementation (balanced binary search tree)
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


# Cool inplementation of binary search tree in python3
class Node(object):
    def __init__(self, data = 0):
        self.data = data
        
        # Height is defined as the longest path from current node to the leaf
        self.height = 0
        self.parent = None

        self.left =  None
        self.right = None

class bst(object):
    def __init__(self):
        self.head = None

    def __update_height(self, cur):
        while cur != None:
            cur.height = 1 + max(height(cur.left), height(cur.right))
            cur = cur.parent

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
        self.__update_height(temp)
        self.balance(temp)

    def right_rotate(self, x):
        y = x.left
        y.parent = x.parent
        if x.parent == None:
            self.head = y
        else:
            if y.parent.data < y.data:
                y.parent.right = y
            else:
                y.parent.left = y

        temp = y.right
        if temp != None:
            temp.parent = x
        x.left = temp
        x.parent = y
        y.right = x
        
    def left_rotate(self, x):
        y = x.right
        y.parent = x.parent
        if x.parent == None:
            self.head = y
        else:
            if y.parent.data > y.data:
                y.parent.left = y
            else:
                y.parent.right = y

        temp = y.left
        if temp != None:
            temp.parent = x
        x.right = temp
        x.parent = y
        y.left = x

    def balance(self, temp):
        while temp != None:
            if abs(height(temp.right) - height(temp.left)) >= 2:
                if height(temp.right) > height(temp.left):
                    if height(temp.right.right) >= height(temp.right.left):
                        self.left_rotate(temp)
                    else:
                        self.right_rotate(temp.right)
                        self.__update_height(temp.right.right)
                        
                        self.left_rotate(temp)
                else:
                    if height(temp.left.left) >= height(temp.left.right):
                        self.right_rotate(temp)
                    else:
                        self.left_rotate(temp.left)
                        self.__update_height(temp.left.left)
                        
                        self.right_rotate(temp)
                self.__update_height(temp)
            temp = temp.parent

    def inorder(self, temp):
        if temp != None:
            self.inorder(temp.left)
            print((temp.data, temp.height), end = ' ')
            self.inorder(temp.right)

def height(node):
    if node == None:
        return -1
    else:
        return node.height