# Introduction #

Add your content here.


# Details #


### 说明 ###
此函数为LSA模型训练程序，给定测试文本及训练好的SVM模型和词典的长度，即可为LSA模型进行训练。
LSA模型虽然在实际实验中没有得到预想的效果，但是在某些场景下应该会有用，所以LSA模型训练与预测的程序仍然保留。
### 调用示例 ###
usage:%prog [options](options.md) filename svm\_model M

完整形式：
python lsa\_tms\_train.py -f ../ sample.test -R ../ result/score.result -i 1,2
-D ../model/dic.key -M ../model/tms.model -r 0,1,2
其含义为对sample.test 中的第1,2列(列从0开始，1,2要融合在一起)进行预测，结果放在score.result文件中，其中第一列为分数，其余列为指定的第0，1,2列。指定词典以及训练好的模型。

### 参数说明 ###
  1. -p，--path，模型保存的路径，默认情况下为”../”
  1. -e, --threshold 。LSA模型选取top n阈值。默认情况下为1.0
  1. -K,--K  。选取的前k个特征根。
  1. -f,--for\_lsa\_train 。SVM模型预测训练文本，并构造适合LSA模型的训练文本。默认为“for\_lsa.train”
  1. -t,--train\_name；LSA模型做出的SVM训练文本格式,默认为“lsa.train”
  1. -m,--model\_name；LSA模型的名称.默认为“lsa.model”
  1. -A,--tms\_param；即SVM训练的参数，完全兼容libtms，输入的格式为 –A “-s 0 –c 1.0 –g 0.25” 。为了避免和现在的参数相混淆，所以要加上双引号。默认为“-s 0 –c 1.0 –g 0.25”
  1. -a, --param\_name,指定生成的分类模型的名称，默认为tms.param