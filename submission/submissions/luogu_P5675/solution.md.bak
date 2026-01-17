# P5675 题解

2022/08/04，fix：第一堆石子应小于其他堆

# Nim类石子游戏介绍

（学过的话可以跳到**题目分析**部分

## $\rm{Description}$

给定数列 $n_1, n_2, \cdots, n_k$，表示有 $k$ 堆物品，第 $i$ 堆物品的数量为 $n_i$。

两人轮流从中取物品，规则：**每次可以从一堆中拿走任意正整数个物品**。先拿走最后一根的人胜利。

对于给定的数列，判断先手是否必胜，若必胜，输出第一次应该在哪堆取多少物品。

## $\rm{Solution}$

### 必胜必败分析

**先手必胜，当且仅当 $n_1\oplus n_2\oplus\cdots\oplus n_k\neq 0$。**

对于其他 `nim游戏` ，假设状态表示为 $(a_1, a_2, \cdots,a_n)$，那么先手必胜，当且仅当 $\operatorname{sg}(a_1)\oplus \operatorname{sg}(a_2)\oplus\cdots\oplus \operatorname{sg}(a_n)$，证明BFS。

本题中 $\operatorname{sg}(i)=i$，所以有上面的结论。

### 证明

设 $s=n_1\oplus n_2\oplus\cdots\oplus n_k$.

也就是证明：

1. 当 $s \neq 0$ 时，存在一种取法，使得 $s=0$.
2. 当 $s=0$ 时，无论怎么取物品，$s$ 都不等于 $0$.

#### 命题一

因为 $s\neq 0$，根据异或的定义，存在一堆物品 $i$，满足 $n_i\oplus s<n_i$ ，那么就从第 $i$ 堆取走 $n_i-(n_i\oplus s)$，剩下 $n_i\oplus s$ 个物品。

此时，$s_{\rm{new}}=n_1\oplus n_2\cdots\oplus n_k\oplus s=s\oplus s=0$.

所以命题一成立。

#### 命题二

反证法。若否，则 $s=0$ 时，存在一种取物品的方法使得 $s_{\rm{new}}=0$.

设取走第 $i$ 堆的若干物品，第 $i$ 堆剩余 $n_i'$ 个物品。

所以 $s_{\rm{new}}=n_1\oplus n_2\cdots\oplus n_i'\oplus\cdots\oplus n_k=0=s$.

把 $s$ 的定义式代入，得到 $n_i=n_i'$，产生矛盾。

所以命题二成立。

# 题目分析

显然，可以看出这个问题与`Nim`类游戏相关。`Nim`类游戏先手**必胜，当且仅当每堆石子的数量的异或和不为 $0$**。

所以Alice先手必败仅有两种情况：

1. 异或和为 $0$；
2. 异或和不为 $0$，但`Alice`选择的第一堆石子无法使异或和变成0.

第一种情况容易处理，对于第二种情况，可以发现：**只有指定选的第一堆石子数量，小于其他堆的异或和**时，才能够做到：删去一堆棋子，异或和也不为 $0$.

所以就可以枚举`Alice`先选择哪一堆，然后每次`DP`处理：有多少种选择方法使得异或和等于 $j$.

通过数学方法进行分析，容易得到上一段中的 $j\in[0, 256]$，于是直接二维 `DP` 即可。

`DP`状态：$f_{i, j}$ 表示，当固定一堆不选时，其余的前 $i$ 堆，异或和为 $j$ 的方案数量。

每次从上一行转移过来，具体看代码就行了。

## 代码

```c++
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int MAXN = 208, MAXJ = 270, mod = 1e9 + 7; 
int n;
int a[MAXN];
int dp[MAXN][MAXJ]; //dp[i][j]表示，当固定一堆不选时，其余的前i堆，异或和为j的方案数量 
signed main() {
	scanf("%lld", &n);
	for(int i = 1; i <= n; i++) {
		scanf("%lld", &a[i]);
	}
	int ans = 0; dp[0][0] = 1;
	for(int i = 1; i <= n; i++) {
		for(int j = 1; j <= n; j++) {
			for(int k = 0; k < 256; k++) {
				if(i == j) dp[j][k] = dp[j-1][k];
				else dp[j][k] = (dp[j - 1][k] + dp[j - 1][k ^ a[j]]) % mod;
			} 
		}
		for(int j = a[i]; j < 256; j++) {
			ans = (ans + dp[n][j]) % mod;
		}
	}
	cout << ans << endl;
	return 0;
}
```

