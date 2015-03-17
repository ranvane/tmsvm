<div id="maincol">

<table width="100%">
 <tbody><tr class="pscontent">
 <td class="pscolumnl">

 <div class="phead">Project Information</div>

 <div class="psicon">
 <div class="psicon-container goog-inline-block">
 ![](https://ssl.gstatic.com/codesite/ph/images/star_off.gif "Click to star project")
 </div>
 <span>
 Starred by <span id="star_count">59</span>&nbsp;user<span id="plural">s</span>
 </span>
 </div> 

*   [Project feeds](/p/tmsvm/feeds)
**   **Code license**
*   [GNU GPL v3](http://www.gnu.org/licenses/gpl.html)
**   <span id="project_labels">
 **Labels**

 [TextClassification](/hosting/search?q=label:TextClassification), [svm](/hosting/search?q=label:svm), [TextMining](/hosting/search?q=label:TextMining), [LSA](/hosting/search?q=label:LSA), [FeatureSelection](/hosting/search?q=label:FeatureSelection), [FeatureExtraction](/hosting/search?q=label:FeatureExtraction), [DimensionReducing](/hosting/search?q=label:DimensionReducing)
 </span>
*
 <div class="psicon">
 <div class="psicon-container goog-inline-block">
 <div style="float:right" class="SPRITE_people-y16 goog-inline-block vt"></div>
 </div>
 <span>**Members**</span>
 </div>

 [zhzhl202@gmail.com](/u/zhzhl202@gmail.com/)*   [2 committers](people/list)
*

 </td>
 <td id="wikicontent" class="psdescription">

## <a name="相信你也会对作者其它的项目感兴趣"></a>相信你也会对作者其它的项目感兴趣[](#相信你也会对作者其它的项目感兴趣)

1.  想从自由文本中找出一些有意义的词语吗？企业名称？商标名称？那就试试[EntNER](https://code.google.com/p/entner/)-基于统计与HMM的命名识别工具2.  不想手动收集训练集？想借助Google帮忙，那就选择[FineSearch](https://code.google.com/p/fine-searcher/)解析Google、Baidu等搜索引擎结果页面，并解析得到正文文本。

## <a name="特别提示"></a>特别提示[](#特别提示)

1.  Linux下用户请从Downloads中找到for_linux版本进行下载，不用通过svn获取2.  Linux下的版本已经不支持liblinear,如果有特别需要的,可以直接联系我

## <a name="简介"></a>简介[](#简介)

**文本挖掘**无论在学术界还是在工业界都有很广泛的应用场景。而**文本分类**是文本挖掘中一个非常重要的手段与技术。现有的分类技术都已经非常成熟，SVM、KNN、Decision Tree、AN、NB在不同的应用中都展示出较好的效果，前人也在将这些分类算法应用于文本分类中做出许多出色的工作。但在实际的商业应用中，仍然有很多问题没有很好的解决，比如文本分类中的**高维性**和**稀疏性**、类别的**不平衡**、**小样本**的训练、**Unlabeled样本**的有效利用、如何选择最佳的训练样本等。这些问题都将导致**curve of dimension ** 、 **过拟合**等问题。 这个开源系统的目的是集众人智慧，将文本挖掘、文本分类前沿领域效果非常好的算法实现并有效组织，形成一条完整系统将文本挖掘尤其是文本分类的过程自动化。该系统提供了Python和Java两种版本。 

### <a name="主要特征"></a>主要特征[](#主要特征)

该系统在封装** libsvm **、** liblinear **的基础上，又增加了** 特征选择 **、** LSA特征抽取 **、** SVM模型参数选择 **、** libsvm格式转化模块 ** 以及一些实用的工具。其主要特征如下： 

1.  **封装**并完全**兼容*libsvm、liblinear。 **
2.  **基于**Chi*的**feature selection** 见  [feature_selection](/p/tmsvm/wiki/feature_selection)3.  基于**Latent Semantic Analysis** 的**feature extraction** 见  [feature_extraction](/p/tmsvm/wiki/feature_extraction)4.  支持Binary,Tf,log(tf),Tf*Idf,tf*rf,tf*chi等多种**特征权重** 见 [feature_weight](/p/tmsvm/wiki/feature_weight)5.  文本特征向量的**归一化** 见 [Normalization](/p/tmsvm/wiki/Normalization)6.  利用**交叉验证**对SVM模型**参数自动选择**。 见  [SVM_model_selection](/p/tmsvm/wiki/SVM_model_selection)7.  支持macro-average、micro-average、F-measure、Recall、Precision、Accuracy等**多种评价指标 **见[evaluation_measure](/p/tmsvm/wiki/evaluation_measure)8.  支持**多个SVM模型**同时进行模型预测9.  采用python的csc_matrix支持存储大稀疏矩阵。10.  引入第三方分词工具自动进行分词11.  将文本直接转化为libsvm、liblinear所支持的格式。

### <a name="使用该系统可以做什么"></a>使用该系统可以做什么[](#使用该系统可以做什么)

1.  对文本**自动**做SVM模型的**训练**。包括Libsvm、Liblinear包的选择，分词，词典生成，特征选择，SVM参数的选优，SVM模型的训练等都可以一步完成。2.  利用生成的模型对未知文本做**预测**。并返回预测的标签以及该类的隶属度分数。可自动识别libsvm和liblinear的模型。3.  自动**分析**预测结果，**评判模型效果**。计算预测结果的F值、召回率、准确率、Macro,Micro等指标，并会计算特定阈值、以及指定区间所有阈值下的相应指标。4.  **分词**。对文本利用mmseg算法对文本进行分词。5.  **特征选择**。对文本进行特征选择，选择最具代表性的词。6.  **SVM参数的选择**。利用交叉验证方法对SVM模型的参数进行识别，可以指定搜索范围，大于大数据，会自动选择子集做粗粒度的搜索，然后再用全量数据做细粒度的搜索，直到找到最优的参数。对libsvm会选择c,g(gamma)，对与liblinear会选择c。7.  对文本直接生成libsvm、liblinear的输入格式。libsvm、liblinear以及其他诸如weka等数据挖掘软件都要求数据是具有向量格式，使用该系统可以生成这种格式：label index:value8.  SVM模型训练。利用libsvm、liblinear对模型进行训练。9.  利用**LSA对进行Feature Extraction*，从而提高分类效果。 **

## **<a name="开始使用"></a>开始使用[](#开始使用)**

**[QuickStart](/p/tmsvm/wiki/QuickStart)里面提供了方便的使用指导 **

## <a name="如何使用"></a>如何使用[](#如何使用)

该系统可以在命令行（Linux或cmd中）中直接使用，也可以在程序通过直接调用源程序使用。 在程序中使用。 
<pre class="prettyprint"><span class="com">#将TMSVM系统的路径加入到Python搜索路径中</span><span class="pln">
</span><span class="kwd">import</span><span class="pln"> sys
sys</span><span class="pun">.</span><span class="pln">path</span><span class="pun">.</span><span class="pln">insert</span><span class="pun">(</span><span class="lit">0</span><span class="pun">,</span><span class="pln">yourPath</span><span class="pun">+</span><span class="str">"\tmsvm\src"</span><span class="pun">)</span></pre><pre class="prettyprint"><span class="kwd">import</span><span class="pln"> tms

</span><span class="com">#对data文件夹下的binary_seged.train文件进行训练。</span><span class="pln">
tms</span><span class="pun">.</span><span class="pln">tms_train</span><span class="pun">(“../</span><span class="pln">data</span><span class="pun">/</span><span class="pln">binary_seged</span><span class="pun">.</span><span class="pln">train</span><span class="pun">”)</span><span class="pln"> 

</span><span class="com">#利用已经训练好的模型，对对data文件夹下的binary_seged.test文件预测</span><span class="pln">
tms</span><span class="pun">.</span><span class="pln">tms_predict</span><span class="pun">(“../</span><span class="pln">data</span><span class="pun">/</span><span class="pln">binary_seged</span><span class="pun">.</span><span class="pln">test</span><span class="pun">”,”../</span><span class="pln">model</span><span class="pun">/</span><span class="pln">tms</span><span class="pun">.</span><span class="pln">config</span><span class="pun">”)</span><span class="pln">

</span><span class="com">#对预测的结果进行分析，评判模型的效果</span><span class="pln">
tms</span><span class="pun">.</span><span class="pln"> tms_analysis</span><span class="pun">(“../</span><span class="pln">tms</span><span class="pun">.</span><span class="pln">result</span><span class="pun">”)</span></pre>

在命令行中调用 
<pre class="prettyprint"><span class="com">#对data文件夹下的binary_seged.train文件进行训练。</span><span class="pln">
$python auto_train</span><span class="pun">.</span><span class="pln">py </span><span class="pun">[</span><span class="pln">options</span><span class="pun">]</span><span class="pln"> &nbsp;</span><span class="pun">../</span><span class="pln">data</span><span class="pun">/</span><span class="pln">binary_seged</span><span class="pun">.</span><span class="pln">train

</span><span class="com">#利用已经训练好的模型，对对data文件夹下的binary_seged.test文件预测</span><span class="pln">
python predict</span><span class="pun">.</span><span class="pln">py </span><span class="pun">../</span><span class="pln">data</span><span class="pun">/</span><span class="pln">binary_seged</span><span class="pun">.</span><span class="pln">train </span><span class="pun">../</span><span class="pln">model</span><span class="pun">/</span><span class="pln">tms</span><span class="pun">.</span><span class="pln">config

</span><span class="com">#对预测的结果进行分析，评判模型的效果</span><span class="pln">
$python result_anlaysis</span><span class="pun">.</span><span class="pln">py </span><span class="pun">../</span><span class="pln">tms</span><span class="pun">.</span><span class="pln">result</span></pre>

上面的调用形式都是使用系统中默认的参数，更具体、灵活的参数见程序调用接口 

## <a name="输入格式"></a>输入格式[](#输入格式)

<tt>label value1 [value2]</tt> 

1.  其中label是定义的类标签，如果是binary classification，建议positive样本为1，negative样本为-1。如果为multi-classification。label可以是任意的整数。2.  其中value为文本内容。3.  label 和value以及value1 和value2之间需要用特殊字符进行分割，如”\t”

## <a name="模型输出"></a>模型输出[](#模型输出)

*   模型结果会放在指定保存路径下的“model”文件夹中，里面有3个文件，默认情况下为dic.key 、 tms.model和tms.config 。

1.  其中dic.key为特征选择后的词典；2.  tms.model为训练好的SVM分类模型;3.  tms.config为模型的配置文件，里面记录了模型训练时使用的参数。*   临时文件会放在“temp”文件夹中。里面有两个文件：tms.param和tms.train。

## <a name="源程序说明"></a>源程序说明[](#源程序说明)

1.  src:即该系统的源代码，提供了5个可以在Linux下可以直接调用的程序:auto_train.py、train.py、predict.py为在Linux下通过命令行调用的接口。2.  tms.py 为在程序中调用的主文件，直接通过import tms 即可调用系统的所有函数。其他文件为程序中实现各个功能的文件。3.  lsa_src：LSA模型的源程序。4.  dependence:系统所依赖的一些包。包括libsvm、liblinear、Pymmseg在Linux32位和64位以及windows下的支持包(dll,so文件)。5.  tools:提供的一些有用的工具，包括result_analysis.py等。6.  java：java版本的模型预测程序，

## <a name="项目重要更新日志"></a>项目重要更新日志[](#项目重要更新日志)

*   2012/09/21 针对linux下的bug进行修正。重新生成win和linux版本的。*   2012/03/08 增加stem模块，并修正了几个Bug。*   2011/11/22 tmsvm正式发布。

## <a name="联系方式"></a>联系方式[](#联系方式)

邮箱:zhzhl202@163.com 

## <a name="Thanks"></a>Thanks[](#Thanks)

本系统引用了libsvm、liblinear的包，非常感谢Chih-Jen Lin写出这么优秀的软件。本系统还引用了Pymmseg，非常感谢pluskid能为mmseg写出Python下可以直接使用的程序 

从最初的想法萌生到第一版上线，中间试验了很多算法，最终因为效果不好删掉了很多代码，在这期间得到了许多人的帮助，非常感谢杨铮、江洋、敏知、施平等人的悉心指导。特别感谢丽红一直以来的默默支持。   

# <a name="English_Version"></a>English Version[](#English_Version)

A text mining system based on svm.This system focus on text classification based on the libsvm and liblinear, especially some key issues in text classification,for example high dimensionality , text vector sparse, unbalance training sample and so on. This system aim to build a complete system on all aspect in text mining by realizing some mature algorithm . This system has show outstanding effects in reality using,especially in information filtering problem 

 </td>
 </tr>
</tbody></table>
<script src="https://ssl.gstatic.com/codesite/ph/17435595315869588898/js/prettify/prettify_core_compiled.js"></script>
<script type="text/javascript">
 prettyPrint();
</script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/17435595315869588898/js/ph_core.js"></script>

</div>
