# Bag of mice (翻译版)

## 题目描述

袋子里有$w$ 只白鼠和$b$ 只黑鼠 ，A和B轮流从袋子里抓，谁先抓到白色谁就赢。A每次随机抓一只，B每次随机抓完一只之后会有另一只随机老鼠跑出来。如果两个人都没有抓到白色则B赢。A先抓，问A赢的概率。

### 输入
一行两个数$w,b$ 。
### 输出
A赢的概率，误差$10^{-9}$ 以内。
### 数据范围
$0\le w,b\le 1000$ 。

## 输入格式

The only line of input data contains two integers $ w $ and $ b $ ( $ 0<=w,b<=1000 $ ).

## 输出格式

Output the probability of the princess winning. The answer is considered to be correct if its absolute or relative error does not exceed $ 10^{-9} $ .

## 提示

Let's go through the first sample. The probability of the princess drawing a white mouse on her first turn and winning right away is 1/4. The probability of the dragon drawing a black mouse and not winning on his first turn is 3/4 \* 2/3 = 1/2. After this there are two mice left in the bag — one black and one white; one of them jumps out, and the other is drawn by the princess on her second turn. If the princess' mouse is white, she wins (probability is 1/2 \* 1/2 = 1/4), otherwise nobody gets the white mouse, so according to the rule the dragon wins.

## 时空限制

时间限制: 2000 ms
内存限制: 250 MB
