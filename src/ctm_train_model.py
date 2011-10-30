#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: ctm_train_model.py
'''此文件转为训练分类器模型，读入的文件格式
Label    value1 [value2...]#即第一个为类标签，第二个为内容，中间用Tab隔开
'''
#from ctm_train_model_config import *
import math
from svm import *
from svmutil import *
from fileutil import read_list,read_dic
from ctmutil import *
from lsa import *
from feature_select import feature_select
from grid_search_param import grid
import os
import time

def ctm_train(filename,indexs,main_save_path,stopword_filename,svm_param,dic_name,model_name,train_name,param_name,ratio,delete,str_splitTag,tc_splitTag):
    '''训练的自动化程序，先进行特征选择，重新定义词典，根据新的词典，自动选择SVM最优的参数。
    然后使用最优的参数进行SVM分类，最后生成训练后的模型。
    需要保存的文件：（需定义一个主保存路径）
                 模型文件：词典.key+模型.model
                临时文件 ：svm分类数据文件.train
    
    '''
    print "-----------------现在正在进行特征选择---------------"
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
    feature_select(filename,indexs,dic_path,ratio,stop_words_dic,str_splitTag=str_splitTag,tc_splitTag=tc_splitTag)
    
    print "-----------------再根据特征选择后的词典构造新的SVM分类所需的训练样本-------------------"
    if os.path.exists(main_save_path):
        if os.path.exists(main_save_path+"temp/") is False:
            os.makedirs(main_save_path+"temp/")
    #temp_name = "svm_"+ str(time.strftime('%Y-%m-%d@%H-%M-%S',time.localtime(time.time())))    
    
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


def lsa_svm_train(filename,svm_model_path,M,main_save_path,threshold,K,svm_param,for_lsa_train,train_name,param_name,model_name):
    '''此处的filename为libsvm的格式，训练普通的模型是放置在temp中train文件。'''
    if os.path.exists(main_save_path):
        if os.path.exists(main_save_path+"lsa/") is False:
            os.makedirs(main_save_path+"lsa/")
        if os.path.exists(main_save_path+"model/") is False:
            os.makedirs(main_save_path+"model/")
        if os.path.exists(main_save_path+"temp/") is False:
            os.makedirs(main_save_path+"temp/")
    print"--------------------使用SVM模型预测训练文本，为LSA模型准备输入------------------------------"
    for_lsa_train_save_path = main_save_path +"temp/"+for_lsa_train
    save_train_for_lsa(filename,svm_model_path,for_lsa_train_save_path)
    print"--------------------构造LSA模型------------------------------"
    lsa_train_save_path = main_save_path +"temp/"+train_name
    lsa_save_path = main_save_path +"lsa/lsa"
    ctm_lsa(M,threshold,K,for_lsa_train_save_path,lsa_train_save_path,lsa_save_path)
    
    print"--------------------选择最优的c,g------------------------------"
    search_result_save_path  = main_save_path +"temp/"+param_name
    c,g=grid(lsa_train_save_path,search_result_save_path)
    
    print "-----------------根据得到的最优参数，训练模型，并将模型进行保存----------"
    svm_param = svm_param + " -c "+str(c)+" -g "+str(g)
    model_save_path  = main_save_path+"model/"+model_name
    ctm_train_model(lsa_train_save_path,svm_param,model_save_path)

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
    '''总共有5个特征位需要填充，分别是内容得分，是否有外连接、是否有QQ，所发送的链接商品ID是否同属于某个人，是否为虚拟商品'''
    m = svm_load_model(svm_model)
    f = file(filename,'r')
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        text_temp=""
        for i in content_indexs:
          text_temp+=str_splitTag+text[i]  
          p_lab,p_acc,p_sc = svm_predict() 



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
    y,x = svm_read_problem(test_path)
    m = svm_load_model(model_save_path)
    p_lab,p_acc,p_sc = svm_predict(y,x,m)
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

def add_sample_to_model_lsa(extra_filename,indexs,dic_path,glo_aff_path,sample_save_path,model_path,LSA_path,LSA_model_path,delete,str_splitTag,tc_splitTag):
    '''将之前误判的样本，放入到LSA样本中重新训练。'''
    dic_list = read_list(dic_path,dtype=str)
    glo_aff_list = read_list(glo_aff_path)
    f= file(extra_filename,'r')
    fs = file(sample_save_path,'a')
    m= svm_load_model(model_path)
    lsa_m = svm_load_model(LSA_model_path)
    U = load_lsa_model(LSA_path,"U") 
    for line in f.readlines():
        text = line.strip().split(tc_splitTag)
        text_temp=""
        for i in indexs:
          text_temp+=str_splitTag+text[i]  
        #y,x = cons_pro_for_svm(text[0],text_temp.strip().split(str_splitTag),dic_list)
        vec = cons_vec_for_cla(text_temp.strip().split(str_splitTag),dic_list,glo_aff_list)
        y,x=cons_svm_problem(text[0],vec)
        p_lab,p_acc,p_sc=svm_predict(y,x,m)
        if delete == True and len(vec)==vec.count(0):
            continue
        weight = cal_weight(p_sc[0][0])
        vec = [0]*len(vec)
        for key in x[0].keys():
           vec[int(key)-1]= weight*float(x[0][key])
        vec = pre_doc_svds(vec,U)
        save_list_train_sample(fs,text[0],vec)
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


