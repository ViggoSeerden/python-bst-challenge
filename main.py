import random
from collections import OrderedDict


class Node:

    def __init__(self, num):
        self.left = None  # initially nothing in left subtree
        self.right = None  # and nothing in right subtree
        self.num = num


def insert(current_node, new_node):
    if new_node.num < current_node.num:
        if current_node.left is None:
            current_node.left = new_node
        else:
            insert(current_node.left, new_node)
    else:
        if current_node.right is None:
            current_node.right = new_node
        else:
            insert(current_node.right, new_node)


length = random.randint(10, 30)
numbers = []

for x in range(length):
    node = random.randint(1, 100)
    numbers.append(node)

unique_numbers = list(OrderedDict.fromkeys(numbers))

print("Nodes: ", unique_numbers)
root = Node(unique_numbers[0])
print("Root Node: ", root.num)
unique_numbers.pop(0)

for i in range(len(unique_numbers)):
    new_node = Node(unique_numbers[i])
    insert(root, new_node)

print('')


def print_tree(node, level=0, prefix='', suffix='--------------------------------------------------'):
    if node is not None:
        print_tree(node.right, level + 1, 'R ', '')
        print(' ' * 4 * level + prefix + str(node.num) + suffix)
        print_tree(node.left, level + 1, 'L ', '')


print_tree(root)
