
# coding: utf-8

# In[36]:


class Soluton(object):
    def __init__(self):
        self._heapArray = []

    def __len__(self):
        return len(self._heapArray)

    def is_empty(self):
        return 0 is len(self)

    def _left(self, i):
        return 2*i + 1#取得left child

    def _right(self, i):
        return 2*i + 2#取得right child

    def _parent(self, i):
        return (i - 1) // 2 #將array調整成Max Heap, 因為只有判斷父節點, 所以做陣列長度一半就好

    def _has_left(self, i):
        return self._left(i) < len(self)

    def _has_right(self, i):
        return self._right(i) < len(self)

    def _swap(self, i , j):
        self._heapArray[i], self._heapArray[j] = self._heapArray[j], self._heapArray[i]
    
    def _trickle_up(self, i):
        #Base
        if i <= 0:
            return
        parent_idx = self._parent(i)
        if self._heapArray[parent_idx] < self._heapArray[i]:
            self._swap(parent_idx, i)
            self._trickle_up(parent_idx)

    def add(self, value, key):
        item = Item(value, key)
        self._heapArray.append(item)
        self._trickle_up(len(self) - 1)

    def _trickle_down(self, i):
        if self._has_left(i):
            left_idx = self._left(i) #big child idx
            bigchild = left_idx
            if self._has_right(i):
                right_idx = self._right(i)
                if self._heapArray[left_idx] < self._heapArray[right_idx]:
                    bigchild = right_idx
            if self._heapArray[bigchild] > self._heapArray[i]:
                self._swap(i, bigchild)
                self._trickle_down(bigchild)

    def max(self):
        return self._heapArray[0]._val, self._heapArray[0]._key

    def delete(self):
        self._swap(0, len(self) - 1)
        retval = self._heapArray.pop()
        self._trickle_down(0)
        return (retval._val, retval._key)
        

def heap_sort(self,nums):

    for a in self:
        hp.add(a, a)
    del self[:] #del的用法比較特別，del刪除的是變量，而不是數據。
    while not hp.is_empty():
        self.insert(0,hp.max()[0])  # reverse max-heap 
        hp.delete()

    
if __name__ == "__main__":
    a = [10,5,7,2,3,8]
    print(a)
    heapsort(a)
    print (a)
output=Solution().heap_sort([10,5,7,2,3,8])
output

