#开始使用该系统。

# Introduction #

系统可以直接在Linux下调用，也可以直接调用源代码


# Details #


  1. 要下载该软件可以通过svn命令将源代码check out到本地，`svn checkout http://tmsvm.googlecode.com/svn/trunk/ tmsvm`。  也可以通过svn软件直接操作，见下面的教程 http://sae.sina.com.cn/?m=devcenter&catId=212。  或者是在http://code.google.com/p/tmsvm/downloads/list 页面将源代码下载下来。
  1. 下载程序说明文档，也在下载页面。
  1. 在src/example.py为示例程序，可以通过那里的程序直接调用函数
  1. 如果想使用LSA部分，请把必备的scipy和numpy安装上，见[install\_Scipy\_Numpy\_on\_Ubuntu](install_Scipy_Numpy_on_Ubuntu.md)，如果不适用可以跳过这一步
  1. OK，这些操作完成以后，就可以按照你的程序要求修改程序或者是使用，Good Luck。

## 调用示例 ##
该系统可以在命令行（Linux或cmd中）中直接使用，也可以在程序通过直接调用源程序使用。
在程序中使用。
```
import tms

//对data文件夹下的binary_seged.train文件进行训练。
tms.tms_train(“../data/binary_seged.train”) 

//利用已经训练好的模型，对对data文件夹下的binary_seged.test文件预测
tms.tms_predict(“../data/binary_seged.test”,”../model/tms.config”)

//对预测的结果进行分析，评判模型的效果
tms. tms_analysis(“../tms.result”)
```
在命令行中调用
```
//对data文件夹下的binary_seged.train文件进行训练。
$python auto_train.py [options]  ../data/binary_seged.train

//利用已经训练好的模型，对对data文件夹下的binary_seged.test文件预测
$python predict.py ../data/binary_seged.train ../model/tms.config

//对预测的结果进行分析，评判模型的效果
$python result_anlaysis.py ../tms.result
```
上面的调用形式都是使用系统中默认的参数，更具体、灵活的参数见程序调用接口

有问题或者是建议，请联系 zhzhl202@163.com