# Zuma

## 题目描述

Genos recently installed the game Zuma on his phone. In Zuma there exists a line of $ n $ gemstones, the $ i $ -th of which has color $ c_{i} $ . The goal of the game is to destroy all the gemstones in the line as quickly as possible.

In one second, Genos is able to choose exactly one continuous substring of colored gemstones that is a palindrome and remove it from the line. After the substring is removed, the remaining gemstones shift to form a solid line again. What is the minimum number of seconds needed to destroy the entire line?

Let us remind, that the string (or substring) is called palindrome, if it reads same backwards or forward. In our case this means the color of the first gemstone is equal to the color of the last one, the color of the second gemstone is equal to the color of the next to last and so on.

## 输入格式

The first line of input contains a single integer $ n $ ( $ 1<=n<=500 $ ) — the number of gemstones.

The second line contains $ n $ space-separated integers, the $ i $ -th of which is $ c_{i} $ ( $ 1<=c_{i}<=n $ ) — the color of the $ i $ -th gemstone in a line.

## 输出格式

Print a single integer — the minimum number of seconds needed to destroy the entire line.

## 提示

In the first sample, Genos can destroy the entire line in one second.

In the second sample, Genos can only destroy one gemstone at a time, so destroying three gemstones takes three seconds.

In the third sample, to achieve the optimal time of two seconds, destroy palindrome 4 4 first and then destroy palindrome 1 2 3 2 1.

## 时空限制

时间限制: 2000 ms
内存限制: 500 MB
