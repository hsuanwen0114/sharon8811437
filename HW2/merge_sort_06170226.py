
# coding: utf-8

# In[59]:


#一開始先定義我的merge
def merge(left, right):#先將陣列分割成左邊跟右邊
    array = []

    while any(left) and any(right):
        if left[0] < right[0]:#如果左邊第0個位置的數字小於右邊地0個數字時，append左邊的值
            array.append(left.pop(0))
            #pop函式用於移除列表中的一個元素，並且返回該元素的值。我在這邊設第0個位置
        else:
            array.append(right.pop(0))#反之，append右邊的值
                     

    if not left and any(right): #如果沒有左邊的元素而有右邊的，就append右邊的
        array.append(right.pop(0)) 

    if not right and any(left):#如果沒有右邊的元素而有右邊的，就append左邊的
        array.append(left.pop(0))

    return array

left = [1,2,3,10]
right = [7,12,14]
merge(left, right)
#在這邊的結果只能跑到比left大的第一個數字，沒辦法跑完left&right兩個陣列，覺得是上面兩個if有錯所以稍微做修改


# In[60]:


def merge(left, right):
    array = []

    while any(left) and any(right):
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
                     

    while any(left) or any(right):#多加了一行，表示左邊與右邊其中一方不存在時，他才會往下跑，下面的兩個條件在這個while裡
        if not left and any(right):
            array.append(right.pop(0))

        if not right and any(left):
            array.append(left.pop(0))

    return array

#假設我的left與right分別為以下兩個陣列
left = [1,2,3,10]
right = [7,12,14]
merge(left, right)        


# In[52]:


#接下來要將上面的merge sort（排序）
mylist = [5, 7, 9, 2, 15, 1, 46, 22]
def mergeSort(mylist):
    size = len(mylist)#返回對象的長度

    if size <= 1 :
        return mylist
    else: 
        middle = size // 2 #將他的長度分為二
        return merge(mergeSort(mylist[:middle]), mergeSort(mylist[middle:]))#在middle前面或後面的差別
    

print(mergeSort(mylist))


# In[53]:


#後來詢問助教，助教說演算法不適合用any，any的定義中已經有一個迭代了，時間複雜度會增加，所以試著刪去，發現有沒有any都無所謂所以刪除
def merge(left, right):
    array = []

    while left and right:
        if left[0] < right[0]:
            array.append(left.pop(0))
        else:
            array.append(right.pop(0))
                     

    while left or right:
        if not left and right:
            array.append(right.pop(0))

        if not right and any(left):
            array.append(left.pop(0))

    return array

mylist = [5, 7, 9, 2, 15, 1, 46, 22]

def mergeSort(mylist):
    size = len(mylist)

    if size <= 1 :
        return mylist
    else: 
        mid = size // 2
        return merge(mergeSort(mylist[:mid]), mergeSort(mylist[mid:]))


print(mergeSort(mylist))


# In[61]:


#最後套入助教所要的格式就好了
class Solution(object):
    
    def merge_sort(self,nums):
        size = len(nums)

        if size <= 1 :
            return nums
        else: 
            mid = size // 2
            return self.merge(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))

    
    
    def merge(self,left, right):
        array = []

        while left and right:
            if left[0] < right[0]:
                array.append(left.pop(0))
            else:
                array.append(right.pop(0))

        while left or right:

            if not left and right:
                array.append(right.pop(0))

            if not right and left:
                array.append(left.pop(0))

        return array
output=Solution().merge_sort([5, 7, 9, 2, 15, 1, 46, 22])
output

