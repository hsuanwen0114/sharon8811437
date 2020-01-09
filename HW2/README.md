## heap sort教學
首先要先了解heap tree  
heap tree是一個二元樹（二元樹意思：每個節點最多就兩個子節點、子節點有左右之分） 

其中heap tree分為max tree和min tree  
做法如圖（示範max tree)1  
![image](https://github.com/hsuanwen0114/sharon8811437/blob/master/heapsort/heapsort%E6%B5%81%E7%A8%8B%E5%9C%96.png)

再者要把max heap heap sort 如圖（由左到右，上到下）
![image](https://github.com/hsuanwen0114/sharon8811437/blob/master/heapsort/heapsort%E6%B5%81%E7%A8%8B%E5%9C%962.png)


就完成了耶～
* 如果需要由大排到小，要將第一張圖的max heap改為min heap
## merge sort（合併程序法）教學
1.先將問題拆成子問題，將子問題逐一解決  
2.將子問題的結果合併
* 基本步驟分為拆解與合併


![image](https://github.com/hsuanwen0114/sharon8811437/blob/master/merge%20sort/merge%20sort.png)
# mergesort&heapsort比較  

* merge sort:   
合併排序法，會需要使用到空間，但相對的它在時間複雜度的表現，比其它幾個演算法優質些。  
使用Divide and Conquer的演算法來實作。  
1.將數列分成（divide）兩個子數列，每一個數列擁有n/2個數字。 
2.除非此子數列夠小（只剩一個數字，因為一個就是排好了），否則再繼續重覆（1）。 
3.merge每一個子數列使之成為單一數列。  


* heap sort: 
Heap在觀念上是一棵complete binary tree,每個node內的資料比它左右兩側child nodes內的資料都小,一個heap內如果有一個元素x的資料值改變，因而違反了 heap property，我們可以用upheap和downheap來修復這個heap tree 
1.將陣列轉換成Heap Tree。  
2.在將Heap Tree轉換成Max Heap。  
3.將最上面的節點root與最後面的節點交換位置。  
4.再將Tree轉換成Max Heap。  
(然後一直re re re re這流程，直到完全排序完成)  


![image](https://github.com/hsuanwen0114/sharon8811437/blob/master/heapsort/mergesort%26heapsort%E6%AF%94%E8%BC%83%E5%9C%96.png)

mergesort的原理是先將陣列分開再重新排序並合併  
heapsort是將他們先排序成max tree or min tree再用swap把位置交換  
理論上 heapsort比mergesort跑得還快    
他不用像mergesort一樣次每次method call 都需要去跟記憶體要一塊位置   
