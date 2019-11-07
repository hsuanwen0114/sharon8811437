# mergesort&heapsort比較  

* merge sort:   
合併排序法，會需要使用到空間，但相對的它在時間複雜度的表現，比其它幾個演算法優質些。
使用Divide and Conquer的演算法來實作。



![image](https://github.com/hsuanwen0114/sharon8811437/blob/master/heapsort/mergesort%26heapsort%E6%AF%94%E8%BC%83%E5%9C%96.png)

mergesort的原理是先將陣列分開再重新排序並合併  
heapsort是將他們先排序成max tree or min tree再用swap把位置交換  
理論上 heapsort比mergesort跑得還快    
他不用像mergesort一樣次每次method call 都需要去跟記憶體要一塊位置   
[mergesort流程圖、意義參考資料](http://marklin-blog.logdown.com/posts/1910136) 
[heapsort流程圖、意義參考資料](http://marklin-blog.logdown.com/posts/1910116)
