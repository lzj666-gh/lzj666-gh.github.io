# Yet Another Segments Subset (翻译版)

## 题目描述

## 题目描述

给你 $n$ 个线段，每个线段用左右端点 $l_i, r_i$ 表示。  
现在要你从中选出尽量多的线段，使得他们两两之间要么完全不相交，要么其中一个完全包含另一个。

你需要回答 $t$ 次询问。

## 输入格式

第一行是一个数字 $t(t\leq1000)$，表示有 $t$ 个查询。

每个查询有 $n(n\leq3000)$ 个线段，每个线段有两个整数 $l_i,r_i(1\leq l_i \leq r_i\leq 2\times10^5)$ 代表左右边界。

同一个查询的所有线段中保证没有两个线段是完全一样的，并且数据保证所有查询的 $n$ 加起来不超过 $3000$。

## 输出格式

每个查询输出一行一个数字，代表最多能选多少个满足题意的线段。




## 输入格式

The first line of the input contains one integer $ t $ ( $ 1       \le t \le 1000 $ ) — the number of test cases. Then $ t $ test cases follow.

The first line of the test case contains one integer $ n $ ( $ 1 \le n \le 3000 $ ) — the number of segments. The next $ n $ lines describe segments. The $ i $ -th segment is given as two integers $ l_i $ and $ r_i $ ( $ 1 \le l_i \le r_i \le       2 \cdot 10^5 $ ), where $ l_i $ is the left border of the $ i $ -th segment and $ r_i $ is the right border of the $ i $ -th segment.

Additional constraint on the input: there are no duplicates in the list of segments.

It is guaranteed that the sum of $ n $ does not exceed $ 3000 $ ( $ \sum n \le 3000 $ ).

## 输出格式

For each test case, print the answer: the maximum possible size of the subset of the given set of segments such that each pair of segments in this subset either non-intersecting or one of them lies inside the other one.

## 时空限制

时间限制: 3000 ms
内存限制: 250 MB
