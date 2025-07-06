# Little Pony and Expected Maximum

## 题目描述

Twilight Sparkle was playing Ludo with her friends Rainbow Dash, Apple Jack and Flutter Shy. But she kept losing. Having returned to the castle, Twilight Sparkle became interested in the dice that were used in the game.

The dice has $ m $ faces: the first face of the dice contains a dot, the second one contains two dots, and so on, the $ m $ -th face contains $ m $ dots. Twilight Sparkle is sure that when the dice is tossed, each face appears with probability ![](https://cdn.luogu.com.cn/upload/vjudge_pic/CF453A/b5732959c34191186d5d84c95f93d0143eb6fff6.png). Also she knows that each toss is independent from others. Help her to calculate the expected maximum number of dots she could get after tossing the dice $ n $ times.

## 输入格式

A single line contains two integers $ m $ and $ n $ ( $ 1<=m,n<=10^{5} $ ).

## 输出格式

Output a single real number corresponding to the expected maximum. The answer will be considered correct if its relative or absolute error doesn't exceed $ 10^{-4} $ .

## 提示

Consider the third test example. If you've made two tosses:

1. You can get 1 in the first toss, and 2 in the second. Maximum equals to 2.
2. You can get 1 in the first toss, and 1 in the second. Maximum equals to 1.
3. You can get 2 in the first toss, and 1 in the second. Maximum equals to 2.
4. You can get 2 in the first toss, and 2 in the second. Maximum equals to 2.

The probability of each outcome is 0.25, that is expectation equals to:

![](https://cdn.luogu.com.cn/upload/vjudge_pic/CF453A/a611917193fd806daca7707d914db660d20dd0a4.png)You can read about expectation using the following link: http://en.wikipedia.org/wiki/Expected\_value

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
