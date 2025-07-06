# [USACO07OCT] Obstacle Course S

## 题目描述

Consider an N x N (1 <= N <= 100) square field composed of 1

by 1 tiles. Some of these tiles are impassible by cows and are marked with an 'x' in this 5 by 5 field that is challenging to navigate:

```cpp
. . B x . 
. x x A . 
. . . x . 
. x . . . 
. . x . . 
```
Bessie finds herself in one such field at location A and wants to move to location B in order to lick the salt block there.  Slow, lumbering creatures like cows do not like to turn and, of course, may only move parallel to the edges of the square field. For a given field, determine the minimum number of ninety degree turns in any path from A to B. The path may begin and end with Bessie facing in any direction. Bessie knows she can get to the salt lick.



## 输入格式

Line 1: A single integer: N

Lines 2..N + 1: Line i+1 represents row i of the field with N characters as above (i.e., '.', 'x', 'A', and 'B'); no spaces are present on a line


## 输出格式

Line 1: A single integer, the minimum number of turns the cow must make in a traversal

## 提示

只可以上下左右四个方向行走，并且不能走出这些格子之外。开始和结束时的方向可以任意。

### 数据范围及约定

对于全部数据，保证 $2\le N\le 100$。


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
