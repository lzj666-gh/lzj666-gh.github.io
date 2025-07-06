# P4216 题解

这是一种题解没有的 $ O(m\log n) $ 做法。

首先第一步转化。设这是第 $ x $ 个任务，若 $ opt $ 为 $ 1 $，危险值大于 $ c $ 的只有可能在第 $ x-c-1 $ 个任务以前出现。

于是题目就变成了在某一时刻单点加和在某一时刻链上查询，离线即可去掉“某一时刻”。

单点加和链上查询，大家用的应该都是树剖，复杂度是 $ O(\log^2n) $ 的。然而使用 DFS 序和差分，将单点加转化为子树加，将链上查询转化为单点查询。

具体来说就是设一个 $ s[u] $ 表示节点 $ u $ 到根节点有多少个节点是危险的，那么单点加就可以变成子树加，在 DFS 序上就是区间加。

链上查询只需要查询 $ u,v,LCA(u,v),f[LCA(u,v)] $，也就是单点查。

区间加单点查，树状数组上！

极短的代码：
```cpp
#include<cstdio>
#include<vector>
const int M=2e5+5;
int n,m,dfc,d[M],f[M],dfn[M],siz[M],son[M],top[M];
int BIT[M];int opt[M],x[M],y[M],ans[M];
std::vector<int>G[M],id[M];
void DFS1(int u){
	dfn[u]=++dfc;d[u]=d[f[u]]+1;siz[u]=1;
	for(int&v:G[u]){
		DFS1(v);siz[u]+=siz[v];
		if(siz[v]>siz[son[u]])son[u]=v;
	}
}
void DFS2(int u,int tp){
	top[u]=tp;if(!son[u])return;DFS2(son[u],tp);
	for(int&v:G[u])if(v!=son[u])DFS2(v,v);
}
inline int LCA(int u,int v){
	while(top[u]^top[v]){
		if(d[top[u]]>d[top[v]])u=f[top[u]];
		else v=f[top[v]];
	}
	return d[u]>d[v]?v:u;
}
inline int dis(const int&u,const int&v){
	return d[u]+d[v]-(d[LCA(u,v)]<<1)+1;
}
inline void Add(int x,const int&val){
	for(;x<=n;x+=1<<__builtin_ctz(x))BIT[x]+=val;
}
inline int Query(int x){
	int ans=0;
	for(;x>=1;x-=1<<__builtin_ctz(x))ans+=BIT[x];
	return ans;
}
inline int Q(const int&x,const int&y){
	int lca=LCA(x,y);
	return Query(dfn[x])+Query(dfn[y])-Query(dfn[lca])-Query(dfn[f[lca]]);
}
signed main(){
	register int i,k;
	scanf("%d",&n);
	for(i=1;i<=n;++i)scanf("%d",f+i),G[f[i]].push_back(i);
	for(i=1;f[i];i=f[i]);
	DFS1(i);DFS2(i,i);
	scanf("%d",&m);
	for(i=1;i<=m;++i){
		scanf("%d",opt+i);
		if(opt[i]==1){
			scanf("%d%d%d",x+i,y+i,&k);
			if(k<i)id[i-k-1].push_back(i);
		}
		if(opt[i]==2){
			scanf("%d",x+i);
		}
	}
	for(i=1;i<=m;++i){
		if(opt[i]==2){
			Add(dfn[x[i]],1);Add(dfn[x[i]]+siz[x[i]],-1);
		}
		for(int&v:id[i])ans[v]=Q(x[v],y[v]);
		if(opt[i]==1){
			printf("%d %d\n",dis(x[i],y[i]),ans[i]);
		}
	}
}
```