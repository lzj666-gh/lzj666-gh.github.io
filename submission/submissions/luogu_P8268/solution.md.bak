# P8268 题解

### Preface

咱就是说，题目中 $n$ 良心地开小了……配方中的反应物数量总和（设为 $m$）应该可以开到 $10^5$ 级别。

### Analysis

从每个配方的生成物向反应物连有向边，发现是 DAG。因为每种材料用于生成不同材料的量不同，比较难办，我们采用**二分答案**。

假设当前我们二分到答案为 $A$。设 $b_i$ 为第 $i$ 种材料需要的量。初始化 $b_i=0\ (i<n)$ 而 $b_n=A$。

然后我们从 $n$ 到 $1$ 枚举材料 $x$：

* 若 $b_x\le a_x$，那直接跳过 $x$，因为已经够用了。

* 否则，枚举 $x$ 的出边到达的点 $y$，执行 $b_y\ +\!\!=b_x-a_x$（注意是 $+\!\!=$），表示 $y$ 节点还需要空出 $b_x-a_x$ 的量来生成材料 $x$。 

* 当然，如果 $x$ 没有出边（不能被制造），判断无解。

若无无解则为有解。

时间

$$O\left((n+m)\log\sum_{i=1}^{n}a_i\right)$$

### Detail

注意 $b$ 数组可能会爆 long long，所以当有 $b_i$ 过大直接判无解即可。

### Code

```cpp
//Said no more counting dollars. We'll be counting stars.
#include<bits/stdc++.h>
using namespace std;
#define pb emplace_back
#define IOS ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define For(i,j,k) for(int i=j;i<=k;i++)
#define Rof(i,j,k) for(int i=j;i>=k;i--)
#define int long long
#define N 102

int n,a[N],b[N],p[N];
vector<int> e[N];
priority_queue<int> q;
bool check(int x){
	For(i,1,n) b[i]=(i==n?x:0);
	Rof(i,n,1){
		if(b[i]>a[i] && e[i].empty()) return false;
		if(b[i]<=a[i]) continue;
		if(b[i]-a[i]>p[i-1]) return false;
		for(int j:e[i]){
			b[j]+=b[i]-a[i];
		}
	}
	return true;
}
signed main(){IOS;
	cin>>n;
	For(i,1,n) cin>>a[i];
	For(i,1,n) p[i]=p[i-1]+a[i];
	int q,x,y,z;
	cin>>q;
	while(q--){
		cin>>x>>y;
		while(y--){
			cin>>z;
			e[x].pb(z);
		}
	}
	int l=a[n]+1,r=0,mid,res=a[n];
	For(i,1,n) r+=a[i];
	while(l<=r){
		mid=(l+r)>>1;
		if(check(mid)) res=mid,l=mid+1; 
		else r=mid-1;
	}
	cout<<res<<endl;
return 0;}
```