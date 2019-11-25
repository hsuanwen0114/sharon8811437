class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    
    def insert(self, root, val):
        if root == None:
            root = TreeNode(val)
            return root
        else:
            if val > root.val:
                if root.right == None:
                    newnode = TreeNode(val)
                    root.right = newnode
                    
                else:
                    self.insert(root.right, val)
            if val <= root.val:
                if root.left == None:
                    newnode = TreeNode(val)
                    root.left = newnode
                    
                else:
                    self.insert(root.left, val)
                    
            return root
                
    def search(self, root, target):
        if target< root.val:
            if root.left!=None:
                return self.search(root.left, target)    
            else:
                return None 
        elif target> root.val:  
            if root.right!=None:
                return self.search(root.right, target)
            else:
                return None
        elif target==root.val:
                return root#當節點等於目標時，回傳正確
               
                
                
    def children_count(self, node):
        a = 0
        if node.left:
            a += 1
        if node.right:
            a += 1
        return a
    
    def delete(self, root, target):#delete有三種可能
        x = self.children_count(root)
        if root==None:
            return root
        else:
            if target<root.val:                         
                root.left=self.delete(root.left,target)
                
            elif target>root.val:                       
                root.right=self.delete(root.right,target)
                
            else: 
                if x == 0:
                    root  = None
                elif x == 1:
                    if root.left != None:
                        root = root.left
                        root.left = None

                    if root.right != None:
                        root = root.right
                        root.right = None
                else:
                    root = root.left
                    root.left = None
                
            return root
        
    def modify(self, root, target, new_val):
        if target is not new_val: 
            Solution().insert(root,new_val)
            return Solution().delete(root,target)
        else:
            
            return root    
