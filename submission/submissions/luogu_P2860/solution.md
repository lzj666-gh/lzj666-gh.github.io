# P2860 题解

题解 P2860 【冗余路径】

注意：因为已有题解讲明白了题意和思路，所以我就不在此重复了，我只是想说明一下最简单清晰的一个方法——这就是一个求双联通分量的模板（当然，你也可以理解为无向图缩点）

所以，打一遍模板即可。当然，对于这个模板，我想要讲的清楚一些。

对于无向图的缩点，由于是无向图，所以要从u到v建一条边，又要从v到u建一条边，但是，在tarjan时会有两条边重复，这是一个麻烦，而且，还不得不建两条边，这该怎么办呢？

解决的方法就是，当同一条无向边的两条有向边的其中一条走过时，把另一条同时赋值为走过，这就要用到一个神奇的公式，^1。 举例来说，0^1=1,1^1=0; 2^1=3,3^1=2; 4^1=3,3^1=4......相信大家已经都发现了规律。而建边的时候，一条无向边的两条有向边刚好相差1，这不很OK嘛？问题解决了。

不过要注意，我的cnt，就是边的初始值，赋值为1，这是用来凑数字的。所以边，是从第2，3条；第4,5条......这样下去的（对于0,1条，因为自己代码习惯，我就直接从2开始了，0,1条加进去应该也可以，你想试的话也可以试试）

其余地方，就和有向图的缩点完全一样了。

```cpp
#include <bits/stdc++.h>
using namespace std;
const int N=5e3+5,M=1e4+5;
int n,m,vis[M<<1],du[N],ans;
int cnt=1,head[N],u[M],v[M];
int now,top,col,dfn[N],low[N],sta[N],color[N];
struct edge{int next,to;}e[M<<1];

inline void add(int u,int v)
{
	cnt++;
	e[cnt].next=head[u];
	e[cnt].to=v;
	head[u]=cnt;
	cnt++;
	e[cnt].next=head[v];
	e[cnt].to=u;
	head[v]=cnt;
}

inline void tarjan(int u)
{
	dfn[u]=low[u]=++now;	
	sta[++top]=u;
	for (register int i=head[u]; i; i=e[i].next)
	if (!vis[i])
	{
	vis[i]=vis[i^1]=1;
		if (!dfn[e[i].to])
		{
			tarjan(e[i].to);	
			low[u]=min(low[u],low[e[i].to]);
		}
		else low[u]=min(low[u],dfn[e[i].to]);
	}
	if (low[u]==dfn[u])
	{
		color[u]=++col;	
		while (sta[top]!=u) color[sta[top]]=col,top--;
		top--;
	}
}

int main(){
memset(head,0,sizeof(head));
memset(dfn,0,sizeof(head));
//下面过程如果不懂，看前面的几篇题解吧
	scanf("%d%d",&n,&m);
	for (register int i=1; i<=m; ++i) scanf("%d%d",&u[i],&v[i]),add(u[i],v[i]);
	for (register int i=1; i<=n; ++i) if (!dfn[i]) tarjan(i);
	for (register int i=1; i<=m; ++i) if (color[u[i]]!=color[v[i]]) du[color[u[i]]]++,du[color[v[i]]]++;
	for (register int i=1; i<=col; ++i) if (du[i]==1) ans++;
printf("%d\n",ans+1>>1);
return 0;	
}
```
# 代码可以当作模板收藏。
