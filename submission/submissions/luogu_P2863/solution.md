# P2863 题解

## 1.1 简述强联通分量与Tarjan
在有向图G中，如果两个顶点间至少存在一条路径，称两个顶点强连通。如果有向图G的每两个顶点都强连通，称G是一个强连通图。非强连通图有向图的极大强连通子图，称为强连通分量。

~~说白了就是如果一个有向图的子图里每个点可以两两互达，那么这个子图是一个强联通分量~~

Tarjan算法就是基于DFS求强联通分量的算法。


## 2.1 Tarjan思想

#### 2.1.1 Tarjan维护的变量
在Tarjan算法中我们维护如下的变量：
```
vector<int> G[maxn];//图本身（邻接表）
stack<int>s;//栈，存放答案
int vis[maxn];//标记点是否在栈中
int dfn[maxn];//节点i的时间戳
int low[maxn];//节点i能够回溯到的最早位于栈中的节点。（子树的根，可以理解为并查集的“祖先”一类的东西）
int color[maxn];//每个点属于第几个强联通分量
int colornum;//强连通分量的个数
int cnt;//当前时间
```

#### 2.2.2 Tarjan算法运行过程

1. 按照深度优先遍历的方式遍历这张图。
2. 遍历当前节点所出的所有边。在遍历过程中：

    ( 1 ) 如果当前边的终点还没有访问过，访问。

	回溯回来之后比较当前节点的low值和终点的low值。将较小的变为当前节点的low值。（因为遍历到终点时有可能触发了2）

	( 2 )  如果已经访问过，那我们一定走到了一个之前已经走过的点（终点的时间戳一定比当前的小）

	则比较当前节点的low值和终点的dfn值。将较小的变为当前节点的low值
3. 在回溯过程中，对于任意节点u用其出边的终点v的low值来更新节点u的low值。因为节点v能够回溯到的已经在栈中的节点，节点u也一定能够回溯到。因为存在从u到v的直接路径，所以v能够到的节点u也一定能够到。

4. 当一个节点的dfn值和low值相等时，这个节点是一个强联通分量的“根”。压栈，输出。

~~我知道这让你听得很迷糊，~~先来一段伪代码看看吧。
```
void tarjan(int u)//当前节点
{
	dfn[u]=low[u]=++cnt;//该节点本身是一个强联通分量
    节点入栈;
    vis[u]=true;//当前节点已入栈
    for(遍历该节点所有出边)
    {
    	int v=当前边的终点;
        if (!dfn[v])
        {
        	tarjan(v);//深度优先遍历
            low[u]=min(low[u],low[v]);
        }
        else low[u]=min(dfn[v],low[u]);
    }
    if (low[u]==dfn[u])
    {
    	while(栈顶!=v)
        {
            染色;
        	出栈;
        }
    }
    染色;
    出栈;
}
```
手模一组数据就不模啦，网上到处都是。

## 3.1 完整code
这里以洛谷P2863 `[USACO06JAN]牛的舞会The Cow Prom`为例。题意为：给定一个图，要求图中节点数大于一的强联通分量个数。
对于这道~~模板~~题，我们应当做到一遍A掉。
```
#include<bits/stdc++.h>
#define maxn 10001
using namespace std;
vector<int>G[maxn];
stack<int>s;
int n,m;
int dfn[maxn],used[maxn],vis[maxn],low[maxn],color[maxn],num[maxn],colornum=0,cnt=0,ans=0;
void paint(int x)
{
    s.pop();
    color[x]=colornum;
    num[colornum]++;
    vis[x]=false;
}
void tarjan(int x)
{
    dfn[x]=low[x]=++cnt;
    s.push(x);
    vis[x]=used[x]=true;
    for(int i=0;i<G[x].size();i++)
    {
        int q=G[x][i];
        if (!dfn[q])
        {
            tarjan(q);
            low[x]=min(low[x],low[q]);
        }
        else if (vis[q]) low[x]=min(low[x],dfn[q]);
    }
    if (low[x]==dfn[x])
    {
        colornum++;
        while(s.top()!=x)
        {
            int t=s.top();
            paint(t);
        }
        paint(x);
    }
}
int main()
{
    cin>>n>>m;
    for(int i=1;i<=m;i++)
    {
        int u,v;
        cin>>u>>v;
        G[u].push_back(v);
    }
    for(int i=1;i<=n;i++)
    {
        if (!used[i]) tarjan(i);
    }
    for(int i=1;i<=colornum;i++)
    {
        if (num[i]>1) ans++;
    }
    cout<<ans;
    return 0;
}
```

### 3.2 我接下来学习什么算法？
缩点。[ P2341 [HAOI2006]受欢迎的牛](https://www.luogu.org/problemnew/show/P2341)可以作为一道模板题。

敬请期待。