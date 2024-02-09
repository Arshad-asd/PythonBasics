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
    def dfs(self,root):
        result = []
        def dfs_recursive(node,level):
            if node is not None:
                if len(result) <= level:
                    result.append([])
                result[level].append(node.key)
                dfs_recursive(node.left,level+1)
                dfs_recursive(node.right,level+1)
        dfs_recursive(root,0)
        print(result)
    def search(self,root,key):
        if root is None or root.key == key:
            return root
        if root.key > key:
            return self.search(root.left,key)
        return self.search(root.right,key)
    
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
bst.dfs(bst.root)
search_result = bst.search(bst.root, 3)
if search_result:
    print(f"Key  found in the BST.")
else:
    print(f"Key  not found in the BST.")

print(bst.is_valid_BST(bst.root))