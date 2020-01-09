
# coding: utf-8

# In[3]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if root == None:
            return 0
            
        left_depth = Solution().maxDepth(root.left)
        right_depth = Solution().maxDepth(root.right)
        
        
        return left_depth+1 if left_depth>=right_depth else right_depth+1

