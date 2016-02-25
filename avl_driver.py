from avlADT import bst
# driver program
a = bst()
temp = map(int, input().split(' '))
for i in temp:
    a.insert(i)
    a.inorder(a.head)
    print()