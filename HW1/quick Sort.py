def quick_sort(aaa):
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
quick_sort(aaa)
