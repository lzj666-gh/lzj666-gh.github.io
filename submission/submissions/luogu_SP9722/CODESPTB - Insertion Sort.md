# CODESPTB - Insertion Sort

## 题目描述

Insertion Sort is a classical sorting technique. One variant of insertion sort works as follows when sorting an array a\[1..N\] in non-descending order:

 ```

for i <- 2 to N
    j <- i
    while j > 1 and a[j] < a[j - 1]
        swap a[j] and a[j - 1]
        j <- j - 1
```
 The pseudocode is simple to follow. In the ith step, element a\[i\] is inserted in the sorted sequence a\[1..i - 1\]. This is done by moving a\[i\] backward by swapping it with the previous element until it ends up in it's right position.

 As you probably already know, the algorithm can be really slow. To study this more, you want to find out the number of times the swap operation is performed when sorting an array.

## 输入格式

The first line contains the number of test cases T. T test cases follow. The first line for each case contains N, the number of elements to be sorted. The next line contains N integers a\[1\],a\[2\]...,a\[N\].

## 输出格式

Output T lines, containing the required answer for each test case.

## 提示

1 <= T <= 5

1 <= N <= 100000

1 <= a[i] <= 1000000

## 时空限制

时间限制: 3000 ms
内存限制: 1500 MB
