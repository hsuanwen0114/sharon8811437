# Hash Table
## Hash table原理
是一種輸入字串，然後輸出數字的函數。也就是「將字串對應至數字」  
例如：“Apple” → 雜湊函數 → 3   

作用原理：  
1、雜湊函數始終將一個特定的名稱對應於相同的數字，每次輸入 “Apple”，都會得到相同的數字(例如 3)。  
2、雜湊函數將不同的字串對應至不同的索引值。例： “Apple” 對應至 3；”Milk” 對應至 4。  
3、雜湊函數知道`陣列的大小`，而且只傳回有效的索引值。

hash table有個很重要的點就是碰撞（兩個資料存到同一個table），碰撞問題越多效能越慢，好的雜湊函數會避免碰撞的發生 
當碰撞發生時就要用linklist把資料串連再一起  
## Hash Function（雜湊函式）   
雜湊函式把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來  
基本特性：  
如果兩個雜湊值是不相同的（根據同一函式），那麼這兩個雜湊值的原始輸入也是不相同的（確定性）  
湊函式一定有著有限的值域，比如固定長度的位元串  
* add   
顧名思義就是新增些什麼：）  
好的狀態是當發生碰撞時把同個位置的key值串再一起才不會打架   
不好的狀態就是當同個位置有兩個key值時只取一個，沒有將所有資料放進去   

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20add.png)   

* remove 

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20remove.png)  

* contains  
有點像是binary search tree中的search
去找裡頭本身就有的值（注意：不在裡面就等於沒有這個東西！）  
如果一開始就是None 回傳false  
如果上面的條件不成立就用迴圈來找值有找到傳true 沒找到就傳false（先把node定義好)   

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20contains.png)  
