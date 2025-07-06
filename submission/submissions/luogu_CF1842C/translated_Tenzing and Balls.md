# Tenzing and Balls (翻译版)

## 题目描述

有一个大小为 $n$ 的数组 $a$。你可以进行下列操作任意多次：

选择 $i$ 和 $j$，使$1\leq i \lt j \leq |a|$ 并且$a_i=a_j$，
从数组中删除 $a_i,a_{i+1},…,a_{j}$
（并将 $a_j$ 右边的所有元素的索引减少 $j−i+1$）。

求出能删除数的最大数量。

注：$|a|$ 表示 $a$ 数组的大小。

## 输入格式

Each test contains multiple test cases. The first line of input contains a single integer $ t $ ( $ 1\leq t\leq 10^3 $ ) — the number of test cases. The description of test cases follows.

The first line contains a single integer $ n $ ( $ 1\leq n\leq 2\cdot 10^5 $ ) — the number of balls.

The second line contains $ n $ integers $ a_1,a_2,\ldots,a_n $ ( $ 1\leq a_i \leq n $ ) — the color of the balls.

It is guaranteed that sum of $ n $ of all test cases will not exceed $ 2\cdot 10^5 $ .

## 输出格式

For each test case, output the maximum number of balls Tenzing can remove.

## 提示

In the first example, Tenzing will choose $ i=2 $ and $ j=3 $ in the first operation so that $ a=[1,3,3] $ . Then Tenzing will choose $ i=2 $ and $ j=3 $ again in the second operation so that $ a=[1] $ . So Tenzing can remove $ 4 $ balls in total.

In the second example, Tenzing will choose $ i=1 $ and $ j=3 $ in the first and only operation so that $ a=[2] $ . So Tenzing can remove $ 3 $ balls in total.

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
