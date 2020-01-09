先附上我的程式碼
```class Nodes:
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
一開始因為ＢＳＴ所以打了linkedlist的程式碼，首先要了解他的意思：  
連結串列(Linked List)是串列(List)的一種，是一種常見的資料結構，利用這個資料結構也能進一步實作出其他的資料結構，例如堆疊(Stack)和佇列(Queue)等。  
它的特性是能夠不使用連續的記憶體空間的情況下，能夠保有並使用一份連續的資料；相對來看，陣列則需要使用連續的記憶體空間。  
流程圖如下（擷取網路上）  
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/binary%20search%20tree/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202020-01-10%20%E4%B8%8A%E5%8D%883.11.37.png)  
Linked-list是由一連串的節點（Node）所構成，每個節點指向下一個節點，而最後一個節點則指向Null（在python裡面是None）  
因此，每個節點本身應該要有兩種屬性（attribute），一個是本身帶有的值或者是資料，另一個則是指向下一個節點的指標（pointer）  
