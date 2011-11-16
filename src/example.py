#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: example.py

import tms
'''采用程序默认参数对模型'''
#模型训练，输入的文件为binary_seged.train,需要训练的为文件中的第1个字段(第0个字段为lablel),保存在data文件夹中。特征选择保留top %10的词，使用liblinear
#tms.tms_train("../data/binary_seged.train")
#模型预测，
#tms.tms_predict("../data/binary_seged.test","../data/model/tms.config",result_save_path="../data/binary_seged.result")
#对结果进行分析
#tms.tms_analysis("../data/binary_seged.result")

'''配置多个模型进行预测'''
tms.tms_predict_multi("../data/binary_seged.test", ["../data/libsvm_model/tms.config","../data/liblinear_model/tms.config"],indexes_lists=[[1],[1]],result_save_path="../data/binary_seged.result")