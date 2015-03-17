# Introduction #

特征选择是文本分类中比较常用的方法，即从原特征中选择有代表性的特征子集，从而达到降维的目的，常用的特征选择的方法有mutual information、information gain、chi等。


# Details #
一般来讲，feature\_selection简便易行，计算出各个特征的权重，然后选择top n%的特征作为最具代表性的特征。另外还有一种方法是F-score+SVM，即首先计算出各个特征的F-Score，然后选择一部分进行n-flods的SVM交叉验证，最终选择最好的特征集。
根据`[1]`中的实验结果,chi方法是效果最好的特征选择方法


## Reference ##
  1. Y Yang, A comparative study on feature selection in text categorization