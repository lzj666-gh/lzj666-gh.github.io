# P1137 题解

我看了一下其他大佬的题解，大部分都是拓扑排序加上DP。那么我想有的人是不明白为什么这么做的，拓扑排序有什么性质使得可以DP呢?下面我就提一下。

对一个有向无环图(Directed Acyclic Graph简称DAG)G进行拓扑排序，是将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边(u,v)∈E(G)，则u在线性序列中出现在v之前。 （源自百度）

通俗的说就是，一张有向无环图的拓扑序可以使得任意的起点u,它的一个终点v，在序列中的顺序是u在前v在后

我下面先附上代码，然后在继续说明

```
#include<bits/stdc++.h>
using namespace std;

const int maxn=100000+15;
int n,m,sum,tot;
int head[maxn],ru[maxn],ts[maxn],dp[maxn];
struct EDGE
{
	int to;int next;
}edge[maxn<<2];
void add(int x,int y)
{
	edge[++sum].next=head[x];
	edge[sum].to=y;
	head[x]=sum;
}
void topsort()
{
	queue <int> q;
	for (int i=1;i<=n;i++)
	if (ru[i]==0) {
	q.push(i);
	ts[++tot]=i;
}
	while (!q.empty())
	{
		int u=q.front();q.pop();
		for (int i=head[u];i;i=edge[i].next)
		{
			int v=edge[i].to;
			ru[v]--;
			if (ru[v]==0) {
			q.push(v);ts[++tot]=v;
		}
		}
	}
}
int main()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=m;i++)
	{
		int u,v;
		scanf("%d%d",&u,&v);
		add(u,v);
		ru[v]++;
	}
	topsort();
	for (int i=1;i<=n;i++) dp[i]=1;
	for (int i=1;i<=n;i++)
	{
		int u=ts[i];
		for (int j=head[u];j;j=edge[j].next)
		{
			int v=edge[j].to;
			dp[v]=max(dp[v],dp[u]+1);
		}
	}
	for (int i=1;i<=n;i++)
	printf("%d\n",dp[i]);
	return 0;
}
```

仔细看DP部分，还记得DP需要满足什么原则吗？无后效性。如果不是在拓扑序中进行DP,会完全破坏无后效性（当然这也下面为什么有人用记忆化搜索的原因，记忆化搜索同样可以解决无后效性的问题）。正是因为拓扑序u在前,v在后的性质，这才选择使用拓扑排序，毕竟它的代码实现很轻松，而且运行时间也不差。

至于怎么求拓扑序，就是把入度为0（就是没有边把它作为终点）的点入队，并加入拓扑序。之后断掉以这个点为起点的边，即将这些边的终点的入度减一，直到队为空就好。

那么就是这些了，希望对大家有帮助