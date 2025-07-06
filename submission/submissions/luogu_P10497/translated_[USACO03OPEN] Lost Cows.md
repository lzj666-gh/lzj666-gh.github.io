# [USACO03OPEN] Lost Cows (翻译版)

## 题目描述

### 题目描述

有 $N$ 头奶牛，已知它们的编号为 $1∼N$ 且各不相同，但不知道每头奶牛的具体编号。

现在这 $N$ 头奶牛站成一列，已知第 $i$ 头奶牛前面有 $a_i$ 头牛编号小于它，求每头奶牛的编号。

### 输入格式

第 $1$ 行，输入一个整数 $N$

第 $2...N$ 行，每行输入一个整数 $a_i$，表示第 $i$ 头奶牛前面有 $a_i$ 头奶牛的编号小于它（因为第一头奶牛前面没有奶牛，所以 $i$ 从 $2$ 开始）。

### 输出格式

输出包含 $N$ 行，每行输出一个整数表示奶牛的编号。

第 $i$ 行输出第 $i$ 头奶牛的编号。

### 数据范围

$2 \le N \le 8000$。

## 输入格式

Line 1: A single integer, N

Lines 2..N: These N-1 lines describe the number of cows that precede a given cow in line and have brands smaller than that cow. Of course, no cows precede the first cow in line, so she is not listed. Line 2 of the input describes the number of preceding cows whose brands are smaller than the cow in slot #2; line 3 describes the number of preceding cows whose brands are smaller than the cow in slot #3; and so on.

## 输出格式

Lines 1..N: Each of the N lines of output tells the brand of a cow in line. Line #1 of the output tells the brand of the first cow in line; line 2 tells the brand of the second cow; and so on.

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
