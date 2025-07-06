# P10954 题解

[原题传送门](https://www.luogu.com.cn/problem/P10954)

---

## 思路分析

dp。

先考虑设 $f_{i,j}$ 表示 $a$ 的前 $i$ 个数和 $b$ 的前 $j$ 个数的 LCIS 的长度，但发现这样不好转移，我们可以考虑设 $f_{i,j}$ 表示 $a$ 的前 $i$ 个数且以 $b_j$ 结尾的 LCIS 的长度。

考虑状态转移，有两种情况：

- 当 $a_i\ne b_j$，我们不能选 $a_i$（因为序列以 $b_j$ 结尾，所以 $b_j$ 必须选），答案为 $f_{i-1,j}$。

- 当 $a_i=b_j$ 时，我们枚举 $b$ 之前可能的结尾，检查能不能把 $a_i$ 加入，如果可以，答案就是 $\max_{k\in (0,j)}\{f_{i-1,k}+1\}$

答案很明显是 $\max_{i\in n}\{f_{n,j}\}$。

时间复杂度是 $O(n^3)$，$n\leq 3\times10^3$，容易超时，正解在后面。


```cpp
for(int i=1;i<=n;i++){
	int maxn=0;
	for(int j=1;j<=n;j++){
		f[i][j]=f[i-1][j];
		if(a[i]==b[j]){
			int maxn=1;
			for(int k=1;k<j;k++){
				if(a[i]>b[k]){
					maxn=max(maxn,f[i-1][k]+1);
				}
			}
			f[i][j]=max(f[i][j],maxn);
		}
	}
}
```

考虑优化，不难发现因为 $f_{i,j}\ge{f_{k,j}}_{ k\in (1,i-1)}$ ，所以求得的 $maxn$ 是满足 $a_i\ne b_k$ 的 $f_{i-1,k}+1$ 的前缀最大值，其中 $k\in (1,j-1)$。

所以可以直接将第三重循环删去，改成递推求前缀最大和，如此可以减少重复计算。

答案同样是 $\max_{i\in n}\{f_{n,j}\}$。

时间复杂度 $O(n^2)$，空间复杂度 $O(n^2)$。

## $\texttt{code}$

```cpp
/*Written by smx*/
#include<bits/stdc++.h>
using namespace std;
#define int long long
const int MAXN=3e3+5,inf=1e9;
int n,m,ans;
int a[MAXN],b[MAXN],f[MAXN][MAXN];
signed main(){
	//freopen(".in","r",stdin);
	//freopen(".out","w",stdout);
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>a[i];
	}
	for(int i=1;i<=n;i++){
		cin>>b[i];
	}
	for(int i=1;i<=n;i++){
		int maxn=0;
		for(int j=1;j<=n;j++){
			if(a[i]!=b[j]){
				f[i][j]=f[i-1][j];
			}else{
				f[i][j]=maxn+1;
			}
			if(b[j]<a[i]){
				maxn=max(maxn,f[i-1][j]);
			}
		}
	}
	for(int i=1;i<=n;i++){
		ans=max(ans,f[n][i]);
	}
	cout<<ans;
	return 0;
}
```