# BFS(廣度優先搜尋法)  
是一種圖形搜尋演算法。簡單的說，BFS是從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。廣度優先搜尋的實現一般採用open-closed表。 

步驟：  
1.以某一節點開始走訪，接著開始走訪與此節點相臨且並未拜訪的點  
2.由走訪過的節點繼續進行先廣後深的搜尋  
以樹來說即把同一深度的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點

廣度優先搜尋法屬於盲目搜索(uninformed search)是利用佇列(Queue)來處理，通常以迴圈的方式呈現  

### 流程圖
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/BFS%26DFS/%EF%BC%A2%EF%BC%A6%EF%BC%B3.png) 
