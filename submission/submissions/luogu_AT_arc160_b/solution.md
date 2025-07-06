# AT_arc160_b 题解

### 题目链接
[luogu](https://www.luogu.com.cn/problem/AT_arc160_b)

[atcoder](https://atcoder.jp/contests/arc160/tasks/arc160_b)

### 题目大意

给出一个正整数 $n$。

求出满足以下条件的正整数三元组 $(x,y,z)$ 的数量，取模 $998244353$：

- $xy,yz,zx$ 都小于或等于 $n$。

多组数据。$1 \le T \le 100,1 \le n \le 10^9$。

### 思路

令 $m=\lfloor \sqrt{n} \rfloor$。

对 $x,y,z$ 的值分类讨论：

1. $\max(x,y,z) \le m$。

   此时 $x,y,z$ 两两乘积一定都小于 $n$。
   
   每个值都可以取 $[1,m]$ 中的整数，方案数为 $m^3$。
   
2. $\max(x,y,z) > m$。
   
   若 $\max(x,y,z)=x$，那么因为 $xy \le n,xz \le n$，所以 $y$ 和 $z$ 一定都小于 $m$。这就同时满足了 $yz \le n$。
   
   考虑枚举 $x$。那么 $y,z \in[1,\lfloor \frac{n}{x} \rfloor ]$。所以 $y,z$ 的取值方案数为 $\lfloor \frac{n}{x} \rfloor ^2$。不考虑 $x$ 在三元组中的位置，则 $x$ 三个位置都可以放，剩下两个位置就有上述方案，所以总方案数就是 $3 \cdot \lfloor \frac{n}{x} \rfloor ^2$。
   
   显然这个式子[数论分块](https://oi-wiki.org/math/number-theory/sqrt-decomposition/)一下就做完了，注意 $x \in (\sqrt{n},n]$。
   
时间复杂度 $O(T\sqrt{n})$。

#### code

```cpp
#include<bits/stdc++.h>
using namespace std;
#define mod 998244353
#define ll long long
ll n;
void solve(){
	cin>>n;
	ll m=sqrt(n),ans=0;
	ans+=m*m*m%mod;//分类1
	for(ll l=m+1,r;l<=n;l=r+1){//分类2，枚举x
		r=n/(n/l);
		ll lim=n/l;
		ans+=lim*lim*3%mod*(r-l+1)%mod;
		ans%=mod;
	}
	cout<<ans<<'\n';
	return;
}
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);cout.tie(0);
	int t;cin>>t;
	while(t--)solve();
	return 0;
}
```