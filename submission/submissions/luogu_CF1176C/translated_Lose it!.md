# Lose it! (翻译版)

## 题目描述

你有一个长度为$n$的序列$a$，其中每一个元素都是下列6种数字中的一个：$4,8,15,16,23,42$。

你的任务是删掉最少的元素，使得这个序列变成好的。

我们称一个长度为$k$的序列是好的，当且仅当$k$能被$6$整除并且这个序列能划分成$\dfrac k6$个子序列，使得每一个子序列都是$\{4,8,15,16,23,42\}$。

下面几个序列是好的序列：

$[4, 8, 15, 16, 23, 42]$（整个序列作为要求的子序列）；

$[4, 8, 4, 15, 16, 8, 23, 15, 16, 42, 23, 42]$（第一个子序列由第一，二，四，五，七，十个元素构成，第二个子序列由剩下的元素构成）；

$[]$（空序列是好的）.

下面几个序列是不好的序列：

$[4, 8, 15, 16, 42, 23]$

$[4, 8, 15, 16, 23, 42, 4]$

$[4, 8, 15, 16, 23, 42, 4, 8, 15, 16, 23, 23]$

## 输入格式

The first line of the input contains one integer $ n $ ( $ 1 \le n \le 5 \cdot 10^5 $ ) — the number of elements in $ a $ .

The second line of the input contains $ n $ integers $ a_1, a_2, \dots, a_n $ (each $ a_i $ is one of the following numbers: $ 4, 8, 15, 16, 23, 42 $ ), where $ a_i $ is the $ i $ -th element of $ a $ .

## 输出格式

Print one integer — the minimum number of elements you have to remove to obtain a good array.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
