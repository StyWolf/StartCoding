Shell文本处理——cut
##########

>cut命令是Linux下用于切割文本行非常有用的一个简单命令，学习Linux命令一定要善用man和info。  
<!--more-->
###<a name="NAMEs">一、cut介绍</a>

**从`man cut`中可以知道cut命令就是从行中剪切一部分出来，这和cut的表面意思非常的像。但是cut也并不仅仅局限于行。cut可以从文件中剪切也可以从文本流中剪切出一部分来。**

###<a name="options">二、cut命令用法和常用参数</a>  
####1、cut命令用法
######	cut OPTION... [FILE]...
######用法非常的简单cut 命令后直接跟参数和文件或者通过管道把标准输出通过管到给cut

####2、cut常用参数
**Linux的命令参数大多数都有长参数和短参数两种**  
`例如：按照字节进行定位操作`  
`-b, --bytes=LIST`  //长短均可

**cut命令常用剪切用法有三种：字节（byte）、字符（characters）、字段（fields）**  
```python
1、字节（byte）：-b, --bytes
2、字符（characters）：-c, --characters
3、字段（fields）：-f, --fields
```
**其他剪切方法：**  
```python
1、分隔符（默认为TAB）: -d, --delimiter
2、常常表示具体数字：-n
3、不包括不含分隔符的行 ： -s, --only-delimited
4、帮助 ： --help	
5、版本 ： --version
```  
####3、范围的表示方法
```python
N
 只有第N项

 N-
  从第N项一直到行尾
   
  N-M
   从第N项到第M项(包括M)
    
   -M
    从一行的开始到第M项(包括M)
	 
	-
	- 从一行的开始到结束的所有项
	- ```
	-
	- ###<a name="example">三、cut命令实例</a> 
	-
	- **之前一直纠结去拿找实例去练习，后台发现Linux本身就有大量的实例啊，各种配置文件都可以,最好找有规律的比如`ls -l`命令的**
	-
	- #####1、按字节 ： -b
	- ```python
	- $ date
	- 2014年 11月 05日 星期三 11:45:35 CST
	- #选取前面4个字节2014
	- $ date | cut -b 1-4
	- 2014
	- #空格算一个字节，汉字占3个字节
	- #剪切 星期三
	- $ date | cut -b 20-29
	- #多个字节剪切，用逗号隔开
	- #剪切2014和05
	- $ date | cut -b 1-4,15-16
	- 201405
	- ```   
	- #####2、按字符：-f
	- ```python
	- #按字符和按字节差不多，就是空格和汉字都算作一个字符
	- #剪切星期三
	- $ date | cut -c 14-17
	- 星期三
	- ```  
	- #####3、按字段：-f
	- **以下文件为例：test**
	- ```python
	- root:x:0:0:root:/root:/bin/bash
	- bin:x:1:1:bin:/bin:/sbin/nologin
	- daemon:x:2:2:daemon:/sbin:/sbin/nologin
	- adm:x:3:4:adm:/var/adm:/sbin/nologin
	- lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
	- ```  
	- ```python
	- #我们先要一下前面的用户
	- $ cut -d ":" -f 1 test.md
	- cut-test.md
	- root
	- bin
	- daemon
	- adm
	- lp
	- ###-d 参数指定字段分隔符，默认是一TAB来分隔的，这里指定以冒号：来分隔。-f 就是我们按照分隔符分好后的字段
	-
	- #剪切用户和shell
	- $ cut -d ":" -f 1,7 cut-test.md
	- root:/bin/bash
	- bin:/sbin/nologin
	- daemon:/sbin/nologin
	- adm:/sbin/nologin
	- lp:/sbin/nologin
	- ```  
	- ```python
	- #来让我们玩一下 -s 这个参数
	- #创建一个文件类似于这样的：
	-
	- ###-s 参数测试
	-
	- a1	a2	a3	a4
	- b1	b2	b3	b4
	- c1	c2	c3	c4
	- d1    d2    d3    d4
	-
	- #第一行没有TAB，abc三行中间是TAB间隔符，d行是空格间隔符
	- $ cut -f 1-4 -s  cut-test1.md
	- a1	a2	a3	a4
	- b1	b2	b3	b4
	- c1	c2	c3	c4
	-
	- #看到上面只输出了abc三行，而第一行和d行被删除了，因为只有abc三行是TAB间隔符的，-s就是剪切出符合-f规则的字段。
	- ```
	-
	- ###当然了，cut一般我们只用来处理一些有规律的文件，比如说日志什么的，有时候自己拼接出间隔符然后再用cut也不错。
	-
	-
