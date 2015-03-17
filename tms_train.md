# Introduction #

文本SVM分类模型训练使用详解.参数、用法等


# Details #

### 说明 ###
此函数为文本SVM分类模型训练程序，与auto\_tms\_train.py不同的是，该函数可以使模型训练分步进行。
### 调用示例 ###
usage:%prog `[options]` filename
filename 在步骤(-s )1,2,3中代表输入训练文本，在步骤(-s)4,5中代表SVM的输入格式数据。

  * #### 自动进行模型训练 ####
完整形式
python tms\_train.py  -s 1 –p ../ -i 1 –w –d dic.key
–m im. model -t tms.train –a tms.param –r 0.4 –S <sup> -T </sup>M  ../im.train
精简形式：
python tms\_train.py –s 1 –p ../ -i 1 ../im.train

  * #### 特征选择 ####
完整形式：
python tms\_train.py  -s 2 –p ../ -i 1 –d dic.key
–r 0.4 –S ^  ../im.train
精简形式
python tms\_train.py  -s 2 –p ../ -i 1  ../im.train

  * #### 生成SVM模型的输入格式 ####
完整形式：
python tms\_train.py  -s 3 –p ../ -i 1 –D ../dic.key
–S ^  ../im.train
简洁形式：
python tms\_train.py  -s 3 –p ../ -i 1 –D ../dic.key  ../im.train

  * #### SVM模型的参数选择 ####
完整形式：
python tms\_train.py  -s 4 –p ../  -P ../tms.train
其中tms.train 为第3步生成的SVM模型的输入格式

  * #### 模型训练 ####
完整格式：
python tms\_train.py  -s 5 –p ../ -P ../tms.train –A “-c 0 –t 2”


### 输入格式 ###

`label value1 [value2]`

  1. 其中label是定义的类标签，如果是binary classification，建议positive样本为1，negative样本为-1。如果为multi-classification。label可以是任意的整数。
  1. 其中value必须为已经分好词的文本。可以利用ICTCLAS等分词工具预先对文本进行分词。
  1. 文本为UTF-8格式


### 参数说明 ###
  1. -s ,--step,即选择要进行的操作。1为自动训练模型，即auto\_tms\_train.py的功能。2为特征选择。3为根据训练样本生成SVM的输入格式。4为SVM模型参数选择；5为SVM训练
  1. -p，--path，模型保存的路径，默认情况下为”../”
  1. -i，--indexes,输入文本中训练的模型的部分（从0开始编号），默认为[1](1.md)，输入时可用 –i 1,2,3 表示使用第1,2,3作为训练的内容
  1. -w，(布尔型)如果使用此参数代表词典中不去除停用词。如果使用，必须将停用词文件以stopwords.txt 命名，和训练文本放在同一路径下。默认情况下不使用此参数，即需将停用词文件stopwords.txt放在训练文本同一路径下
  1. -A ,--tms\_param。即SVM训练的参数，完全兼容libtms，输入的格式为 –A “-s 0 –c 1.0 –g 0.25” 。为了避免和现在的参数相混淆，所以要加上双引号。默认为“-s 0 –c 1.0 –g 0.25”
  1. -d，--dic\_name。指定特征选择后词典的名称,默认为dic.key
  1. -D,--dic\_path。词典所在的路径及名称
  1. -m, --model\_name,指定生成的分类模型的名称，默认为tms.model
  1. -t, --train\_name,指定生成的分类模型的名称，默认为tms.train
  1. -a, --param\_name,指定生成的分类模型的名称，默认为tms.param
  1. -r，--ratio。指定特征选择保留词的比例。默认为0.4
  1. -T，--tc\_splitTag。训练文本中各部分分割的符号，默认为”\t” -S,--str\_splitTag.训练文本中分词的分割词，默认为”^”


### 结果 ###
模型结果会放在“model”文件夹中，里面有两个文件，默认情况下为dic.key 和 tms.model 。其中dic.key为特征选择后的词典；tms.model为训练好的SVM分类模型。