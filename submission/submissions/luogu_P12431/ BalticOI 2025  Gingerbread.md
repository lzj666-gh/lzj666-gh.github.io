# [BalticOI 2025] Gingerbread

## 题目描述

Toruń has been known for its traditional gingerbread since the Middle Ages. Young Nicolaus would like to buy a set of $n$ boxes with gingerbread cookies in his favourite shop. The shop has very strict rules, though: Nicolaus initially obtains $n$ boxes that are already filled with cookies: the $i$-th box initially contains $a_{i}$ of them. Then, Nicolaus can order some extra cookies. He adds extra cookies to some boxes so that the greatest common divisor$\text{*}$ of the numbers of cookies in all of the boxes becomes equal to 1. It can be proven that this is always possible.

Help Nicolaus by calculating the smallest number of cookies that need to be added in order to make the greatest common divisor of all the numbers equal to 1.

$\text{*}$ The greatest common divisor (GCD) of multiple numbers is the largest positive integer that divides all of them without
remainder.

## 输入格式

The first line contains an integer $n\ (2 \leq n \leq 10^6)$, denoting the number of boxes.

The second line contains $n$ integers $a_{1}, a_{2}, \ldots, a_{n}\ (1 \leq a_{i} \leq 10^7)$, where the $i$-th integer $a_{i}$ denotes the initial number of cookies in the $i$-th box.

## 输出格式

Output one line with a single integer denoting the smallest number of cookies that Nicolaus should add to the boxes. If Nicolaus doesn't have to add any cookies to make the greatest common divisor of the numbers equal to 1, output 0.

## 提示

Explanation of the example: Indeed, the greatest common divisor (GCD) of 90, 84, and 140 is 2, so some cookies must be added. If we add only one cookie, we may obtain the quantities 91, 84, 140 with GCD of 7, or 90, 85, 140 with GCD of 5, or 90, 84, 141 with GCD of 3, so this is not enough. After adding two cookies, one to the first box, and one to the second box, we obtain the quantities 91, 85, 140 with GCD of 1; hence the answer is 2. Note that adding both cookies to the first box does not help: we obtain quantities 92, 84, 140 with GCD of 4.

### Scoring

| Subtask | Constraints | Points |
| :---: | :---: | :---: |
| 1 | $n=2$ | 17 |
| 2 | $n \leq 10$ | 34 |
| 3 | $n \leq 1000$ | 11 |
| 4 | No additional constraints. | 38 |


## 时空限制

时间限制: 2000 ms
内存限制: 256 MB
