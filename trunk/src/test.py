#!/usr/bin/python
#_*_ coding: utf-8 _*_
#author: 张知临 zhzhl202@163.com
import tms
#tms.tms_train("../data/weijin.train",indexes=[4],main_save_path="../model/",stopword_filename="../data/stopwords.txt",svm_type="liblinear",config_name="linear_title.config",dic_name="linear_title.key",model_name="linear_title.model",train_name="linear_title.train",param_name="linear_title.param",ratio=0.4,seg=1,local_fun="tf",global_fun="rf")
#tms.tms_predict_multi("../data/weijin.test",config_files=["../model/model/linear_title.config"],indexes_lists=[[4]],result_save_path="../result/linear_title.result",result_indexes=[0],seg=1)
#tms.tms_analysis("../result/linear_title.result",step=4,output_file="../data/linear_title.analysis",indexes=[0,1,2],predicted_label_index=0,predicted_value_index=1,true_label_index=2,min=0,max=2)=======
#import tms
#tms.tms_predict_multi("../data/weijin.test", ["../data/aliws/model/lineartitle.config","../data/aliws/model/lineartitle_content.config","../data/aliws/model/svmtitle.config","../data/aliws/model/svmtitle_content.config"],[[2],[2,3],[2],[2,3]],result_indexes=[0,1,2,3,4],result_save_path="../data/weijin.result")>>>>>>> .r167

tms.tms_train("../data/weijin_ik_2012_1_10.txt",indexes=[4,5],main_save_path="../model/weijin_12_1_10/",stopword_filename="../data/stopwords.txt",svm_type="liblinear",config_name="weijin_ik_20120110.config",dic_name="weijin_ik_20120110.key",model_name="weijin_ik_20120110.model",train_name="weijin_ik_20120110.train",param_name="weijin_ik_20120110.param",ratio=0.4,seg=0,local_fun="tf",global_fun="rf")