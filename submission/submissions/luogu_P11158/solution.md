# P11158 题解

容易想到对于每个子矩形，考虑有多少种交换方案能使其合法。

显然，合法需要初始时至多只有一个关键点。分别讨论两种情况，下面令 $m = \dfrac{n}{2}$，$l$ 和 $r$ 表示这个子矩形的上下边界，$a$ 和 $b$ 表示左右边界。 

1. 初始没有关键点。由于 $p$ 构成一个排列，所以此时 $[l, r]$ 以外的 $p_i$ 都在 $[a,b]$ 之间。合法只能交换 $[l, r]$ 内的两个点或者外部的两个点，方案数是 $2\dbinom{m}{2} = m(m-1)$。
2. 初始只有一个关键点，此时 $[l,r]$ 外部只有一个关键点 $p_i \notin [a,b]$，方案数是 1。

枚举上下边界 $l,r$，只用求出当前有多少矩形没有关键点和只有一个关键点。前者可以由相邻关键点之间的间隙得到，后者可以由每个关键点的左右间隙得到。

用 set 维护所有关键点的 y 坐标，加入和删除一个点时只有当前点以及左右相邻点会有影响，直接统计即可。

```cpp
// They say that life is always easier
// After you let yourself come undone
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
using namespace std;
using ll = long long;
const int N = 2e5 + 10;
const int MOD = 998244353;
int n, m, a[N], x, y;
ll ans;
set<int> st;
// 统计没有关键点的方案数
void Calc(int len, int k) { 
	if(len >= m) x += k * (len - m + 1);
}
// 统计只有一个关键点的方案数，it 是这个关键点
void Get(set<int>::iterator it, int k) { 
	if(*it < 1 || *it > n) return ;
	int l = *prev(it), p = *it, r = *next(it);
	if(r - l - 1 < m) return ;
	int lef = max(l + 1, p - m + 1);
	int rig = min(p, r - m);
	y += k * (rig - lef + 1);
}
void Add(int k) {
	auto it = st.lower_bound(k);
	int l = *prev(it), r = *it;
	Calc(r - l - 1, -1), Get(prev(it), -1);
	Calc(k - l - 1, 1), Get(it, -1);
	Calc(r - k - 1, 1);
	st.insert(k);
	it = st.find(k);
	Get(prev(it), 1);
	Get(next(it), 1);
	Get(it, 1);
}
void Del(int k) {
	auto it = st.find(k);
	int l = *prev(it), r = *next(it);
	Calc(r - l - 1, 1), Get(prev(it), -1);
	Calc(k - l - 1, -1), Get(next(it), -1);
	Calc(r - k - 1, -1), Get(it, -1);
	auto tl = prev(it), tr = next(it);
	st.erase(it);
	Get(tl, 1), Get(tr, 1);
}
void Solve() {
	cin >> n, m = n / 2;
	for(int i = 1; i <= n; ++i) cin >> a[i];
	st.insert(0), st.insert(n + 1);
	x = m + 1;
	for(int i = 1; i <= m; ++i) 
		Add(a[i]);
	for(int i = m; i <= n; ++i) {
		ans += 1ll * x * m * (m - 1) + y;
		if(i != n) {
			Add(a[i + 1]);
			Del(a[i - m + 1]);
		}
	}
	printf("%lld\n", ans);
}
int main() {
	cin.tie(0)->sync_with_stdio(0);
	int t = 1; //cin >> t;
	while(t--) Solve();
	return 0;
}
```