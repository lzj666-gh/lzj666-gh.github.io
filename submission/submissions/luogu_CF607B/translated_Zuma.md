# Zuma (翻译版)

## 题目描述

$\texttt{Genos}$ 最近在他的手机上下载了祖玛游戏。在祖玛游戏里，存在 $n$ 个一行的宝石，第 $i$ 个宝石的颜色是 $C_i$。这个游戏的目标是尽快的消灭一行中所有的宝石。

在一秒钟，$\texttt{Genos}$ 能很快的挑选出这些有颜色的宝石中的一个回文的、连续的子串，并将这个子串移除。每当一个子串被删除后，剩余的宝石将连接在一起，形成一个新的行列。

你的任务是：求出把整个宝石串都移除的最短时间。

### 输入格式

第一行包含一个整数 $n(1 \le n \le 500)$，表示宝石串的长度。第二行包含 $n$ 个被空格分开的整数，第 $i(1 \le i \le n)$ 个表示这行中第 $i$ 个珠子的颜色。

### 输出格式

输出一个整数，把这行珠子移除的最短时间。

### 样例说明

在第一个例子中，$\texttt{Genos}$ 可以在一秒钟就把这行珠子全部移走。在第二个例子中，$\texttt{Genos}$ 一次只能移走一个珠子，所以移走三个珠子花费他三秒。在第三个例子中，为了达到 $2$ 秒的最快时间，先移除回文串 $\texttt{4 4}$,再移除回文串 $\texttt{1 2 3 2 1}$。

感谢 @Administrator2004 提供的翻译

## 输入格式

The first line of input contains a single integer $ n $ ( $ 1<=n<=500 $ ) — the number of gemstones.

The second line contains $ n $ space-separated integers, the $ i $ -th of which is $ c_{i} $ ( $ 1<=c_{i}<=n $ ) — the color of the $ i $ -th gemstone in a line.

## 输出格式

Print a single integer — the minimum number of seconds needed to destroy the entire line.

## 提示

In the first sample, Genos can destroy the entire line in one second.

In the second sample, Genos can only destroy one gemstone at a time, so destroying three gemstones takes three seconds.

In the third sample, to achieve the optimal time of two seconds, destroy palindrome 4 4 first and then destroy palindrome 1 2 3 2 1.

## 时空限制

时间限制: 2000 ms
内存限制: 500 MB
