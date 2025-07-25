# [USACO08DEC] Hay For Sale S

## 题目描述

Farmer John suffered a terrible loss when giant Australian cockroaches ate the entirety of his hay inventory, leaving him with nothing to feed the cows. He hitched up his wagon with capacity C (1 <= C <= 50,000) cubic units and sauntered over to Farmer Don's to get some hay before the cows miss a meal.

Farmer Don had a wide variety of H (1 <= H <= 5,000) hay bales for sale, each with its own volume (1 <= V\_i <= C). Bales of hay, you know, are somewhat flexible and can be jammed into the oddest of spaces in a wagon.

FJ carefully evaluates the volumes so that he can figure out the largest amount of hay he can purchase for his cows.

Given the volume constraint and a list of bales to buy, what is the greatest volume of hay FJ can purchase?  He can't purchase partial bales, of course. Each input line (after the first) lists a single bale FJ can buy.

约翰遭受了重大的损失：蟑螂吃掉了他所有的干草，留下一群饥饿的牛．他乘着容量为C(1≤C≤50000)个单位的马车，去顿因家买一些干草．  顿因有H(1≤H≤5000)包干草，每一包都有它的体积Vi(l≤Vi≤C).约翰只能整包购买，

他最多可以运回多少体积的干草呢？


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
