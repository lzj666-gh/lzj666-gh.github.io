# P9029 题解

# Solution
首先，观察发现巧克力的顺序是无关紧要的，所以可以先从
小到大排序。

对于 $l - f$ 的值，对巧克力分类讨论：

1. $c_i < k$ 的巧克力对 $l - f$ 值的影响是 $c_i$。
1. $c_i > k$ 的巧克力对 $l - f$ 值的影响是 $2 \times k - c_i$。

观察上面两种情况，不难发现，对 $c_i < k$ 的巧克力，越便宜越好；对 $c_i \ge k$ 的巧克力，越贵越优。

将从小到大的排序处理成对 $l - f$ 的贡献。


假设一开始全部选左边的，若不是最优的，考虑用右边的代替左边的。

左右两边的分界线是 $k$，设左边选取 $x$ (不超过左边的个数）个，观察发现，要找到最小的 $x$，使得左边（从左往右数）第 $x$ 个的贡献小于右边（从右往左数）第 $m - x + 1$ 个的贡献，即不断使用右边的替换左边的，直到替换后变差。

当左边第 $x$ 个的贡献小于第 $m - x + 1$ 的贡献时，左边第 $y$ 个的贡献一定小于第 $m - y + 1$ 的贡献，所以可二分 $x$。

时间复杂度为 $O(q\log{n})$。
# Code
```cpp
#include <bits/stdc++.h>
#define int long long//坏习惯
using namespace std;
const int maxn = 1e5 + 5;
int a[maxn], sum[maxn], n, q;
main()
{
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);//优化 
	cin >> n >> q;
	for (int i = 1; i <= n; i++) cin >> a[i];
	sort(a + 1, a + n + 1);
	for (int i = 1; i <= n; i++) sum[i] = sum[i - 1] + a[i];//前缀和 
	while (q--)
	{
		int k, m; cin >> k >> m;
		int rr = lower_bound(a + 1, a + n + 1, k) - a - 1;
		int l = 0, r = min(m, rr), mid;
		while (l < r)
		{
			mid = l + r + 1 >> 1;
			int x = lower_bound(a + 1, a + n + 1, k * 2 - a[mid]) - a - 1;
			//依次枚举选的边界 
			if (n - x + mid <= m) l = mid;
			else r = mid - 1;
			//若变差则变大，变好则变小 
		}
		cout << sum[l] + 2 * k * (m - l) + sum[n - m + l] - sum[n] << "\n";
		//前r个的和（在原始r以内）加上m-r个后面数的和 
	}
}
```
