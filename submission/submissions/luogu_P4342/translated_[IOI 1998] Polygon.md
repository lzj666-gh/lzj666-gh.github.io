# [IOI 1998] Polygon (翻译版)

## 题目描述

# 题目可能有些许修改，但大意一致

多边形是一个玩家在一个有n个顶点的多边形上的游戏，如图所示，其中n＝4。每个顶点用整数标记，每个边用符号+（加）或符号*（乘积）标记。

![](https://cdn.luogu.org/upload/pic/16086.png)

第一步，删除其中一条边。随后每一步： 

选择一条边连接的两个顶点V1和V2，用边上的运算符计算V1和V2得到的结果来替换这两个顶点。 

游戏结束时，只有一个顶点，没有多余的边。

如图所示，玩家先移除编号为3的边。之后，玩家选择计算编号为1的边，然后计算编号为4的边，最后，计算编号为2的边。结果是0。

![](https://cdn.luogu.org/upload/pic/16088.png)

（翻译者友情提示：这里每条边的运算符旁边的数字为边的编号，不拿来计算）

编写一个程序，给定一个多边形，计算最高可能的分数。

## 输入格式

输入描述一个有n个顶点的多边形，它包含两行。第一行是数字n，为总边数。

第二行描述这个多边形，一共有2n个读入，每两个读入中第一个是字符，第二个是数字。

第一个字符为第一条边的计算符号(t代表相加，x代表相乘)，第二个代表顶点上的数字。首尾相连。 

3 < = n < = 50

对于任何一系列的操作，顶点数字都在[-32768,32767]的范围内。

## 输出格式

第一行，输出最高的分数。在第二行，它必须写出所有可能的被清除后的边仍能得到最高得分的列表，必须严格递增。

感谢@2016c01 提供的翻译

## 输入格式

Your program is to read from standard input. The input describes a polygon with N vertices. It contains two lines. On the first line is the number N. The second line contains the labels of edges 1, ..., N, interleaved with the vertices' labels (first that of the vertex between edges 1 and 2, then that of the vertex between edges 2 and 3, and so on, until that of the vertex between edges N and 1), all separated by one space. An edge label is either the letter t (representing +) or the letter x (representing *). 

3 <= N <= 50 


For any sequence of moves, vertex labels are in the range [-32768,32767]. 


## 输出格式

Your program is to write to standard output. On the first line your program must write the highest score one can get for the input polygon. On the second line it must write the list of all edges that, if removed on the first move, can lead to a game with that score. Edges must be written in increasing order, separated by one space.


## 时空限制

时间限制: 1000 ms
内存限制: 128 MB
