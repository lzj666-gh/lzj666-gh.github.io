# P3469 题解

首先可以对第$i$个节点进行讨论

假如$i$不是割点（即把$i$和它有关的所有边都去除后图依然联通）那么这个图只有$i$是独立在外面的，由于求的是有序点对，所以除了$i$以外的$n-1$个点作为一个大的连通图对$i$加边，即为$2*(n-1)$对

假如$i$是割点，那么会把图分为$a$个连通块以及$i$本身,由于tarjan在求割点的过程中是一棵搜索树往下遍历，所以除了它和它的子树外，还会有其他剩余点共同构成另一个连通块（有点类似树的重心的求法）设$i$所有子树的和为$sum$,第$i$个子树的节点总数为$t[i]$，点对的数量便为$$t[1]*(n-t[1])+t[2]*(n-t[2])+\cdots+t[a]*(n-t[a])+(n-1)+(1+sum)*(n-sum-1)$$

所以在求割点的过程中每遇到一个$low[v]>=dfn[u]$便把对数加上$t[i]*(n-t[i])$最后假如不是割点那直接把对数更新为$2*(n-1)$是割点则加上$n-1+(n-sum-1)*(sum+1)$
最后遍历输出答案即可
```cpp
#include<bits/stdc++.h>
using namespace std;
const int maxn=1000010;
inline int read()
{
	int x=0,t=1;char ch=getchar();
	while(ch>'9'||ch<'0'){if(ch=='-')t=-1;ch=getchar();}
	while(ch>='0'&&ch<='9') x=x*10+ch-'0',ch=getchar();
	return x*t;
}
int n,m,head[maxn],num=0;
int dfn[maxn],low[maxn],size[maxn],tot=0;
long long ans[maxn];
bool cut[maxn];
struct node{
	int v,nex;
}e[maxn];
void add(int u,int v)
{
	e[++num].v=v;
	e[num].nex=head[u];
	head[u]=num;
}
void tarjan(int u)
{
	dfn[u]=low[u]=++tot;
	size[u]=1;
	int flag=0,sum=0;
	for(int i=head[u];i;i=e[i].nex)
	{
		int v=e[i].v;
		if(!dfn[v])
		{
			tarjan(v);
			size[u]+=size[v];
			low[u]=min(low[u],low[v]);
			if(low[v]>=dfn[u])
			{
				ans[u]+=(long long)size[v]*(n-size[v]);
				sum+=size[v];
				flag++;
				if(u!=1||flag>1) cut[u]=true;
			}
		}
		else low[u]=min(low[u],dfn[v]);
	}
	if(!cut[u]) ans[u]=2*(n-1);
	else ans[u]+=(long long)(n-sum-1)*(sum+1)+(n-1);
}
int main()
{
	n=read(),m=read();
	for(int i=1;i<=m;i++)
	{
		int x,y;
		x=read(),y=read();
		add(x,y),add(y,x);
	}
	tarjan(1);
	for(int i=1;i<=n;i++) printf("%lld\n",ans[i]);
	return 0;
}

```