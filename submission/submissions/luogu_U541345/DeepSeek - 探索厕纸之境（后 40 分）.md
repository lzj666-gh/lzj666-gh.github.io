# DeepSeek - 探索厕纸之境（后 40 分）

## 题目描述

有 $n$ 个人在玩 uno，编号为 $1$ 到 $n$。

每个人都有他的手牌的好用程度 $a_i$。（$1\le i \le n$）

你并不知道有那些人分为了一个队，你只想知道有两个队是否「不分上下」。

两个队是「不分上下」的，当且仅当他们「旗鼓相当」。

两个队「旗鼓相当」，当且仅当~~两个队是「不分上下」的~~两个队人数相同，且排序后两个序列完全一样。

还有，在 Deepseek 的定义下，一个队伍必须是一个区间。

所以因为 Deepseek 玩 uno 连输了十局变成了 Deepsick，所以它给你了 $m$ 次询问，每次询问会给你两个区间 $[l,r]$,$[l_2,r_2]$。（区间可能有交）

## 输入格式

第一行两个数 $n,m$。

第二行 $n$ 个数，表示数组 $a$。

接下来 $m$ 行，每行四个数 $l,r,l_2,r_2$ 表示一次询问。

## 输出格式

输出 $m$ 行，每行输出 `Yes` 或 `No`，表达是否**不分上下**。

## 提示

共 $20$ 个数据点。

|测试点编号|数据范围|特殊性质|
|---: |---: |---: |
|#1|$n=m=2\times 10^5$|数据完全随机生成|
|#2~#3|$1\le n,m\le 5000$|无|
|#4~#6|$1\le n,m\le 10^5$，$1\le a_i\le 100$|无|
|#7~#12|$1\le n,m \le 10^5$|无|
|#13~#18|$1\le n,m \le 10^6$|无|
|#19~#20|$1\le n,m \le 10^7$|无|

对于 $100\%$ 的数据，$1\le n,m \le 10^7$，$1\le a_i \le 10^9$。

~~对于 $0\%$ 的数据，DeepSick 上厕所忘带纸，变回了 DeepSeek，所以来看个[逆天的](about:blank)（链接赛后公布）~~。

保证数据有层级。

## 样例解释

对于第三组询问，$[1,3]$ 是 MVP，$[4,5]$ 是躺一狗。

## 其它事项

Idea：LBY，Solution：LBY，Code：DeepSeek & LBY，Data：xuezhiyu。

输入输出文件名 galaseek.in/galaseek.out。

## 时空限制

时间限制: 3000 ms
内存限制: 512 MB
