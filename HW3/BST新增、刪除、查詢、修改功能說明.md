## 原理
基本概念是將資料切成兩半，然後比較搜尋目標在這兩半的左邊或右邊，如果在左邊，將左邊的資料再切成兩半，以此類推，最後尋找到目標物為止。  
很重要的基本條件是：`左邊子樹一定要大於右邊子樹`  
左子樹只要不為空的話，左子樹上所有節點的值都小於根節點的值。  
右子樹只要不為空的話，右子樹上所有節點的值都大於根節點的值。  

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/bst%E5%8E%9F%E7%90%86.png)  
參考資料：！[binary search tree原理]（http://marklin-blog.logdown.com/posts/1731603）

## 新增




## 刪除
刪除基本上有三種情況：  
1.沒有子節點時，可以直接移除。  
2.有一個子節點時，將子節點取代被移除的節點的位置。  
3.有兩個子節點時，將樹作中序排列後，可以選擇被移除節點的前驅。 
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/Untitled%20Diagram.png)    
參考資料:![bst原理](https://emn178.pixnet.net/blog/post/94574434)  
## 查詢

