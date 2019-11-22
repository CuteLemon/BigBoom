# Linux 常见命令行操作

## 为什么需要学习命令行

90%的真实代码都运行在没有显示器的服务器上，你与其交互的方式就是通过黑黢黢的终端界面。如果不会一点常见工具，就像修理工不会用螺丝刀一样奇怪。



### 文件操作

打开文件

#### vi/vim

```bash
  1 
~                                                                     
~                         VIM - Vi IMproved                           
~                                                                     
~                          version 8.1.1312                           
~                      by Bram Moolenaar et al.                       
~            Vim is open source and freely distributable              
~                                                                     
~                   Help poor children in Uganda!                     
~           type  :help iccf<Enter>       for information             
~                                                                     
~           type  :q<Enter>               to exit                     
~           type  :help<Enter>  or  <F1>  for on-line help            
~           type  :help version8<Enter>   for version info            
~ 
```

vi/vim 的操作很奇怪，需要经年累月的训练才能很好的掌握（同时变身码怪）。推荐参考 cool shell 的博客进行第一阶段的训练。你遇到的第一个困难可能是如何退出VIM编辑器。



#### cat

打开文件并输出到终端中。

```bash
▶ cat aaple-trading-hour.csv 
,open,high,low,close,volume
2015-08-03 09:30:00,1214500,1215800,1214500,1214900,1028608
2015-08-03 09:30:01,1214600,1215000,1214600,1215000,1236
2015-08-03 09:30:02,1215000,1215000,1214600,1215000,3314
2015-08-03 09:30:03,1215000,1215000,1214500,1215000,6396
2015-08-03 09:30:04,1214900,1215000,1214600,1214800,2226
2015-08-03 09:30:05,1215000,1215000,1214600,1214900,3174
2015-08-03 09:30:06,1214900,1215000,1214900,1215000,601
2015-08-03 09:30:07,1214900,1215000,1214700,1215000,4400
2015-08-03 09:30:08,1214700,1215000,1214700,1215000,956

```



#### head

输出文件前N行到终端中

```bash
▶ head -5  ./aapl-trading-hour.csv
,open,high,low,close,volume
2015-08-03 09:30:00,1214500,1215800,1214500,1214900,1028608
2015-08-03 09:30:01,1214600,1215000,1214600,1215000,1236
2015-08-03 09:30:02,1215000,1215000,1214600,1215000,3314
2015-08-03 09:30:03,1215000,1215000,1214500,1215000,6396
```



### 系统管理

####ps

显示进程

```bash
▶ ps
  PID TTY           TIME CMD
11760 ttys000    0:00.58 /bin/zsh -l
15551 ttys001    0:00.22 /bin/zsh -l
16105 ttys001    0:00.07 python
```



####kill

关闭进程

```bash
# 通过PID来关闭进程
▶ kill 16105

# 通过进程名来关闭
▶ killall python
```



### 字符处理

####grep

查找文件中特定的字符串

```bash
▶ grep 'cat' README.md 
cat
ncat
cat url-list.txt | xargs wget -c
```



####awk

是处理日志、csv 等格式规范的文件神器

$1代表第一列

$2代表第二列...

$(NF-1) 代表倒数第二列

```bash
▶ awk '{print $1}' aaple-trading-hour.csv 
,open,high,low,close,volume
2015-08-03
2015-08-03
2015-08-03
2015-08-03
2015-08-03
2015-08-03
2015-08-03
2015-08-03
2015-08-03

#强制以',' 作为分隔符切分
▶ awk -F ',' '{print $1}' aaple-trading-hour.csv 

2015-08-03 09:30:00
2015-08-03 09:30:01
2015-08-03 09:30:02
2015-08-03 09:30:03
2015-08-03 09:30:04
2015-08-03 09:30:05
2015-08-03 09:30:06
2015-08-03 09:30:07
2015-08-03 09:30:08

```



## 多工具联合使用

### 管道

将上一个操作的输出，作为下一个操作的输入。以此向管道/流水线一样操作各工具。



### | 操作

```bash
# 筛选出名字叫Python的进程的PID
▶ ps | grep 'python' | awk '{print $1}' 
19903
```



能否通过管道操作直接将Python的进程Kill 掉呢？试试

```bash
▶ ps |grep 'python' |awk '{print $1}'|kill
kill: not enough arguments
```

看起来不行，我们需要另外一个小工具xargs来帮忙。

### xargs

```bash
▶ ps |grep -F 'python'| awk '{print $1}'|xargs kill
kill: 21113: No such process
```



##常见问题集锦



#### 快速求和

awk '{sum+=$1} END {print "Sum = ", sum}'

```bash
▶ cat aaple-trading-hour.csv|awk -F ',' '{sum+=$2}END{print sum}'
10933500
```

