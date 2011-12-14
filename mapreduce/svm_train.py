#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import sys
sys.path.append('.')
from hstream import *
import tms_svm

def read_param(filename):
    params=list()
    for line in file(filename):
        params.append(line.strip())
    return params

default_param_file="./params"
params = read_param(default_param_file)

class SvmTrain(HStream):
    '''input 为SVM训练需要的数据'''

#    def __init__(self,param_file=default_param_file):
#        pass
#        self.parse_args()
#        print self.default_param_file
#        self.param_file=param_file
#        self.params = self.read_param(self.param_file)

    def mapper(self,key, value):
        '''mapper function'''
        for param in params:
            self.write_output( param, value )

    def reducer(self, key, values):
        '''reducer function'''
        prob_y=[]
        prob_x=[]
        c,g=key.split()
        for value in values:
            line = line.split(None,1)
            if len(line)==1: line+=['']
            label, features = line
            xi={}
            for e in features.split():
                ind, val = e.split(":")
                xi[int(ind)] = float(val)
            prob_y +=[float(label)]
            prob_x +=[xi]
        self.write_output( key, str(length))
    
#    def parse_args(self):
#        parser = OptionParser(usage="")
#        parser.add_option("-p", "--paramFile",help="param filename",dest="paramFile")
#        options,args = parser.parse_args()
#        if options.paramFile:
#            self.default_param_file=options.paramFile
        

    
if __name__ == '__main__':
	SvmTrain()
