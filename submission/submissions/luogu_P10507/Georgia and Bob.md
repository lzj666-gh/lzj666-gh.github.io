# Georgia and Bob

## 题目描述

Georgia and Bob decide to play a self-invented game. They draw a row of grids on paper, number the grids from left to right by $1 , 2 , 3 , \cdots ,$ and place $N$ chessmen on different grids, as shown in the following figure for example:

![](https://cdn.luogu.com.cn/upload/image_hosting/tti7635d.png)

Georgia and Bob move the chessmen in turn. Every time a player will choose a chessman, and move it to the left without going over any other chessmen or across the left edge. The player can freely choose number of steps the chessman moves, with the constraint that the chessman must be moved at least ONE step and one grid can at most contains ONE single chessman. The player who cannot make a move loses the game.

Georgia always plays first since "Lady first". Suppose that Georgia and Bob both do their best in the game, i.e., if one of them knows a way to win the game, he or she will be able to carry it out.

Given the initial positions of the $n$ chessmen, can you predict who will finally win the game? 

## 输入格式

The first line of the input contains a single integer $T (1 \leq T \leq 20)$, the number of test cases. Then $T$ cases follow. Each test case contains two lines. The first line consists of one integer $N (1 \leq N \leq 1000)$, indicating the number of chessmen. The second line contains $N$ different integers $P_1, P_2 \dots P_n (1 \leq P_i \leq 10000)$, which are the initial positions of the $n$ chessmen.

## 输出格式

For each test case, prints a single line, "Georgia will win", if Georgia will win the game; "Bob will win", if Bob will win the game; otherwise 'Not sure'.

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
