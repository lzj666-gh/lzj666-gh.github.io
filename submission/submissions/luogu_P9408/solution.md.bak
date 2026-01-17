# P9408 题解

## 题目大意

有一串由数字 $0\sim 9$ 组成的序列 ${a}$ ，每次可以花费 $1$ 的代价将一个数变为其相邻的数 （$0$ 和 $9$ 也相邻）。求将其变为某个位置为峰值的左不减右不增序列的最小代价。

## 题目分析

乍一看可能感觉这题是贪心，但仔细一想会发现操作之间是相牵连的，故放弃贪心，更换思考角度。

可以发现，单调不减和单调不增是好解决的，可以设计状态 $dp_{i,j}$ 表示前 $i$ 个数中，将最后一位变为 $j$，且前 $i$ 个数单调不减的最小代价，可以很容易得到转移方程 $dp_{i,j}=\min\limits_{0\le k\le j}{dp_{i-1,k}}+dis(a_i,j)$，其中第一项可以前缀最小值来维护，$dis(x,y)$ 表示将 $x$ 变为 $y$ 需要的代价，值为 $\min (|x-y|,10-|x-y|)$。那么反过来的处理方法也是一样了，设计状态 $f_{i,j}$ 表示第 $i\sim n$ 单调不增，第 $i$ 个数设置为 $j$ 的最小代价，，最后的答案就是 $\min\limits_{1\le i\le n,0\le j\le 9}{dp_{i,j}+f_{i,j}}$。总复杂度 $O(10 n)$，可以通过此题。

#### update：这里要注意，计算答案时由于 $dp_{i,j}$ 和 $f_{i,j}$ 都计算了一次 $dis_{a_i,j}$，所以还得减去一次 $dis_{a_i,j}$。

```cpp
#include<bits/stdc++.h>
#define ll long long
#define L x<<1
#define R x<<1|1
#define mid (l+r>>1)
#define lc L,l,mid
#define rc R,mid+1,r
#define rep(x,y,z) for(int x=(y);x<=(z);x++)
using namespace std;
const int N=5e6+5;
inline int read(){int s=0,w=1;char c=getchar();while(c<48||c>57) {if(c=='-') w=-1;c=getchar();}while(c>=48&&c<=57) s=(s<<1)+(s<<3)+c-48,c=getchar();return s*w;}
inline void pf(ll x){if(x<0) putchar('-'),x=-x;if(x>9)pf(x/10);putchar(x%10+48);}
int n,a[N],f[N][10],g[N][10],ff[10],ans=2147000000;
inline int dis(int x,int y){
	return min(abs(x-y),10-abs(x-y));
}
int main(){
	n=read();
	rep(i,1,n)a[i]=read();
	rep(i,0,9)f[1][i]=dis(a[1],i),g[n][i]=dis(a[n],i);
	ff[0]=f[1][0];
	rep(i,1,9)ff[i]=min(ff[i-1],f[1][i]);
	rep(i,2,n){
		f[i][0]=ff[0]+dis(a[i],0);
		ff[0]=f[i][0];
		rep(j,1,9)f[i][j]=ff[j]+dis(a[i],j),ff[j]=min(ff[j-1],f[i][j]);
	}
	ff[0]=g[n][0];
	rep(i,1,9)ff[i]=min(ff[i-1],g[n][i]);
	for(int i=n-1;i>=1;i--){
		g[i][0]=ff[0]+dis(a[i],0);
		ff[0]=g[i][0];
		rep(j,1,9)g[i][j]=ff[j]+dis(a[i],j),ff[j]=min(ff[j-1],g[i][j]);
	}
	rep(i,1,n)rep(j,0,9){
		ans=min(ans,f[i][j]+g[i][j]-dis(a[i],j));
	}
	cout <<ans;
	return 0;
}
```
