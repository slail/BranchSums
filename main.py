# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    '''
    Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
    A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.
    Each BinaryTree node has an integer value , a left child node, and a right child node. Children nodes can either be Binary Tree nodes themselves or None / null
    '''
    sums = []
    currentBranchSum(root, 0, sums)
    return sums


def currentBranchSum(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    currentBranchSum(node.left, newRunningSum, sums)
    currentBranchSum(node.right, newRunningSum, sums)
