the best feature(term) weight measure in the sample vector construction according
to the papers.

# Introduction #

特征权重(feature/term weight)是指特征向量值的计算方式，论文中常用的计算方式有`tf*idf,binary,tf,tf*chi`等，但哪一种方式是在文本分类中最好、最有效的方式呢？


# Details #

根据文献`[1][2][3]`中所得到的结果，他们在数据集**Reuters-21578**和 **20 Newsgroups**上，利用分类算法SVM和KNN等方法，得到的结论如下：
  1. 并非所有的**supervised 方法**都比**unsupervised方法**好，**`tf*chi,tf*odd`**做出的效果都是相当差得，而有的如**`tf*rf`**(作者自己提出的[3](3.md))方法却比较好。
  1. idf类方法虽然考虑了词的分布特征，但是在实际实验中效果有时没有提升反而会**下降**，如**tf`*`idf**,虽然这个方法在paper中频繁的被使用。因为idf是没有考虑到类别的区分度。
  1. tf类方法在实验中是取得非常好的效果，如**tf**,log(tf)等。而且这种方法非常简便、实用
  1. binary方法是最简洁的方法，其包含的语义较少，自然其效果比较差。

## Conclusion ##
在程序中**首选tf**作为特征权重，因为他的效果非常好，而且简便



## Reference ##
  1. Zhi-Hong Deng, A **Comparative Study** on **Feature Weight** in Text   Categorization,ADVANCED WEB TECHNOLOGIES AND APPLICATIONS 2004
  1. Man LAN,Proposing a New **Term Weighting** Scheme for Text Categorization,AAAI,2006
  1. Man Lan,**A comprehensive**comparative study**on**term weighting