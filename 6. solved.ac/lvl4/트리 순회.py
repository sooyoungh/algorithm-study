import sys
input = sys.stdin.readline

n = int(input())
tree = dict()
for _ in range(n):
    par, left, right = input().split()
    tree[par] = [left, right]

result_preorder = []
result_inorder = []
result_postorder = []


def preorder(par):  # 부모, 왼쪽, 오른쪽
    if par != '.':
        result_preorder.append(par)
        preorder(tree[par][0])
        preorder(tree[par][1])


def inorder(par):  # 왼쪽, 부모, 오른쪽
    if par != '.':
        inorder(tree[par][0])
        result_inorder.append(par)
        inorder(tree[par][1])


def postorder(par):  # 왼쪽, 오른쪽, 부모
    if par != '.':
        postorder(tree[par][0])
        postorder(tree[par][1])
        result_postorder.append(par)


preorder('A')
inorder('A')
postorder('A')

print("".join(map(str, result_preorder)))
print("".join(map(str, result_inorder)))
print("".join(map(str, result_postorder)))
