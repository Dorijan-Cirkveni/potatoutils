class BinaryTreeNode:
    '''
    Basic node of a basic binary tree.
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        return
    def compare(self, value, getDirection=False):
        X=self.left if value>self.value else self.right
        return (X,value>self.value) if getDirection else X


class BinaryTree:
    """
    Basic binary tree.
    """
    def __init__(self):
        self.root=None
        self.size=0
        return
    #--------------------------------------------------------------------------
    #The following functions do not change the data structure.
    def __sizeof__(self):
        return self.size
    def __contains__(self, item):
        current=
    #--------------------------------------------------------------------------
    #The following functions DO change the data structure.
    def insert(self,value,log:list=None):
        if self.root is None:
            self.root=BinaryTreeNode(value)
            self.size=1
            return
        current=self.root
        last=None
        while current is not None:
            last=current
            if log is not None:
                X=last.compare(value,True)
                last=X[0]
                log.append((last,X[1]))
            else:
                current=last.compare(value)

        return
    def remove(self,value):
        return

