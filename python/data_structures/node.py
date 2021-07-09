class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = []