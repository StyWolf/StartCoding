###Shell文本处理——grep  
> grep 是一种强大的文本搜索工具，它基于正则表达式匹配并打印出匹配的行。也就是说grep就是linux下强大的行过滤工具。  

####TOC  
* grep 语法
* grep [options]主要参数
* grep pattern主要参数
* grep 实例练习  


####grep 基本语法
```
  grep [OPTIONS] PATTERN [FILE...]
  grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]
```
####grep [options]参数  
#####option参数类别
1.  匹配器的选择
2.  匹配控制
3.  通用输出控制
4.  文件和目录选择
5.  输出行前缀控制
6.  上下文控制
7.  其他参数  

#####1、匹配器的选择  
```
  -E, --extended-regexp     PATTERN 是一个可扩展的正则表达式(缩写为 ERE)
  -F, --fixed-strings       PATTERN 是一组由断行符分隔的定长字符串。
  -G, --basic-regexp        PATTERN 是一个基本正则表达式(缩写为 BRE)
  -P, --perl-regexp         PATTERN 是一个 Perl 正则表达式

  egrep和fgrep是Unix的grep RE扩展，Linux采用的应该是GNU的grep可以通过-E，-F来实现egrep和fgrep，并且linux的grep扩展更强可以通过-P来采用perl的RE正则匹配。
```  
_______________
#####2、匹配控制
```
 -e PATTERN, --regexp=PATTERN     用PATTERN来进行匹配操作,grep默认匹配规则，可以省略。
 -f FILE, --file=FILE             从 FILE 中取得 PATTERN 行
 -i, --ignore-case                忽略大小写
 -v, --invert-match               反转，选择不匹配的行
 -w, --word-regexp                PATTERN 仅完全匹配字词
 -x, --line-regexp                PATTERN 仅完全匹配一行
 -s, --no-messages                不显示出错信息
 -V, --version                    显示版本信息并退出
 --help                           显示grep帮助并退出
```  
#####3、通用输出控制
```
  -m, --max-count=NUM       NUM 次匹配后停止
  -b, --byte-offset         输出的同时打印字节偏移
  -n, --line-number         输出的同时打印行号
      --line-buffered       每行输出清空
  -H, --with-filename       为每一匹配项打印文件名
  -h, --no-filename         输出时不显示文件名前缀
      --label=LABEL         将LABEL 作为标准输入文件名前缀
  -o, --only-matching       仅显示匹配的部分
  -q, --quiet, --silent     不显示所有输出
  --binary-files=TYPE       假设二进制文件的TYPE类型
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                --binary-files=type
  -I                        --binary-files=without-match  
  -d, --directories=ACTION  操作目录的方法;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      操作设备、先入先出队列、套接字的方法;
                            ACTION is 'read' or 'skip'

  -r, --recursive           like --directories=recurse
  -R, --dereference-recursive
                            likewise, but follow all symlinks
    --include=FILE_PATTERN
                            search only files that match FILE_PATTERN
      --exclude=FILE_PATTERN
                            skip files and directories matching FILE_PATTERN
      --exclude-from=FILE   skip files matching any file pattern from FILE
      --exclude-dir=PATTERN directories that match PATTERN will be skipped.
  -L, --files-without-match 只打印不匹配 FILES 的文件名
  -l, --files-with-matches  只打印匹配 FILES 的文件名
  -c, --count               只打印每个 FILE 中的匹配行数目
  -T, --initial-tab         行首 tabs 分隔（如有必要）
  -Z, --null                在FILE文件最后打印空字符
```

#####4、文件控制
```
  -B, --before-context=NUM  打印以文本起始的NUM 行
  -A, --after-context=NUM   打印以文本结尾的NUM 行
  -C, --context=NUM         打印输出文本NUM 行
  -NUM                      same as --context=NUM
      --group-separator=SEP use SEP as a group separator
      --no-group-separator  use empty string as a group separator
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
   -U, --binary             不要清除行尾的CR 字符(MSDOS/WINDOWS)
   -u, --unix-byte-offsets  当CR 字符不存在，报告字节偏移(MSDOS/WINDOWS)
```  
#####5、输出行前缀控制
#####6、上下文控制
#####7、其他参数  
____________________________________
####grep pattern主要参数
grep 的匹配模式是正则表达式（RE）,这里只列出一些主要RE，具体的以后再写个完整的备忘RE。  

```
  \： 转义。忽略正则表达式中特殊字符的原有含义。
  ^： 匹配正则表达式的开始行。
  $:  匹配正则表达式的结束行。
  [ ]：单个字符，如[A]即A符合要求 。
  [ - ]：范围，如[A-Z]，即A、B、C一直到Z都符合要求。
  [^ ]:反向选择
  .：任意一个字节
  * ：重复字节。
  {}：限定连续 RE 字符范围
```

egrep和grep -E的元字符扩展
```
  +     匹配一个或多个先前的字符
  ?     匹配零个或多个先前的字符
  a|b|c 匹配a或b或c
  ()    分组符号
```  
________________________________________
####grep 实例练习  
```
#将/etc/passwd中的root行取出来
$ grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
operator:x:11:0:operator:/root:/sbin/nologin
或者从标准输出读入
$ cat /etc/passwd | grep root  

#将/etc/passwd中的root行取出来并显示行号并给关键字换个颜色显示
###显示关键字颜色是很好的功能，如果不想每次都加--color=auto，可以在～/.bashrc中添加 alias grep='grep --color=auto'
$ grep -n --color=auto root /etc/passwd
1:root:x:0:0:root:/root:/bin/bash
10:operator:x:11:0:operator:/root:/sbin/nologin

#将/etc/passwd中不是root的行显示出来
$ grep -v root /etc/passwd
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
oprofile:x:16:16:Special user account to be used by OProfile:/var/lib/oprofile:/sbin/nologin

#同时列出多个匹配
#将/etc/passwd中显示匹配root和nologin行
$ grep root /etc/passwd | grep nologin
operator:x:11:0:operator:/root:/sbin/nologin
```  

```
#来玩玩向前取几行和向后取几行
$ cat grep-test1.md
drwx------.   3 zhangjian zhangjian  4096 9月  19 12:22 .adobe/
-rw-------.   1 zhangjian zhangjian  7508 10月 19 00:43 .bash_history
-rw-r--r--.   1 zhangjian zhangjian    18 8月   9 2013 .bash_logout
drwxrwxr-x.   3 zhangjian zhangjian  4096 9月  19 15:39 .java/
-rw-r--r--    1 zhangjian zhangjian   297 10月 17 01:25 .bash_profile
-rw-r--r--.   1 zhangjian zhangjian   231 8月   9 2013 .bashrc
drwxrwxr-x    3 zhangjian zhangjian  4096 11月  1 22:18 .kingsoft/

#取出上面文件中含有drwxrwxr-x的行并标上行号和关键字颜色
$ grep -n --color drwxrwxr-x grep-test1.md
4:drwxrwxr-x.   3 zhangjian zhangjian  4096 9月  19 15:39 .java/
7:drwxrwxr-x    3 zhangjian zhangjian  4096 11月  1 22:18 .kingsoft

#取出含有drwxrwxr-x行的前两行和后一行
$ grep -n -A1 -B2 --color=auto drwxrwxr-x grep-test1.md
2--rw-------.   1 zhangjian zhangjian  7508 10月 19 00:43 .bash_history
3--rw-r--r--.   1 zhangjian zhangjian    18 8月   9 2013 .bash_logout
4:drwxrwxr-x.   3 zhangjian zhangjian  4096 9月  19 15:39 .java/
5--rw-r--r--    1 zhangjian zhangjian   297 10月 17 01:25 .bash_profile
6--rw-r--r--.   1 zhangjian zhangjian   231 8月   9 2013 .bashrc
7:drwxrwxr-x    3 zhangjian zhangjian  4096 11月  1 22:18 .kingsoft/

###可以看到第4行的前两行和后一行被取出了，这对调试信息很有用

#来练习在文件和目录中查找
$ grep 'linux' * #在当前目录下查找带有linux的行
$ grep -r 'linux' * #在当前目录及子目录中查找带有linux的行
$ grep -l -r 'linux' * #只显示含有linux行的文件名
####linux 的find命令也可以查找文件但是好像不能查找文件中内容，不是很清楚以后有时间尝试一下
```  
######grep正则匹配
```
#练习测试文件为鸟哥的范例文件
$ wget http://linux.vbird.org/linux_basic/0330regularex/regular_express.txt
#一、先来个最简单的查找字符
$ grep -n 'game' regular_express.txt
3:Football game is not use feet only.

#反转 不显示含有game的行
$ grep -vn 'game' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
4:this dress doesn't fit me.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
7:Her hair is very beauty.
8:I can't finish the test.
9:Oh! The soup taste good.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
13:Oh!	My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.
21:# I am VBird
22:

#练习一下忽略大小写-i
$ grep -in 'gnu' regular_express.txt
6:GNU is free air not free beer.

##二、[]查找字符集合
$ grep -n '[tb]est' regular_express.txt
8:I can't finish the test.
15:You are the best is mean you are the no. 1.
18:google is the best tools for search keyword.
#可以看到把含有test和best的行全部取出来，[]只选取其中一个

#取出有数字的行
$ grep -n '[0-9]' regular_express.txt
5:However, this dress is about $ 3183 dollars.
15:You are the best is mean you are the no. 1.\

#取出有大写字母的行
$ grep -n '[A-Z]' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
3:Football game is not use feet only.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
7:Her hair is very beauty.
8:I can't finish the test.
9:Oh! The soup taste good.
11:This window is clear.
13:Oh!	My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
20:go! go! Let's go.
21:# I am VBird

##三、行尾和行首字符^$
#让this出现在行首
$ grep -n '^this' regular_express.txt
4:this dress doesn't fit me.

#开头是小写字符的行
$ grep -n '^[a-z]' regular_express.txt
2:apple is my favorite food.
4:this dress doesn't fit me.
10:motorcycle is cheap than car.
12:the symbol '*' is represented as start.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.

#开头不是小写字符的行
$ grep -n '^[^a-z]' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
3:Football game is not use feet only.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
7:Her hair is very beauty.
8:I can't finish the test.
9:Oh! The soup taste good.
11:This window is clear.
13:Oh!	My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
21:# I am VBird
########这里的'^[^a-z]'第一个^表示行首，第二个^表示反向

#要尾数是.的那一行
$ grep -n '\.$' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
20:go! go! Let's go.

#取出空白行
$ grep -n '^$' regular_express.txt
22:
#去除空白行和注释
$ grep -vn '^$' regular_express.txt | grep -v '^#'

#####四、任意一个字符.和重复字符*
#查找含有g??d的行
$ grep -n 'g..d' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
9:Oh! The soup taste good.
16:The world <Happy> is the same with "glad".

#查找含有两个或两个以上o的行
$ grep -n 'oo*' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
4:this dress doesn't fit me.
5:However, this dress is about $ 3183 dollars.
6:GNU is free air not free beer.
9:Oh! The soup taste good.
10:motorcycle is cheap than car.
11:This window is clear.
12:the symbol '*' is represented as start.
13:Oh!	My god!
14:The gd software is a library for drafting programs.
15:You are the best is mean you are the no. 1.
16:The world <Happy> is the same with "glad".
17:I like dog.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.

#查找g和g之间仅能存在至少一个o
$ grep -n 'goo*g' regular_express.txt
18:google is the best tools for search keyword.
19:goooooogle yes!

#开头和结尾都是g的字符
$ grep -n 'g.*g' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
14:The gd software is a library for drafting programs.
18:google is the best tools for search keyword.
19:goooooogle yes!
20:go! go! Let's go.

#####.表示任意字符，*表示重复0个或多个前面RE字符的意思

#####五、限定连续RE字符的范围{}
#找到含有两个o的字符串
$ grep -n 'o\{2\}' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
9:Oh! The soup taste good.
18:google is the best tools for search keyword.
19:goooooogle yes!

#找到含有2-5个o的
$ grep -n 'o\{2,5\}' regular_express.txt
1:"Open Source" is a good mechanism to develop programs.
2:apple is my favorite food.
3:Football game is not use feet only.
9:Oh! The soup taste good.
18:google is the best tools for search keyword.
19:goooooogle yes!
```  

