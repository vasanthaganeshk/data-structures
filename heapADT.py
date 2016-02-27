"""
max heap implementaion
Copyright (C) 2016 Vasantha Ganesh K <vasanthaganesh.k@tuta.io>.

This file is part of data-structures.

data-structures is free software. you can redistribute it and/or modify
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


class max_heap(object):
    def __init__(self, l1 = None):
        self.node = [] if l1 == None else l1
        self.size = len(l1)
    def max(self):
        return self.node(0)
    def heapify(self, i):
        if i < self.size//2:
            cur, left, right = self.node[i], self.node[2*i], self.node[2*i + 1]
            if right >= left and cur < right:
                    self.node[i], self.node[2*i + 1] = self.node[2*i + 1], self.node[i]
                    self.heapify(2*i + 1)
            elif cur < left:
                    self.node[i], self.node[2*i] = self.node[2*i], self.node[i]
                    self.heapify(2*i)
    def build(self):
        for i in range(self.size//2, -1, -1):
            self.heapify(i)
    def pop(self):
        self.node[0], self.node[self.size - 1] = self.node[self.size - 1], self.node[0]
        self.size -= 1
        self.heapify(0)
        return self.node[self.size]

#driver program
a = list(map(int, input().split(' ')))
a = max_heap(a)
a.build()
for i in range(a.size):
    print(a.pop())
