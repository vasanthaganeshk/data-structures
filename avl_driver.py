"""
Avl tree implementation
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


from avlADT import bst
# driver program
a = bst()
temp = map(int, input().split(' '))
for i in temp:
    a.insert(i)
    a.inorder(a.head)
    print()