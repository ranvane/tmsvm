# Introduction #

ref:http://www.cnblogs.com/LeftNotEasy/archive/2011/05/29/2062324.html


# Details #

Scipy在Ubuntu下的安装

  1. 下载scipy与numpy的package
> > http://www.scipy.org/Download#head-e68e4e32955ab584e1ac94e2b767f00179eac137
  1. sudo apt-get install libatlas-sse2-dev（科学计算库）
  1. sudo apt-get install gfortran（编译器）
  1. 执行下面的命令：
    * export BLAS=/path/to/libblas.so
    * export LAPACK=/path/to/liblapack.so
    * export ATLAS=/path/to/libatlas.so
> > > 在安装libatlas-sse2-dev2后，libblas.so的路径为：/usr/lib/sse2/atlas/
  1. 进入numpy的目录, 执行（安装numpy）
    * python setup.py build --fcompiler=gnu95
    * sudo python setup.py install --prefix=/usr/local
  1. 进入scipy的目录，执行下面相同的命令
    * python setup.py build --fcompiler=gnu95
    * sudo python setup.py install --prefix=/usr/local