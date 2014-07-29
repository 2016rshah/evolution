from Tree import *
import random

def evolve(tree, rate):
    string = tree.cargo
    mutation = random.randint(0, rate)
    if(mutation==0):
        chars = []
        for s in string:
            chars.append(s)
        i = random.randint(0, len(chars)-1)
        chars[i] = "1"
        string = ''.join(chars)
    tree.left = Tree(tree.cargo, depth = tree.depth+1)
    tree.right = Tree(string, depth = tree.depth+1)
    return tree
def evolveLeaves(tree, rate):
    if(tree.left!=None and tree.right!=None):
        evolveLeaves(tree.left, rate)
        evolveLeaves(tree.right, rate)
    else:
        tree = evolve(tree, rate)
        return tree


root = Tree("00000000")
r = int(input("What do you want the mutation rate to be (i.e mutates 1 in ____ times)?"))
root = evolve(root, r)
for generation in range(0, 10):
    evolveLeaves(root, r)
root.convertFromBin(root)
s = set()
root.leaves(root, s)
root.printTree(root)
print(s)

