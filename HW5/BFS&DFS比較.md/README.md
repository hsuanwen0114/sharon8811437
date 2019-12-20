# DFS（深度優先搜尋法）

是一種用來遍尋一個樹或圖的演算法。
步驟：  
1.從起點開始，選一邊與起點相鄰的點行走，行走過的點會被標記起來  
2.將下一個點視為起點，繼續選擇與該點相鄰的點行走  
3.直到發現所有的點都已被標記過   

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/BFS%26DFS/dfs.png)  

# BFS(廣度優先搜尋法)  

1.以某一節點開始走訪，接著開始走訪與此節點相臨且並未拜訪的點  
2.由走訪過的節點繼續進行先廣後深的搜尋  
以樹來說即把同一深度的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點

廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現  

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/BFS%26DFS/%EF%BC%A2%EF%BC%A6%EF%BC%B3.png)  

