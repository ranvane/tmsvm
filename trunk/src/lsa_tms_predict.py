#!/usr/bin/python
#author: ’≈÷™¡Ÿ zhzhl202@163.com
from ctm_predict_model import *
from optparse import *

def list_callback(option,opt,value,parser):
    setattr(parser.values,option.dest,value.split(','))

def main():
    usage="usage: %prog [options] filename dic_path model_path lsa_path lsa_model_path "
    parser = OptionParser(usage=usage)
    parser.add_option("-i","--indexes",dest="indexes",action="callback",type="string",default=[0],callback=list_callback)
    parser.add_option("-r","--result_indexes",dest="result_indexes",action="callback",type="string",default=[0],callback=list_callback,help="specify the content indexes that output with the predicted score")
    parser.add_option("-R","--result_save",dest="result_save")
    options, args = parser.parse_args() 
    
    if options.indexes :
        indexes =[int(i) for i in options.indexes]
    if options.result_indexes:
        result_indexes  =[int(i) for i in options.result_indexes]
    
    filename = args[0]
    dic_path = args[1]
    model_path = args[2]
    LSA_path = args[3]
    LSA_model_path = args[4]
    delete = False
    change_decode=False
    in_decode="UTF-8"
    out_encode="GBK"
    ctm_predict_lsa(filename,indexes,dic_path,options.result_save,result_indexes,model_path,LSA_path,LSA_model_path,delete=delete,tc_splitTag=options.tc_splitTag,str_splitTag=options.str_splitTag,change_decode=change_decode,in_decode=in_decode,out_encode=out_encode)

if __name__ =="__main__":
    main()