# P1807 题解

- **Upd 2021/3/10:修了一下 $\LaTeX$，并改正了评论中提到的问题。**

大家有没有发现，这题的正解是拓扑+DP……  
反正闲着没事，写篇拓扑玩玩。因为题目中说了

>且当为 $G$ 中的一条边时有 $i < j$。

所以点 $1$ 绝对是一个没有入度的点，而且不会出现环。而这一点正好满足拓扑的要求。但是，题目并不保证只有点 $1$ 是没有入度的。所以要判断其他没有入度的点。而对他们的处理是？也许你一开始会想到加入队列，那你就错了！他们本身是无法到达的点，所以根本不可能会延伸到其他地方，如果加入队列，那么就会导致个别点，甚至所有点的答案错误。那么就是不管他？还是错了！如果不管，那么他们延伸出来的点的入度永远大于 $0$，因为还有那些点。以至于发生和上一种方法一样的错误，甚至使终点无法到达！那么解决方法就是先做一遍 for 循环，找到那些点，再把延伸出来的点的入度 $-1$，如果这些点入读 $-1$ 后又变成了入度为 $0$ 的点，那么再做同样的处理。至于一个点的最长路的转移方程就是：  
$min\{\text{入度1+相应的边},\text{入度2+相应的边……入度n加相应的边}\}$  
和 SPFA、dijkstra 的松弛操作差不多。  
**代码：**
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m,in[1505];//存入度数量
vector<int>g[1505];//存边
vector<int>d[1505];//存边权
queue<int>q;//队列
int v[1505];//存最长路
int main()
{
	cin>>n>>m;
	for(int i=1;i<=m;i++)
	{
		int ff,tt,dd;
		cin>>ff>>tt>>dd;
		g[ff].push_back(tt);
		d[ff].push_back(dd);
		in[tt]++;
	}
	for(int i=2;i<=n;i++)
	{
		v[i]=-1e9;
		if(!in[i]) q.push(i);
	}//初始化
	while(!q.empty())
	{
		int x=q.front();
		q.pop();
		for(int i=0;i<g[x].size();i++)
			if(!--in[g[x][i]]) q.push(g[x][i]);
	}
	//废弃其他的入度为0的点。
	q.push(1);
	while(!q.empty())
	{
		int x=q.front();
		q.pop();
		for(int i=0;i<g[x].size();i++)
		{
			if(v[g[x][i]]<v[x]+d[x][i]) v[g[x][i]]=v[x]+d[x][i];//松弛
			if(!--in[g[x][i]]) q.push(g[x][i]);//如果入度为0就加入队列
		}
	}
	if(v[n]==-1e9) cout<<"-1";
	else cout<<v[n];//输出结果
	return 0;
}
```
安利[博客](https://www.luogu.org/blog/yhdhg1395754790/)