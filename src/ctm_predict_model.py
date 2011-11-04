#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: ctm_predict_model.py

'''此文件主要存放一些预测所常用的函数'''

from ctm_train_model import cons_vec_for_cla,cons_svm_problem,cons_pro_for_svm
from svm import *
from svmutil import *
from fileutil import read_dic
from lsa import load_lsa_model,cal_weight,pre_doc_svds
import math

def cal_sc(lab,m,text,dic_list,str_splitTag):
    '''输入标签，模型，待预测的文本，词典，以及词分词用的符号
    返回的是一个浮点数
    '''
    vec = cons_vec_for_cla(text.strip().split(str_splitTag),dic_list)
    y,x=cons_svm_problem(lab,vec)
    p_lab,p_acc,p_sc=svm_predict(y,x,m)

    return float(p_sc[0][0])

def cal_sc_optim(lab,m,text,dic_list,str_splitTag):
    '''输入标签，模型，待预测的文本，词典，以及词分词用的符号
    返回的是一个预测标签与得分，如果是二分类，返回的是直接得分，如果为多分类，返回的是经过计算的综合分数。
    '''
    y,x = cons_pro_for_svm(lab,text.strip().split(str_splitTag),dic_list)
    p_lab,p_acc,p_sc=svm_predict(y,x,m)  
    #在这里要判定是二分类还是多分类，如果为二分类，返回相应的分数，如果为多分类，则返回预测的标签。
 
    return p_lab[0],sum_pre_value(p_sc[0]),number_pre_value(p_sc[0])
  

def sum_pre_value(values):
    '''返回具有最大投票数的标签所获得分数的总和'''
    size = len(values)
    k = 1+int(math.sqrt(2*size+1))
    vote=[0]*k
    score=[0]*k
    p=0
    for i in range(k):
        for j in range(i+1,k):
            if values[p]>0:
                vote[i]+=1
                score[i]+=math.fabs(values[p])
            else : 
                vote[j]+=1
                score[j]+=values[p]
            p+=1
    max = 0 
    for i in range(1,k):
        if vote[i]>vote[max]:
            max = i
    return score[max]

def number_pre_value(values):
    '''返回具有最大投票数的标签所获得支持分数的个数'''
    size = len(values)
    k = 1+int(math.sqrt(2*size+1))
    vote=[0]*k
    p=0
    for i in range(k):
        for j in range(i+1,k):
            if values[p]>0:
                vote[i]+=1
            else : vote[j]+=1
            p+=1
    max = 0 
    for i in range(k):
        if vote[i]>max:
            max = vote[i]
    return max

def ctm_predict_lsa(filename,indexes,dic_path,result_save_path,result_indexes,model_path,LSA_path,LSA_model_path,delete,str_splitTag,tc_splitTag,change_decode=False,in_decode="UTF-8",out_encode="GBK"):
    '''使用LSA模型进行预测的程序
    其过程为：首先使用普通的SVM模型进行打分，然后利用打分值对原向量做伸缩处理
    最后使用LSA模型进行预测得分。
    @param result_indexes:需要和评分结果一起存储的值。
    '''
    dic_list = read_dic(dic_path,dtype=str)
    f= file(filename,'r')
    fs = file(result_save_path,'w')
    m= svm_load_model(model_path)
    lsa_m = svm_load_model(LSA_model_path)
    U = load_lsa_model(LSA_path,"U")

    for line in f.readlines():
        if change_decode ==True:
            line = line.decode(in_decode).encode(out_encode,'ignore')
        text = line.strip().split(tc_splitTag)
        if len(text)<indexes[len(indexes)-1]+1 or len(text)<result_indexes[len(result_indexes)-1]+1:
            continue

        text_temp=""
        for i in indexes:
            text_temp+=str_splitTag+text[i]  
        vec = cons_vec_for_cla(text_temp.strip().split(str_splitTag),dic_list)
        y,x=cons_svm_problem(1,vec) #此处的lab 默认为1
        p_lab,p_acc,p_sc=svm_predict(y,x,m)
                
        weight = cal_weight(p_sc[0][0])
        vec = [0]*len(vec)
        for key in x[0].keys():
           vec[int(key)-1]= weight*float(x[0][key])
        vec = pre_doc_svds(vec,U)
        y,x=cons_svm_problem(text[0],vec)
        lsa_lab,lsa_acc,lsa_sc = svm_predict(y,x,lsa_m)
        fs.write(str(p_sc[0][0])+"\t"+str(lsa_sc[0][0])+"\t")
        for index in result_indexes:
            fs.write(text[index]+"\t")
        fs.write("\n")

    f.close()
    fs.close()

    
    
def ctm_predict(filename,indexes,dic_path,result_save_path,result_indexes,model_path,str_splitTag,tc_splitTag,delete=False,change_decode=False,in_decode="UTF-8",out_encode="GBK"):
    '''一般形式的下得模型预测，即单个模型。'''
    dic_list = read_dic(dic_path,dtype=str)  
    f= file(filename,'r')
    fs = file(result_save_path,'w')
    m= svm_load_model(model_path)
    for line in f.readlines():
        if change_decode ==True:
            line = line.decode(in_decode).encode(out_encode,'ignore')
        text = line.strip().split(tc_splitTag)
        if len(text)<indexes[len(indexes)-1]+1 or len(text)<result_indexes[len(result_indexes)-1]+1:
            continue       
        text_temp=""
        for i in indexes:
            text_temp+=str_splitTag+text[i]                   
        #sc=cal_sc(1,m,text_temp,dic_list,str_splitTag)
        label,sc,num=cal_sc_optim(1,m,text_temp,dic_list,str_splitTag)
        fs.write(str(label)+"\t"+str(sc)+"\t")
        for index in result_indexes:
            fs.write(text[index]+"\t")
        fs.write("\n")
    f.close()
    fs.close()

def ctm_predict_multi(filename,indexes_lists,dic_path_list,result_save_path,result_indexes,model_path_list,str_splitTag,tc_splitTag,delete=False,change_decode=False,in_decode="UTF-8",out_encode="GBK"):
    '''多个模型的预测，如一个文本有多个模型需要预测
    其中title_indexes，dic_path ，model_path为二维度的。
    '''
    k = len(dic_path_list) #得到预测模型的个数
    dic_lists=[]
    models=[]
    for i in range(k):
        dic_lists.append(read_dic(dic_path_list[i],dtype=str))
        models.append(svm_load_model(model_path_list[i]))
        
    f= file(filename,'r')
    fs = file(result_save_path,'w')
    
    for line in f.readlines():
        if change_decode ==True:
            line = line.decode(in_decode).encode(out_encode,'ignore')
        text = line.strip().split(tc_splitTag)
        
        for j in range(k):
            indexes = indexes_lists[j]
            m = models[j]
            dic_list = dic_lists[j]
            if len(text)<indexes[len(indexes)-1]+1 or len(text)<result_indexes[len(result_indexes)-1]+1:
                sc=0  
            else:     
                text_temp=""
                for index in indexes:
                    text_temp+=str_splitTag+text[index]                   
                label,sc,num=cal_sc_optim(1,m,text_temp,dic_list,str_splitTag)
            fs.write(str(label)+"\t"+str(sc)+"\t")
        for index in result_indexes:
            if index>len(text)-1:
                break
            fs.write(text[index]+"\t")
        fs.write("\n")
    f.close()
    fs.close()
