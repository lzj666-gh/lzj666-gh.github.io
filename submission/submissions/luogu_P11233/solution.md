# P11233 题解

PS：声明，本做法由同机房巨佬 @[hanss6](https://www.luogu.com.cn/user/537719) 提供，经其本人同意后在此记录。

提供一个代码实现非常简单十分简短的做法。

返璞归真，状态没必要设置那么复杂，设 $f_i$ 表示考虑到第 $i$ 位的答案。显然的，对于每一个位置 $i$ 可以令 $f_i = f_{i-1}$。

用 $lst_i$ 记录 $i$ 上一次出现的位置，初始化令所有的 $lst_i = 0$，每遍历到一个位置，动态更新 $lst_{a_i} = i$。然后枚举区间更新 $f_i$，也可以预处理出来一个 $g$ 数组辅助转移，复杂度 $O(n^2)$。

[50pts code](https://www.luogu.com.cn/paste/62aiymf9)

使用前缀和优化，每当 $a_i=a_{i-1}$ 时，更新前缀和数组 $s_i$。最后对于 $a_i$ 如果 $lst_{a_i}$ 存在，对于 $f_i$ 的转移为：

$$f_i=\max_{i=1}^{n}\{f_{lst_{a_i}+1}+a_i+s_i-s_{lst_{a_i}}\}$$

最终的答案为 $f_n$。

复杂度 $O(n)$。

```cpp
#include <bits/stdc++.h>

#define int long long
#define rint register int
#define endl '\n'
#define m(a) memset(a, 0, sizeof a)

using namespace std;

const int N = 1e6 + 5;

int n, T;
int a[N], lst[N], f[N];
int s[N], ans; 

signed main() 
{
	cin >> T;
	while (T--) 
	{
		cin >> n;
		m(a), m(lst), m(f), m(s);
		for (rint i = 1; i <= n; i++) cin >> a[i];
		for (rint i = 2; i <= n; i++) s[i] = (a[i] == a[i - 1] ? s[i - 1] + a[i] : s[i - 1]);
		for (rint i = 1; i <= n; i++) 
		{
			f[i] = f[i - 1];
			if (lst[a[i]]) f[i] = max(f[i], f[lst[a[i]] + 1] + a[i] + s[i] - s[lst[a[i]] + 1]);
			lst[a[i]] = i;
		}
		cout << f[n] << endl;
	} 
	return 0;
}
```