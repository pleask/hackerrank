""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
def checkBST(root):
    return checkBSTRec(root, float("-inf"), float("inf"))

def checkBSTRec(root, minVal, maxVal):
    if root is None:
        return True

    return minVal < root.data < maxVal and checkBSTRec(root.left, minVal, root.data) and checkBSTRec(root.right, root.data, maxVal)


      
