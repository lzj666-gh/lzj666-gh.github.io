# Look Back

## 题目描述

You are given an array of integers $ a_1, a_2, \ldots, a_n $ . You need to make it non-decreasing with the minimum number of operations. In one operation, you do the following:

- Choose an index $ 1 \leq i \leq n $ ,
- Set $ a_i = a_i \cdot 2 $ .

An array $ b_1, b_2, \ldots, b_n $ is non-decreasing if $ b_i \leq b_{i+1} $ for all $ 1 \leq i < n $ .

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
