# P7464 题解

[传送门](https://www.luogu.com.cn/problem/P7464)

#### 前置知识：

前缀和，dfs。

#### 题意：

+ $T$ 组数据，每组数据给出一个正整数 $n$，求所有满足 $i<j<k$ 且 $i\times j\times k\le n$ 的正整数三元组 $(i,j,k)$ 的个数。

+ $T\le 10^5$，$n\le 10^6$。

下文中，若未做特殊说明，则默认 $i<j<k$。

#### 分析：

考虑只有单个询问的情况。注意到 $i$ 是 $\sqrt[3]n$ 级别的，可以尝试暴力枚举。

注意到在枚举的过程中，我们可以把求 $i\times j\times k\le n$ 的三元组个数，看做求所有 $i\times j\times k=m,m\le n$ 的三元组个数。因此当 $n$ 取 $10^6$ 时，对于所有 $m\le 10^6$，我们在 dfs 时就已经求出了 $i\times j\times k=m$ 的三元组 $(i,j,k)$ 的个数。

考虑多个询问的情况。对于询问 $n'$，由于 $n'\le 10^6$，所以我们已经求出了对于所有 $m\le n'$ 的 $i\times j\times k=m$ 的三元组个数。可以使用前缀和将其相加，从而 $O(1)$ 求出答案。

#### 思路：

1. 对于所有 $m\le 10^6$，通过 dfs 求出 $i\times j\times k=m$ 的三元组个数。dfs 只需要一次。

2. 将求出的答案前缀和处理，对于每一个询问 $O(1)$ 解决。

---

#### dfs 部分

下面分析 dfs 的复杂度。~~因为太水了只好开始瞎扯~~

令 $i$ 从 $1$ 枚举到 $n$，考虑 $i=i_0$ 时需要枚举多少 $j$ 和 $k$。

$j$ 从 $1$ 枚举到 $\dfrac n {i_0}$，而对于 $j=j_0$ 的情况，$k$ 从 $1$ 枚举到 $\dfrac n {i_0\times j_0}$。因此，枚举的时间复杂度是 $\sum\limits_{j_0=1}^{\frac n{i_0}}\dfrac n{i_0\times j_0}=\dfrac n{i_0}\sum\limits_{j_0=1}^{\frac n{i_0}}\dfrac 1{j_0}$，是 $\dfrac n{i_0}\log\dfrac n{i_0}$ 级别的。

所以总时间复杂度为 $O(\sum\limits_{i=1}^n\dfrac ni\log\dfrac ni)$。

可以写一个程序计算这个时间复杂度。我算出来的结果是 $1.5\times 10^8$，可以接受。

当然，实际上枚举的时候可以不从 $1$ 开始，也不必枚举到 $n$ 等上界，因此复杂度会更小。

代码实现应该不用多说吧（

---

完整代码：

```cpp
#include <bits/stdc++.h>
using namespace std;
const int mN=1e6+100;
int mp[mN];

void dfs(int st, int v, long long now) {	//now 存的是目前所有数的乘积 
	if(st==3) ++mp[now];
	else for(int i=v+1; now*i<mN; ++i) dfs(st+1, i, now*i);	//从 v+1 枚举到 1e6/now
}
int main() {
	dfs(0, 0, 1);
	for(int i=1; i<mN; ++i) mp[i]+=mp[i-1];	//前缀和处理 
	int T, n;
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &n);
		printf("%d\n", mp[n]);
	}	
	return 0;
}
```