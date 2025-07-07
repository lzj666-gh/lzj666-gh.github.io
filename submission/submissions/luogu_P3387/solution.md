# P3387 题解

缩点，就是把一张有向有环图中的环缩成一个个点，形成一个有向无环图。

首先我介绍一下为什么这题要缩点（有人肯定觉得这是放屁，这不就是缩点的模板题吗？但我们不能这么想，考试的时候不会有人告诉你打什么板上去吧）

根据题目意思，我们只需要找出一条点权最大的路径就行了，不限制点的个数。那么考虑对于一个环上的点被选择了，一整条环是不是应该都被选择，这一定很优，能选干嘛不选。很关键的是题目还允许我们重复经过某条边或者某个点，我们就不需要考虑其他了。因此整个环实际上可以看成一个点（选了其中一个点就应该选其他的点）

那么就正式开始缩环为点了。当然了，首先肯定是找环，为大家推荐两篇博客（不是我宣传，这两篇博客也只是我找的[]
(http://blog.csdn.net/acmmmm/article/details/16361033)）[](http://blog.csdn.net/sentimental_dog/article/details/53790582)

希望博客被我转载的博主不要介意。

看看这两篇博客，我觉得大家就有了一个基本认识了。在缩点操作中，最重要的是维护三个东西，它们在我代码里分别是stac（栈）（ps：之所以不加k是因为万能头文件的荼毒），dfn（时间戳），low(够追溯到的最早的栈中节点的次序号)，详细的解释在代码注释里。

下面就是考虑对这三个东西的运用。详细参考博客（博客带图），需要注意的是，当dfn[u]==low[u]时，表明u一定是环上的一点，且环上的其他点就是u的子树。为什么呢？看代码  
low[x]=dfn[x]=++tim;
           
low[x]=min(low[x],low[v]);

我截取了两句代码，第一句是对点x的low，dfn的初始化。在之后的操作中,low[x]始终取自己子树low[v]的较小值，那么什么情况会使得dfn[u]又“重新”和low[u]相等呢，就是在u的子树中有一条边（就是博客1中的后向边）直接指回了u。这样不就是形成了一个环了吗？

之后就是把环上所有的点的sd都变成这个u，即用u代替整个环，并把权值集中在u上

还有值得注意的，这个栈表示的究竟是什么？（这个在博客1中也有），根据我的理解表示的是当前搜索的一条链上的一个个点吧。

下面我附上代码先

```cpp
#include<bits/stdc++.h>
using namespace std;

const int maxn=10000+15;
int n,m,sum,tim,top,s;
int p[maxn],head[maxn],sd[maxn],dfn[maxn],low[maxn];//DFN(u)为节点u搜索被搜索到时的次序编号(时间戳)，Low(u)为u或u的子树能够追溯到的最早的栈中节点的次序号 
int stac[maxn],vis[maxn];//栈只为了表示此时是否有父子关系 
int h[maxn],in[maxn],dist[maxn];
struct EDGE
{
	int to;int next;int from;
}edge[maxn*10],ed[maxn*10];
void add(int x,int y)
{
	edge[++sum].next=head[x];
	edge[sum].from=x;
	edge[sum].to=y;
	head[x]=sum;
}
void tarjan(int x)
{
	low[x]=dfn[x]=++tim;
	stac[++top]=x;vis[x]=1;
	for (int i=head[x];i;i=edge[i].next)
	{
		int v=edge[i].to;
		if (!dfn[v]) {
		tarjan(v);
		low[x]=min(low[x],low[v]);
	}
	    else if (vis[v])
	    {
	    	low[x]=min(low[x],low[v]);
		}
	}
	if (dfn[x]==low[x])
	{
		int y;
		while (y=stac[top--])
		{
			sd[y]=x;
			vis[y]=0;
			if (x==y) break;
			p[x]+=p[y];
		}
	}
}
int topo()
{
	queue <int> q;
	int tot=0;
	for (int i=1;i<=n;i++)
	if (sd[i]==i&&!in[i])
	{
		q.push(i);
        dist[i]=p[i];
	 } 
	while (!q.empty())
	{
		int k=q.front();q.pop();
		for (int i=h[k];i;i=ed[i].next)
		{
			int v=ed[i].to;
			dist[v]=max(dist[v],dist[k]+p[v]);
			in[v]--;
			if (in[v]==0) q.push(v);
		}
	}
    int ans=0;
    for (int i=1;i<=n;i++)
    ans=max(ans,dist[i]);
    return ans;
}
int main()
{
	scanf("%d%d",&n,&m);
	for (int i=1;i<=n;i++)
	scanf("%d",&p[i]);
	for (int i=1;i<=m;i++)
	{
		int u,v;
		scanf("%d%d",&u,&v);
		add(u,v);
	}
	for (int i=1;i<=n;i++)
	if (!dfn[i]) tarjan(i);
	for (int i=1;i<=m;i++)
	{
		int x=sd[edge[i].from],y=sd[edge[i].to];
		if (x!=y)
		{
			ed[++s].next=h[x];
			ed[s].to=y;
			ed[s].from=x;
			h[x]=s;
			in[y]++;
		}
	}
	printf("%d",topo());
	return 0;
}
```

在处理了环后，我们就重新建立一张图，以每个环为节点（孤立一个点也算也算环的，其实也就是强联通分量了）。在这张图中我们要dp，显然对于任意边<u,v>,dp[v]=max(dp[v],dp[u]+p[v])，p[v]是v是这个环的总权值。

那么怎么解决无后效性问题呢？答案就是拓扑排序，至于为什么，在我的另一篇题解里我有提及。这下我有安利嫌疑了，但我还是希望大家去看一看，下面我附上链接。

[](https://www.luogu.org/blog/xxzh2425/p1137-lv-xing-ji-hua-ti-xie)
这也是一篇题解，其实主要讲的就是拓扑排序解决DP的无后效性问题了

那么就讲完了，如果有帮助，希望大家不要吝啬自己的赞。