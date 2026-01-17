# P3128 题解

LCA+树上差分

我们要统计每个点经过几次，也就是在每一条路径上，给路径上的点+1，所以我们此题用树上差分就可以很快得得到每个点经过的次数

具体是这样的：假设一条u到v的路径，那么这条路径是u--->lca(u,v)--->v的，所以我们把u--->lca(u,v)与lca(u,v)--->v两条路径各自加一，也就是++power[u],++power[v],power[lca(u,v)]-=2

但是这样一来，lca(u,v)上+2又-2等于0，也就是u--->v整条路经上除了lca(u,v)都加了1，为了排除这个干扰，我们把power[lca(u,v)]-=2改成- -power[lca(u,v)],- -power[lca(u,v)的父亲]

LCA用倍增比较方便，最后遍历整棵树统计和

Code:
```
#include <bits/stdc++.h>
using namespace std;
#define maxn 50010
#define ll long long
#define res register int
struct Node{
	int to,next;
};
Node edge[maxn<<2]; //链式前向星要多开几倍数组
int head[maxn<<2],power[maxn],n,m,d[maxn],fa[maxn][30],ans,num;

inline int read(){ //快读
	int s=0;
	char c=getchar();
	while (c<'0' || c>'9') c=getchar();
	while (c>='0' && c<='9') s=s*10+c-'0',c=getchar();
	return s;
}
//链式前向星
inline void add(int x,int y){edge[++num].to=y,edge[num].next=head[x],head[x]=num;}
//接下来是初始化
inline void work(int u,int fath){
	d[u]=d[fath]+1,fa[u][0]=fath;
	for (res i=0;fa[u][i];++i) fa[u][i+1]=fa[fa[u][i]][i];
	for (res i=head[u];i;i=edge[i].next){
		int e=edge[i].to;
		if (e!=fath) work(e,u);
	}
}
//倍增求LCA
inline int Lca(int u,int v){
	if (d[u]>d[v]) swap(u,v);
	for (res i=20;i>=0;--i) if (d[u]<=d[v]-(1<<i)) v=fa[v][i];
	if (u==v) return u;
	for (res i=20;i>=0;--i) if (fa[u][i]!=fa[v][i]) u=fa[u][i],v=fa[v][i];
	return fa[u][0];
}
//累计
inline void Get(int u,int fath){
	for (res i=head[u];i;i=edge[i].next){
		int e=edge[i].to;
		if (e==fath) continue;
		Get(e,u);
		power[u]+=power[e];
	}
	ans=max(ans,power[u]);
}

int main(){
	n=read(),m=read();
	int x,y;
	for (res i=1;i<n;++i){
		x=read(),y=read();
		add(x,y); add(y,x);
	}
	work(1,0);
	for (res i=1; i<=m; ++i){
		x=read(),y=read();
		int lca=Lca(x,y);
		++power[x];++power[y];--power[lca];--power[fa[lca][0]]; //树上差分
	}
	Get(1,0);
	printf("%d\n",ans);
	return 0;
}
```