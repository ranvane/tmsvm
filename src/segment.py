#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author:张知临 zhzhl202@163.com
#Filename: segment.py
import sys
import os
depend_path = os.path.dirname(os.getcwd())+"/dependence"
sys.path.insert(0,depend_path)

import pymmseg as seg
seg.dict_load_defaults()

def term_seg(text,str_splitTag,type):
    seg_text =""
    if type==1:
        line =  seg.Algorithm(text)
        for l in line:
            seg_text+=str(l)+str_splitTag
    return seg_text

def file_seg(filename,out_filename,str_splitTag,type):
    f = open(filename,'r')
    fw = open(out_filename,'w')
    for line in f.readlines():
        fw.write(term_seg(line,str_splitTag)+"\n")
    fw.close()
    f.close()
        
        
        

def main():
    file_seg("../data/test.txt","../data/test_segmented.txt","^")
    f = file("../data/test.txt")
    text =f.readline()
    print term_seg(text,"^")
    
