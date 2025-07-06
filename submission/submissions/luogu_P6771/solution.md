# P6771 题解

> [P6771](https://www.luogu.com.cn/problem/P6771)

这是一道很明显的 dp 问题。

首先 dp 最重要的三要素是：动态表示、动态转移、初始状态。  
只要这三个要素搞明白了，基本就能把这题做出来了。

### solution

让我们来看看这题的动态表示、动态转移和初始状态。

**状态表示**：  
$dp_{i,j}$ 表示用前 $i$ 种方块是否可以拼成高度 $j$  

**状态转移**：  
$
dp_{i,j}=
\begin{cases}\\\\\\\\\\\end{cases}
\begin{matrix}
dp_{i-1,j} && \text{用}0\text{块第}i\text{种方块}\\
dp_{i-1,j-h_{i}} && \text{用}1\text{块第}i\text{种方块}\\
&\ldots&\\
dp_{i-1,j-k\times h_{i}} && \text{用}k\text{块第i种方块}\\
&\ldots&\\
dp_{i-1,j-c_{i}\times h_{i}} && \text{用}c_{i}\text{块第}i\text{种方块}\\
\end{matrix}$  
$
dp_{i,j}|=dp{i,j-k\times h_{i}};(h_{i}\le j\le a_{i}, 1\le k\le c_i)
$  

**初始状态**：  
$dp_{i,j}=\mathrm{false};dp_{0,0}=\mathrm{true}$


最后物品维可以直接省掉，即：  
$dp_{j}|=dp_{j-k\times h_{i}};(h_{i}\le j\le a_{i}, 1\le k\le c_i)$

那么写出这三要素就很容易写出代码了

### code

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<string>
#define line cout << endl
using namespace std;

const int NR = 405;
struct node {
	int h, a, c;
};
node e[NR];
int n;
bool dp[40005];

bool cmp (node x, node y) {
	return x.a < y.a; 
}

int main () {
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> e[i].h >> e[i].a >> e[i].c;
	dp[0] = true;
	sort (e + 1, e + n + 1, cmp);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= e[i].c; j++) {
			for (int k = e[i].a; k >= e[i].h; k--) {
				dp[k] |= dp[k - e[i].h];//动态转移方程
			}
		}
	}
	for (int i = e[n].a; i >= 0; i--) {
		if (dp[i]) {
			cout << i << endl;
			break;
		}
	}
	return 0;
}
```