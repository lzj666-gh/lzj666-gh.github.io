# UVA1194 题解

题目地址：[UVA1194 Machine Schedule](https://www.luogu.org/problemnew/show/UVA1194)

#### 二分图最小覆盖模型的要素

每条边有两个端点，二者至少选择一个。简称 $2$ 要素。

#### $2$ 要素在本题中的体现

每个任务要么在 $A$ 上以 $a_i$ 模式执行，要么在机器 $B$ 上以 $b_i$ 模式执行。

把 $A,B$ 的 $m$ 种模式分别作为 $m$ 个左部点和右部点，每个任务作为边连接左部 $a_i$ 节点和右部 $b_i$ 节点。

求这张二分图的最小覆盖，时间复杂度为 $O(nm)$ 。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N = 106;
int n, m, k, f[N], ans;
bool v[N];
vector<int> e[N];

bool dfs(int x) {
	for (unsigned int i = 0; i < e[x].size(); i++) {
		int y = e[x][i];
		if (v[y]) continue;
		v[y] = 1;
		if (!f[y] || dfs(f[y])) {
			f[y] = x;
			return 1;
		}
	}
	return 0;
}

inline void Machine_Schedule() {
	cin >> m >> k;
	for (int i = 1; i <= n; i++) e[i].clear();
	for (int i = 0; i < k; i++) {
		int x, y;
		scanf("%d %d %d", &i, &x, &y);
		e[x].push_back(y);
	}
	memset(f, 0, sizeof(f));
	ans = 0;
	for (int i = 1; i <= n; i++) {
		memset(v, 0, sizeof(v));
		ans += dfs(i);
	}
	cout << ans << endl;
}

int main() {
	while (cin >> n && n) Machine_Schedule();
	return 0;
}
```