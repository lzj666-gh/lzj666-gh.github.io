# P2740 题解

### 注意:在此出现的代码均不保证可以AC，代码是我在AC这道题两个月以上后临时敲的，仅为笔者在写这篇题解时临时敲出来的，未进行过正确性验证，请不要尝试使用某两个快捷键。   
相当经典的一道网络流题目。        
分析题意，发现从1-M的最大流即为所求。    
刚好在这里介绍几个网络流算法(会网络最大流算法的同学们就可以跳过了):        
算法1.EK(Edmond-Karp)算法:       
EK是一个**增广路**算法。         
介绍增广路之前，我们要先介绍一个概念，**残余网络**    ：   
一个图的残余网络，指图中边容量与当前流量的差值边构成的集合。      
简单来说，就是流过一个流之后，我们的路径减少的容量。     
这个算法是基于这样一个事实的:     
残余网络中的任何一个从终点到起点的有向路径都对应着原图中的一条增广路径。          
我们将原图中的容量减去当前流量的动作叫做增广。     
但是，我们当前做出的选择未必是最优的，所以我们对每条边建立一条反向边，容量为正向边减少的容量之和。    
我们一直进行增广操作，直到我们无法在进行增广:已经**没有**可以从s流向t的流了，路径**堵塞**了。     
我们过一遍算法流程(以最小费用最大流为范例):     
1.我们需要用一个遍历算法来判断有没有从s到达t的流。    
只要能从s流向t，我们就进行增广。   
由于我们这里的是最小费用最大流，我们使用spfa来判断:
```cpp
void mcmf()
{
    while(spfa(s,t))
    {
```
我们将在讲完这个算法主过程后展示用于判断的spfa代码。                 
```cpp
    while(spfa(s,t))
    {
        int now=t;
        maxf+=flow[t];
        minc+=dist[t]*flow[t];
```
我们用```last[i]```表示流到i点的当前流量。    
根据到达t点的当前流量，我们更新网络总最大流。   
我们用```pre[i]```表示点i的前驱(即路径上i的**前一个**点)       
用```last[i]```表示路径中指向i的边(即**要**进行**流量减少**的边) 
```cpp
        while(now!=s)
        {
            a[last[now]].flow-=flow[t];
            a[last[now]^1].flow+=flow[t];
            now=pre[now];
        }
    }
}
```
我们再顺着前驱往前回溯，并沿途更新正反两条边的流量。         
mcmf主过程完整代码:
```cpp
void mcmf()
{
    while(spfa(s,t))
    {
        int now=t;
        maxf+=flow[t];
        minc+=dist[t]*flow[t];
        while(now!=s)
        {
            a[last[now]].flow-=flow[t];
            a[last[now]^1].flow+=flow[t];
            now=pre[now];
        }
    }
}
```
spfa过程详解:      
初始化：      
初始化中，我们要将当前最大流，当前最小费用置为INF，以及将vis数组置为0。
同时，将```dist[s]```置为0，将```pre[s]```置为-1(代表没有前驱)，再将s入队。      
```cpp
bool spfa(int s,int t)
{
    queue<int> q;
    memset(vis,0,sizeof(vis));
    memset(flow,INF,sizeof(flow));
    memset(dist,INF,sizeof(dist));
    q.push(s);
    dist[s]=0;
    pre[t]=-1;
    vis[s]=1;
```
我们与普通的spfa过程一样，顺序取出，遍历每个点:
```cpp
    while(!q.empty())
    {
        int now=q.front();
        q.pop();
        vis[now]=0;
        for(int i=head[now];i!=-1;i=a[i].next)
        {
            int v=a[i].to;
```
然后顺着最短路走。        
在这里，有几点要注意：       
1.我们跑的是**网络流**算法，所以我们只能经过**剩余流量大于零的路径**          
2.我们在这里要记录pre数组和last数组的值。      
3.有些人可能会怀疑spfa算法跑网络流的**正确性**，但由于我们只在**流量不为零的路径**上进行松弛，所以我们的spfa算法是正确的(我们取的**最短路径**也必定是一条**增广路径**)。      
4.我们在更新flow数组时，记得要取**min值**。
```cpp
            if(a[i].flow>0&&dist[v]>dist[now]+a[i].cost)
            {
                dist[v]=dist[now]+a[i].cost;
                pre[v]=now;
                last[v]=i;
                flow[v]=min(flow[now],a[i].flow);
                if(!vis[v])
                {
                    q.push(v);
                    vis[v]=1;
                }
```
算法结束:       
在这里的的spfa是一个判断算法，所以我们最后要输出一个bool值，在这里，我们判断```pre[t]```是否为-1即可。(即是否能够流向t)
```
            }
        }
    }
    return pre[t]!=-1;
}
```
spfa过程代码
```cpp
bool spfa(int s,int t)
{
    queue<int> q;
    memset(vis,0,sizeof(vis));
    memset(flow,INF,sizeof(flow));
    memset(dist,INF,sizeof(dist));
    q.push(s);
    dist[s]=0;
    pre[t]=-1;
    vis[s]=1;
    while(!q.empty())
    {
        int now=q.front();
        q.pop();
        vis[now]=0;
        for(int i=head[now];i!=-1;i=a[i].next)
        {
            int v=a[i].to;
            if(a[i].flow>0&&dist[v]>dist[now]+a[i].cost)
            {
                dist[v]=dist[now]+a[i].cost;
                pre[v]=now;
                last[v]=i;
                flow[v]=min(flow[now],a[i].flow);
                if(!vis[v])
                {
                    q.push(v);
                    vis[v]=1;
                }
            }
        }
    }
    return pre[t]!=-1;
}
```
EK算法求解草地排水完整代码：
```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<algorithm>
#include<complex>
#include<iostream>
#include<map>
#include<queue>
#include<vector>
#define INF 0x3f3f3f3f
using namespace std;
struct edge
{
    int to,next,flow,cost;
}a[2000020];
int cnt(0);
int n,m,s,t;
int x,y,z,f;
int flow[1000010],head[1000010];
int dist[1000010],vis[1000010];
int pre[1000010],last[1000010];
int maxf(0),minc(0);
void addedge(int xi,int yi,int fi,int ci)
{
    a[cnt].to=yi;
    a[cnt].next=head[xi];
    a[cnt].flow=fi;
    a[cnt].cost=ci;
    head[xi]=cnt++;
}
bool spfa(int s,int t)
{
    queue<int> q;
    memset(vis,0,sizeof(vis));
    memset(flow,INF,sizeof(flow));
    memset(dist,INF,sizeof(dist));
    q.push(s);
    dist[s]=0;
    pre[t]=-1;
    vis[s]=1;
    while(!q.empty())
    {
        int now=q.front();
        q.pop();
        vis[now]=0;
        for(int i=head[now];i!=-1;i=a[i].next)
        {
            int v=a[i].to;
            if(a[i].flow>0&&dist[v]>dist[now]+a[i].cost)
            {
                dist[v]=dist[now]+a[i].cost;
                pre[v]=now;
                last[v]=i;
                flow[v]=min(flow[now],a[i].flow);
                if(!vis[v])
                {
                    q.push(v);
                    vis[v]=1;
                }
            }
        }
    }
    return pre[t]!=-1;
}
void mcmf()
{
    while(spfa(s,t))
    {
        int now=t;
        maxf+=flow[t];
        minc+=dist[t]*flow[t];
        while(now!=s)
        {
            a[last[now]].flow-=flow[t];
            a[last[now]^1].flow+=flow[t];
            now=pre[now];
        }
    }
}
int main()
{
    memset(head,-1,sizeof(head));
    scanf("%d%d",&m,&n);
    s=1,t=n;
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d%d%d",&x,&y,&z,&f);
        addedge(x,y,z,f);
        addedge(y,x,0,-f);
    }
    mcmf();
    printf("%d",maxf);
    return 0;
}

```
算法2.Dinic算法:          
Dinic算法也是一个增广路算法。       
相信你们在看了前面的EK算法后，对增广路已经有了一定的了解。        
由于我们一般的增广路算法可能会一直会对同一条路径进行增广，会十分地浪费时间。       
例:       
![https://i.loli.net/2018/12/04/5c060e0682acd.jpg](https://i.loli.net/2018/12/04/5c060e0682acd.jpg)          
这可以说是一个经典例子了。       
考虑从2到3的，容量为1的有向路径，我们会反复地增广这条路径，甚至可能会对其进行1998次增广,十分的浪费时间。         
所以我们引入了**分层图**的概念:      
我们把图分为k层，一个点的层数对应其在bfs过程中的深度。         
在这种情况下，我们只从层次小的点走向层次大的点。      
我们用一个bfs过程来完成分层。     
bfs分层详解:      
与EK的spfa相似，Dinic的bfs过程也是一个判断函数，判断是否能从s走到t。      
来过一遍bfs流程:        
1.没什么好说的初始化：
```cpp
bool bfs(int s)
{
	queue<int> q;
	while(!q.empty())q.pop();
	memset(dep,-1,sizeof(dep));
	dep[s]=1;
	q.push(s);
```
注意这里将s的深度设为了1。        
2.接下来的过程与一般的bfs类似。       
只是注意这里要记录下深度(```dep[i]```)，并且判断流量是否为零(与EK的技巧是一样的)
```cpp
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
		for(int i=head[t];i!=-1;i=a[i].next)
		{
			int v=a[i].to;
			int f=a[i].flow;
			if((f>0)&&(dep[v]==-1))
			{
				dep[v]=dep[t]+1;
				q.push(v);
			}
```
在结束时要记得返回bfs的判断值。
如果```dep[t]```不为-1时代表我们能搜到t。     
如下:
```cpp
		}
	}
	return dep[t]!=-1;
}
```
bfs代码:
```cpp
bool bfs(int s)
{
	queue<int> q;
	while(!q.empty())q.pop();
	memset(dep,-1,sizeof(dep));
	dep[s]=1;
	q.push(s);
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
		for(int i=head[t];i!=-1;i=a[i].next)
		{
			int v=a[i].to;
			int f=a[i].flow;
			if((f>0)&&(dep[v]==-1))
			{
				dep[v]=dep[t]+1;
				q.push(v);
			}
		}
	}
	return dep[t]!=-1;
}
```
bfs结束之后，我们使用dfs进行一次遍历，并且沿路更新我们的当前流。      
dfs过程详解:         
我们规定int dfs(int u,int dist)代表当前在流入的流量为dist，编号为u的点,返回的值为当前网络可行的最大流量。        
首先是边界条件：
```cpp
int dfs(int u,int dist)
{
	if(u==t)return dist;
```
如果搜到了终点，就输出流入的流量。      
然后我们向下一个点进行搜索:
```cpp
	for(int i=head[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		int f=a[i].flow;
```
在这之后，我们试图对每一个当前点能到达的，且层数比当前点大一的点进行递归。          
但若网络在这里的流量为0(即被"阻塞"了)，就不再行考虑了。
```cpp
		if((dep[v]==dep[u]+1)&&(f!=0))
		{
			int df(dfs(v,min(dist,f)));
```
df代表"Δf"(流量差)，即当前状况下可行的最大流量。
我们依据这个，对每个流经的边进行更新。
```cpp
			if(df>0)
			{
				a[i].flow-=df;
				a[i^1].flow+=df;
				return df;
			}
		}
	}
	return 0;
}
```
dfs过程完整代码:      
```cpp
int dfs(int u,int dist)
{
	if(u==t)return dist;
	for(int i=head[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		int f=a[i].flow;
		if((dep[v]==dep[u]+1)&&(f!=0))
		{
			int df(dfs(v,min(dist,f)));
			if(df>0)
			{
				a[i].flow-=df;
				a[i^1].flow+=df;
				return df;
			}
		}
	}
	return 0;
}
```
接下来分析dinic的主过程，有了我们前面的基础支持，理解起来就不会太难了。       
首先我们初始化最大流:       
```cpp
void dinic()
{
	maxf=0;
	int nowf(0);
```
然后我们不断地尝试去构建分层图。
```cpp
	while(bfs(s))
	{
		nowf=INF;
```
每构建一次分层图，我们就尝试一次增广,并更新流量:
```
		while(nowf)
		{
			nowf=dfs(s,INF);
			maxf+=nowf;
		}
	}
}
```
这样就结束了。   
dinic主过程完整代码:    
```cpp
void dinic()
{
	maxf=0;
	int nowf(0);
	while(bfs(s))
	{
		nowf=INF;
		while(nowf)
		{
			nowf=dfs(s,INF);
			maxf+=nowf;
		}
	}
}
```
dinic算法求解草地排水完整代码:   
```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<algorithm>
#include<complex>
#include<iostream>
#include<map>
#include<queue>
#include<vector>
#define INF 0x3f3f3f3f
using namespace std;
struct edge
{
	int next,to,flow;
}a[2000020];
int n,m;
int s,t;
int cnt(0);
int head[1000010];
int dep[1000010];
int maxf(0);
void addedge(int xi,int yi,int fi)
{
	a[cnt].to=yi;
	a[cnt].next=head[xi];
	a[cnt].flow=fi;
	head[xi]=cnt++;
}
bool bfs(int s)
{
	queue<int> q;
	while(!q.empty())q.pop();
	memset(dep,-1,sizeof(dep));
	dep[s]=1;
	q.push(s);
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
		for(int i=head[t];i!=-1;i=a[i].next)
		{
			int v=a[i].to;
			int f=a[i].flow;
			if((f>0)&&(dep[v]==-1))
			{
				dep[v]=dep[t]+1;
				q.push(v);
			}
		}
	}
	return dep[t]!=-1;
}
int dfs(int u,int dist)
{
	if(u==t)return dist;
	for(int i=head[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		int f=a[i].flow;
		if((dep[v]==dep[u]+1)&&(f!=0))
		{
			int df(dfs(v,min(dist,f)));
			if(df>0)
			{
				a[i].flow-=df;
				a[i^1].flow+=df;
				return df;
			}
		}
	}
	return 0;
}
void dinic()
{
	maxf=0;
	int nowf(0);
	while(bfs(s))
	{
		nowf=INF;
		while(nowf)
		{
			nowf=dfs(s,INF);
			maxf+=nowf;
		}
	}
}
int main()
{
	memset(head,-1,sizeof(head));
	scanf("%d%d",&m,&n);
	s=1,t=n;
	for(int i=1;i<=m;i++)
	{
		int x,y,f;
		scanf("%d%d%d",&x,&y,&f);
		addedge(x,y,f);
		addedge(y,x,0);
	}
	dinic();
	printf("%d",maxf);
	return 0;
}

```
算法3.ISAP(Improved Shortest Augmenting Path，更优最短增广路径算法):     
我们发现，其实在dinic算法中，每次求分层图带来的区别并不大。      
例:(4个点，5条边，从4号点到3号点)
```cpp
4 5 4 3
4 2 30
4 3 20
2 3 20
2 1 30
1 3 40
```
在上例中，一共会求解3次分层图，得到的结果如下:
```cpp
第一次求解时:
第一层:4
第二层:2,3
第三层:1
第四层:空

第二次求解时:
第一层:4
第二层:2
第三层:1,3
第四层:空

第三次求解时:
第一层:4
第二层:2
第三层:1
第四层:3
```
可以发现，其实只有3号节点的层数发生了改变，而且每次改变都是层次+1的过程。   
可不可以省掉分层图重复的求解步骤呢?     
答案是可以。    
我们在ISAP算法中，只跑一次bfs,处理出每个点的深度，然后对于每一次更新后的点，我们将其进行"推移"——将它的深度+1。       
注意我们加上的几个优化:      
1.gap优化:```gap[i]```代表层数为i的分层图中的点数，若一个层次没有点了，就将当前点置为最高层点。      
2.当前弧优化:```arcs[i]```记录head的一个副本。    
我们来看看isap的bfs过程:       
我们还是老套路，过一遍算法流程。      
初始化:
```cpp
void bfs(int s)
{
	memset(dep,0,sizeof(dep));
	memset(gap,0,sizeof(gap));
	queue<int>q;
	dep[s]=1;
	gap[1]=1;
	q.push(s);
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
```
我们除了处理点深度外，还要记录一个gap数组。      
别忘了将gap的第一项置为1(s的层次为1)。     
然后还是记录下深度，并更新gap数组:
```cpp
		for(int i=head[t];i!=-1;i=a[i].next) 
		{
			int v=a[i].to;
			if(!dep[v])
			{
				q.push(v);
				dep[v]=dep[t]+1;
				gap[dep[v]]++;
			}
		}
	}
}
```
bfs过程:  
```cpp
void bfs(int s)
{
	memset(dep,0,sizeof(dep));
	memset(gap,0,sizeof(gap));
	queue<int>q;
	dep[s]=1;
	gap[1]=1;
	q.push(s);
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
		for(int i=head[t];i!=-1;i=a[i].next) 
		{
			int v=a[i].to;
			if(!dep[v])
			{
				q.push(v);
				dep[v]=dep[t]+1;
				gap[dep[v]]++;
			}
		}
	}
}
```
然后在dfs过程中也有一些小小的改动:      
在前面的都跟dinic的一样:
```cpp
int dfs(int u,int dist)
{
	if (u==t)return dist;
	int sum(0);
	int nowf(0);
	for (int i=arcs[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		if (dep[u]==dep[v]+1)
		{
			nowf=dfs(v,min(dist,a[i].flow));
			sum+=nowf;
			dist-=nowf;
			a[i].flow-=nowf;
			a[i^1].flow+=nowf;
			if(!dist)return sum;
		}
	}
```
但在算法结束前，我们要记录下每一个点的"偏移"。    
这样子我们就可以不用使用多次bfs来更新层次了:
```cpp
	if(!(--gap[dep[u]]))dep[s]=n+1;
	dep[u]++;
	gap[dep[u]]++;
	arcs[u]=head[u];
	return sum; 
} 
```
dfs过程:
```cpp
int dfs(int u,int dist)
{
	if (u==t)return dist;
	int sum(0);
	int nowf(0);
	for (int i=arcs[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		if (dep[u]==dep[v]+1)
		{
			nowf=dfs(v,min(dist,a[i].flow));
			sum+=nowf;
			dist-=nowf;
			a[i].flow-=nowf;
			a[i^1].flow+=nowf;
			if(!dist)return sum;
		}
	}
	if(!(--gap[dep[u]]))dep[s]=n+1;
	dep[u]++;
	gap[dep[u]]++;
	arcs[u]=head[u];
	return sum; 
} 
```
isap主过程:        
isap的主过程也十分的简单，主要分为以下几步:      
1.分层图初始化。    
2.通过dfs来更新最大流和分层图。    
isap主过程代码:
```cpp
void isap()
{
	maxf=0;
	bfs(t);
	memcpy(&arcs[1],&head[1],sizeof(int)*n);
	maxf=dfs(s,INF);
	while(dep[s]<=n)maxf+=dfs(s,INF);
}
```
isap求解草地排水完整代码:     
```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<algorithm>
#include<complex>
#include<iostream>
#include<map>
#include<queue>
#include<vector>
#define INF 0x3f3f3f3f
using namespace std;
struct edge
{
	int next,to,flow;
}a[2000020];
int n,m;
int s,t;
int cnt(0);
int head[1000010];
int dep[1000010];
int arcs[1000010];
int gap[1000010];
int maxf(0);
void addedge(int xi,int yi,int fi)
{
	a[cnt].to=yi;
	a[cnt].next=head[xi];
	a[cnt].flow=fi;
	head[xi]=cnt++;
}
void bfs(int s)
{
	memset(dep,0,sizeof(dep));
	memset(gap,0,sizeof(gap));
	queue<int>q;
	dep[s]=1;
	gap[1]=1;
	q.push(s);
	while(!q.empty())
	{
		int t=q.front();
		q.pop();
		for(int i=head[t];i!=-1;i=a[i].next) 
		{
			int v=a[i].to;
			if(!dep[v])
			{
				q.push(v);
				dep[v]=dep[t]+1;
				gap[dep[v]]++;
			}
		}
	}
}
int dfs(int u,int dist)
{
	if (u==t)return dist;
	int sum(0);
	int nowf(0);
	for (int i=arcs[u];i!=-1;i=a[i].next)
	{
		int v=a[i].to;
		if (dep[u]==dep[v]+1)
		{
			nowf=dfs(v,min(dist,a[i].flow));
			sum+=nowf;
			dist-=nowf;
			a[i].flow-=nowf;
			a[i^1].flow+=nowf;
			if(!dist)return sum;
		}
	}
	if(!(--gap[dep[u]]))dep[s]=n+1;
	dep[u]++;
	gap[dep[u]]++;
	arcs[u]=head[u];
	return sum; 
} 
void isap()
{
	maxf=0;
	bfs(t);
	memcpy(&arcs[1],&head[1],sizeof(int)*n);
	maxf=dfs(s,INF);
	while(dep[s]<=n)maxf+=dfs(s,INF);
}
int main()
{
	memset(arcs,-1,sizeof(arcs));
	memset(head,-1,sizeof(head));
	scanf("%d%d",&m,&n);
	s=1,t=n;
	for(int i=1;i<=m;i++)
	{
		int x,y,f;
		scanf("%d%d%d",&x,&y,&f);
		addedge(x,y,f);
		addedge(y,x,0);
	}
	isap();
	printf("%d",maxf);
	return 0;
}

```
算法4(没错，还有):HLPP算法       
等着看ff的同学们很抱歉，ff下线了~~其实是我不会~~。    
相信大家已经看增广路看得脑袋都疼了。所以我来介绍一个~~玄学~~算法，不依赖增广路的那种。    
HLPP(Highest Label Preflow Push，最高标号预流推进)算法，是一个**预流推进**算法。      
预流推进算法需要了解几个定义:      
**超额流**:预流推进算法允许我们将流量**存储**在**任意**节点中。存储在**非原点**的节点中的流量就叫做超额流。       
**推送**:一个节点将其超额流送到下一个节点的过程叫做推送。    
**节点高度**:为了防止有些节点打太极(你推送给我，我推送给你，一直推送到TLE)，我们给每一个节点设定一个**高度**(类似于分层图)，并规定推送操作只能从**高点向低点**进行。    
特别地，我们将原点的高度设为n。以保证它可以在一开始流向任何节点。      
**重贴标签**：如果一个节点的**超额流**因为自身的**高度过低**而无法被推送，我们就将它**抬高**，这个过程叫重贴标签。      
有了这几个概念，我们就可以预流推进了。           
走一遍算法流程:     
首先是预流推进的bfs，作用是处理出每个点的高度。      
一步一步分析:     
1.先将每一个点的高度都置为INF。
```cpp
il bool bfs()
{
    queue<ll> q;
    memset(h+1,INF,sizeof(ll)*n);
    h[ed]=0;
    q.push(ed);
```
然后我们来一次逆向bfs，来判断是否存在一条从s到t的可行流。      
2.与一般的bfs过程一样，我们利用队列来遍历这张图，并保留当前节点。       
```cpp
    while(!q.empty())
    {
        ll t=q.front();
        q.pop();
        for(re ll i=head[t];i!=-1;i=a[i].next)
        {
            ll v=a[i].to;
```
3.我们对于每一条可行流，我们都将其入队，并更新其高度。      
注意：这里跑的是反向边，而我们通过正向边来判断可行流，所以是```a[i^1].flow```
```cpp
            if(a[i^1].flow&&h[v]>h[t]+1)
            {
                h[v]=h[t]+1;
                q.push(v);
            }
        }
    }
    return h[st]!=INF;
}
```
bfs过程代码:
```cpp
il bool bfs()
{
    queue<ll> q;
    memset(h+1,INF,sizeof(ll)*n);
    h[ed]=0;
    q.push(ed);
    while(!q.empty())
    {
        ll t=q.front();
        q.pop();
        for(re ll i=head[t];i!=-1;i=a[i].next)
        {
            ll v=a[i].to;
            if(a[i^1].flow&&h[v]>h[t]+1)
            {
                h[v]=h[t]+1;
                q.push(v);
            }
        }
    }
    return h[st]!=INF;
}
```
然后是几个关键操作:     
1.重贴标签操作:       
我们重贴标签的操作十分简单，原理就是将u的高度提高到恰好能使流量流向其所能到达的最低点。
```cpp
il void relabel(int u)
{
    h[u]=INF;
    for(re int i=head[u];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if((a[i].flow)&&(h[v]+1<h[u]))h[u]=h[v]+1;
    }
}
```
2.推送操作:     
所谓推送，就是将超额流分摊到其他节点上。    
我们来看看算法过程:       
1.由于推送必定只能到一个点的相邻节点，我们就取出其每一个能到达的点:      
```cpp
il void push(int u)
{
    for(re int i=head[u];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
```
然后我们就可以试图推送自己的流量了。    
推送有几个条件：     
1.高度要足够。     
2.边上要有剩余的容量。    
我们用e数组记录下每一个点的超额流量。    
```cpp
        if((a[i].flow)&&(h[v]+1==h[u]))
        {
            ll df=min(e[u],a[i].flow);
            a[i].flow-=df;
            a[i^1].flow+=df;
            e[u]-=df;
            e[v]+=df;
```
如果我们的目标点不是起点或中点，且不再优先队列里，我们就将其入队。
```cpp
            if((v!=st)&&(v!=ed)&&(!vis[v]))
            {
                pq.push(v);
                vis[v]=1;
            }
```
如果都推送完了，就可以结束了。
```cpp
            if(!e[u])break;
        }
    }
}
```
推送过程:
```cpp
il void push(int u)
{
    for(re int i=head[u];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if((a[i].flow)&&(h[v]+1==h[u]))
        {
            ll df=min(e[u],a[i].flow);
            a[i].flow-=df;
            a[i^1].flow+=df;
            e[u]-=df;
            e[v]+=df;
            if((v!=st)&&(v!=ed)&&(!vis[v]))
            {
                pq.push(v);
                vis[v]=1;
            }
            if(!e[u])break;
        }
    }
}
```
hlpp主过程:      
我们来逐步分析一下hlpp的主过程:      
我们首先将图中点的高度都处理出来。      
```cpp
inline ll hlpp()
{
    if(!bfs())return 0;
    h[st]=n;
    memset(gap,0,sizeof(int)*(n<<1));
	for(re int i=1;i<=n;i++)if(h[i]!=INF)gap[h[i]]++;
```
然后我们将s点能直接到达的点入栈。       
```cpp
    for(re int i=head[st];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if(ll f=a[i].flow)
        {
            a[i].flow-=f;a[i^1].flow+=f;
            e[st]-=f;e[v]+=f;
            if(v!=st&&v!=ed&&!vis[v])
            {
                pq.push(v);
                vis[v]=1;
            }
        }
    }
```
对于每一个原，汇点之外的点，只要它还有**残余**的**超额流**(即e数组中的值不为0)时，就进行推送，推送完后就重新贴标签。     
这样写的时间复杂度为```O(n^2*sqrt(m))```若将贴标签的动作前置（就像算法导论中做的那样），我们就可以得到复杂度为```O(n^3)```的另一种实现方式。   
注意:这里的pq是一个**优先队列**，排序依据是每一个点的高度，以保证当前取出的点最高。        
实现过程：
```cpp
    while(!pq.empty())
    {
        int  t=pq.top();pq.pop();
        vis[t]=0;push(t);
        if(e[t])
        {
            gap[h[t]]--;
            if(!gap[h[t]])
            {
                for(re int v=1;v<=n;v++)
                {
                    if(v!=st&&v!=ed&&h[v]>h[t]&&h[v]<n+1)
                    {
                        h[v]=n+1;
                    }
                }
            }
            relabel(t);gap[h[t]]++;
            pq.push(t);vis[t]=1;
        }
    }
```
hlpp主过程代码:
```cpp
inline ll hlpp()
{
    if(!bfs())return 0;
    h[st]=n;
    memset(gap,0,sizeof(int)*(n<<1));
	for(re int i=1;i<=n;i++)if(h[i]!=INF)gap[h[i]]++;
    for(re int i=head[st];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if(ll f=a[i].flow)
        {
            a[i].flow-=f;a[i^1].flow+=f;
            e[st]-=f;e[v]+=f;
            if(v!=st&&v!=ed&&!vis[v])
            {
                pq.push(v);
                vis[v]=1;
            }
        }
    }
    while(!pq.empty())
    {
		int  t=pq.top();pq.pop();
        vis[t]=0;push(t);
        if(e[t])
        {
            gap[h[t]]--;
            if(!gap[h[t]])
            {
                for(re int v=1;v<=n;v++)
                {
                    if(v!=st&&v!=ed&&h[v]>h[t]&&h[v]<n+1)
                    {
                        h[v]=n+1;
                    }
                }
            }
            relabel(t);gap[h[t]]++;
            pq.push(t);vis[t]=1;
        }
    }
    return e[ed];
}
```
使用HLPP求解草地排水:
```cpp
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<climits>
#include<ctime>
#include<algorithm>
#include<complex>
#include<iostream>
#include<map>
#include<queue>
#include<vector>
#define ll long long
#define INF ((1ll<<31ll)-1ll)*(1<<17ll)*2ll+1ll
#define re register
#define il inline
using namespace std;
struct edge
{
    int to,next;
	ll flow;
}a[2000020];
int head[10010];
int gap[10010];
ll h[10010];
ll e[10010];
int vis[10010];
int cnt(0);
int n,m,st,ed;
struct cmp
{
    il bool operator ()(int xi,int yi)const
    {
        return h[xi]<h[yi];
    }
};
priority_queue<int,vector<int>,cmp> pq;
il void addedge(int xi,int yi,ll fi)
{
    a[cnt].to=yi;
    a[cnt].next=head[xi];
    a[cnt].flow=fi;
    head[xi]=cnt++;
}
il bool bfs()
{
    queue<int> q;
    memset(h+1,INF,sizeof(ll)*n);
    h[ed]=0;
    q.push(ed);
    while(!q.empty())
    {
        int t=q.front();
        q.pop();
        for(re int i=head[t];i!=-1;i=a[i].next)
        {
            int v=a[i].to;
            if(a[i^1].flow&&h[v]>h[t]+1)
            {
                h[v]=h[t]+1;
                q.push(v);
            }
        }
    }
    return h[st]!=INF;
}
il void push(int u)
{
    for(re int i=head[u];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if((a[i].flow)&&(h[v]+1==h[u]))
        {
            ll df=min(e[u],a[i].flow);
            a[i].flow-=df;
            a[i^1].flow+=df;
            e[u]-=df;
            e[v]+=df;
            if((v!=st)&&(v!=ed)&&(!vis[v]))
            {
                pq.push(v);
                vis[v]=1;
            }
            if(!e[u])break;
        }
    }
}
il void relabel(int u)
{
    h[u]=INF;
    for(re int i=head[u];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if((a[i].flow)&&(h[v]+1<h[u]))h[u]=h[v]+1;
    }
}
inline ll hlpp()
{
    if(!bfs())return 0;
    h[st]=n;
    memset(gap,0,sizeof(int)*(n<<1));
	for(re int i=1;i<=n;i++)if(h[i]!=INF)gap[h[i]]++;
    for(re int i=head[st];i!=-1;i=a[i].next)
    {
        int v=a[i].to;
        if(ll f=a[i].flow)
        {
            a[i].flow-=f;a[i^1].flow+=f;
            e[st]-=f;e[v]+=f;
            if(v!=st&&v!=ed&&!vis[v])
            {
                pq.push(v);
                vis[v]=1;
            }
        }
    }
    while(!pq.empty())
    {
		int  t=pq.top();pq.pop();
        vis[t]=0;push(t);
        if(e[t])
        {
            gap[h[t]]--;
            if(!gap[h[t]])
            {
                for(re int v=1;v<=n;v++)
                {
                    if(v!=st&&v!=ed&&h[v]>h[t]&&h[v]<n+1)
                    {
                        h[v]=n+1;
                    }
                }
            }
            relabel(t);gap[h[t]]++;
            pq.push(t);vis[t]=1;
        }
    }
    return e[ed];
}
signed main()
{
    memset(head,-1,sizeof(head));
    scanf("%d%d",&m,&n);
    st=1;ed=n;
    for(re int i=1;i<=m;i++)
    {
        int x,y;
		ll f;
        scanf("%d%d%lld",&x,&y,&f);
        addedge(x,y,f);
        addedge(y,x,0);
    }
    ll maxf=hlpp();
    printf("%lld",maxf);
    return 0;
}
```