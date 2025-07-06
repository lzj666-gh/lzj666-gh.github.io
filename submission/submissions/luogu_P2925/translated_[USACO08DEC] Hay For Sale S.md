# [USACO08DEC] Hay For Sale S (翻译版)

## 题目描述

## 题目描述
农民 John 面临一个很可怕的事，因为防范力度不大所以他存储的所有稻草都被蟑螂吃光了，他将面临没有稻草喂养奶牛的局面。在奶牛断粮之前，John 拉着他的马车到农民 Don 的农场中买一些稻草给奶牛过冬。已知 John 的马车可以装的下 $C(1\le C\le5\times10^4)$ 立方的稻草。

农民 Don 有 $H(1\le H\le5\times10^3)$ 捆体积不同的稻草可供购买，每一捆稻草有它自己的体积 $V_i(1\le V_i\le C)$。面对这些稻草 John 认真的计算如何充分利用马车的空间购买尽量多的稻草给他的奶牛过冬。

现在给定马车的最大容积 $C$ 和每一捆稻草的体积 $V_i$，John 如何在不超过马车最大容积的情况下买到最大体积的稻草？他不可以把一捆稻草分开来买。

## 输入格式：
第一行两个整数，分别为 $C$ 和 $H$。
第 $2$ 到 $H+1$ 行:每一行一个整数代表第 $i$ 捆稻草的体积 $V_i$。

## 输出格式：

一个整数，为 John 能买到的稻草的体积。

###### 修改 by zhangsenhao6728

## 输入格式

\* Line 1: Two space-separated integers: C and H

\* Lines 2..H+1: Each line describes the volume of a single bale: V\_i


## 输出格式

\* Line 1: A single integer which is the greatest volume of hay FJ can purchase given the list of bales for sale and constraints.


## 提示

The wagon holds 7 volumetric units; three bales are offered for sale with volumes of 2, 6, and 5 units, respectively.


Buying the two smaller bales fills the wagon.


## 时空限制

时间限制: 1500 ms
内存限制: 125 MB
