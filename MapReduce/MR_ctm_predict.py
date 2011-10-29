#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math 
import sys
sys.path.append('.')
from hstream import *
from MR_ctm_predict_config import *
from svmutil import *
from svm import *

def cal_sc_optim(lab,m,text,dic_list,str_splitTag):
    y,x = cons_pro_for_svm(lab,text.strip().split(str_splitTag),dic_list)
    p_lab,p_acc,p_sc=svm_predict(y,x,m)
    
    if len(p_sc[0])>1:        
        return p_lab[0]
    else:             
        return p_sc[0][0]

def read_dic(filename,dtype=str):
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
    y=[float(label)]
    x={}
    real_x={} 
    for term in text:
        term  = term.strip()
        if dic.has_key(term) :
            index = int(dic.get(term))
            if x.has_key(index):
                x[index]+=1.0
            else:
                x[index]=1.0
    vec_sum = 0.0
    for key in x.keys():
        if x[key]!=0:
            vec_sum+=x[key]**2.0   
    vec_length=math.sqrt(vec_sum)
    if vec_length!=0:
        for key in x.keys():
            x[key]=float(x[key])/vec_length
    return y,[x]

def ctm_predict_multi(text,indexes_lists,dics,models,str_splitTag,tc_splitTag):
    k = len(dics)     
    score_list=[0]*k
    
    for j in range(k):
        indexes = indexes_lists[j]
        m = models[j]
        dic_list = dics[j]
        if len(text)<indexes[len(indexes)-1]+1 :
            sc=0  
        else:     
            text_temp=""
            for index in indexes:
                text_temp+=str_splitTag+text[index]                   
            sc=cal_sc_optim(1,m,text_temp,dic_list,str_splitTag)
        score_list[j]=float(sc)
    return score_list

#read the needed dic and model
k = len(dic_path_list) 
dic_lists=[]
models=[]
for i in range(k):
    dic_lists.append(read_dic(dic_path_list[i],dtype=str))
    models.append(svm_load_model(model_path_list[i]))

class Post_Check(HStream):
    def mapper(self, key, value):
        text = value.strip().split(tc_splitTag)
        if  len(text)>=result_indexes[len(result_indexes)-1]+1:        
            score_list = ctm_predict_multi(text,indexes_lists,dic_lists,models,str_splitTag,tc_splitTag)          
            #for score in score_list:
                #if score>0:
            output_value =""
            for score in score_list:
                output_value += str(score)+tc_splitTag 
            for index in result_indexes:
                 output_value += text[index]+ tc_splitTag 
            print output_value

    def reducer(self,key,values):
        pass

if __name__ =="__main__":
    Post_Check()

#def predict(value):
#    text = value.strip().split(tc_splitTag)
#    if  len(text)>=result_indexes[len(result_indexes)-1]+1:  
#        score_list = ctm_predict_multi(text,indexes_lists,dic_lists,models,str_splitTag,tc_splitTag)         
#        output_value =""
#        for score in score_list:
#            output_value += str(score)+tc_splitTag 
#        for index in result_indexes:
#             output_value += text[index]+ tc_splitTag 
#        print output_value
#
#filename ="sample.txt"
#for value in file(filename,'r'):
#    predict(value)
