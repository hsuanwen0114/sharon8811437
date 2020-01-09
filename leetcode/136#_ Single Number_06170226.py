
# coding: utf-8

# In[3]:


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for each in nums:
            temp ^= each
        return temp

