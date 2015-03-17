# Introduction #

auto\_tms\_train.py 模块的使用详解


# Details #

### 说明 ###
此函数为文本SVM分类模型自动训练程序，给定训练文本及设置相应参数，即可得到训练好的模型。
### 调用方法 ###
usage:%prog `[options]` filename

### 输入格式 ###

`label value1 [value2]`

  1. 其中label是定义的类标签，如果是binary classification，建议positive样本为1，negative样本为-1。如果为multi-classification。label可以是任意的整数。
  1. 其中value必须为已经分好词的文本。可以利用ICTCLAS等分词工具预先对文本进行分词。
  1. 文本为UTF-8格式

### 参数说明 ###

  1. -p，--path，模型保存的路径。默认为 ”../”
  1. -i，--indexes,输入文本中训练的模型的部分（从0开始编号），默认为[1](1.md)，输入时可用     –i 1,2,3 表示使用第1,2,3作为训练的内容
  1. -w，(布尔型)如果使用此参数代表词典中不去除停用词。如果使用，必须将停用词文件以stopwords.txt 命名，和训练文本放在同一路径下。默认情况下不使用此参数，即需将停用词文件stopwords.txt放在训练文本同一路径下
  1. -A ,--tms\_param。即SVM训练的参数，完全兼容libtms，输入的格式为 –A “-s 0 –c 1.0 –g 0.25” 。为了避免和现在的参数相混淆，所以要加上双引号。
  1. -d，--dic\_name。指定特征选择后词典的名称,默认为dic.key
  1. -m, --model\_name,指定生成的分类模型的名称，默认为tms.model
  1. -t, --train\_name,指定生成的分类模型的名称，默认为tms.train
  1. -a, --param\_name,指定生成的分类模型的名称，默认为tms.param
  1. -r，--ratio。指定特征选择保留词的比例。默认为0.4
  1. -T，--tc\_splitTag。训练文本中各部分分割的符号，默认为”\t”
  1. -S,--str\_splitTag.训练文本中分词的分割词，默认为”^”

### 结果 ###
模型结果会放在“model”文件夹中，里面有两个文件，默认情况下为dic.key 和 tms.model 。其中dic.key为特征选择后的词典；tms.model为训练好的SVM分类模型。
临时文件会放在“temp”文件夹中。里面有两个文件：tms.param和tms.train。其中tms.param为SVM模型参数选择时所实验的参数。tms.train是供libtms训练器所使用的输入格式。

### Note ###
正常情况下，训练一个模型会经过特征选择，生成SVM输入格式，SVM参数选择，SVM模型训练这几个步骤。其中SVM参数选择将花费较长的时间(为了能训练出最好的模型，程序默认会进行两轮参数搜索，粗粒度和细粒度，共实验150对(c,g)，其中每对(c,g)都要经过4-flods的交叉验证。如果训练样本的个数在5000以下，整个模型的训练时间在十分钟左右，如果训练文本的数量级为万，则训练时间将达到几个小时。)。如果忍受不了这么长的时间。可以进行分步训练[tms\_train](tms_train.md)，或者是选择在晚上进行训练。

### 调用示例 ###
`$cat set.train`

1	<sup>台</sup>军<sup>人事</sup>大幅<sup>变动</sup>	<sup>据</sup>台湾<sup>东森</sup>新闻<sup>报道	</sup>台<sup>军</sup>将领<sup>将</sup>有<sup>大</sup>调动^……

1 朝鲜<sup>已经</sup>准备<sup>好</sup>对<sup>美国</sup>进行<sup>先发制人</sup>的<sup>打击	</sup>朝鲜<sup>人民</sup>武装<sup>力量</sup>部<sup>部长</sup>金一<sup>哲</sup>次帅<sup>4月</sup>8日<sup>在</sup>平壤<sup>公开</sup>表示……

1 <sup>伊朗</sup>开始<sup>大规模</sup>投产<sup>地对空导弹	报道</sup>还<sup>援引</sup>伊朗<sup>国防</sup>部长<sup>穆斯塔法</sup>•<sup>穆罕默德</sup>•<sup>纳贾尔</sup>话说……
……

-1 五一<sup>期间</sup>外出<sup>旅游</sup>人数<sup>仍然</sup>保持<sup>上升</sup>趋势	记者<sup>在</sup>甘肃<sup>、</sup>宁夏<sup>两</sup>省<sup>采访</sup>时<sup>发现</sup>……

-1 承德<sup>避暑山庄</sup>永佑<sup>寺</sup>全新<sup>的</sup>面貌<sup>与</sup>游客<sup>“</sup>见面	<sup>记者</sup>从<sup>承德市</sup>旅游局<sup>获悉</sup>，<sup>目前</sup>永佑<sup>寺</sup>内<sup>“</sup>陆<sup>合</sup>塔……

-1 强迫<sup>购物</sup>、<sup>强迫</sup>参加<sup>自费</sup>活动	许多<sup>游客</sup>游<sup>完</sup>泰国<sup>回来</sup>总会<sup>表示</sup>不满<sup>。</sup>“<sup>去</sup>之前<sup>交</sup>一次^团费……
……

训练文本总共有两类，每行代表一类的样本，总共有3个字段，第一个字段为类别，第二个类别为标题，第3个字段为内容。标号为1的类为军事类，-1的为旅游类。

#### 对标题+内容训练 ####

  1. 完整形式：
$Python  auto\_tms\_train.py  –p ../ -i 1,2 –w –d dic.key
–m im.model  -t tms.train –a tms.param –r 0.4 –S ^  ../set.train
  1. 精简形式：
python auto\_tms\_train.py   -i 1,2 ../set.train