####扩展正则表达式egrep和grep -E
#####主要是增加了额外的正则表达式元字符集，也就是上面的扩展级中的几个元字符 + ？ | （）
```
##+匹配一个或多个
#查找至少一个数字的行
$ egrep -n '[0-9]+' regular_express.txt
或
$ grep -n -E '[0-9]+' regular_express.txt
或对于标准的grep,如果在扩展元字符前加\，grep会自动启用-E选项
$ grep -n '[0-9]\+' regular_express.txt
5:However, this dress is about $ 3183 dollars.
15:You are the best is mean you are the no. 1.

#找到含有ea和ee的行
$ grep -n -E 'ea|ee' regular_express.txt
3:Football game is not use feet only.
6:GNU is free air not free beer.
7:Her hair is very beauty.
10:motorcycle is cheap than car.
11:This window is clear.
15:You are the best is mean you are the no. 1.
18:google is the best tools for search keyword.

#找到g和d之间只含有0个或1个o
$ grep -n -E 'go?d' regular_express.txt
13:Oh!	My god!
14:The gd software is a library for drafting programs.

#搜索一个或者多个连续的no的行
$ grep -n -E '(no)+' regular_express.txt
3:Football game is not use feet only.
6:GNU is free air not free beer.
15:You are the best is mean you are the no. 1.
```  
#####fgrep的使用
fgrep查询速度好像比grep快，但是只能找固定的文本，而不是规则。
```
#找到含有*的行
$ fgrep -n '*' regular_express.txt
或者
$ grep -n -F '*' regular_express.txt
'*' regular_express.txt
```
_________________________________________________
参考资料<http://blog.csdn.net/ameyume/article/details/7600743>  
