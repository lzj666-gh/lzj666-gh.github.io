# [POI 2011] LIZ-Lollipop (翻译版)

## 题目描述


给一个只有 $1$ 和 $2$ 的序列，每次询问有没有一个子串的和为 $x$。

### 输入格式

第一行两个整数 $n, m$（$1 \le n, m \le 10 ^ 6$）。

第二行一个长为 $n$ 的只含 $\texttt T$ 和 $\texttt W$ 的字符串，$\texttt T$ 代表 $2$，$\texttt W$ 代表 $1$。

接下来 $m$ 行，每行一个整数 $x$（$1 \le x \le 2\times 10 ^ 6$）表示一次询问。

### 输出格式

$m$ 行，如果有解则输出两个整数 $l, r$ 表示区间 $[l, r]$ 的和是 $x$，如果无解则输出字符串 `NIE`。

## 输入格式

In the first line of the standard input there are two integers $n$ and $m$      ($1\le n,m \le 1\ 000\ 000$), separated by a single space.

These denote, respectively, the number of segments of the last lollipop left      in store, and the number of values of $k$ to consider.

The lollipop's segments are numbered from 1 to $n$.

The second line gives an $n$-letter description of the lollipop, consisting      of letters T and W, where T denotes a strawberry flavoured segment, while W - vanilla flavoured;the $i$-th of these letters specifies the flavour of the $i$-th segment.

In the following $m$ lines successive values of $k$($1\le k\le 2\ 000\ 000$) to consider are given, one per line.


## 输出格式

Your program should print out exactly $m$ lines, giving, one per line,      the results for successive values of $k$, to the standard output.

If for a given value of $k$ it is impossible to break the lollipop in such a way that there is a contiguous fragment worth exactly $k$ bythalers, then the word      NIE (no in Polish) should be printed. Otherwise, two integers $l$ and $r$ ($1\le l\le r\le n$), separated by single spaces, should      be printed, such that the fragment of the lollipop composed of the segments      numbered from $l$ to $r$ inclusively is worth exactly $k$ bythalers. If there are multiple such pairs, your program is free to choose one arbitrarily.


## 提示


SPJ 对于格式的要求较为严格。对于每个询问后，应紧跟一个换行符。在最后一次输出你的答案以及一个换行符后不应有任何输出。


由 zhouyonglong 提供 SPJ。


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
