#!/usr/bin/python2.6
# coding: gbk
#Filename: utility_tools.py
'''
一些实用工具，包括
1、编码转换
2、将样本按照比例分割成训练样本和测试样本

'''
import os.path
from random import *
from fileutil import *

def encode_trans(in_filename,in_decode,out_encode,out_filename=""):
    '''对文件的编码进行转换
    转换后的文件可以自己指定，或者是系统自己生成，在文件后面加上 "$out_enncode"
    '''
    f1= file(in_filename,'r')
    if len(out_filename.strip())==0:
        filename= in_filename.split(".")
        if len(filename)>=2:
            out_filename = ".".join(filename[0:len(filename)-1])+"_"+out_encode+"."+filename[len(filename)-1]
        else:
            out_filename=in_filename+"_"+out_encode
    f2=file(out_filename,'w')
    while True:
        line=f1.readline()
        if len(line)==0:
            break
        f2.write(line.decode(in_decode).encode(out_encode,'ignore'))
        
def sel_train_test_set(filename,train_filename,test_filename,all_num,ratio):
    '''将总的文本按照比例分割成训练文本和测试文本'''
    num_dic = dict()
    test_num= int(all_num*ratio)
    count=0
    while len(num_dic)<test_num:
        num_dic[randint(1,all_num)] = 1
    train_f = file(train_filename,'w')
    test_f = file(test_filename,'w')
    for line in file(filename,'r').readlines():
        count+=1
        if num_dic.has_key(count) is True:
            test_f.write(line)
        else:
            train_f.write(line)
    train_f.close()
    test_f.close()
 
def extract_random(filename,number,all_num,save_path):  
    '''从文件中随机读取$number条的记录放入到结果文件中。'''  
    num_dic = dict()
    count=0
    while len(num_dic)<number:
        num_dic[randint(1,all_num)] = 1
    fw= file(save_path,'w')
    for line in file(filename,'r').readlines():
        count+=1
        if num_dic.has_key(count) is True:
            fw.write(line)

    fw.close()

def extract_random_by_condition(filename,number,all_num,save_path): 
    '''从文件中随机读取$number条的满足条件的记录放入到结果文件中。''' 
    num_dic = dict()
    count=0
    while len(num_dic)<number:
        num_dic[randint(1,all_num)] = 1
    fw= file(save_path,'w')
    for line in file(filename,'r').readlines():
        part = line.split("\t")
        if part[0]=='normal' and float(part[7])<0.3 and float(part[7])>-1.2:
            count+=1
            if num_dic.has_key(count) is True:
                fw.write(line)
    fw.close()

def extract_by_lin_num(filename,line_num_path,save_path):
    '''根据输入的行号，从文件中抽取指定的行号的内容'''
    f= file(filename,'r')
    line_list = read_list(line_num_path,dtype=int)
    fw= file(save_path,'w')
    count=0
    for line in f.readlines():
        count+=1
        if line_list.count(count)>0:
            fw.write(line)
            line_list.remove(count)
    f.close()
    fw.close()
  
def extract_by_id(filename,id_num,id_dic,save_path):
    fw=file(save_path,'w')
    for line in file(filename,'r').readlines():
        part = line.split("\t")
        if id_dic.has_key(part[id_num]) is True:
            fw.write(str(id_dic[part[id_num]])+"\t")
            fw.write("\t".join(part[1:]))

    fw.close()


  
def split_by_lin_nums(filename,lin_nums,file_prefix,c_p):
    '''把一个大文件，按照行数平分为若干份，指定每个文件的行数'''
    f= file(filename,'r')
    count =0
    file_count=1
    all_count=1
    out_f = file(c_p+"data/20110820_all_data/"+file_prefix+"_"+str(file_count),'w')
    for line in f.readlines():
        line=line.decode('UTF-8').encode('gbk','ignore')
        all_count+=1
        if count==lin_nums:
            out_f.close()
            file_count+=1
            out_f= file(c_p+"data/20110820_all_data/"+file_prefix+"_"+str(file_count),'w')
            print "now system is editing the" +str(file_count)+"file"
            count=0
        out_f.write(line)
        count+=1
    out_f.close()
    print all_count


    

def main(): 


    c_p = os.path.dirname(os.getcwd())
    '''---------------------------------------------------------
    -------------测试编码转换--
    in_filepath = "D:/张知临/数据/旺旺欺诈聊天/"
    in_filenames =["qizha_test_20111010aa","qizha_test_20111010ab","qizha_test_20111010ac"]
    #out_filename = "D:/张知临/数据/旺旺欺诈聊天/im_info_2_gbk.txt"
    in_decode="UTF-8"
    out_encode ="gbk"
    for in_filename in in_filenames:
        encode_trans(in_filepath+in_filename,in_decode,out_encode)
    '''
    
    '''----------------------------------------------------------------
    -------从结果中随机选取一定数量的训练样本 -----------
    
    filename  ="D:/张知临/源代码/python_ctm/model/im_info/im_info_2.result"  
    number =26000
    all_num=750000
    save_path ="D:/张知临/数据/旺旺欺诈聊天/正常样本待挑选2.txt"
    extract_random_by_condition(filename,number,all_num,save_path)
   ------------------------------'''
    
    '''----------------------------------------------------------------
        根据已有的样本Id，从源文件中把相应的样本抽取出来。--------------------------------------'''
    
    filename  = "D:/张知临/数据/旺旺欺诈聊天/im_info_2_gbk.txt"
    id_dic = read_dic("D:/张知临/数据/旺旺欺诈聊天/训练文本Id")
    id_num = 1
    save_path  ="D:/张知临/数据/旺旺欺诈聊天/训练样本2.txt"
    extract_by_id(filename,id_num,id_dic,save_path)
    
    
    '''---测试从总样本中构造训练和测试集--
    filename=c_p+ "model/model_0829_dic1/ctm_post_5230.data"
    train_f=c_p+ "model/model_0829_dic1/post.train"
    test_f=c_p+ "model/model_0829_dic1/post.test"
    ratio= 0.35
    sel_train_test_set(filename,train_f,test_f,5230,ratio)
    '''
    
    ''' 从文件中抽取指定行的内容。
    filename = c_p+"Dictionary/Dic1.glo"
    line_num_path = c_p+"model/model_0829_dic1/title.line"
    save_path = c_p+"model/model_0829_dic1/Dic1_title.glo"
    extract(filename,line_num_path,save_path)
    '''
    
    '''
         分割大文件
    filename =c_p+ "data/20110820_all_data/all_data_0819.txt"
    lin_nums=5000
    file_prefix = "part_data"
    split_by_lin_nums(filename,lin_nums,file_prefix)
    '''
    
main()