《資料壓縮期末專題 － 適應性霍夫曼編碼》
===================

這次期末專題原本想做圖片壓縮的，可我怕我其他科炸掉，就先做我認為比較簡單的文字編碼，順便練練Python，  
想說能速速將它解決，結果還是花了不少時間，代表我的Python還得再加強QQ。


《霍夫曼編碼介紹》
-------------
霍夫曼編碼法（Huffman’s Encode）是霍夫曼在1952年所提出的一種無失真壓縮技術，其原理是將欲壓縮之字串，先讀一遍，將字串中的每一相異單字元（Single Character）的出現頻率，做成統計，依此建構霍夫曼樹（Huffman’s Tree）。每一相異單字元，用0與1予以編碼，出現次數逾多者，給予較少的位元編碼，最後將這些位元串組合起來，並加上Huffman’s tree ，就成為壓縮檔案。Huffman編碼法為依資訊源符號出現機率，在對資訊源符號逐一編碼條件下(The symbols be coded one at a time)，最佳之編碼方法。  
  
Huffman編碼法的特點在於所編碼出來的檔案具有唯一碼性質的即時碼。也就是各個相異字元所編碼出所位元串並不相同，解碼時能立即解出。也就是說，Huffman編碼法之解碼過程為即時(Instantaneous) 且為唯一(Uniquely Decodable) 之解碼。


![enter image description here](http://i.imgur.com/mM4JTRK.png)

   
### Adaptive Huffman coding

在霍夫曼編碼中，有個缺點是除了壓縮後的資料外，它還得傳送機率表給解碼端，否則解碼端無法正確地做解碼的工作。如果想要壓縮好一點，必須有更多的統計資料，但同時必須要送出更多的統計資料到解壓縮端。而適應性編碼可以利用已經讀過的資料機動的調整霍夫曼樹。

> 這是它的流程圖，原本上課的時候聽不太懂，多虧這張圖，我才能順利搞懂~~ 。
![enter image description here](http://img.bimg.126.net/photo/XtprWZC6lfknhRdpp8tHMA==/333547847418928747.jpg)

