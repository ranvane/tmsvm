#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author: 张知临 zhzhl202@163.com
from ctm_train_model import *
from optparse import OptionParser
import os
     
def main():
    usage ="usage:%prog [options] filename svm_model M "
    parser = OptionParser(usage=usage)
    parser.add_option("-p","--path",dest="save_main_path",default="../")
    parser.add_option("-e","--threshold",dest="threshold",type="float",default=1.0)
    parser.add_option("-K","--K",dest="K",type="int",default=500)
    parser.add_option("-f","--for_lsa_train",dest="for_lsa_train",default="for_lsa.train")
    parser.add_option("-t","--train_name",dest="train_name",default="lsa.train")
    parser.add_option("-m","--model_name",dest="model_name",default="lsa.model")    
    parser.add_option("-A","--svm_param",dest="svm_param",default="'-s 0 -t 2 '")
    parser.add_option("-a","--param_name",dest="param_name",default="lsa.param")

    options, args = parser.parse_args() 
    if options.svm_param:
        svm_param = options.svm_param.replace("'","") 
    filename = args[0]
    svm_model = args[1]
    M = int(args[2])
    lsa_svm_train(filename,svm_model,M,options.save_main_path,options.threshold,options.K,svm_param,options.for_lsa_train,options.train_name,options.param_name,options.model_name)

if __name__ =="__main__":
    main()