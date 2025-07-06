# P11232 题解

通过了民间数据。

首先对于每辆车，能够判定它为超速的测速仪肯定是一段区间，如果这段区间不在 $1\sim m$ 的范围内，则这辆车不会被判定为超速。否则，我们可以将这段区间看成一个限定条件，即我们在所选出来的测速仪中，对于每一个限定条件 $l_i,r_i$，至少有一个测速仪（假设这个测速仪的位置为 $x$）满足 $l_i\le x\le r_i$，并且我们希望选出来的测速仪尽可能少。

下面进行分类讨论，得出限定区间。

对于每个车子 $i$，其超速情况分为以下两种：

- 当 $a_i>0$ 时，若 $v_i>V$，则这辆车在一开始就超速了，那么限定区间的左端点即为满足 $p_j>d_i$ 的最小的 $j$；否则，根据公式，这辆车驶入 $d_i+\frac{V^2-v_i^2}{2a_i}$ 这个位置时，其速度会到达 $V$，那么限定区间的左端点即为满足 $p_j>d_i+\frac{V^2-v_i^2}{2a_i}$ 的最小的 $j$。而以上情况的区间右端点显然都为 $m$，因为车子的速度是单调递增的。

- 当 $a_i\le 0$ 时，若 $v_i\le V$，则代表这辆车的速度永远都不会超过 $V$，所以这辆车不会被判定为超速；反之则代表 $v_i>V$，限定区间的左端点即为满足 $p_j>d_i$ 的最小的 $j$，再根据公式，二分出最大的满足 $\sqrt{v_i^2+2a_i\times(p_k-d_i)}>V$ 的 $k$，作为限定区间的右端点。

接下来考虑如何选出最少的点使得对于每个限定区间，至少有一个测速仪在该区间内。

首先将所有区间以左端点为第一关键字、右端点为第二关键字排序（左端点按照从小到大的顺序，右端点按照从大到小的顺序排序）。对于两个区间 $[l_i,r_i]$ 及 $[l_j,r_j]$，若 $l_i\le l_j,r_i\ge r_j$，那么 $[l_i,r_i]$ 这个区间是没有用的，因为一个点若在 $[l_j,r_j]$ 内，它也必定在 $[l_i,r_i]$ 内，所以对于这样的区间，是可以不考虑的。

那么在处理之后就满足所有区间的左端点、右端点都是按照升序排序的，再每次贪心的选当前区间的右端点，覆盖到不能覆盖的区间为止。

```cpp
#include <bits/stdc++.h>
using namespace std;
int a[100005], d[100005], v[100005], p[100005];
int del[100005];

struct node {
	int ql, qr;
	friend bool operator<(node l, node r) {
		if (l.ql != r.ql)
			return l.ql < r.ql;
		return l.qr > r.qr;
	}
} s[100005];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);
	int t;
	cin >> t;
	while (t--) {
		int n, m, L, V;
		cin >> n >> m >> L >> V;
		for (int i = 1; i <= n; i++)
			cin >> d[i] >> v[i] >> a[i];
		for (int i = 1; i <= m; i++)
			cin >> p[i];
		int tot = 0;
		for (int i = 1; i <= n; i++) {
			if (a[i] <= 0 && v[i] <= V)
				continue;
			if (a[i] > 0) {
				int wei = V * V - v[i] * v[i];
				wei /= (2 * a[i]);
				wei += d[i];
				if (v[i] > V)
					wei = d[i] - 1;
				int l = 1, r = m, ans = 0;
				while (l <= r) {
					int mid = (l + r) / 2;
					if (p[mid] > wei) {
						r = mid - 1;
						ans = mid;
					} else
						l = mid + 1;
				}
				if (!ans)
					continue;
				s[++tot].ql = ans, s[tot].qr = m;
			} else {
				int l = 1, r = m, pos = 0;
				while (l <= r) {
					int mid = (l + r) / 2;
					if (p[mid] >= d[i]) {
						r = mid - 1;
						pos = mid;
					} else
						l = mid + 1;
				}
				if (!pos)
					continue;
				l = pos, r = m;
				int ans = 0;
				while (l <= r) {
					int mid = (l + r) / 2;
					double su = sqrt(v[i] * v[i] * 1.0 + 2.0 * a[i] * (p[mid] - d[i]));
					if (su > V) {
						l = mid + 1;
						ans = mid;
					} else
						r = mid - 1;
				}
				if (ans < pos)
					continue;
				s[++tot].ql = pos, s[tot].qr = ans;
			}
		}
		sort(s + 1, s + tot + 1);
		int mr = 1000000000;
		for (int i = tot; i >= 1; i--) {
			if (mr <= s[i].qr)
				del[i] = 1;
			mr = min(mr, s[i].qr);
		}
		int ans = 0, fu = 0;
		for (int i = 1; i <= tot; i++) {
			if (del[i]) {
				del[i] = 0;
				continue;
			}
			if (fu < s[i].ql) {
				ans++;
				fu = s[i].qr;
			}
		}
		cout << tot << " " << m - ans << "\n";
	}
}
```