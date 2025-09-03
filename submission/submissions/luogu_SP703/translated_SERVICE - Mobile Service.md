# SERVICE - Mobile Service (翻译版)

## 题目描述

### 题目描述

有一个公司有  $3$ 个流动员工。任何时刻只有一名员工可以移动，不允许同一位置上有  $2$ 个及以上员工。

每次移动需要花费，从位置  $p$ 移动到位置  $q$ 需要花费  $c(p,q)$ 的价钱。不移动不需要花费（即  $c(i,i)=0$ ）但不保证  $c(p,q)=c(q,p)$ 。

现在给出  $N$ 个请求，第  $i$ 个请求发生在位置  $x_i$ 。公司必须按照顺序，派一名员工到位置  $x_i$ ，过程中不能去其他地方，也就是必须直接过去。

  $3$ 个流动员工的初始位置分别为  $1,2,3$ 。

求公司的最小花费。

### 输入格式

第一行一个数  $T$ ，表示数据组数。

每组数据的第一行有两个数  $L,N$ ，表示有  $L$ 个位置和  $N$ 个请求。

接下来的  $L$ 行中的每一行都包含  $L$ 个非负整数。其中第  $i+1$ 行第  $j$ 个数是  $c(i,j)$ ，表示价钱。

最后一行，有  $n$ 个整数，分别为  $x_1,x_2,x_3 ... x_n$ 表示请求的位置。

### 输出格式

一行一个数，表示每组数据的最小花费。

### 数据范围与说明

对于  $100\%$ 的数据满足  $3 \le L \le 200 , 1 \le N \le 1000 ,0 \le c(i,j) \le 2000$ 。

## 输入格式

 The first line of input contains the number of test cases - nTest. Each test case contains:

 The first line of each test cases contains two integers, L and N. L (3 <= L <= 200) is the number of locations and N (1 <= N <= 1000) is the number of requests. Locations are identified by the integers from 1 to L. Each of the next L lines contains L non-negative integers. The jth number in the line i+1 is the cost C(i,j), and it is less than 2000.

 The last of each test cases contains N integers, the list of the requests. A request is identified by the identifier of the location where the request occurs. Initially, the three service staff employees are located at location 1, 2 and 3, respectively.

## 输出格式

 For each test case write the minimal total cost in a separate line.

## 时空限制

时间限制: 2448 ms
内存限制: 1500 MB
