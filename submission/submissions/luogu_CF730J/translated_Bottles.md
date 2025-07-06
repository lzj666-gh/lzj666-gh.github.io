# Bottles (翻译版)

## 题目描述

### 题目描述

有 $n$ 瓶水，第 $i$ 瓶水的水量为 $a_i$，容量为 $b_i$。将 $1$ 单位水从一个瓶子转移到另一个瓶子所消耗时间为 $1$ 秒，且可以进行无限次转移。求储存所有水所需最小瓶子数 $k$ 以及该情况下所用最小时间 $t$。

### 输入格式

第一行输入一个正整数 $n$（$1\le n\le 100$）。

第二行输入 $n$ 个正整数，第 $i$ 个正整数表示 $a_i$（$1\le a_i \le 100$）。

第三行输入 $n$ 个正整数，第 $i$ 个正整数表示 $b_i$（$1\le b_i \le100$）。

对于每一个 $i$，满足$a_i\le b_i$。

### 输出格式

输出一行两个整数：$k$ 和 $t$。

## 输入格式

The first line contains positive integer $ n $ ( $ 1<=n<=100 $ ) — the number of bottles.

The second line contains $ n $ positive integers $ a_{1},a_{2},...,a_{n} $ ( $ 1<=a_{i}<=100 $ ), where $ a_{i} $ is the amount of soda remaining in the $ i $ -th bottle.

The third line contains $ n $ positive integers $ b_{1},b_{2},...,b_{n} $ ( $ 1<=b_{i}<=100 $ ), where $ b_{i} $ is the volume of the $ i $ -th bottle.

It is guaranteed that $ a_{i}<=b_{i} $ for any $ i $ .

## 输出格式

The only line should contain two integers $ k $ and $ t $ , where $ k $ is the minimal number of bottles that can store all the soda and $ t $ is the minimal time to pour the soda into $ k $ bottles.

## 提示

In the first example Nick can pour soda from the first bottle to the second bottle. It will take 3 seconds. After it the second bottle will contain $ 3+3=6 $ units of soda. Then he can pour soda from the fourth bottle to the second bottle and to the third bottle: one unit to the second and two units to the third. It will take $ 1+2=3 $ seconds. So, all the soda will be in two bottles and he will spend $ 3+3=6 $ seconds to do it.

## 时空限制

时间限制: 2000 ms
内存限制: 500 MB
