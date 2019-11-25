## 原理
基本概念是將資料切成兩半，然後比較搜尋目標在這兩半的左邊或右邊，如果在左邊，將左邊的資料再切成兩半，以此類推，最後尋找到目標物為止。  
很重要的基本條件是：`左邊子樹一定要大於右邊子樹`  
左子樹只要不為空的話，左子樹上所有節點的值都小於根節點的值。  
右子樹只要不為空的話，右子樹上所有節點的值都大於根節點的值。  

![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/bst%E5%8E%9F%E7%90%86.png)  
參考資料：  
[binary search tree原理]（http://marklin-blog.logdown.com/posts/1731603）

## 學習歷程  
首先我記得老師上上週時上課說了如果link list不會，這次的作業就不會  
因此我花了3天去寫我的 linl list `老師說不要欠程式債`  
寫的時候沒有遇上什麼大問題  
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
執行成功   
接下來就可以開始用binary search tree！！（好累喔程式債真的不能欠fk）    


## 流程圖

### insert
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/insert%20bst.jpg)  
### search
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/search%20bst.jpg)  
### delete
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/delete%20bst.jpg)  
### modify
這個不需要流程圖，我打這個的時間大概是delete的1/20   


整體參考資料： 老師放在moodle的投影片  

我真的覺得一次比一次還難，上一個作業花了大概五天去完成，這次花了快一個禮拜   
打完後真的有點想哭
