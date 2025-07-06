# IOIers&&teachers

## 题目描述

本题的输入是一个故事，十分生动形象。

## 输入格式

有$n$行，$m$个人，$k$个老师，在第一行依次输入,老师名称为1，2，3，...（$k\leq9$），学生名称为A,B,C,...（$m\leq26$）。

接下来$n$行讲述了一个生动形象的故事，但是你只需要注意特定句式，列表如下：

> 1.sb. opened florr.io(sb. 打开了 florr.io，此时如果有老师，那么 sb. 会被发现)
>
> 2.some teacher comes in(some teacher 进来了)
>
> 3.some teacher goes out(some teacher 走了)
>
> 4.sb. closed florr.io(sb. 关闭了 florr.io)

## 输出格式

第一行若干个字母，表示被发现了的IOIers（用A,B,C,...）。

如果所有人都被发现了，那么在第二行输出`bad,bad,bad IOIers!!!`

## 提示

$n\leq4\times10^5$

时空均在STD的两倍以上

## 时空限制

时间限制: 100 ms
内存限制: 128 MB
