# P8855 题解

## 题意

给定一棵 $N$ 个结点的树，所有边的权值均为 $1$。从结点 $1$ 出发，依次经过 $M$ 个指定结点，求路径总长度的最小值。

## 思路

定义 $\textup{dis}(x,y)$ 为 $x$ 与 $y$ 的距离，$\textup{dep}(x)$ 为 $x$ 的深度（根结点 $\textup{dep}(1) = 0$），$\textup{lca}(x,y)$ 为 $x$ 与 $y$ 的最近公共祖先。

结点 $u$ 与 $v$ 的距离为：

$\begin{aligned}
\textup{dis}(u,v) &= \textup{dis}(u,\textup{lca}(u,v)) + \textup{dis}(v,\textup{lca}(u,v))\\
&= \textup{dep}(u) - \textup{dep}(\textup{lca}(u,v)) + \textup{dep}(v) - \textup{dep}(\textup{lca}(u,v))\\
&= \textup{dep}(u) + \textup{dep}(v) - 2 \times \textup{dep}(\textup{lca}(u,v)).
\end{aligned}$

树剖。查询时求 LCA 即可。

时间复杂度为 $\mathcal{O}(N + M \log N)$。

## Code

```cpp
#include<bits/stdc++.h>
#define int long long
#define maxn 30010

using namespace std;

int n,m,tot,tim,lnk[maxn],lst=1,ans;

struct node{
	int dep,siz,fa,hson,top;
}a[maxn];

struct edge{
	int to,nxt;
}e[maxn<<1];

inline int read(){
	int ret=0,f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9')ret=ret*10+(ch&15),ch=getchar();
	return ret*f;
}

void add_e(int x,int y){
	e[++tot]=(edge){y,lnk[x]};
	lnk[x]=tot;
}

void dfs1(int u,int dep){
	a[u].dep=dep;
	a[u].siz=1;
	for(int i=lnk[u];i;i=e[i].nxt){
		int v=e[i].to;
		if(v==a[u].fa)continue;
		a[v].fa=u;
		dfs1(v,dep+1);
		a[u].siz+=a[v].siz;
		if(a[v].siz>a[a[u].hson].siz)a[u].hson=v;
	}
}

void dfs2(int u,int top){
	a[u].top=top;
	if(a[u].hson){
		dfs2(a[u].hson,top);
		for(int i=lnk[u];i;i=e[i].nxt){
			int v=e[i].to;
			if(v==a[u].fa||v==a[u].hson)continue;
			dfs2(v,v);
		}
	}
}

int lca(int u,int v){
	while(a[u].top!=a[v].top){
		if(a[a[u].top].dep<a[a[v].top].dep)swap(u,v);
		u=a[a[u].top].fa;
	}
	return a[u].dep<a[v].dep?u:v;
}

int qry(int u,int v){
	return a[u].dep+a[v].dep-(a[lca(u,v)].dep<<1);
}

signed main(){
	n=read();
	for(int i=1;i^n;i++){
		int u=read(),v=read();
		add_e(u,v),add_e(v,u);
	}
	dfs1(1,0),dfs2(1,1);
	m=read();
	while(m--){
		int x=read();
		ans+=qry(lst,x);
		lst=x;
	}
	printf("%lld\n",ans);
	return 0;
}
```