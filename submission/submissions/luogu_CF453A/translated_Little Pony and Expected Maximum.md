# Little Pony and Expected Maximum (翻译版)

## 题目描述

暮暮刚刚在和她的朋友——AJ（苹果杰克）、FS（小蝶）、RD（云宝黛西）玩Ludo游戏。但是她马品没攒够总是输。回到城堡过后，她对游戏用的骰子产生了兴趣。

题目描述

这个骰子有M面：骰子的第一面有一个点，第二面有两个点，以此类推，第m面含有M点。暮暮确信的是，当掷骰子时，每一面都有1/m的可能性出现，并且每次投掷的概率都是都是独立的。请你帮助她计算掷N次骰子后每次得到的点数中最大值的期望。

输入输出格式

输入格式：

一行两个整数 m 和 n (1 ≤ m, n ≤ 10^5).

输出格式：

输出一行一个实数，与答案误差不大于10^-4

## 输入格式

A single line contains two integers $ m $ and $ n $ ( $ 1<=m,n<=10^{5} $ ).

## 输出格式

Output a single real number corresponding to the expected maximum. The answer will be considered correct if its relative or absolute error doesn't exceed $ 10^{-4} $ .

## 提示

Consider the third test example. If you've made two tosses:

1. You can get 1 in the first toss, and 2 in the second. Maximum equals to 2.
2. You can get 1 in the first toss, and 1 in the second. Maximum equals to 1.
3. You can get 2 in the first toss, and 1 in the second. Maximum equals to 2.
4. You can get 2 in the first toss, and 2 in the second. Maximum equals to 2.

The probability of each outcome is 0.25, that is expectation equals to:

![](https://cdn.luogu.com.cn/upload/vjudge_pic/CF453A/a611917193fd806daca7707d914db660d20dd0a4.png)You can read about expectation using the following link: http://en.wikipedia.org/wiki/Expected\_value

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
