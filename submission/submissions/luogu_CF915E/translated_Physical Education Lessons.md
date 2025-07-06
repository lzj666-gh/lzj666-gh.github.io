# Physical Education Lessons (翻译版)

## 题目描述

#### 题意：
Alex高中毕业了，他现在是大学新生。虽然他学习编程，但他还是要上体育课，这对他来说完全是一个意外。快要期末了，但是不幸的Alex的体育学分还是零蛋！

Alex可不希望被开除，他想知道到期末还有多少天的工作日，这样他就能在这些日子里修体育学分。但是在这里计算工作日可不是件容易的事情：

从现在到学期结束还有 $n$ 天(从 $1$ 到 $n$ 编号)，他们一开始都是工作日。接下来学校的工作人员会**依次**发出 $q$ 个指令，每个指令可以用三个参数 $l,r,k$ 描述：

- 如果 $k=1$，那么从 $l$ 到 $r$ （包含端点）的所有日子都变成**非**工作日。

- 如果 $k=2$，那么从 $l$ 到 $r$ （包含端点）的所有日子都变成**工作日**。

帮助Alex统计每个指令下发后，剩余的工作日天数。

#### 输入格式：

第一行一个整数 $n$，第二行一个整数 $q$ $(1\le n\le 10^9,\;1\le q\le 3\cdot 10^5)$，分别是剩余的天数和指令的个数。

接下来 $q$ 行，第 $i$ 行有 $3$ 个整数 $l_i,r_i,k_i$，描述第 $i$ 个指令 $(1\le l_i,r_i\le n,\;1\le k\le 2)$。

#### 输出格式：

输出 $q$ 行，第 $i$ 行表示第 $i$ 个指令被下发后剩余的工作日天数。

Translated by 小粉兔

## 输入格式

The first line contains one integer $ n $ , and the second line — one integer $ q $ ( $ 1<=n<=10^{9} $ , $ 1<=q<=3·10^{5} $ ) — the number of days left before the end of the term, and the number of orders, respectively.

Then $ q $ lines follow, $ i $ -th line containing three integers $ l_{i} $ , $ r_{i} $ and $ k_{i} $ representing $ i $ -th order ( $ 1<=l_{i}<=r_{i}<=n $ , $ 1<=k_{i}<=2 $ ).

## 输出格式

Print $ q $ integers. $ i $ -th of them must be equal to the number of working days left until the end of the term after the first $ i $ orders are published.

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
