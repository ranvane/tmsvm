#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author: 张知临 zhzhl202@163.com
#Filename: im_train.py
from optparse import OptionParser
from ctm_train_model import *
import os


def list_callback(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))

def main():
    usage ="usage:%prog [options] version=%prog 1.0"
    parser = OptionParser(usage=usage)
    parser.add_option("-s","--step",type="choice",choices=["1","2","3","4","5"],dest="step",help="step1 is auto training the svm model")
    parser.add_option("-p","--path",dest="save_main_path")
    parser.add_option("-P","--problem_path",dest="problem_save_path")
    parser.add_option("-i","--indexes",dest="indexes",action="callback",type="string",default=[1],callback=list_callback)
    parser.add_option("-w","--stopword",action="store_false",dest="stopword",default=True)
    parser.add_option("-d","--dic_name",dest="dic_name",default="dic.key")
    parser.add_option("-D","--dic_path",dest="dic_path")
    parser.add_option("-m","--model_name",dest="model_name",default="tms.model")
    parser.add_option("-t","--train_name",dest="train_name",default="tms.train")
    parser.add_option("-a","--param_name",dest="param_name",default="tms.param")
    parser.add_option("-r","--ratio",dest="ratio",type="float",default=0.4)
    parser.add_option("-A","--svm_param",dest="svm_param",default="'-s 0 -t 2 -c 1.0 -g 0.25'")
    parser.add_option("-T","--tc_splitTag",dest="tc_splitTag",type="string",default="\t")
    parser.add_option("-S","--str_splitTag",dest="str_splitTag",type="string",default="^")

    options, args = parser.parse_args() 
    if options.indexes:
        indexes = [int(i) for i in options.indexes]
    if options.step:
        step = int(options.step)

    if options.stopword ==False:
        stopword_filename=""
    else:
        stopword_filename = os.path.dirname(args[0])+"/stopwords.txt"
        
    if options.svm_param:
        svm_param = options.svm_param.replace("'","") 
    if step==1:
        ctm_train(args[0],indexes,options.save_main_path,stopword_filename,svm_param=svm_param,dic_name=options.dic_name,model_name=options.model_name,train_name=options.train_name,param_name=options.param_name,ratio=options.ratio,delete=True,str_splitTag=options.str_splitTag,tc_splitTag=options.tc_splitTag)

    if step==2:
        ctm_feature_select(args[0],indexes,options.save_main_path,options.dic_name,options.ratio,stopword_filename,str_splitTag=options.str_splitTag,tc_splitTag=options.tc_splitTag)
    
    if step==3:
        if os.path.exists(options.save_main_path):
            if os.path.exists(options.save_main_path+"temp/") is False:
                os.makedirs(options.save_main_path+"temp/")
        sample_save_path  = options.save_main_path +"temp/svm.train"
        cons_train_sample_for_cla(args[0],indexes,options.dic_path,sample_save_path,delete=True,str_splitTag=options.str_splitTag,tc_splitTag=options.tc_splitTag)
    
    if step==4:
        search_result_save_path  = options.save_main_path +"temp/"+"svm.param"
        #problem_save_path = options.main_save_path +"temp/"+"svm.train"
        c,g=grid(args[0],search_result_save_path)
        print "best c = %s\t g = %s\n"%(c,g)
    
    if step==5:
        model_save_path  = options.save_main_path+"model/"+options.model_name
        ctm_train_model(options.problem_save_path,svm_param,model_save_path)

if __name__ == "__main__":
    main()
