class TreeNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,root,key):
        if root is None:
            return TreeNode(key)
        if root.key == key: 
           return root
        elif root.key > key:
            root.left = self.insert(root.left,key)
        elif root.key < key:
            root.right = self.insert(root.right,key)
        return root
    def delete(self,root, key):
        if root is None:
            return None

        if root.key > key:
            root.left = self.delete(root.left, key)
        elif root.key < key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                succ = self.getSucc(root.right)
                root.key = succ.key
                root.right = self.delete(root.right, succ.key)

        return root

    def getSucc(self,curr):
        while curr.left is not None:
            curr = curr.left
        return curr

    def preorder(self, root):
        if root is not None:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)
    def bfs(self,root):
        result = []
        def bfs_recurse(node,level):
            if node is not None:    
                if len(result) <= level:
                    result.append([])
                result[level].append(node.key)
                bfs_recurse(node.left,level+1)
                bfs_recurse(node.right,level+1)
        bfs_recurse(root,0)
        print(result)
    def traversing(self,root,key):
         if root is None:
              return False
         if root.key == key:
              return True
         if root.key > key:
              return self.traversing(root.left,key)
         return self.traversing(root.right,key)
    
    def is_valid_BST(self,root,min_val = float('-inf'),max_val = float('inf')):
        if root is None:
            return True
        if not min_val < root.key < max_val:
            return False
        return self.is_valid_BST(root.left,min_val,root.key) and self.is_valid_BST(root.right,root.key,max_val)

bst = BST()
bst.root = bst.insert(bst.root,10)
bst.root = bst.insert(bst.root,50)
bst.root = bst.insert(bst.root,20)
bst.root = bst.insert(bst.root,5)
print('preorder')
bst.preorder(bst.root)
print('preorder')
bst.inorder(bst.root)
print('postorder')
bst.postorder(bst.root)
bst.bfs(bst.root)
search_result = bst.search(bst.root, 3)
if search_result:
    print(f"Key  found in the BST.")
else:
    print(f"Key  not found in the BST.")

print(bst.is_valid_BST(bst.root))