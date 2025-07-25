# P9619 题解

### 题目描述

现在有 $n$ 个节点的完全图，第 $i$ 个节点的点权为 $a_i$。如果 $u,v$ 之间存在一条边的话，贡献为 $a_u \oplus a_v$。一颗生成树的价值就是全部边的边权和，希望求出原图全部生成树的价值和。

$n \leqslant 10^6$。

### 思路点拨

实际上，对于任何一条边 $(u,v)$，在全部生成树中出现次数是一样的。这一点很好理解吧。

全部生成树的边的数量和就是 $n^{n-2}\times (n-1)$，将其均摊到每一条边就是 $\dfrac{n^{n-2}\times (n-1)}{n\times (n-1)\times \frac{1}{2}}=2\times n^{n-3}$，令其为 $w$ 表示每一条边的出现次数。

我们现在的目的就是求出每一条边的价值和然后乘上 $w$ 就是答案。价值和十分好算，我们枚举每一个二进制位，对于第 $i$ 个元素，如果该位上是 $1$ 就找 $i+1,i+2,..,n$ 这些元素里哪些该位是 $0$；如果该位上是 $0$ ,就找 $i+1,i+2,..,n$ 这些元素里哪些该位是 $1$。数量乘上 $2^{bit}$，$bit$ 就看你现在枚举到第几位了。过程可以使用前缀和优化，$O(n \log W)$。

这一部分放一个代码 $cnt$ 就是上述的 $\sum_{i=1}^n sum_{j=1}^n a_i \oplus a_j$。

```cpp
	for(int i=0;i<=31;i++){
		for(int j=1;j<=n;j++){
			if(a[j]&(1ll<<i)) sum[j]=sum[j-1]+1;
			else sum[j]=sum[j-1];
		}
		for(int j=1;j<=n;j++){
			if(a[j]&(1ll<<i)) cnt=(cnt+(1ll<<i)*((n-j)-(sum[n]-sum[j])))%mod;
			else cnt=(cnt+(1ll<<i)*(sum[n]-sum[j]))%mod;
		}
	}
```


本题还是比第一题简单了不少。