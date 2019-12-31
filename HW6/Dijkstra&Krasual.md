# Dijkstra
最短路徑的演算法，主要在講說指定一個點到於各個頂點的最短路徑，又稱「單源最短路徑」。

步驟：  
1. 至起始點找尋尚未拜訪的相鄰結點  
2. 更新最短路徑表  
3. 找尋目前未拜訪的最短路徑結點，將此結點設為起始點，並設為已拜訪   
4. 重複第一步，直到所有結點皆為已拜訪 

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/dijkstra/dijkstra.png)  


 # Kruskal
 Kruskal演算法是一種用來尋找最小生成樹的演算法
 步驟：
1. 將所有的邊，依照權重的大小排序  
2. 再來依序加入權重最小的邊  
3. 如果 造成cycle時，則必須捨棄  
4. 直到增加了n - 1條邊為止。(假設有 n 個節點)  

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/dijkstra/kruskal.png)  

參考資料：  
![dijkstral](https://ithelp.ithome.com.tw/articles/10209593)  
![dijkstral流程圖參考](http://www.csie.ntnu.edu.tw/~u91029/Path.html)  
![kruskal流程圖參考](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html)  
