#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: example.py
'''Tmsvm示例程序,演示如果调用程序'''
import tms #这个是训练的入口模块，需要引入

def auto_train():
    '''此示例演示如何自动对模型进行训练，输入的训练样本，并配置相应的参数。
    输入文件的格式为 label value1 [values2...]
      具体的参数列表如下：
    filename 训练文本所在的文件名
    indexes：需要训练的指标项,默认[1]
    main_save_path 模型保存的路径,默认”../“
    stopword_filename 停用词的名称以及路径 ;默认不使用停用词.
    svm_type :svm类型：libsvm 或liblinear.默认"libsvm"
    svm_param  用户自己设定的svm的参数,这个要区分libsvm与liblinear参数的限制；默认 " "
    dic_name 用户自定义词典名称;默认“dic.key”
    model_name用户自定义模型名称 ;默认"svm.model"
    train_name用户自定义训练样本名称 ；默认“svm.train”
    param_name用户自定义参数文件名称 ；默认"svm.param"
    ratio 特征选择保留词的比例 ；默认 0.4
    delete对于所有特征值为0的样本是否删除,True or False。默认 True
    str_splitTag 分词所用的分割符号 默认"^",
    tc_splitTag训练样本中各个字段分割所用的符号 ，默认"\t"
    seg 分词的选择：0为不进行分词；1为使用mmseg分词；2为使用aliws分词
    param_select ;是否进行SVM模型参数的搜索。True即为使用SVM模型grid.搜索，False即为不使用参数搜索。
    local_fun：即对特征向量计算特征权重时需要设定的计算方式:x(i,j) = local(i,j)*global(i).可选的有tf,logtf
    global_fun :全局权重的计算方式：有"one","idf","rf"
    '''
    #example 1 :指定输入文件，其他使用默认参数。
    filename = "../data/binary.train"
    tms.tms_train(filename)
    
    #example 2 :指定输入文件，以及设定具体的参数。对与剩余的参数也可以按照这种方式进行。
    filename = "../data/binary.train"
    indexes = [1] #指定输入对输入文件的第二个字段进行SVM模型训练。
    main_save_path ="../data/" #指定模型保存的路径。
    segment = 1 #选择使用分词
    svm_type="liblinear" #使用liblinear作为SVM模型。
    tms.ctm_train(filename,seg=segment,main_save_path=main_save_path,svm_type=svm_type)

def segment():
    '''对输入文件进行分词'''
    

def feature_select():
    '''对输入文件进行特征选择。具体的参数如下：
    filename 训练文本所在的文件名
    indexes：需要训练的指标项,默认[1]
    main_save_path 模型保存的路径,默认”../“
    stopword_filename 停用词的名称以及路径 ;默认和训练样本同路径下的stopwords.txt
    dic_name 用户自定义词典名称;默认“dic.key”
    ratio 特征选择保留词的比例 ；默认 0.4
    str_splitTag 分词所用的分割符号 默认"^",
    tc_splitTag训练样本中各个字段分割所用的符号 ，默认"\t"
    seg 分词的选择：0为不进行分词；1为使用mmseg分词；2为使用aliws分词
    global_fun :即对特征向量计算特征权重时需要设定的计算方式:x(i,j) = local(i,j)*global(i).全局因子计算方式
             可选的计算方式有"one","idf","rf"
    '''
    filename = "../data/binary_seged.train" 
    tms.ctm_feature_select(filename)
auto_train()    




