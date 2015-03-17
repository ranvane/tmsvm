# Introduction #
使用该系统可以做：

  1. 对文本自动做SVM模型的训练。
  1. 利用生成的模型对未知文本做预测。
  1. 分词。对文本利用mmseg算法对文本进行分词。
  1. 特征选择。
  1. SVM参数的选择。
  1. 对文本直接生成libsvm、liblinear的输入格式。
  1. SVM模型训练。利用libsvm、liblinear对模型进行训练。
  1. 自动计算结果的F值、召回率、准确率、Macro,Micro等指标，并会计算特定阈值、以及指定区间所有阈值下的相应指标。

  * 具体该怎么使用呢，我们通过几个程序来来进行说明。具体程序在src/example.py文件中有例子 

### 演示如何自动对模型进行训练，输入的训练样本，并配置相应的参数 ###

> example 1
> 指定输入文件，其他使用默认参数。
> filename = "../data/binary.train"
> train\_model.ctm\_train(filename)

> example 2 :指定输入文件，以及设定具体的参数。对与剩余的参数也可以按照这种方式进行。
> filename = "../data/binary.train"
> indexes = [1](1.md) #指定输入对输入文件的第二个字段进行SVM模型训练。
> main\_save\_path ="../data/" #指定模型保存的路径。
> segment = 1 #选择使用分词
> svm\_type="liblinear" #使用liblinear作为SVM模型。
> train\_model.ctm\_train(filename,seg=segment,main\_save\_path=main\_save\_path,svm\_type=svm\_type)