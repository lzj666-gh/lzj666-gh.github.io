# Broken robot (翻译版)

## 题目描述

## 题意翻译
$n$ 行 $m$ 列的矩阵，现在在 $(x,y)$，每次等概率向左，右，下走或原地不动，但不能走出去，问走到最后一行期望的步数。

注意，$(1,1)$ 是木板的左上角，$(n,m)$ 是木板的右下角。
### 输入输出格式
#### 输入格式
第一行为两个整数 $n,m$。

第二行为两个整数 $x,y$。
#### 输出格式
一行，输出所需移动步数的数学期望值，至少保留 $4$ 位小数的值。
### 说明/提示
$1\le n,m\le 10^3$，$1\le x\le n$，$1\le y\le m$。

## 输入格式

On the first line you will be given two space separated integers $ N $ and $ M $ ( $ 1<=N,M<=1000 $ ). On the second line you will be given another two space separated integers $ i $ and $ j $ ( $ 1<=i<=N,1<=j<=M $ ) — the number of the initial row and the number of the initial column. Note that, $ (1,1) $ is the upper left corner of the board and $ (N,M) $ is the bottom right corner.

## 输出格式

Output the expected number of steps on a line of itself with at least $ 4 $ digits after the decimal point.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
