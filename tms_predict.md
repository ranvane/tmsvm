# Introduction #

对SVM模型预测部分进行详解


# Details #


### 说明 ###
此函数为文本SVM分类模型预测程序，给定测试文本及设置相应参数，即可为样本进行预测。
### 调用示例 ###
usage:%prog `[options]` filename dic\_path model\_path

完整形式：
python tms\_predict.py -f ../ sample.test -R ../ result/score.result -i 1,2
-D ../model/dic.key -M ../model/tms.model -r 0,1,2

其含义为对sample.test 中的第1,2列(列从0开始，1,2要融合在一起)进行预测，结果放在score.result文件中，其中第一列为分数，其余列为指定的第0，1,2列。指定词典以及训练好的模型。


### 结果 ###
预测的结果会写入到指定的文件中。其中第一列为预测的分数。其余列为指定的需要同结果一同输出的内容。
### 参数说明 ###
  1. -i，--indexes,输入文本中训练的模型的部分（从0开始编号），默认为1，输入时可用 –i 1,2,3 表示使用第1,2,3作为训练的内容
  1. -r，----result\_indexes。指定与预测分数一块输出的文本的指标项，其中预测分数放在第一列，其余的依次排列。默认为1，调用方式为 –r 1,2,3
  1. -R,--result\_save 。结果保存的路径及文件名称。
  1. -T，--tc\_splitTag。训练文本中各部分分割的符号，默认为”\t”
  1. -S,--str\_splitTag.训练文本中分词的分割词，默认为”^”