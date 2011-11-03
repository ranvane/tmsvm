#!/usr/bin/python

#author:zhzhl202@163.com
#Filename: corpus_process.py

import os

def merge_with_label(f,files,label,tc_splitTag):
    for fi in files:
        fr = file(fi,'r')
        text = "".join(fr.readlines())
        text = text.replace("\n","")
        text = text.replace("\t","")
        if len(text.split("\t"))>2:
            print text.split("\t")
        f.write(tc_splitTag.join([label,text]))
        f.write("\n")

def merge(f,files):
    for fi in files:
        fr = file(fi,'r')
        text = "".join(fr.readlines())
        text = text.replace("\n","")
        text = text.replace("\t","")
        f.write(text+"\n")
        
f = file("D:/trainset.txt",'w')
paths = "D:/sougou"
for path_name in os.listdir(paths):
    basename = os.path.basename(paths+"/"+path_name)
    label = str(float(basename[1:]))
    files = os.listdir(paths+"/"+path_name)
    for i in range(len(files)):
        files[i]=paths+"/"+path_name+"/"+files[i]
    merge(f,files)
    
f.close()

    
