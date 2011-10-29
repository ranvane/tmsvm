#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Filename: post_check_new_config.py
import os.path
import time
import sys
sys.path.append('.')

#split tag between id,title,content,dd1,dd2
tc_splitTag="\t"
#split tag between single term after segment by Aliws
str_splitTag ="^"

#imodel_path="/home/minzhi.cr/bangpai/zhangzhilin/MapReduce_src/model/weijin_danger/"
dic_path_list = ["weijin_all_kinds_title.key","weijin_all_kinds_title_content.key", \
"weijin_big_kinds_title.key","weijin_big_kinds_title_content.key",\
"weijin_danger_title.key","weijin_danger_title_content.key"]
model_path_list = ["weijin_all_kinds_title.model","weijin_all_kinds_title_content.model",\
                   "weijin_big_kinds_title.model","weijin_big_kinds_title_content.model",\
                   "weijin_danger_title.model","weijin_danger_title_content.model"]
indexes_lists = [ [3],[3,4],[3],[3,4],[3],[3,4] ]
result_indexes=[0,1,2]
#模型的阈值，如果得分超过了阈值，则输出预测结果，对与binary classifier,返回的是预测分值，这里可以设置具体的阈值。
#对与multi classifier，返回的是预测标签，通常来说，各种违规类都大于0，所以这里可以设置大于0
#threholds = [0,0] 
