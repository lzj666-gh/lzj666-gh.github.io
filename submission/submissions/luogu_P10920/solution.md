# P10920 题解

[Problem Link](https://www.luogu.com.cn/problem/P10920)

**题目大意**

> 给定 $n$ 位 01 串 $S$，其中有一些通配符可以任意换成 $0/1$，求最大的 $k$ 使得存在 $i$ 满足 $S[i,i+k-1]=S[i+k,i+2k-1]$。
>
> 数据范围：$n\le 10^5$。

**思路分析**

这个问题显然很难做到 polylog 或者根号，因此考虑 `std::bitset` 优化。

从大到小枚举 $k$，某个位置 $i$ 不合法当且仅当 $S_i=0,S_{i+k}=1$ 或 $S_{i}=1,S_{i+k}=0$，`std::bitset` 维护为 $0/1$ 的位置，用右移和求交并操作可以维护出所有不合法位置 $i$ 的集合。

那么我们检验 $k$ 是否合法只要在这个集合中找到 $\ge k$ 的连续的 $0$。

对于 $k\le \omega$ 的情况可以 $\mathcal O(n)$ 暴力判断每个 $k$ 是否合法，其中 $\omega$ 为 `std::bitset` 字长。

对于 $k>\omega $ 的情况，这个 $0$ 区间一定跨越了 $>1$ 个长度为 $\omega$ 的块，我们可以遍历每个块并维护当前最长全 $0$ 后缀。

如果一个块非空，那么只有其最长 $0$ 前缀和后缀有可能有贡献，可以 `__builtin_clz` 和 `__builtin_ctz` 维护，需要手写 `bitset`。

时间复杂度 $\mathcal O\left(n\omega+\dfrac{n^2}\omega\right)$

**代码呈现**

```cpp
#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;
const int MAXN=1e5+5,S=1575;
char s[MAXN];
int n;
ull f[S],g[S],t[S];
bool chk(int x) {
	for(int i=0,c=0;i+x<n;++i) {
		if(s[i]!='?'&&s[i+x]!='?'&&s[i]!=s[i+x]) c=0;
		else ++c;
		if(c>=x) return true;
	}
	return false;
}
void solve() {
	memset(f,0,sizeof(f));
	memset(g,0,sizeof(g));
	scanf("%d%s",&n,s);
	for(int i=0;i<n;++i) {
		if(s[i]=='0') f[i>>6]|=1ull<<(i&63);
		if(s[i]=='1') g[i>>6]|=1ull<<(i&63);
	}
	for(int i=n/2;i>64;--i) {
		memset(t,0,sizeof(t));
		int ed=(n-i)>>6;
		for(int j=0,b=i>>6,r=i&63;j<=ed;++j) {
			ull F=f[j+b]>>r,G=g[j+b]>>r;
			if(r) F|=f[j+b+1]<<(64-r),G|=g[j+b+1]<<(64-r);
			t[j]=(F&g[j])|(G&f[j]);
		}
		for(int c=(n-i);c<((ed+1)<<6);++c) t[c>>6]|=1ull<<(c&63);
		int x=t[0]?__builtin_clzll(t[0]):64;
		for(int j=1;j<=ed;++j) {
			if(!t[j]) {
				if((x+=64)>=i) return printf("%d\n",i),void();
			} else {
				if(x+__builtin_ctzll(t[j])>=i) return printf("%d\n",i),void();
				x=__builtin_clzll(t[j]);
			}
		}
	}
	for(int i=min(n/2,64);i;--i) if(chk(i)) return printf("%d\n",i),void();
	puts("0");
}
signed main() {
	int T; scanf("%d",&T);
	while(T--) solve();
	return 0;
}
```