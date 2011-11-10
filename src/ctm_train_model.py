#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: ctm_train_model.py
'''此文件转为训练分类器模型，读入的文件格式
Label    value1 [value2...]#即第一个为类标签，第二个为内容，中间用Tab隔开
'''
#from ctm_train_model_config import *
import math
import tms_svm
import segment
from fileutil import read_list,read_dic
from ctmutil import *
from feature_select import feature_select
from grid_search_param import grid
import os
import time

def ctm_train(filename,indexs,main_save_path,stopword_filename,svm_param,dic_name,model_name,train_name,svm_type,param_name,ratio,delete,str_splitTag,tc_splitTag,segment):
    '''训练的自动化程序，分词,先进行特征选择，重新定义词典，根据新的词典，自动选择SVM最优的参数。
    然后使用最优的参数进行SVM分类，最后生成训练后的模型。
    需要保存的文件：（需定义一个主保存路径）
                 模型文件：词典.key+模型.model
                临时文件 ：svm分类数据文件.train
    filename 训练文本所在的文件名
    indexs需要训练的指标项
    main_save_path 模型保存的路径
    stopword_filename 停用词的名称以及路径 ;
    svm_type :svm类型：1为libsvm ;2为liblinear
    svm_param  用户自己设定的svm的参数,这个要区分libsvm与liblinear参数的限制；例如"-s 0 -t 2 -c 0.2 "
    dic_name 用户自定义词典名称;例如“dic.key”
    model_name用户自定义模型名称 ;例如"svm.model"
    train_name用户自定义训练样本名称 ；例如“svm.train”
    param_name用户自定义参数文件名称 ；例如"svm.param"
    ratio 特征选择保留词的比例 ；例如 0.4
    delete对于所有特征值为0的样本是否删除,True or False
    str_splitTag 分词所用的分割符号 例如"^"
    tc_splitTag训练样本中各个字段分割所用的符号 ，例如"\t"
    segment 分词的选择：0为不进行分词；1为使用mmseg分词；2为使用aliws分词
    
    '''

    #如果模型文件保存的路径不存在，则创建该文件夹
    dic_path= main_save_path+"model/"+dic_name
    if os.path.exists(main_save_path):
        if os.path.exists(main_save_path+"model/") is False:
            os.makedirs(main_save_path+"model/")
    #如果没有给出停用词的文件名，则默认不使用停用词
    if stopword_filename =="":
        stop_words_dic=dict()
    else:
        stop_words_dic = read_dic(stopword_filename)
    
    #如果需要分词，则对原文件进行分词
    if segment!=0:
        print "-----------------正在对源文本进行分词-------------------"
        segment_file = os.path.dirname(filename)+"/segmented"
        segment.file_seg(filename, segment_file, str_splitTag,segment)
        filename = segment_file
    
    print "-----------------现在正在进行特征选择---------------"      
    feature_select(filename,indexs,dic_path,ratio,stop_words_dic,str_splitTag=str_splitTag,tc_splitTag=tc_splitTag)
    
    print "-----------------再根据特征选择后的词典构造新的SVM分类所需的训练样本-------------------"
    #要设定SVM模型的类型
    tms_svm.set_svm_type(svm_type)
    
    if os.path.exists(main_save_path):
        if os.path.exists(main_save_path+"temp/") is False:
            os.makedirs(main_save_path+"temp/")  
    
    problem_save_path  =main_save_path+"temp/"+train_name
    cons_train_sample_for_cla(filename,indexs,dic_path,problem_save_path,delete,str_splitTag,tc_splitTag)
    
    print"--------------------选择最优的c,g------------------------------"
    search_result_save_path  = main_save_path +"temp/"+param_name
    c,g=grid(problem_save_path,search_result_save_path)
    
    print "-----------------根据得到的最优参数，训练模型，并将模型进行保存----------"
    svm_param = svm_param + " -c "+str(c)+" -g "+str(g)
    model_save_path  = main_save_path+"model/"+model_name
    ctm_train_model(problem_save_path,svm_param,model_save_path)

def ctm_feature_select(filename,indexs,main_save_path,dic_name,ratio,stopword_filename,str_splitTag,tc_splitTag):
    #如果模型文件保存的路径不存在，则创建该文件夹
    dic_path= main_save_path+"model/"+dic_name
    if os.path.exists(main_save_path):
        if os.path.exists(main_save_path+"model/") is False:
            os.makedirs(main_save_path+"model/")
    #如果没有给出停用词的文件名，则默认不使用停用词
    if stopword_filename =="":
        stop_words_dic=dict()
    else:
        stop_words_dic = read_dic(stopword_filename)
    feature_select(filename,indexs,dic_path,ratio,stop_words_dic,str_splitTag,tc_splitTag)


