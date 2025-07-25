# [USACO5.3] 校园网Network of Schools

## 题目描述

有一些学校会向其他学校分享软件，即如果这个学校得到了软件，那么在分享列表中的学校也会得到软件。注意这种关系是单向的，即如果 $a$ 在 $b$ 的列表中，那么 $b$ 不一定在 $a$ 的列表中。

现在，你需要向其中一些学校下发新软件。为了节约下发软件的成本，你需要回答以下两个问题。

1. 至少需要向几个学校下发新软件，可以使得所有学校均获得新软件。
2. 定义一次扩展为在某个学校的分享列表中增加一个学校。至少需要进行几次扩展，才可以使得无论对哪个学校**仅下发一次软件**就可以使得所有学校获得新软件。

两个问题相互独立。

## 输入格式

输入文件的第一行包括一个正整数 $N$，表示学校数目。学校的编号为数字 $1$ 到 $N$。

接下来 $N$ 行，每行都表示一个分享列表，第 $i+1$ 行为学校 $i$ 的分享列表中的学校编号。每个列表用 $0$ 结束，空列表只用一个 $0$ 表示。

## 输出格式

你的程序应该在输出文件中输出两行。

第一行应该包括一个正整数，表示问题 $1$ 的解。

第二行应该包括一个非负整数，表示问题 $2$ 的解。

## 提示

$2 \le N \le 100$。

题目翻译来自 NOCOW。

USACO Training Section 5.3

## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
