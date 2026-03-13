# [UOI 2024] Points on a Line

## 题目描述

This is an interactive problem.

There are $n$ points on a number line with integer coordinates $x_1, x_2, \ldots, x_n$. It is guaranteed that $1\le x_i\le n$ for $1\le i\le n$.

A point $x_k$ is considered to be between points $x_i$ and $x_j$ if and only if it belongs to the segment constructed on points $x_i$ and $x_j$. Formally, point $x_k$ is between points $x_i$ and $x_j$ if and only if $x_i \leq x_k \leq x_j$ or $x_j \leq x_k \leq x_i$.

You need to find any two indices $i$ and $j$ such that all $n$ points are between points $x_i$ and $x_j$.

You can use the following query: select three indices ($i$, $j$, $k$) and find out if point $x_k$ is between points $x_i$ and $x_j$.

You are allowed to use no more than $22222$ queries.

It is guaranteed that the coordinates of the points are fixed before the interaction begins. In other words, the **interactor is not adaptive**.

## 输入格式

The first line contains a single integer $n$ ($3 \le n \le 2 \cdot 10^4$) --- the number of points.

## 输出格式

To make a query, output "$\tt{?}$ $i$ $j$ $k$" ($1 \le i, j, k \le n$), then output a newline character and perform the $\tt{flush}$ operation.

In response to the query, the jury program will output a single integer $f$ ($f \in \{0,1\}$). If $f = 1$, then point $x_k$ is between points $x_i$ and $x_j$; if $f = 0$, then point $x_k$ is not between them.

If the query is invalid (i.e., the maximum number of queries is exceeded or the query parameters are invalid), the jury program will output $\texttt{-1}$ and terminate. In this case, terminate the program to receive the verdict $\tt{Wrong Answer}$.

When you are ready to provide an answer, output it in the format "$\tt{!}$ $i$ $j$" ($1 \leq i, j \leq n$), where $i$ and $j$ are the sought indices of points. After that, terminate the program.

The $\tt{flush}$ operation is performed as follows:

- $\texttt{fflush(stdout)}$ or $\texttt{cout.flush()}$ in $\tt{C++}$;
- $\texttt{System.out.flush()}$ in $\tt{Java}$;
- $\texttt{flush(output)}$ in $\tt{Pascal}$;
- $\texttt{sys.stdout.flush()}$ in $\tt{Python}$.

You can see the templates given.

## 提示

|4||
|:-:|:-:|
||? 1 4 2|
|1||
||? 1 4 3|
|1||
||! 1 4|

In the example, the points have coordinates $x = [1, 2, 3, 4]$.

### Scoring

- ($17$ points): $n \le 20$;
- ($16$ points): $n \le 100$;
- ($30$ points): $n \le 10000$;
- ($23$ points): $n \le 20000$, $x_i \le 2$;
- ($10$ points): $n \le 12000$;
- ($4$ points): without additional constraints.

## 时空限制

时间限制: 1000 ms
内存限制: 256 MB
