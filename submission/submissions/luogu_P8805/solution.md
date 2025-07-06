# P8805 题解

## P8805 [蓝桥杯 2022 国 B] 机房 

这题就是树上前缀和的板子。

要想掌握这一题，就需要先学会 LCA 和前缀和。

[LCA学习笔记](https://www.luogu.com.cn/blog/QWE78/lca-xue-xi-bi-ji)

首先，在树里面，任意两个结点之间有且只有一条路径。而这一条路径的“转折点”，就是这两个点的最近公共祖先。所以我们就可以拆分成两条链去想。设有两点 $[p,q]$ ，那么一条是 $[p,lca(p,q)]$，另一条是$[q,lca(q,p)]$。

题目之中的“延迟”，也就是经过一个点的所需时间且不变，这就是点权。而要快速查询链上某一段区间的和，前缀和就是不二之选。我们从根节点开始往下遍历，设 $sum[i]$ 表示从根节点到 $i$ 结点之间的延迟总和。可以通过遍历求解。

在查询的时候，其实就是 $sum[p]+sum[q]$，但是 $sum[lca(q,p)]$ 这个地方我们加了两次且这一段我们是不需要的，所以要减去。但是这样会减去 $lca(q,p)$ 的点权。但是在 $p$ 和 $q$ 的路径中，会经过 $lca(p,q)$，所以我们还要加上 $lca(q,p)$ 的点权。

我们用 $a$ 数组表示点权，那就应该是：

$$ans=sum[p]+sum[q]-2\times sum[lca(q,p)]+a[lca(q,p)]$$

$Code$：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N =1e6+10;
vector<int> g[N<<1];
int sum[N],a[N],dep[N],fa[N][20],n,m;
inline int read(){
  	int x=0,w=1;char ch=0;
  	while(ch<'0'||ch>'9'){if(ch=='-')w=-1;ch=getchar();}
  	while(ch>='0'&&ch<='9'){x=x*10+(ch-'0');ch=getchar();}
  	return x*w;
}

inline void write(int x){
  	static int sta[35];int top=0;
  	do{sta[top++]=x%10,x/=10;}while (x);
  	while(top)putchar(sta[--top]+48);
}
void dfs(int u,int fath)
{
	dep[u]=dep[fath]+1;
	fa[u][0]=fath;
	for(int i=1;(1<<i)<=dep[u];i++)
		fa[u][i]=fa[fa[u][i-1]][i-1];
	for(int i=0;i<g[u].size();i++)
	{
		int v=g[u][i];
		if(v==fath)
			continue;
		sum[v]=sum[u]+a[v];
		dfs(v,u);
	}
}
int lca(int x,int y)
{
	if(dep[x]<dep[y])
		swap(x,y);
	int d=dep[x]-dep[y];
	for(int i=0;i<=log2(n);i++)
		if((1<<i)&d)
			x=fa[x][i];
	if(x==y)
		return x;
	for(int i=log2(n);i>=0;i--)
	{
		if(fa[x][i]!=fa[y][i])
			x=fa[x][i],y=fa[y][i];
	}
	return fa[x][0];
}
signed main()
{
	//freopen(".in","r",stdin);
	//freopen(".out","w",stdout);
	cin>>n>>m;
	for(int i=1,u,v;i<n;i++)
		cin>>u>>v,g[u].push_back(v),g[v].push_back(u);
	for(int i=1;i<=n;i++)
		a[i]=g[i].size(),sum[i]=g[i].size();
	dfs(1,0);
	for(int i=1;i<=m;i++)
	{
		int u,v;
		cin>>u>>v;
//		cout<<sum[u]<<" "<<sum[v]<<" "<<sum[lca(u,v)]<<" "<<a[lca(u,v)]<<endl;
		cout<<sum[u]+sum[v]-2*sum[lca(u,v)]+a[lca(u,v)]<<endl;
	}
	return 0;
}


```
