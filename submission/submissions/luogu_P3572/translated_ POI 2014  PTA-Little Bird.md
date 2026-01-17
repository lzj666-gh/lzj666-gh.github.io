# [POI 2014] PTA-Little Bird (翻译版)

## 题目描述

有 $n$ 棵树排成一排，第 $i$ 棵树的高度是 $d_i$。

有 $q$ 只鸟要从第 $1$ 棵树到第 $n$ 棵树。

当第 $i$ 只鸟在第 $j$ 棵树时，它可以飞到第 $j+1, j+2, \cdots, j+k_i$ 棵树。

如果一只鸟飞到一颗高度大于等于当前树的树，那么它的劳累值会增加 $1$，否则不会。

由于这些鸟已经体力不支，所以它们想要最小化劳累值。

### 输入格式

第一行输入 $n$。

第二行 $n$ 个数，第 $i$ 个数表示 $d_i$。

第三行输入 $q$。

接下来 $q$ 行，每一行一个整数，第 $i$ 行的整数为 $k_i$。

### 输出格式

共 $q$ 行，每一行输出第 $i$ 只鸟的最小劳累值。

### 数据范围

$1 \le n \le 10^6$，$1 \le d_i \le 10^9$，$1 \le q \le 25$，$1 \le k_i \le n - 1$。


## 输入格式

There is a single integer $n$ ($2\le n\le 1\ 000\ 000$) in the first line of the standard input:

the number of trees in the Byteotian Line Forest.

The second line of input holds $n$ integers $d_1,d_2,\cdots,d_n$ ($1\le d_i\le 10^9$)separated by single spaces: $d_i$ is the height of the i-th tree.

The third line of the input holds a single integer $q$ ($1\le q\le 25$): the number of birds whoseflights need to be planned.

The following $q$ lines describe these birds: in the $i$-th of these lines, there is an integer $k_i$ ($1\le k_i\le n-1$) specifying the $i$-th bird's stamina. In other words, the maximum number of trees that the $i$-th bird can pass before it has to rest is $k_i-1$.


## 输出格式

Your program should print exactly $q$ lines to the standard output.

In the $i$-th line, it should specify the minimum number of tiresome flight legs of the $i$-th bird.


## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
