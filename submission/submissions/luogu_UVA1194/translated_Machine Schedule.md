# Machine Schedule (翻译版)

## 题目描述

有两台机器 $A,B$ 分别有 $n,m$ 种模式。

现在有 $k$ 个任务。对于每个任务 $i$ ，给定两个整数 $a_i$ 和 $b_i$ ，表示如果该任务在 $A$ 上执行，需要设置模式为 $a_i$ ；如果该任务在 $B$ 上执行，需要设置模式为 $b_i$ 。

每台机器第一次开机默认处在0模式，且第一次开机不需要消耗时间。任务可以以任意顺序被执行，但每台机器转换一次模式就要重启一次。求怎样分配任务并合理安排顺序，能使机器重启次数最少。

$1 \leq n,m \leq 100$，$1 \leq k \leq 1000$，$0 \leq a_i \lt n$，$0 \leq b_i \lt m$。

可能有多组数据。

## 时空限制

时空限制信息获取失败
