# mergesort&heapsort比較  
mergesort的原理是先將陣列分開再重新排序並合併  
heapsort是將他們先排序成max tree or min tree再用swap把位置交換  
理論上 heapsort比mergesort跑得還快    
他不用像mergesort一樣次每次method call 都需要去跟記憶體要一塊位置   
