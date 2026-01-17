# P2568 题解

[$$\Large\texttt{My Blog}$$](https://hydingsy.github.io/articles/problem-BZOJ-2818-GCD/)

---

## Description

> 题目链接：[Luogu 2568](https://www.luogu.org/problemnew/show/P2568)

给定整数 $n$，求 $1\le x,y\le n$ 且 $\gcd(x,y)$ 为素数的数对 $(x,y)$ 有多少对。

数据范围：$1\le n\le 10^7$

------

## Solution

> 本题和[「Luogu 2257」YY 的 GCD](https://www.luogu.org/problemnew/show/P2257)（[题解](https://hydingsy.github.io/articles/problem-Luogu-2257-YY-GCD/)） 几乎完全一样，但是本题由于是**单组询问**，所以不需要 $O(n)$ 的预处理和 $O(\sqrt n)$ 的单次询问复杂度。

首先我们枚举质数：
$$\sum_{p\in\text{prime}}\sum_{i=1}^n\sum_{j=1}^n[\gcd(i,j)=p]$$
对 $\gcd$ 进行套路式的变形：
$$\sum_{p\in\text{prime}}\sum_{i=1}^{\left\lfloor\frac{n}{p}\right\rfloor}\sum_{j=1}^{\left\lfloor\frac{n}{p}\right\rfloor} [\gcd(i,j)=1]$$
接下来改变 $j$ 的枚举上界（其中 $-1$ 的原因是 $i=j=1$  时的答案会被重复统计，因此注意这里的 $-1$ 是在 $\sum_{p\in\text{prime}}$ 中的，而不是在 $\sum_{i=1}^{\left\lfloor\frac{n}{p}\right\rfloor}$ 中的）：
$$\sum_{p\in\text{prime}}\left(\sum_{i=1}^{\left\lfloor\frac{n}{p}\right\rfloor}\left(2\sum_{j=1}^i [\gcd(i,j)=1]\right)-1\right)$$
此已经可以发现最后一个 $\sum$ 是的值就是 $\varphi(i)$，故原式化为：
$$\sum_{p\in\text{prime}}\left(2\sum_{i=1}^{\left\lfloor\frac{n}{p}\right\rfloor}\varphi(i)-1\right)$$
所以我们可以线性筛求出 $\varphi(i)$ 的值并做前缀和，枚举 $p\in\text{prime}\ \text{and}\ p\le n$ 并统计答案即可。

**时间复杂度**：$O(n)$

------

## Code

```cpp
#include <cstdio>

const int N=1e7+5,M=1e6+5;
int n,tot,p[M],phi[N];
long long sum[N];
bool flg[N];

void sieve(int n) {
	phi[1]=1;
	for(int i=2;i<=n;++i) {
		if(!flg[i]) p[++tot]=i,phi[i]=i-1;
		for(int j=1;j<=tot&&i*p[j]<=n;++j) {
			flg[i*p[j]]=1;
			if(i%p[j]==0) {
				phi[i*p[j]]=phi[i]*p[j];
				break;
			} else {
				phi[i*p[j]]=phi[i]*phi[p[j]];
			}
		}
	}
	for(int i=1;i<=n;++i) sum[i]=sum[i-1]+phi[i];
}
int main() {
	scanf("%d",&n);
	sieve(n);
	long long ans=0;
	for(int i=1;i<=tot;++i) ans+=2*sum[n/p[i]]-1;
	printf("%lld\n",ans);
	return 0;
}
```

