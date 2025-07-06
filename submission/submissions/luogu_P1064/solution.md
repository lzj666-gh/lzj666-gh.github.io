# P1064 题解

### 这道题看起来比较难，但是如果整理好思路，非常简单。
-----
## 基本思路
既然物品分为主件和附件两类，且每个主件最多包含两个附件，那么我们不妨枚举所有的主件。那么，对于每次枚举，会有五种情况：
+ 什么都不买
+ 只买主件
+ 买主件和第一个附件
+ 买主件和第二个附件
+ 买主件和两个附件

只要把这五种情况最终的价值算出来，取最大值就可以了。

-----
## 如何开数组？
建立两个二维数组 $V_{65,3}$ 和 $P_{65,3}$，含义如题目描述。$V_{i, j}$ 和 $P_{i, j}$ 分别表示第 $i$ 个物品的第 $j$ 个附件的价格和重要度（当 $j = 0$ 时，表示主件）。

-----
## 如何预处理数组？
+ 如果是主件，则令 $V_{i, 0}, P_{i, 0} = \_v, \_p$。
+ 如果是物品 $\_q$ 的第 $j$ 个附件，则令 $V_{q,j}, P_{q,j} = \_v, \_p$。

-----
## 动态转移方程
我们可以用 $F_j$ 表示花费钱数为 $j$ 时，价格与重要度乘积的最大值。
易知：
+ 当 $F_j \geqslant V_{i, 0}$ 时，$F_j = \max\{F_j, F_{j - V{i, 0}} + V_{i, 0} \times P_{i, 0}\}$
+ 当 $F_j \geqslant (V_{i, 0} + V_{i, 1})$ 时，$F_j = \max\{F_j, F_{j - V{i, 0} - V_{i, 1}} + V_{i, 0} \times P_{i, 0} + V_{i, 1} \times P_{i, 1}\}$
+ 当 $F_j \geqslant (V_{i, 0} + V_{i, 2})$ 时，$F_j = \max\{F_j, F_{j - V{i, 0} - V_{i, 2}} + V_{i, 0} \times P_{i, 0} + V_{i, 2} \times P_{i, 2}\}$
+ 当 $F_j \geqslant (V_{i, 0} + V_{i, 1} + V_{i, 2})$ 时，$F_j = \max\{F_j, F_{j - V{i, 0} - V_{i, 1} - V_{i, 2}} + V_{i, 0} \times P_{i, 0} + V_{i, 1} \times P_{i, 1} + V_{i, 2} \times P_{i, 2}\}$

列出了状态转移方程，套背包公式就好了

-----
## 代码简化
**难道你真的要在 $\texttt{for}$ 循环内部写如此麻烦的数组下标吗？不怕写晕自己吗？**

对于这种数组下标很乱的状态转移方程，最好把下标写短一点。怎么写短呢？

观察一下刚才列出的状态转移方程，发现 $V_{i, j1} + V_{i, j2}$ 等下标被写了很多遍。不妨使用函数来计算这些值，在下标里面写函数调用。不妨：
+ 定义 $\texttt{cost2(int x, int y)}$ 计算 $V_{i, x} + V_{i, y}$、
+ 定义 $\texttt{cost3(int x, int y, int z)}$ 计算 $V_{i, x} + V_{i, y} + V_{i, z}$、
+ 定义 $\texttt{rpp(int x)}$ 计算 $V_{i, x} \times P_{i, x}$

于是，状态转移方程可以简化成这样：
+ 当 $F_j \geqslant V_{i, 0}$ 时，$F_j = \max\{F_j, F_{j - V{i, 0}} + \texttt{rpp(0)}\}$
+ 当 $F_j \geqslant \texttt{cost2(0, 1)}$ 时，$F_j = \max\{F_j, F_{j - \texttt{cost2(0, 1)}} + \texttt{rpp(0)} + \texttt{rpp(1)}\}$
+ 当 $F_j \geqslant \texttt{cost2(0, 2)}$ 时，$F_j = \max\{F_j, F_{j - \texttt{cost2(0, 2)}} + \texttt{rpp(0)} + \texttt{rpp(2)}\}$
+ 当 $F_j \geqslant \texttt{cost3(0, 1, 2)}$ 时，$F_j = \max\{F_j, F_{j - \texttt{cost3(0, 1, 2)}} + \texttt{rpp(0)} + \texttt{rpp(1)} + \texttt{rpp(2)}\}$

这样就显得好多了。

-----
## 完整 AC 代码
```cpp
//【P1064】金明的预算方案 - 洛谷 - 100
#include <iostream>
#include <algorithm> 

const int kMaxN = 32000, kMaxM = 60; // 常量名前带 k，符合命名规范
int v[kMaxM + 5][3], p[kMaxM + 5][3];
int f[kMaxN + 5];

int main() {
	int n, m;
	std::cin >> n >> m;
	for (int i = 1; i <= m; ++i) {
		int _v, _p, _q;
		std::cin >> _v >> _p >> _q;
		if (!_q) { // 是主件 
			v[i][0] = _v;
			p[i][0] = _p;
		} else {
			if (v[_q][1] == 0) { // 是第一个附件 
				v[_q][1] = _v;
				p[_q][1] = _p;
			} else { // 是第二个附件 
				v[_q][2] = _v;
				p[_q][2] = _p;
			}
		}
	}
	
	for (int i = 1; i <= m; ++i)
		for (int j = n; j >= 0; --j) {
        	// 用 lambda 表达式代替函数定义（C++11 偷懒专用)
			auto cost2 = [v, p, i](int x, int y) { return v[i][x] + v[i][y]; };
			auto cost3 = [v, p, i](int x, int y, int z) { return v[i][x] + v[i][y] + v[i][z]; };
			auto rpp = [v, p, i](int x) { return v[i][x] * p[i][x]; };
			
			if (j >= v[i][0]) // 够买主件 
				f[j] = std::max(f[j], f[j - v[i][0]] + rpp(0));
			if (j >= cost2(0, 1)) // 还够买第一个附件 
				f[j] = std::max(f[j], f[j - cost2(0, 1)] + rpp(0) + rpp(1));
			if (j >= cost2(0, 2)) // 还够买第二个附件 
				f[j] = std::max(f[j], f[j - cost2(0, 2)] + rpp(0) + rpp(2));
			if (j >= cost3(0, 1, 2)) // 还够买两个附件 
				f[j] = std::max(f[j], f[j - cost3(0, 1, 2)] + rpp(0) + rpp(1) + rpp(2));
		}
		
	std::cout << f[n] << std::endl;
}
```