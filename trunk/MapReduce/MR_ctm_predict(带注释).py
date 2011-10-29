#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author 张知临 zhzhl202@163.com
import math 
import sys
sys.path.append('.')
from hstream import *
from MR_ctm_predict_config import *
from svmutil import *
from svm import *



def cal_sc_optim(lab,m,text,dic_list,str_splitTag):
    '''输入标签，模型，待预测的文本，词典，以及词分词用的符号
    返回的是一个浮点数
    '''
    y,x = cons_pro_for_svm(lab,text.strip().split(str_splitTag),dic_list)
    print dic_list 
    p_lab,p_acc,p_sc=svm_predict(y,x,m)
    #在这里要判定是二分类还是多分类，如果为二分类，返回相应的分数，如果为多分类，则返回预测的标签。
    if len(p_sc[0])>1: #多分类，返回预测的标签
        return p_lab[0]
    else:             #二分类，返回具体的预测分值。
        return p_sc[0][0]


def read_dic(filename,dtype=str):
    '''因为要维持dic顺序，'''
    f= file(filename,'r')
    dic={}
    count=0
    for line in f.readlines():
        line=line.split("\t")
        count+=1
        if len(line)<1:
            continue
        if len(line)==1:
            dic[dtype(line[0].strip())]=count
        else:
            dic[dtype(line[0].strip())]=float(line[1])

    f.close()
    return dic

def cons_pro_for_svm(label,text,dic):
    '''根据构造的输入的类标签和以及经过分词后的文本和词典，SVM分类所用的输入格式，会对特征向量进行归一化
        注意：这个实现已经去除了全局因子的影响，意味着特征权重直接使用词频。
    x begin from 1'''
    y=[float(label)]
    x={}
    real_x={} #因为x的keys可能是无序的，所以要先对x中的进行排序，然后
    #构造特征向量
    for term in text:
        term  = term.strip()
        if dic.has_key(term) :
            index = int(dic.get(term))
            if x.has_key(index):
                x[index]+=1.0
            else:
                x[index]=1.0
    #计算特征向量的模
    vec_sum = 0.0
    for key in x.keys():
        if x[key]!=0:
            vec_sum+=x[key]**2.0
    #对向量进行归一化处理。
    vec_length=math.sqrt(vec_sum)
    if vec_length!=0:
        for key in x.keys():
            x[key]=float(x[key])/vec_length
    return y,[x]

def ctm_predict_multi(text,indexes_lists,dics,models,str_splitTag,tc_splitTag):
    '''多个模型的预测，如一个文本有多个模型需要预测
    则输入一条记录，返回多个模型的预测得分。
    需配置多项：1、各个模型需要检测的字段的位置。2、词典列表。3、模型列表
    其他的还有str_splitTag,tc_splitTag
    其中title_indexes，dic_path ，model_path为二维度的。
    '''
    k = len(dics) #得到预测模型的个数
    score_list=[0]*k
    
    for j in range(k):
        indexes = indexes_lists[j]
        m = models[j]
        dic_list = dics[j]
        if len(text)<indexes[len(indexes)-1]+1 :
            #如果需要预测的范围超过文本的范围，则预测分数赋予0
            
            sc=0  
        else:     
            text_temp=""
            for index in indexes:
                text_temp+=str_splitTag+text[index]                   
           # print text_temp
            sc=cal_sc_optim(1,m,text_temp,dic_list,str_splitTag)
        score_list[j]=float(sc)
    return score_list

#read the needed dic and model
k = len(dic_path_list) #得到预测模型的个数
dic_lists=[]
models=[]
for i in range(k):
    dic_lists.append(read_dic(dic_path_list[i],dtype=str))
    models.append(svm_load_model(model_path_list[i]))
#for i in range(k):
   # print dic_lists[i]
class Post_Check(HStream):
    #count=0
    def mapper(self, key, value):
     #   if count==0:
      #      for i in range(k):
       #         print dic_lists[i]
        #count+=1
        text = value.strip().split(tc_splitTag)
        if  len(text)>=result_indexes[len(result_indexes)-1]+1:
            #如果需要输出的范围超过文本的范围，跳过。
            
            score_list = ctm_predict_multi(text,indexes_lists,dic_lists,models,str_splitTag,tc_splitTag)
            #如果分数列表中有一个大于0，则输出结果。
            for score in score_list:
                #if score>0:
                 output_value =""
                 for score in score_list:
                     output_value += str(score)+tc_splitTag 
                 for index in result_indexes:
                     output_value += text[index]+ tc_splitTag 
                 print output_value
                 break
        else:
            print "输入文件字段数目不符合输出规则"

    def reducer(self,key,values):
        pass

if __name__ =="__main__":
    Post_Check()
