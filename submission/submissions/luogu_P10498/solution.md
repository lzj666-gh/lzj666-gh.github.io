# P10498 题解

## 题目大意

根据题目模拟操作，输出 $t$ 秒后石头最多的格子里有多少个石头。

## 分析

首先，$1 \le t \le 10^8$，暴力枚举必然超时，我们发现，操作序列的长度极短，仅有 $1$ 至 $6$，所以每 $60$ 秒为一个周期，所有操作序列均会回到第一个操作，然后循环，故考虑矩阵快速幂加速递推。

先要考虑如何构建矩阵。

### 一、考虑放置操作

我们先将其简化一下：只考虑网格是一维，且每个格子上的操作也只有一种的情况。

假设我们输入的数据为：

```
1 3 2 3
012
0
1
2
```

根据题目，我们可以知道，每秒钟我们在第一个格子上放 $0$ 个石头，在第二个格子上放 $1$ 个石头，在第二个格子上放 $2$ 个石头。

然后让我们思考一下如何创建状态矩阵，三个时刻每一格石头的个数即为 `0 0 0`，`0 1 2`，`0 2 4`。

我们发现每一秒某个格子上增加的石头数量都是一样的。

我们将这三个网格上的石头的数量设为 $a_1,a_2,a_3$，代表第 $0$ 秒时的状态（转移前的状态），$a_1',a_2',a_3'$ 表示第 $1$ 秒时的状态(转移后的状态)。

通过分析我们可以列出下列表达式：

$$
a_1' = 1 \times a_1 + 0 \\
a_2' = 1 \times a_2 + 1 \\
a_3' = 1 \times a_3 + 2
$$

变换一下：

$$
a_1' = 1 \times a_1 + 0 \times a_2 + 0 \times a_3 + 0 \\
a_2' = 0 \times a_1 + 1 \times a_2 + 0 \times a_3 + 1 \\
a_3' = 0 \times a_1 + 0 \times a_2 + 1 \times a_3 + 2
$$

但是还要解决一个问题，那就是结尾加上去的 $0,1,2$。

我们知道结尾加上的数是不会随着时间的变化而变化的，所以我们设 $a_0 = 1$，则：

$$
a_0 = a_0 \\
0 = 0 \times a_0 \\
1 = 1 \times a_0 \\
2 = 2 \times a_0
$$

将其与上面的式子结合我们就可以得到：

$$
a_0' = 1 \times a_1 + 0 \times a_1 + 0 \times a_2 + 0 \times a_3 \\
a_1' = 0 \times a_1 + 1 \times a_1 + 0 \times a_2 + 0 \times a_3 \\
a_2' = 1 \times a_1 + 0 \times a_1 + 1 \times a_2 + 0 \times a_3 \\
a_3' = 2 \times a_1 + 0 \times a_1 + 0 \times a_2 + 1 \times a_3
$$

（$a_0'$ 为 $a_0$ 转移后的值）

这样我们就得到了状态矩阵：

$$
\begin{bmatrix}
1 & 0 & 0 & 0 
\end{bmatrix}
$$

和转移矩阵：

$$
\begin{bmatrix}
1 & 0 & 1 & 2 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 二、考虑移动操作

若当前状态矩阵为：

$$

\begin{bmatrix}
a_0 & a_1 & a_2 & a_3 
\end{bmatrix}
=
\begin{bmatrix}
1 & 2 & 3 & 4 
\end{bmatrix}
$$

变化一下：

$$
a_0' = 1 \times a_1 + 0 \times a_1 + 0 \times a_2 + 0 \times a_3 \\
a_1' = 0 \times a_1 + 0 \times a_1 + 0 \times a_2 + 0 \times a_3 \\
a_2' = 0 \times a_1 + 1 \times a_1 + 1 \times a_2 + 0 \times a_3 \\
a_3' = 0 \times a_1 + 0 \times a_1 + 0 \times a_2 + 1 \times a_3
$$

所以转移矩阵为：

$$
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

矩阵的构建就实现完了。

### 三、考虑代码实现

设 $\forall i \in [1,n],j \in [1,m],num(i,j) = (i - 1) \times m + j$。

把网格看做 $n \times m$ 的一维向量，定义 $1$ 行 $n \times m + 1$ 列的状态矩阵 $F$，下标为 $0$ 至 $n \times m$，其中 $F_{num(i,j)}$ 记录格子 $(i,j)$ 中石头的个数。

特别地，令 $F_0$ 始终等于 $1$。

$F$ 会随着时间的增长而不断变化。设 $F_k$表示 $k$ 秒之后的状态矩阵。

在游戏开始时，根据题意和 $F$ 的定义，有：

$$
F_0
=
\begin{bmatrix}
1 & 0 & 0 & \cdots & 0 
\end{bmatrix}
$$

注意到操作序列的长度不超过 $6$，而 $1$ 至 $6$ 的最小公倍数是 $60$，所以每经过 $60$ 秒，所有操作序列都会重新处于最开始的字符处。我们可以统计出第 $k$ 秒（$1 \le k \le 60$）各个格子执行了什么字符，第 $k + 60$ 秒执行的字符与第 $k$ 秒一定是相同的。

