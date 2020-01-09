## 原理
基本概念是將資料切成兩半，然後比較搜尋目標在這兩半的左邊或右邊，如果在左邊，將左邊的資料再切成兩半，以此類推，最後尋找到目標物為止。  
很重要的基本條件是：`左邊子樹一定要大於右邊子樹`  
左子樹只要不為空的話，左子樹上所有節點的值都小於根節點的值。  
右子樹只要不為空的話，右子樹上所有節點的值都大於根節點的值。  

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/bst%E5%8E%9F%E7%90%86.png)  

## 新增
當要插入一個新節點時：  
若新節點比根節點小，往左子樹走  
若新節點比根節點大，往右子樹走  
在插入節點時, 只會有一個地方可以插入. 找到個位置的時間複雜度是 O(h), h 是樹的高度  
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/insert%20bst.png)  
參考資料：
[bst insert](https://github.com/shenyun2304/swift-algorithm-club-zhTW/tree/master/Binary%20Search%20Tree)

## 刪除
刪除基本上有三種情況：  
1.沒有子節點時，可以直接移除。  
2.有一個子節點時，將子節點取代被移除的節點的位置。  
3.有兩個子節點時，將樹作中序排列後，可以選擇被移除節點的前驅。 
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/Untitled%20Diagram.png)    
參考資料:
[bst delete](https://emn178.pixnet.net/blog/post/94574434)   

## 修改
修改有一個前提，`要修改的目標必須小於根節點右大於左子樹`  
其他的情況，直接delete數字，再insert新的值  
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/bst%20modify.png)    
參考資料：  
[bst modify](https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/)  

## 查詢
在樹中找一個值的基本概念和新增一樣  
1.要查的值小於目前的節點，往左子樹  
2.要查的值大於目前的節點，往右子樹    
這個動作會一直遞迴到我們找到目標值（或走訪完所有節點仍找不到）    
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/bst%E6%90%9C%E5%B0%8B%20(1).png)   
多虧了這種結構, 搜尋非常的快速. 只使用了 O(h) 時間. 如果有個擁有百萬節點的樹, 而節點左右平衡的很好, 那大概只需要花 20 次走訪便能找到值. ( 這個概念非常像陣列中的 [二元搜尋](../Binary Search). )  
