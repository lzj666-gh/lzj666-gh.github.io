# [USACO12DEC] First! G

## 题目描述

Bessie 一直在研究字符串。她发现，通过改变字母表的顺序，她可以按改变后的字母表来排列字符串（字典序大小排列）。

例如，Bessie 发现，对于字符串 $\texttt{omm},\texttt{moo},\texttt{mom}$ 和 $\texttt{ommnom}$，她可以使用标准字母表使 $\texttt{mom}$ 排在第一个（即字典序最小），她也可以使用字母表 $\texttt{abcdefghijklonmpqrstuvwxyz}$ 使得 $\texttt{omm}$ 排在第一个。然而，Bessie 想不出任何方法（改变字母表顺序）使得 $\texttt{moo}$ 或 $\texttt{ommnom}$ 排在第一个。

接下来让我们通过重新排列字母表的顺序来计算输入中有哪些字符串可以排在第一个（即字典序最小），从而帮助 Bessie。

要计算字符串 $X$ 和字符串 $Y$ 按照重新排列过的字母表顺序来排列的顺序，先找到它们第一个不同的字母 $X_i$ 与 $Y_i$，按重排后的字母表顺序比较，若 $X_i$ 比 $Y_i$ 先，则 $X$ 的字典序比 $Y$ 小，即 $X$ 排在 $Y$ 前；若没有不同的字母，则比较 $X$ 与 $Y$ 长度，若 $X$ 比 $Y$ 短，则 $X$ 的字典序比 $Y$ 小，即 $X$ 排在 $Y$ 前。

## 输入格式

第 $1$ 行：一个数字 $N$（$1\le N \le 30,000$），表示 Bessie 正在研究字符串的数量。

第 $2\sim N+1$ 行：每行包含一个非空字符串。所有字符串包含的字符总数不会超过 $300,000$。输入中的所有字符都是小写字母，即 $a\sim z$。输入不包含重复的字符串。

## 输出格式

第 $1$ 行：一个数字 $K$，表示按重排的字母表顺序排列后可以排在第一个的字符串数量。

第 $2\sim K+1$ 行：第 $i+1$ 行包含第 $i$ 个按重排的字母表顺序排列后可以排在第一个的字符串。字符串应该按照它们在输入中的顺序来输出。

## 提示

样例即题目描述中给出的例子，只有 $\texttt{omm}$ 和 $\texttt{mom}$ 在各自特定的字典序下可以被排列在第一个。

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