对于 $1$ 至 $60$ 之间的每个 $k$，各个格子在第 $k$ 秒执行的操作字符可以构成一个转移矩阵 $A_k$，矩阵行、列下标都为 $0$ 至 $n \times m$。

构造方法如下：

1. 若网格 $(i,j)$ 第 $k$ 秒的操作字符为 `N`，且 $i > 1$，则令 $A_k[num(i,j),num(i - 1, j)] = 1$，表示将石头推至上方的格子。字符 `W`，`S` 与 `E` 类似。

1. 若网格 $(i,j)$ 第 $k$ 秒的操作字符为数字 $x$，则令 $A_k[0,num(i, j)] = x,A_k[num(i,j),num(i,j)] = 1$，表示该格中原有的石头不动，再拿 $x$ 块石头。

1. 令 $A_k[0,0] = 1$。

1. 令 $A_k$ 剩余部分均为 $0$。

上述构造实际上把状态矩阵的第 $0$ 列作为"石头来源"，$A_k[0,0] = 1$ 保证了 $F_0$ 始终为 $1$，$A_k[0,num(i, j)] = x$ 相当于从"石头来源"获取 $x$ 个石头，放到格子 $(i,j)$ 中。

使用矩阵乘法加速递推，遇到常数项时，经常需要在状态矩阵中添加一个额外的位置，始终存储常数 $1$，并乘上转移矩阵中适当的系数，累加到状态矩阵的其他位置。

### 四、考虑答案统计

设：

$$
A = \displaystyle \prod_{i = 1}^{60} A_i $$

$$
t = q \times 60 + r(0 \le r \lt 60)
$$

根据上面的讨论：

$$
F_t = F_0 \cdot A^q \cdot \displaystyle \prod_{i = 1}^r A_i
$$

使用矩阵乘法和快速幂计算该式，$F_t$ 第 $1$ 至 $n \times m$ 列中的最大值即为所求。

## AC Code


```cpp
#include <bits/stdc++.h>

using namespace std;

#define ll long long

const int N = 10, M = 65;

struct matrix{ // 矩阵 
	ll c[M][M];
	matrix(){memset(c, 0, sizeof c);} // 生成函数：初始值均为0 
};

int n, m, t, act, x, y;
ll mx;
int idx[N][N], now[N][N];
matrix cg[M], sum, ans;
char c, seq[N][N];

matrix operator*(matrix a, matrix b){ // 新定义矩阵乘 
	matrix u;
	for(int i = 0; i <= n * m; i ++)
		for(int j = 0; j <= n * m; j ++)
			for(int k = 0; k <= n * m; k ++)
				u.c[i][j] += a.c[i][k] * b.c[k][j];
	return u;
}

int gt(int a, int b){return (a - 1) * m + b;} // 将网格中的点降维 

matrix qpow(matrix a, int b){ // 矩阵快速幂 
	matrix u, x = a;
	for(int i = 0; i < M; i ++)
		u.c[i][i] = 1;
	for(; b; b >>= 1){
		if(b & 1) u = u * x;
		x = x * x;
	}
	return u;
}

int main() {
	scanf("%d %d %d %d\n", &n, &m, &t, &act);
	for(int i = 1; i <= n; i ++){
		for(int j = 1; j <= m; j ++){
			scanf("%c", &c);
			idx[i][j] = c - '0' + 1;
		}
		scanf("\n");
	}
	for(int i = 1; i <= act; i ++)
		scanf("%s", seq[i]);
	for(int tim = 1; tim <= 60; tim ++){ // 生成前60次转移矩阵 
		for(int i = 1; i <= n; i ++){
			for(int j = 1; j <= m; j ++){
				x = idx[i][j], y = now[i][j];
				if(isdigit(seq[x][y])){ // 操作字符为数字 
					cg[tim].c[0][gt(i, j)] = seq[x][y] - '0'; // 从“石头来源”取x个石头 
					cg[tim].c[gt(i, j)][gt(i, j)] = 1; // 原来的石头数不变 
				}
				// 操作字符为NWSE 
				if(seq[x][y] == 'N' && i > 1) cg[tim].c[gt(i, j)][gt(i - 1, j)] = 1;
				if(seq[x][y] == 'W' && j > 1) cg[tim].c[gt(i, j)][gt(i, j - 1)] = 1;
				if(seq[x][y] == 'S' && i < n) cg[tim].c[gt(i, j)][gt(i + 1, j)] = 1;
				if(seq[x][y] == 'E' && j < m) cg[tim].c[gt(i, j)][gt(i, j + 1)] = 1;
				// 该位操作位数+1 
				now[i][j] = (y + 1) % strlen(seq[x]);
			}
		}
		cg[tim].c[0][0] = 1;
	}
	// 统计前60次转移 
	sum = cg[1];
	for(int i = 2; i <= 60; i ++)
		sum = sum * cg[i];
	// 快速幂计算每60秒后的矩阵 
	ans.c[1][0] = 1;
	ans = ans * qpow(sum, t / 60);
	// 剩余的不到60次操作 
	for(int i = 1; i <= t % 60; i ++)
		ans = ans * cg[i];
	// 统计最大石头数 
	for(int i = 1; i <= n * m; i ++)
		mx = max(mx, ans.c[1][i]);
	printf("%lld\n", mx);
	return 0;
}
```