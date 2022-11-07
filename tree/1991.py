# Title : 트리 순회
# Date : 2022/11/07
# https://www.acmicpc.net/problem/1991

import sys

def preorder(root):
  if root != -1:
    print(chr(65+root),end='')
    preorder(tree[0][root])
    preorder(tree[1][root])

def inorder(root):
  if root != -1:
    inorder(tree[0][root])
    print(chr(65+root),end='')
    inorder(tree[1][root])
    
def postorder(root):
  if root != -1:
    postorder(tree[0][root])
    postorder(tree[1][root])
    print(chr(65+root),end='')
    
num = int(sys.stdin.readline())
tree = [[-1 for _ in range(num)] for _ in range(2)]

for i in range(num):
  tmp  = sys.stdin.readline().split()
  j = ord(tmp[0]) - 65
  if tmp[1] != '.':
    tree[0][j] = ord(tmp[1]) - 65
  if tmp[2] != '.':
    tree[1][j] = ord(tmp[2]) - 65

preorder(0)
print()
inorder(0)
print()
postorder(0)


# import sys

# def preorder(root):
#   if root != '.':
#     print(root, end='')
#     preorder(tree[root][0])
#     preorder(tree[root][1])
    
# def inorder(root):
#   if root != '.':
#     inorder(tree[root][0])
#     print(root, end='')
#     inorder(tree[root][1])

# def postorder(root):
#   if root != '.':
#     postorder(tree[root][0])
#     postorder(tree[root][1])
#     print(root, end='')

# num = int(sys.stdin.readline())
# tree = {}

# for i in range(num):
#   root, left, right = sys.stdin.readline().split()
#   tree[root] = [left, right]
  
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')