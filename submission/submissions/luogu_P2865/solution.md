# P2865 题解

看到题解好多dijkstra，作为一名钟爱于spfa的蒟蒻看不下去了。

有些spfa要跑两边，代码量要曾长好多(虽然复制)，而且还慢。

下面开始我的表演：

首先看清楚题意：题目说的是从n点往回走(因为双向边，所以好多人注意到也过了)

接着明确一个数组：
	
    d[i][0]表示到i点的最短路
    
    d[i][1]表示到i点的次短路
    
初始化数组，d[n][0]=0,d[n][1]=INF,其他的也都是INF；

然后将点进入队列开始，进行对其他点的更改。

记当前节点编号为u，目前所连边的编号为v。

我们将判断分为两块

(1)d[u][0]对于v点的影响。

(2)d[u][1]对于v点的影响。

####	(1)

如果$$d[u][0]+dis[u,v]<d[v][0]$$,也就是说足影响v点，那么此时的次短路变成了更新前的最短路，最短路更新。


如果
$$d[v][0]<=d[u][0]+dis[u,v]$$

$$d[v][0]>=d[u][0]+dis[u,v]$$

就是说不足以影响最短路，却可以影响次短路，能更新自然更新。

####	(2)

再开始判断d[u][1]对v点的影响

前边(1)部分先更新的最短路。

如果足矣更新最短路：那么到u点的最短路一定小于到u点的次短路，所以用d[u][0]一定更优。

如果没有更新：那么既然最短路都不能更新了，次短路还有啥用。

总的来说对v点最短路这一块理解就好，木有代码。

对于次短路我们要判断一下是否更新。

注意注意：以上判断都需要注意次短路严格小于最短路。

所以：

```cpp
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue> 
using namespace std;
struct ahah{
	int nxt,to,dis;
}edge[200010];
int n,m;
int head[5010],tot;
void add(int x,int y,int z)
{
	edge[++tot].nxt=head[x],edge[tot].to=y,edge[tot].dis=z,head[x]=tot;
}
int d[5010][2];
bool vis[5010];
queue <int> que;
int read()
{
	int sum=0,fg=1; char c=getchar();
	while(c<'0'||c>'9'){if(c=='-')fg=-1;c=getchar();}
	while(c>='0'&&c<='9'){sum=sum*10+c-'0';c=getchar();}
	return sum*fg;
}
void spfa(int s)
{
	memset(d,0x7f,sizeof(d));
	que.push(s);vis[s]=1;
	d[s][0]=0;
	while(!que.empty())
	{
		int u=que.front();
		vis[u]=0;que.pop() ;
		for(int i=head[u];i;i=edge[i].nxt)
		{
			int v=edge[i].to;
			if(d[v][0]>d[u][0]+edge[i].dis)
			{
				d[v][1]=d[v][0];
				d[v][0]=d[u][0]+edge[i].dis;
				if(!vis[v])vis[v]=1,que.push(v);
			}
			if(d[v][1]>d[u][0]+edge[i].dis&&d[u][0]+edge[i].dis>d[v][0])
			{
				d[v][1]=d[u][0]+edge[i].dis;
				if(!vis[v])vis[v]=1,que.push(v);
			}
			if(d[v][1]>d[u][1]+edge[i].dis)
			{
				d[v][1]=d[u][1]+edge[i].dis;
				if(!vis[v])vis[v]=1,que.push(v);
			}
		}
	} 
}
int main()
{
	int x,y,z;
	n=read();m=read();
	for(int i=1;i<=m;i++)
	{
		x=read(),y=read(),z=read();
		add(x,y,z);add(y,x,z);
	}
	spfa(n);
	printf("%d",d[1][1]);
}
```

喜欢您就点个赞，谢谢。

顺便打一波广告，([逃](https://www.cnblogs.com/rmy020718/p/9492307.html)。