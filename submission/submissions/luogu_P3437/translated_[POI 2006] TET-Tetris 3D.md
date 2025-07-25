# [POI 2006] TET-Tetris 3D (翻译版)

## 题目描述

### 题目描述

最近，有人发明了一种三维版的俄罗斯方块。和二维版本类似，一些立方体按照一定的顺序掉落，直到碰到别的方块或是地面才会停止掉落。立方体停止掉落后会一直保持掉落时的位置，直到游戏结束。

你的朋友决定以这个新版本的俄罗斯方块为背景，出一道题。给出每个立方体的掉落顺序和其掉落的轨迹，在所有方块完成掉落后求出最高方块的高度。在这个游戏中，方块均垂直下落，且方块不会旋转或翻转。为了方便描述，我们会建立一个空间直角坐标系，该坐标系的原点为地面的一角，并且坐标轴与地面边缘平行。

现在轮到你解决这个问题了。

### 输入格式

第一行三个整数 $D,S,N$，分别为地面的长度，宽度，和将要掉落的立方体数量。

接下来 $N$ 行，每行五个整数 $d_i,s_i,w_i,x_i,y_i$，描述一个掉落的立方体。其中 $d_i,s_i,w_i$ 分别代表立方体的长，宽，高。立方体的底面（即长 $\times$ 宽的那一面）将正对地面。立方体底面四个角在地面的投影坐标分别为 $(x_i,y_i)$，$(x_i+d_i,y_i)$，$(x_i,y_i+s_i)$，$(x_i+d_i,y_i+s_i)$。

### 输出格式

输出一个整数，即方块掉落结束后最高方块的高度。

### 数据范围

$1 \leq N \leq 20\,000$，$1 \leq D,S \leq 1\,000$，$d_i,s_i \geq 1$，$1 \leq w_i \leq 100\,000$，$0 \leq x_i,d_i+x_i \leq D$，$0 \leq y_i,s_i+y_i \leq S$。

## 输入格式

In the first line of the input there are three integers $D$, $S$ and $N$ ($1\le N\le 20\ 000$, $1\le D,S\le 1\ 000$), separated by single spaces and denoting respectively: the length and the depth of the platform and the number of blocks that are going to fall down on it. In the following $N$ lines the descriptions of subsequent blocks are given, one in each line.

Each description of a block consists of five integers: $d$,$s$,$w$,$x$ and $y$ ($1\le d$, $0\le x$, $d+x\le D$, $1\le s$, $0\le y$, $s+y\le S$, $1\le w\le 100\ 000$), representing a block of length $d$ depth $s$ and height $w$. This very block will be be falling down on the platform with its $d\times s$ face as the bottom, where the length and depth of the block are parallel to those of the platform. The coordinates of the vertices of the projection of the block on the platform are: $(x,y)$, $(x+d,y)$, $(x,y+s)$ and $(x+d,y+s)$.


## 输出格式

The first and only line of the standard output should contain exactly one integer, the height of the highest point of the arrangement of blocks after all have fallen down and stopped.


## 时空限制

时间限制: 1500 ms
内存限制: 256 MB
