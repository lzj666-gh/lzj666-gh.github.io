# Pair of Toys (翻译版)

## 题目描述

给定n个玩具要你选出两个玩具求出k的价值。  
第i个玩具的价值为i。  
样例1：从8个玩具里选出两个使价值为5.  
有以下方案：（1 4）（2 3）。  
若是没有选择方案，输出0
补充：玩具A与玩具B 和 玩具B和玩具A 是同一种选择

## 输入格式

The first line of the input contains two integers $ n $ , $ k $ ( $ 1 \le n, k \le 10^{14} $ ) — the number of toys and the expected total cost of the pair of toys.

## 输出格式

Print the number of ways to choose the pair of toys satisfying the condition above. Print 0, if Tanechka can choose no pair of toys in such a way that their total cost is $ k $ burles.

## 提示

In the first example Tanechka can choose the pair of toys ( $ 1, 4 $ ) or the pair of toys ( $ 2, 3 $ ).

In the second example Tanechka can choose only the pair of toys ( $ 7, 8 $ ).

In the third example choosing any pair of toys will lead to the total cost less than $ 20 $ . So the answer is 0.

In the fourth example she can choose the following pairs: $ (1, 1000000000000) $ , $ (2, 999999999999) $ , $ (3, 999999999998) $ , ..., $ (500000000000, 500000000001) $ . The number of such pairs is exactly $ 500000000000 $ .

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
