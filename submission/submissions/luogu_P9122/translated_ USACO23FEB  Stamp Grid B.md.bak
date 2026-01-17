# [USACO23FEB] Stamp Grid B (翻译版)

## 题目描述

### 题目描述

盖章绘画是一幅黑白画，绘制在一个 $N \times N$ 的画布上，其中某些格子被涂黑，而其他格子为空白。它可以用一个 $N \times N$ 的字符数组表示（$1 \leq N \leq 20$）。如果数组的第 $i$ 行第 $j$ 列的值为 `*`，说明该格子被涂黑；如果为 `.`，则说明该格子为空白。

Bessie 想要完成一幅盖章绘画，因此 Farmer John 借给了她一块 $K \times K$（$1 \leq K \leq N$）的盖章，以及一块空的 $N \times N$ 画布。Bessie 可以将盖章顺时针旋转 $90^\circ$，并在画布上的任意位置盖章，只要盖章完全在画布范围内即可。形式化地说，盖章时，Bessie 选择整数 $i,j$，满足 $i \in [1,N-K+1]$ 且 $j \in [1,N-K+1]$；对于每个 $(i',j')$，其中 $1 \leq i',j' \leq K$，画布上的格子 $(i+i'-1,j+j'-1)$ 会被涂黑，如果盖章在 $(i',j')$ 处有墨迹。Bessie 可以在每次盖章之前旋转盖章。一旦画布上的某个格子被涂黑，就会保持涂黑状态。

Farmer John 想知道，Bessie 是否可以用他的盖章完成她想要的盖章绘画。对于每个 $T$（$1 \leq T \leq 100$）个测试用例，帮助 Farmer John 回答这个问题。

### 输入格式

第一行包含一个整数 $T$，表示测试用例的数量。

每个测试用例以一个整数 $N$ 开始，接下来是 $N$ 行，每行包含由 `*` 和 `.` 构成的字符串，表示 Bessie 想要的盖章绘画。接下来的行包含一个整数 $K$，随后是 $K$ 行，每行包含由 `*` 和 `.` 构成的字符串，表示 Farmer John 的盖章。

相邻的测试用例之间用空行分隔。

### 输出格式

对于每个测试用例，输出一行 `YES` 或 `NO`。

### 样例 1 的解释

在第一个测试用例中，Bessie 可以按以下顺序完成盖章：

1. 在 $(1,1)$ 处盖章  
2. 在 $(1,2)$ 处盖章  
3. 在 $(2,1)$ 处盖章  

在第二个测试用例中，Bessie 可以按以下顺序完成盖章：

1. 在 $(2,2)$ 处盖章  
2. 在 $(2,1)$ 处盖章  
3. 顺时针旋转 $90^\circ$  
4. 顺时针旋转 $90^\circ$  
5. 在 $(1,2)$ 处盖章  

在第三个测试用例中，无法涂黑中间格子，因此无法完成绘画。

在第四个测试用例中，Bessie 可以按以下顺序完成盖章：

1. 顺时针旋转 $90^\circ$  
2. 在 $(1,1)$ 处盖章  
3. 在 $(1,2)$ 处盖章  
4. 在 $(2,2)$ 处盖章

## 输入格式

The first line of input contains $T$, the number of test cases.

Each test case starts with an integer $N$ followed by $N$ lines, each containing a string of `*`s and `.`s, representing Bessie's desired stamp painting. The next line contains $K$ and is followed by $K$ lines, each containing a string of `*`s and `.`s, representing Farmer John's stamp.

Consecutive test cases are separated by newlines. 

## 输出格式

For each test case, output `YES` or `NO` on separate lines. 

## 提示

### Explanation for Sample 1

In the first test case, Bessie can perform the following sequence of stampings:

1. Stamp at $(1,1)$
2. Stamp at $(1,2)$
3. Stamp at $(2,1)$

In the second test case, Bessie can perform the following sequence of stampings:

1. Stamp at $(2,2)$
2. Stamp at $(2,1)$
3. Rotate $90^{\circ}$
4. Rotate $90^{\circ}$
5. Stamp at $(1,2)$

In the third test case, it is impossible to paint the middle cell.

In the fourth test case, Bessie can perform the following sequence of stampings:

1. Rotate $90^{\circ}$
2. Stamp at $(1,1)$
3. Stamp at $(1,2)$
4. Stamp at $(2,2)$

## 时空限制

时间限制: 2000 ms
内存限制: 256 MB
