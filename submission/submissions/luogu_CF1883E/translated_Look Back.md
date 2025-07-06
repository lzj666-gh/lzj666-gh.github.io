# Look Back (翻译版)

## 题目描述

给定长度为 $n$ 的序列 $a$，你可以进行以下操作。  
>选取一个 $i$ 满足 $1\le i\le n$，使 $a_i$ 变为原来的 $2$ 倍。  

求最少需要几次操作使得 $a$ 为一个不下降的序列。

## 输入格式

Each test consists of multiple test cases. The first line contains a single integer $ t $ ( $ 1 \leq t \leq 10^4 $ ) — the number of test cases. This is followed by their description.

The first line of each test case contains an integer $ n $ ( $ 1 \leq n \leq 10^5 $ ) — the size of the array $ a $ .

The second line of each test case contains $ n $ integers $ a_1, a_2, \ldots, a_n $ ( $ 1 \leq a_i \leq 10^9 $ ).

It is guaranteed that the sum of $ n $ over all test cases does not exceed $ 2 \cdot 10^5 $ .

## 输出格式

For each test case, output the minimum number of operations needed to make the array non-decreasing.

## 提示

No operations are needed in the first test case.

In the second test case, we need to choose $ i = 2 $ , after which the array will be $ [2, 2] $ .

In the third test case, we can apply the following operations:

- Choose $ i = 3 $ , after which the array will be $ [3, 2, 2] $ ,
- Choose $ i = 3 $ , after which the array will be $ [3, 2, 4] $ ,
- Choose $ i = 2 $ , after which the array will be $ [3, 4, 4] $ .

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
