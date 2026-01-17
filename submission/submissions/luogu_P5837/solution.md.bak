# P5837 题解

一道略有变形的最短路模板题。

-----------

### 题意简述

给定一个**无向图**，每条边有其代价 $c$ 和限制 $f$。求出一条从 $1$ 到 $n$ 的路径，使得 $\dfrac{\min\{f_i\}}{\sum c_i}$ 最大。

### 解题思路

只要认真想真的不难。

有两个条件，考虑先枚举 $f$。既然要使分母 $\sum c_i$ 最小，那不相当于以 $c$ 为边权跑最短路？

于是我们可以跑 dijkstra 或 spfa。不过为了达到枚举 $f$ 起的限制作用，我们在**每次松弛操作之前**，要先判断这条边的限制是否**大于** $f$。否则不把这条边计算的最短路中，因为它不满足当前限制。

跑完最短路更新答案即可。

这里使用堆优化的 dijkstra，时间复杂度约为 $O(n^2\log n)$，可以通过本题。

当然也有二分等其他做法，不过已经没有必要了。不熟练的还容易出错。所以能简单算的就简单算。

### 实现细节

- 建图注意是无向图。

- 由于需要多次跑最短路，记得清空某些数组。

- 重载`priority_queue`的时候，符号不要写错。

### 参考代码

```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;

#define INF 0x7f7f7f7f
const int MAXN=3005;
int n,m,ans;
struct node
{
	int to,cost,limit;
	bool operator<(const node& a)const
	{
		return cost>a.cost;//方向别反了
	}
};
vector<node> edge[MAXN];
int dis[MAXN],limit[MAXN];
bool visit[MAXN];

void input(void)
{
	cin>>n>>m;
	for(int i=1;i<=m;i++)
	{
		int a,b,x;
		cin>>a>>b>>x>>limit[i];
		edge[a].push_back(node{b,x,limit[i]});//无向图
		edge[b].push_back(node{a,x,limit[i]});
	}
}

int dijkstra(const int limit)
{
	priority_queue<node> q;//记得清空
	memset(visit,false,sizeof(visit));
	memset(dis,INF,sizeof(dis));
	dis[1]=0;
	q.push(node{1,0,limit});
	while(!q.empty())//模板
	{
		const int u=q.top().to;
		q.pop();
		if(visit[u])
		 continue;
		visit[u]=true;
		for(auto v:edge[u])
		 if(v.limit>=limit && dis[v.to]>dis[u]+v.cost)
		 {//注意限制
		 	dis[v.to]=dis[u]+v.cost;
		 	q.push(node{v.to,dis[v.to],limit});
		 }
	}
	return dis[n];
}

int main()
{
	input();
	for(int i=1;i<=m;i++)//枚举 m 次而非 n 次
	 ans=max(ans,limit[i]*int(1e6)/dijkstra(limit[i]));//更新答案
	cout<<ans<<endl;
	return 0;
}
```