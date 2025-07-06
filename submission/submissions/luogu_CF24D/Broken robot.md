# Broken robot

## 题目描述

You received as a gift a very clever robot walking on a rectangular board. Unfortunately, you understood that it is broken and behaves rather strangely (randomly). The board consists of $ N $ rows and $ M $ columns of cells. The robot is initially at some cell on the $ i $ -th row and the $ j $ -th column. Then at every step the robot could go to some another cell. The aim is to go to the bottommost ( $ N $ -th) row. The robot can stay at it's current cell, move to the left, move to the right, or move to the cell below the current. If the robot is in the leftmost column it cannot move to the left, and if it is in the rightmost column it cannot move to the right. At every step all possible moves are equally probable. Return the expected number of step to reach the bottommost row.

## 输入格式

On the first line you will be given two space separated integers $ N $ and $ M $ ( $ 1<=N,M<=1000 $ ). On the second line you will be given another two space separated integers $ i $ and $ j $ ( $ 1<=i<=N,1<=j<=M $ ) — the number of the initial row and the number of the initial column. Note that, $ (1,1) $ is the upper left corner of the board and $ (N,M) $ is the bottom right corner.

## 输出格式

Output the expected number of steps on a line of itself with at least $ 4 $ digits after the decimal point.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
