# P10978 题解

此题使用动态规划。

定义 $f_{i,j}$ 表示第 $i$ 个木匠刷到第 $j$ 块木板时最大的总收入。

考虑转移，共三种情况：

1. 不需要第 $i$ 个木匠进行粉刷。收入为 $f_{i-1,j}$。

2. 第 $i$ 个木匠不需要对第 $j$ 个木板进行粉刷。收入为 $f_{i,j-1}$。

3. 第 $i$ 个木匠对第 $j$ 个木板进行粉刷。枚举上一个工人刷到的木板编号 $k$（须保证能被刷到），第 $i$ 个木匠接着从第 $k+1$ 个木板刷到 $j$，收入为 $f_{i-1,k}+p_i\times (j-k)$。

最后对于这三种情况，取最大值就是答案。

但我们发现第三个方程复杂度太高，需要优化。为了优化，我们把它化简为 $f_{i-1,k}-p_i\times k+p_i\times j$。

我们发现，$p_i\times j$ 是固定不变的，所以只需要找出最大的，符合条件的 $f_{i-1,k}-p_i\times k$。

这个东西可以使用单调队列维护，于是这道题就做完了。

**AC code:**

```cpp
#include<bits/stdc++.h>
using namespace std;
#define int long long
int f[201][20001],n,k,q[20001],h,t,ans;
struct A{int l,p,s;}p[110];
int cmp(A p1,A p2){return p1.s<p2.s;}
signed main(){
	ios::sync_with_stdio(0),cin>>n>>k;
	for(int i=1;i<=k;i++)
		cin>>p[i].l>>p[i].p>>p[i].s;
	sort(p+1,p+k+1,cmp);
	for(int i=1;i<=k;i++){
		h=0,t=1;
		q[0]=max(p[i].s-p[i].l,0ll);
		for(int j=1;j<=n;j++){
			f[i][j]=max(f[i][j-1],f[i-1][j]);
			if(j>=p[i].s+p[i].l)continue;
			while(h<t&&q[h]+p[i].l<j)h++;
			if(j<p[i].s){
				int tp=f[i-1][j]-j*p[i].p;
				while(h<t&&f[i-1][q[t-1]]-q[t-1]*p[i].p<tp)t--;
				q[t++]=j;continue;
			}
			f[i][j]=max(f[i][j],f[i-1][q[h]]+p[i].p*(j-q[h]));
		}
	}
	cout<<f[k][n];
	return 0;
}
```