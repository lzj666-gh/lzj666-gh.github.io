# [Code+#1] 木材

## 题目描述

有 $n$ 棵树，初始时每棵树的高度为 $H_i$，第 $i$ 棵树每月都会长高 $A_i$。现在有个木料长度总量为 $S$ 的订单，客户要求每块木料的长度不能小于  $L$，而且木料必须是整棵树（即不能为树的一部分）。现在问你最少需要等多少个月才能满足订单。


## 输入格式

第一行 $3$ 个用空格隔开的非负整数 $n,S,L$，表示树的数量、订单总量和单块木料长度限制。

第二行 $n$ 个用空格隔开的非负整数，依次为 $H_1,H_2, ... ,H_n$。

第三行 $n$ 个用空格隔开的非负整数，依次为 $A_1,A_2, ... ,A_n$。


## 输出格式

输出一行一个整数表示答案。


## 提示

对于样例，在六个月后，各棵树的高度分别为 $14,47,56$，此时无法完成订单。

在七个月后，各棵树的高度分别为 $16,54,65$，此时可以砍下第 $2$ 和第 $3$ 棵树完成订单了。

 ![](https://cdn.luogu.com.cn/upload/pic/12821.png) 

来自 CodePlus 2017 11 月赛，清华大学计算机科学与技术系学生算法与竞赛协会 荣誉出品。

Credit：idea/郑林楷 命题/郑林楷 验题/王聿中

Git Repo：https://git.thusaac.org/publish/CodePlus201711

感谢腾讯公司对此次比赛的支持。


## 时空限制

时间限制: 1000 ms
内存限制: 500 MB
