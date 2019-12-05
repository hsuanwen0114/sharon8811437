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
 

## 學習歷程 
因為發生碰撞時需要用link list把資料串連再一起  
所以先放上我的link list 

```
class Nodes:
   def __init__(self,data=None):
        self.prev = None
        self.data = data
        self.next = None

class linkedList:
   def __init__(self):
        self.head = Nodes()

   def insertBack(self,data):
        newNode = Nodes(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
        newNode.prev = cur

   def insertFront(self,data):   
        newNode = Nodes(data)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode 
        
   def printList(self):
        cur = self.head
        arr = []
        while cur: 
            if cur.data != None:
                arr.append(cur.data)
            cur = cur.next
        print(arr)

   def remove(self,gone):
        cur = self.head
        print("-------",gone,"will be gone -----")
        while cur:
            if cur.data == gone:
                cur.prev.next = cur.next    
            cur = cur.next

   def reverseOrder(self):
        print("  <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cur = self.head
        lastOne = None
        nextOne = None
        cur = cur.next
        while cur:
            nextOne = cur.next
            cur.next = lastOne
            lastOne = cur
            cur = nextOne
        self.head = lastOne
 ```
        
        
        

### 流程圖 

* add   

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20add.png)   

* remove   
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20remove.png)  

* contains  
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/hashtable/hashtable%20contains.png)  

