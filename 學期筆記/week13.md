# DFS（深度優先搜尋法）
是一種用於遍歷或搜尋樹或圖的演算法。沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。  

步驟：  
1.從起點開始，選一邊與起點相鄰的點行走，行走過的點會被標記起來  
2.將下一個點視為起點，繼續選擇與該點相鄰的點行走  
3.直到發現所有的點都已被標記過  

### 流程圖
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/BFS%26DFS/dfs.png)  
