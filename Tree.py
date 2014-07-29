class Tree:
    def __init__(self, cargo, left = None, right = None, depth = 0):
        self.cargo = cargo
        self.depth = depth
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)
    def total(self, tree):
        if tree == None: return 0
        return tree.total(tree.left) + tree.total(tree.right) + tree.cargo
    def printTree(self, tree):
        if tree != None:
            tree.printTree(tree.right)
            print("\t"*tree.depth+"%s"%tree.cargo)
            tree.printTree(tree.left)
    def convertFromBin(self, tree):
        if tree!= None:
            tree.cargo = int(tree.cargo, 2)
            tree.convertFromBin(tree.left)
            tree.convertFromBin(tree.right)
    def leaves(self, tree, s):
        if(tree.left!=None and tree.right!=None):
            tree.leaves(tree.left, s)
            tree.leaves(tree.right, s)
        else:
            s.add(tree.cargo)
            return s