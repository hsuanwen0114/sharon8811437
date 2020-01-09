# stack   
Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。  
一般的Stack，會有以下幾個處理資料結構的功能：  

* Push(data)：把資料放進Stack。  
把書放進箱子。  
* Pop：把「最上面」的資料從Stack中移除。  
把位於箱子「最上面」的書拿出來。  
* Top：回傳「最上面」的資料，不影響資料結構本身。  
確認目前位於箱子「最上面」的是哪本書。  
* IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。  
確認箱子裡面有沒有書。  
* getSize：回傳Stack裡的資料個數，不影響資料結構本身。  
記錄目前箱子已經裝了多少本書。 
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-10%20%E4%B8%8A%E5%8D%883.23.26.png)   

# queue  
Queue是具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。  
一般的Queue，會有以下幾個處理資料結構的功能：  

* Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。  
在Queue中新增資料又稱為enqueue。  
* Pop：把front所指向的資料從Queue中移除，並更新front。  
從Queue刪除資料又稱為dequeue。  
* getFront：回傳front所指向的資料。  
* getBack：回傳back所指向的資料。  
* IsEmpty：確認Queue裡是否有資料。  
* getSize：回傳Queue裡的資料個數。  
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-10%20%E4%B8%8A%E5%8D%883.27.20.png)  
