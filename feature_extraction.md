# Introduction #

在文本分类中，**降维**是一个非常重要的问题，常用的降维方式有两种：**feature selection**和 **feature extraction**。[feature\_selection](feature_selection.md) 即从原词典中选择一个具有代表性的子集，常用方法有mutual information、information gain、**chi**，而feature extraction是是对原有的特征进行组合，将原高维向量空间映射到新的空低维空间上，从而达到降维的目的，常用的方法有PCA、**LSA\*等。**



# Details #
一般来讲，[feature\_selection](feature_selection.md)简便易行，计算出各个特征的权重，然后选择top n%的特征作为最具代表性的特征。另外还有一种方法是F-score+SVM，即首先计算出各个特征的F-Score，然后选择一部分进行n-flods的SVM交叉验证，最终选择最好的特征集。

而feature extraction则不同，最常用的有LSA(Latent semantic analysis)，其最关键技术就是SVD分解。即对特征-文档矩阵进行SVD分解：**X=USV'**。选取前k个特征值，然后重构X矩阵。实验证明，使用`X'*U(m*k)`即可将原训练文本映射到U空间上。在文本分类领域使用LSA方法常用的有Global SVD 和**Local SVD**。Global SVD已经被实验证明效果非常差，现在大家关注的多为Local SVD，本文实现的LSA是`[2]`中提出的一种local SVD方法

## 改进方向 ##
  1. NMF分解
> > 本系统已经实现了基于LSA的特征抽取方法，见文献`[2]`。在参阅过论文中，在进行矩阵分解时也有很多人使用NMF方法，并对两种方法进行了比较，因为程序中使用了Python的csc\_matrix存储大矩阵，现在还没有找到合适的NMF分解的程序
  1. 其他关于LSA方法的改进
> > LSA方法在文本分类领域还没有太好经得起考验的算法，所以后续将会实验更多LSA算法，直到找出一个效果比较好的方法
## Reference ##

  1. F Sebastiani,Machine learning in automated text categorization ,ACM2002
  1. T,Liu,Improving Text Classification using Local Latent Semantic Indexing,ICDM'04