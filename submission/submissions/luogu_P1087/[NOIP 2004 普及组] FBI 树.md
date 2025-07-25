# [NOIP 2004 普及组] FBI 树

## 题目描述

我们可以把由 0 和 1 组成的字符串分为三类：全 0 串称为 B 串，全 1 串称为 I 串，既含 0 又含 1 的串则称为 F 串。

FBI 树是一种二叉树，它的结点类型也包括 F 结点，B 结点和 I 结点三种。由一个长度为 $2^N$ 的 01 串 $S$ 可以构造出一棵 FBI 树 $T$，递归的构造方法如下：

1. $T$ 的根结点为 $R$，其类型与串 $S$ 的类型相同；
2. 若串 $S$ 的长度大于 $1$，将串 $S$ 从中间分开，分为等长的左右子串 $S_1$ 和 $S_2$；由左子串 $S_1$ 构造 $R$ 的左子树 $T_1$，由右子串 $S_2$ 构造 $R$ 的右子树 $T_2$。

现在给定一个长度为 $2^N$ 的 01 串，请用上述构造方法构造出一棵 FBI 树，并输出它的后序遍历序列。


## 输入格式

第一行是一个整数 $N(0 \le N \le 10)$，  

第二行是一个长度为 $2^N$ 的 01 串。


## 输出格式

一个字符串，即 FBI 树的后序遍历序列。


## 提示

对于 $40\%$ 的数据，$N \le 2$；

对于全部的数据，$N \le 10$。


noip2004普及组第3题


## 时空限制

时间限制: 1000 ms
内存限制: 125 MB
