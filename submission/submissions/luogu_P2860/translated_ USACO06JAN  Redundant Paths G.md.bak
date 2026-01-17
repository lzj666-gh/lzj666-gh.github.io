# [USACO06JAN] Redundant Paths G (翻译版)

## 题目描述

为了从 $F(1 \le F \le 5000)$ 个草场中的一个走到另一个，贝茜和她的同伴们有时不得不路过一些她们讨厌的可怕的树．奶牛们已经厌倦了被迫走某一条路，所以她们想建一些新路，使每一对草场之间都会至少有两条相互分离的路径，这样她们就有多一些选择。

每对草场之间已经有至少一条路径．给出所有 $R\ (F-1 \le R \le 10000)$ 条双向路的描述，每条路连接了两个不同的草场，请计算最少的新建道路的数量，路径由若干道路首尾相连而成．两条路径相互分离，是指两条路径没有一条重合的道路．但是，两条分离的路径上可以有一些相同的草场．对于同一对草场之间，可能已经有两条不同的道路，你也可以在它们之间再建一条道路，作为另一条不同的道路。

## 输入格式

Line 1: Two space-separated integers: F and R




Lines 2..R+1: Each line contains two space-separated integers which are the fields at the endpoints of some path.


## 输出格式

Line 1: A single integer that is the number of new paths that must be built.


## 提示

Explanation of the sample:




One visualization of the paths is:

![](https://cdn.luogu.com.cn/upload/image_hosting/cubnel5k.png)

Building new paths from 1 to 6 and from 4 to 7 satisfies the conditions.

![](https://cdn.luogu.com.cn/upload/image_hosting/rgguiytp.png)

Check some of the routes:

- 1 – 2:  1 –> 2 and 1 –> 6 –> 5 –> 2
- 1 – 4:  1 –> 2 –> 3 –> 4 and 1 –> 6 –> 5 –> 4
- 3 – 7:  3 –> 4 –> 7 and 3 –> 2 –> 5 –> 7

Every pair of fields is, in fact, connected by two routes.

It's possible that adding some other path will also solve the problem (like one from 6 to 7). Adding two paths, however, is the minimum.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
