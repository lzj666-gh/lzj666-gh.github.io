# The Wall (easy) (翻译版)

## 题目描述

### 题意翻译

给定一个长为 $C$ $（1≤C≤100）$ ，宽为 $R$ $(1≤R≤100)$ 的矩形。其中$‘.’$ 表示该区域为空，而 $‘B’$ 表示该区域为实。

现在求有多少个区域为实。

### 输入格式

第一行为两个整数 $C$ 和 $R$ 。

接下来就是 $C·R$ 的字符 $“B”$ 和 $“.”$

### 输出格式

一个整数，表示给定矩形中实的部分的

## 输入格式

The first line of the input consists of two space-separated integers $ R $ and $ C $ , $ 1<=R,C<=100 $ . The next $ R $ lines provide a description of the columns as follows:

- each of the $ R $ lines contains a string of length $ C $ ,
- the $ c $ -th character of line $ r $ is B if there is a brick in column $ c $ and row $ R-r+1 $ , and . otherwise.

 The input will contain at least one character B and it will be valid.

## 输出格式

The number of wall segments in the input configuration.

## 提示

In the first sample case, the 2nd and 3rd columns define the first wall segment, and the 5th column defines the second.

## 时空限制

时间限制: 500 ms
内存限制: 250 MB
