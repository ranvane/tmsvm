#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: example.py

import tms
'''采用程序默认参数对模型训练、预测、结果分析'''
#模型训练，输入的文件为binary_seged.train,需要训练的为文件中的第1个字段(第0个字段为lablel),保存在data文件夹中。特征选择保留top %10的词，使用liblinear
#tms.tms_train("../data/binary_seged.train")
#模型预测，
#tms.tms_predict("../data/binary_seged.test","../data/model/tms.config",result_save_path="../data/binary_seged.result")
#对结果进行分析
#tms.tms_analysis("../data/binary_seged.result")

'''配置多个模型进行预测'''
#tms.tms_predict_multi("../data/binary_seged.test", ["../data/libsvm_model/tms.config","../data/liblinear_model/tms.config"],indexes_lists=[[1],[1]],result_save_path="../data/binary_seged.result")
#tms.tms_analysis("../data/binary_seged.result",indexes=[0,1,2,3,4],true_label_index=4)

'''对文件进行分词'''
#tms.tms_segment("../data/binary.train", indexes=[1])

'''特征选择'''
#tms.tms_feature_select("../data/binary_seged.train", indexes=[1], global_fun="idf", dic_name="test.key", ratio=0.05, stopword_filename="")

'''将输入文件构造为libsvm和liblinear的输入格式'''
tms.cons_train_sample_for_svm("../data/binary_seged.train", "../data/model/dic.key", "../data/tms.train", [1])

'''对SVM模型选择最优的参数'''


'''对没有经过分词的文件进行训练'''
#tms.tms_train("../data/binary.train",seg=1)

'''假设data文件夹下有一个post.train和post.test的训练样本和测试样本，每一行有3个字段：label title content。样本都没有分词
该例子需要完成：
1、对title进行分词、训练，模型保存在../data/post/ 下，所有的文件都有title命名，SVM模型选择使用libsvm，
2、对content进行分词、训练，模型保存在../data/post/ 下，所有的文件都有content命名，SVM模型选择使用liblinear，
'''