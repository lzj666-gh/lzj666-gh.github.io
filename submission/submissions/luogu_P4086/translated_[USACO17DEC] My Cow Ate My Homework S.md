# [USACO17DEC] My Cow Ate My Homework S (翻译版)

## 题目描述

### 题目描述

在你的牛历史课上，你被布置了一份相当长的作业，包含 $N$ 个问题（$3 \leq N \leq 100,000$），每个问题的得分是一个在 0 到 10,000 之间的整数。按照惯例，你的老师计划通过去掉你得分最低的一个问题，然后对剩余问题的得分取平均来给出最终成绩。不幸的是，你的宠物奶牛 Bessie 刚刚吃掉了你前 $K$ 个问题的答案！（$K$ 可能小到 1，也可能大到 $N-2$）。

经过多次解释，你的老师终于相信了你的说法，并同意按照之前的方式对剩余的未被吃掉的部分作业进行评分——即去掉得分最低的问题（或在得分相同的情况下去掉其中一个），然后对剩余问题取平均。

请输出所有能够使你获得最高可能成绩的 $K$ 值，并按升序排列。

### 输入格式

输入的第一行包含 $N$，第二行包含 $N$ 个作业问题的得分。

### 输出格式

请逐行输出所有能够使你获得最高可能成绩的 $K$ 值。

### 说明/提示

如果 Bessie 吃掉了前两个问题，那么剩余的得分是 9、2 和 7。去掉最低分并取平均后，最终成绩为 8，这是可能的最高成绩。

## 输入格式

The first line of input contains $N$, and the next line contains the scores on the $N$ homework questions.


## 输出格式

Please output, one value per line, all values of $K$ which would have earned you the maximum possible score.


## 提示

If Bessie eats the first two questions, then the remaining scores are 9, 2, and 7. Removing the minimum and averaging, we get a final grade of 8, which is the highest possible.


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
