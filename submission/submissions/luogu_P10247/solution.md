# P10247 题解

> 枚举，暴力，优化

## Solution

发现很多点的答案都可以是 $1$。

也就是说，只有 $x_i$ 或 $y_i$ 与 $x_1$ 或 $y_1$ 相等的 $i$ 才需要找到一个非 $1$ 的 $j$。

继续前行，不妨设其中一个值是与 $x_1$ 相等（与 $y_1$ 相等可以同理处理），我们把所有这样的元素单独拿出来。

对于其它的元素，显然没有一个值与 $x_1$ 相等。我们不妨在其中找到了一个元素 $(p, q)$（如果找不到，就退出即可，因为事实上这表明所有点的答案都是 $0$）。

那么又有很多点的答案可以是 $(p, q)$。只有最多两个点 $(\min(x_1, p), \max(x_1, p))$ 和 $(\min(x_1, q), \max(x_1, q))$ 不符合条件，我们 $\mathcal O(n)$ 扫一遍原数组即可。

时间复杂度 $\mathcal O(n)$。这玩意值域无关。

## Code

下面是一份参考实现。

```cpp
#include <bits/stdc++.h>

inline bool ok(int a, int b, int c, int d) {
	if (a == c || a == d || b == c || b == d) return false;
	return true;
}

#define MAXN 300001
int x[MAXN], y[MAXN], res[MAXN];
void solve(std::vector<std::pair<int, int>> &m, int n, int tar) {
	std::vector<int> pos;
	for (int i = 1; i <= n; ++i) if (x[i] != tar && y[i] != tar) pos.push_back(i);
	// for each m, try to find match tar.
	if (pos.empty()) return;
	int P = x[pos[0]], Q = y[pos[0]];
	for (auto [i, key] : m) if (key != P && key != Q) res[i] = pos[0];
	else /* O(1) * O(n) */ 
		for (int u : pos) if (x[u] != key && y[u] != key) res[i] = u;
}
int main() {
	int m, n; std::cin >> m >> n; std::vector<std::pair<int, int>> vX, vY;
	for (int i = 1; i <= n; ++i) std::cin >> x[i] >> y[i];
	for (int i = 2; i <= n; ++i) if (ok(x[1], y[1], x[i], y[i])) res[i] = 1, res[1] = i;
	else if (x[i] == x[1] || y[i] == x[1]) vX.push_back({i, x[i] ^ y[i] ^ x[1]});
	else vY.push_back({i, x[i] ^ y[i] ^ y[1]});
	solve(vX, n, x[1]), solve(vY, n, y[1]);
	for (int i = 1; i <= n; ++i) std::cout << res[i] << " \n"[i == n];
	return 0;
}
```