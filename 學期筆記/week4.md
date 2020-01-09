# Quick sort  
快速排序法是排序演算法的一種，使用Divide and Conquer的演算法來實作。其概念是從數列中挑選一個基準點，大於基準的放一邊，小於的放一邊，如此循環最後可完成排序。
![](https://github.com/hsuanwen0114/sharon8811437/blob/master/quick%20sort/quicksort%E6%B5%81%E7%A8%8B%E5%9C%96.png) 
程式碼如下
```def quick_sort(aaa):
    smaller=[]#比基準值小
    bigger=[]#比基準值大
    keypoint=[]#key值
    
    if len(aaa)<=1:
        return aaa
    else:
        key=aaa[0]#以第一個位置當基準點
        for h in aaa:
            if h<key:
                smaller.append(h)
            elif h>key:
                bigger.append(h)
            else:
                keypoint.append(h)
    smaller=quick_sort(smaller)
    bigger=quick_sort(bigger)
    
    return smaller+keypoint+bigger
    #排序完的aaa要返回

aaa=[22,13,5,7,78,99,3]
```quick_sort(aaa)
