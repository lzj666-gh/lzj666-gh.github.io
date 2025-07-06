# NAPTIME - Naptime

## 题目描述

Goneril is a very sleep-deprived cow. Her day is partitioned into N (3 <= N <= 3,830) equal time periods but she can spend only B (2 <= B < N) not necessarily contiguous periods in bed. Due to her bovine hormone levels, each period has its own utility U\_i (0 <= U\_i <= 200,000), which is the amount of rest derived from sleeping during that period. These utility values are fixed and are independent of what Goneril chooses to do, including when she decides to be in bed.  
  
 With the help of her alarm clock, she can choose exactly which periods to spend in bed and which periods to spend doing more critical items such as writing papers or watching baseball. However, she can only get in or out of bed on the boundaries of a period.  
  
 She wants to choose her sleeping periods to maximize the sum of the utilities over the periods during which she is in bed. Unfortunately, every time she climbs in bed, she has to spend the first period falling asleep and gets no sleep utility from that period.  
  
 The periods wrap around in a circle; if Goneril spends both periods N and 1 in bed, then she does get sleep utility out of period 1.  
  
 What is the maximum total sleep utility Goneril can achieve?

## 输入格式

_t_ – the number of test cases, then _t_ test cases follow.   
 Each test case takes the following form:  
 Two space-separated integers: _N_ and _B_, then _N_ lines follows  
 Each line contains a single integer, _U\_i_, between 0 and 200,000 inclusive

## 输出格式

For each test case output a single integer, the maximum total sleep utility Goneril can achieve.

## 时空限制

时间限制: 1000 ms
内存限制: 62 MB