def cons_train_sample_for_cla(filename,indexs,dic_path,sample_save_path,delete,str_splitTag,tc_splitTag):
    '''根据提供的词典，将指定文件中的指定位置上的内容构造成SVM所需的问题格式，并进行保存'''
    dic_list = read_dic(dic_path,dtype=str)
    f= file(filename,'r')
    fs = file(sample_save_path,'w')
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        text_temp=""
        if len(text)<indexs[len(indexs)-1]+1:
            continue
        for i in indexs:
            text_temp+=str_splitTag+text[i]  
        y,x = cons_pro_for_svm(text[0],text_temp.strip().split(str_splitTag),dic_list)
        if delete == True and len(x[0])==0:
            continue
        save_dic_train_sample(fs,y,x)
    f.close()
    fs.close()

def extract_im_feature(filename,content_indexs,feature_indexs,dic_path,svm_model,delete,str_splitTag,tc_splitTag):
    ''''''
    m = tms_svm.load_model(svm_model)
    f = file(filename,'r')
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        text_temp=""
        for i in content_indexs:
          text_temp+=str_splitTag+text[i]  
          p_lab,p_acc,p_sc =tms_svm.predict() 



def save_dic_train_sample(f,y,x):
    '''将构造的svm问题格式进行保存
    y为list x为list里面为 词典。[ {} ]
    '''
    for i in range(len(y)):
        f.write(str(y[i]))
        #将字典有序的输出来。
        #sorted(dic.items(),key=lamda dic:dic[0],reverse = False)
        #dic =x[0]
        #sorted_keys=sorted(dic.items(),key=lambda dic:dic[0],reverse=False)
        sorted_keys = x[i].keys()
        sorted_keys.sort()
        for key  in sorted_keys:
            f.write("\t"+str(key)+":"+str(x[i][key]))
        f.write("\n")


def save_list_train_sample(f,lab,vec):
    '''将特征向量以SVM的输入格式进行保存，
    lab 为str，vec为list
    '''
    f.write(lab)
    for i  in range(len(vec)):
        if vec[i]!=0:
            f.write("\t"+str(i+1)+":"+str(vec[i]))
    f.write("\n")


def save_train_for_lsa(test_path,model_save_path,lsa_train_save_path):
    '''predict trainset using the initial classifier  ,and save the trainset with
    lsa format : label score feature
    '''
    y,x = tms_svm.read_problem(test_path)
    m = tms_svm.load_model(model_save_path)
    p_lab,p_acc,p_sc = tms_svm.predict(y,x,m)
    f= file(lsa_train_save_path,'w')
    for i  in range(len(y)):
        f.write(str(int(y[i]))+"\t"+str(p_sc[i][0])+"\t")
        dic =x[i]
        sorted_x = sorted(dic.items(),key = lambda dic:dic[0])
        for key in sorted_x:
            f.write(str(key[0])+":"+str(key[1])+"\t")
        f.write("\n")
    f.close()
    

def add_sample_to_model(extra_filename,indexs,dic_path,sample_save_path,delete,str_splitTag,tc_splitTag):
    '''将之前误判的样本，放入到样本中重新训练。'''
    dic_list = read_dic(dic_path,dtype=str)
    #glo_aff_list = read_list(glo_aff_path)
    f= file(extra_filename,'r')
    fs = file(sample_save_path,'a')
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        text_temp=""
        for i in indexs:
          text_temp+=str_splitTag+text[i]  
        y,x = cons_pro_for_svm(text[0],text_temp.strip().split(str_splitTag),dic_list)
        if delete == True and len(x)==0:
            continue
        save_dic_train_sample(fs,y,x)
    f.close()
    fs.close()




#def main():
#    filename = "D:/张知临/源代码/python_ctm/model/im_info/10.15_30000/temp/im.train"
#    svm_model_path = "D:/张知临/源代码/python_ctm/model/im_info/10.15_30000/model/im.model"
#    M = 8368
#    main_save_path = "D:/张知临/源代码/python_ctm/model/im_info/10.15_30000/"
#    threshold = 1.0 
#    K = 50
#    for_lsa_train = "for_lsa.train"
#    train_name = "lsa.train"
#    svm_param = " "
#    param_name = "lsa.param"
#    model_name = "lsa.model"
#    lsa_svm_train(filename,svm_model_path,M,main_save_path,threshold,K,svm_param,for_lsa_train,train_name,param_name,model_name)


