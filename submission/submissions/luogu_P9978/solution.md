# P9978 题解

赛时差点没切。

------------

这个题目描述很屎，要手模一下我才发现两个结论：

1. $a,\,b$ 序列里都没有出现的数，一定能全部互相匹配上，因此答案要加上 $a,\,b$ 里都没有出现过的数的个数。

2. $a,\,b$ 序列里出现过的数的贡献，本质上是对 $b$ 及 **$b$ 的翻转**做 $k - 1$ 次向右循环移位，然后取最多的 $a_i = b_i$ 的 $i$ 数量。为什么要翻转因为环是无向的。

举例来说，样例三：

```
6 4
1 2 3 4
4 3 2 5
```

我们令 $b$ 翻转，循环移位 $0$ 次可以得到最优答案。

第一类的贡献非常好算，因为值域是 $[1,\,n]$，开个桶统计就行了。

第二类贡献，考虑令 $s_i$ 为 $b_i$ 循环移位多少次之后会产生贡献，因为 $a,\,b$ 各自的数互不重复，所以是对的。具体的，令 $d_i$ 为 $a_i$ 的出现位置，分讨 $b$ 的循环移位次数，可得到 $s_i$ 的值，答案即为 $\max_{0 \le i \le k} s_i$。

```cpp
#include <bits/stdc++.h>
#define x first
#define y second
using namespace std;
typedef long long int ll;
using pll = pair<ll, ll>;
const int maxn = 5e5 + 10;
const ll mod = 998244353LL;
const ll inf = 1145141919810LL;
int n, k; ll a[maxn], b[maxn], cnt[maxn], sum[maxn]; int d[maxn]; pll c[maxn];
int main() {
	scanf("%d%d", &n, &k); ll ans = 0;
	for (int i = 1; i <= k; i++) scanf("%lld", &a[i]), ++cnt[a[i]], d[a[i]] = i;
	for (int i = 1; i <= k; i++) scanf("%lld", &b[i]), ++cnt[b[i]];
	for (int i = 1; i <= k; i++) {
		int u = d[b[i]];
		if (!u) continue;
		if (u >= i) ++sum[u - i];
		else ++sum[k - i + u];
	}
	for (int i = 0; i <= k; i++) ans = max(ans, sum[i]);
	reverse(a + 1, a + k + 1); memset(d, 0, sizeof(d)); memset(sum, 0, sizeof(sum));
	for (int i = 1; i <= k; i++) d[a[i]] = i;
	for (int i = 1; i <= k; i++) {
		int u = d[b[i]];
		if (!u) continue;
		if (u >= i) ++sum[u - i];
		else ++sum[k - i + u];
	}
	for (int i = 0; i <= k; i++) ans = max(ans, sum[i]);
	for (int i = 1; i <= n; i++) ans += !cnt[i];
	printf("%lld\n", ans);
	return 0;
}
```
