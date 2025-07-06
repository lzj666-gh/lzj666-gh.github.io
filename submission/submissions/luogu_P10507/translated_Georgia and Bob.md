# Georgia and Bob (翻译版)

## 题目描述

**【题目描述】**

有一个无限长的棋盘，从左到右编号为 $1,2,3,\cdots$。有 $n$ 个棋子在棋盘上，定义一次操作为把一枚棋子向左移动至少一格，不可以逾越其他棋子，不可与其他棋子重合，不可移出棋盘。

告诉你这 $n$ 个棋子的位置（不保证顺序且保证没有棋子重合），Georgia 和 Bob 轮流进行操作，Georgia 先手，谁无法操作谁输。问最后谁会赢？

![](https://cdn.luogu.com.cn/upload/image_hosting/tti7635d.png)


**【输入格式】**


**本题有多组数据**。

第一行一个整数 $T$，表示数据组数。

对于每组数据：

第一行一个整数 $n$。  

接下来一行 $n$ 个整数，表示每个棋子的位置。

**【输出格式】**

对于每组数据，若 Georgia 胜输出 `Georgia will win`，若 Bob 胜输出 `Bob will win`，若平局则输出 `Not sure`。


## 输入格式

The first line of the input contains a single integer $T (1 \leq T \leq 20)$, the number of test cases. Then $T$ cases follow. Each test case contains two lines. The first line consists of one integer $N (1 \leq N \leq 1000)$, indicating the number of chessmen. The second line contains $N$ different integers $P_1, P_2 \dots P_n (1 \leq P_i \leq 10000)$, which are the initial positions of the $n$ chessmen.

## 输出格式

For each test case, prints a single line, "Georgia will win", if Georgia will win the game; "Bob will win", if Bob will win the game; otherwise 'Not sure'.

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
