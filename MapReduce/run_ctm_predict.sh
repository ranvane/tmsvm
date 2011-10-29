#--------------------------------------------------------------------------------
#[Subject   --  (CTM Predict)  Tbso Hadoop streaming 
#[Author    --  zhangzhilin.pt]
#[Created   --  2011.09.15]
#[Update    --  ]
#[UpAuthor  --  ]
#[Comment   --  2011.09.15     +first commit ]
#--------------------------------------------------------------------------------

#!/bin/bash

source /home/tbso/conf/set_env.sh
source /home/tbso/conf/common_tables.sh
source /home/tbso/conf/common_utils.sh

# step2 :predict post score :

INPUT=/group/tbso-dev/minzhi.cr/tmp/zhangzhilin
OUTPUT=${YUNTI_RESULT}/CTM_Predict/20111022

$HADOOP fs -rmr ${OUTPUT}

main_path=/home/minzhi.cr/bangpai/zhangzhilin/MapReduce_src/model
$HADOOP jar $STREAMINGJAR -D mapred.job.name='CTM_Predict' \
    -D mapred.reduce.tasks=1 \
    -files hstream.py,libsvm.so.2,MR_ctm_predict_config.py,MR_ctm_predict.py,svm.py,svmutil.py,\
    	${main_path}/weijin_all_kinds_title.key,${main_path}/weijin_all_kinds_title_content.key,\
			${main_path}/weijin_big_kinds_title.key,${main_path}/weijin_big_kinds_title_content.key,\
			${main_path}/weijin_danger_title.key,${main_path}/weijin_danger_title_content.key,\
			${main_path}/weijin_all_kinds_title.model,${main_path}/weijin_all_kinds_title_content.model,\
			${main_path}/weijin_big_kinds_title.model,${main_path}/weijin_big_kinds_title_content.model,\
			${main_path}/weijin_danger_title.model,${main_path}/weijin_danger_title_content.model \
    -mapper "MR_ctm_predict.py -m" \
    -reducer org.apache.hadoop.mapred.lib.IdentityReducer \
    -input ${INPUT} \
    -output ${OUTPUT}

#$HADOOP fs -cat ${OUTPUT}/* > ${JOB_DIR}/test_result.txt
