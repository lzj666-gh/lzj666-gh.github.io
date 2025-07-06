# Physical Education Lessons

## 题目描述

This year Alex has finished school, and now he is a first-year student of Berland State University. For him it was a total surprise that even though he studies programming, he still has to attend physical education lessons. The end of the term is very soon, but, unfortunately, Alex still hasn't attended a single lesson!

Since Alex doesn't want to get expelled, he wants to know the number of working days left until the end of the term, so he can attend physical education lessons during these days. But in BSU calculating the number of working days is a complicated matter:

There are $ n $ days left before the end of the term (numbered from $ 1 $ to $ n $ ), and initially all of them are working days. Then the university staff sequentially publishes $ q $ orders, one after another. Each order is characterised by three numbers $ l $ , $ r $ and $ k $ :

- If $ k=1 $ , then all days from $ l $ to $ r $ (inclusive) become non-working days. If some of these days are made working days by some previous order, then these days still become non-working days;
- If $ k=2 $ , then all days from $ l $ to $ r $ (inclusive) become working days. If some of these days are made non-working days by some previous order, then these days still become working days.

Help Alex to determine the number of working days left after each order!

## 输入格式

The first line contains one integer $ n $ , and the second line — one integer $ q $ ( $ 1<=n<=10^{9} $ , $ 1<=q<=3·10^{5} $ ) — the number of days left before the end of the term, and the number of orders, respectively.

Then $ q $ lines follow, $ i $ -th line containing three integers $ l_{i} $ , $ r_{i} $ and $ k_{i} $ representing $ i $ -th order ( $ 1<=l_{i}<=r_{i}<=n $ , $ 1<=k_{i}<=2 $ ).

## 输出格式

Print $ q $ integers. $ i $ -th of them must be equal to the number of working days left until the end of the term after the first $ i $ orders are published.

## 时空限制

时间限制: 1000 ms
内存限制: 250 MB
