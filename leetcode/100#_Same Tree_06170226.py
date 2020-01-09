
# coding: utf-8

# In[3]:


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not (p or q):
            return True
        elif (hasattr(p, 'val') and hasattr(q, 'val')) and p.val == q.val:
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False
        else:
            return False

