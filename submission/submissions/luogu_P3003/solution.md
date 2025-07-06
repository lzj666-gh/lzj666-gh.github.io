# P3003 题解

本来这是道裸题，显然最短路一定是$min(dis[s][a],dis[s][b])+dis[a][b]$。开始我思维混乱，一直在想从起点跑到$a$后是否跑回起点再去$b$点会更快？但我及时醒悟了，从$a$到起点再到$b$点如果最短，自然也会包括在$a,b$的最短路径里，无需额外判断。所以要求的就是上面那个东西，对每个询问两次最短路就够了。

但是这题稍微卡了一下SPFA，SPFA应该只有70分~~为什么我有80~~，所以并不是真的那么模板。dijkstra好，但我懒得打。故介绍一个十分简单，但许多人并不知道的优化。

SLF：松弛操作时优化入队，代码：

```cpp
if(b.size()&&dis[edge[i].to]<dis[b.front()])
	b.push_front(edge[i].to);
else
	b.push_back(edge[i].to);
```


优先选择dis值更小的点进行操作，显然算法可以跑得更快。

![](https://cdn.luogu.com.cn/upload/image_hosting/56c4t4ou.png?x-oss-process=image/resize,m_lfit,h_170,w_225)

优化挺明显。

还有个lll优化：每次将入队结点距离和队内距离平均值比较，如果更大则插入至队尾。据说本题卡了，我没打。

正权图还是要用dijkstra，SPFA太好卡了。

最后注意一点：在帮大佬改代码时总出现奇怪的CPU报错，但感觉却和我的AC代码什么区别也没有，于是把我交了的代码拷下来又跑了一遍，发现昨天好好的代码发生了同样的错误……真不知道我是怎么A的。其实是在进行SLF优化时未判断队列是否为空就直接访问$b.front()$，RE与否全靠运气……在访问前加个判断就好了。

下面是代码。在提交的基础上修复了上面的问题。

```cpp
#include<bits/stdc++.h>
struct node
{
	int from,to,dis,next;
}edge[400001];
int n,m,num,head[200001],dis[200001],book[200001];
std::deque<int> b;
void add(int u,int v,int w)
{
	edge[++num].from=u;
	edge[num].to=v;
	edge[num].dis=w;
	edge[num].next=head[u];
	head[u]=num;
	return;
}

int spfa(int s,int t)
{
	memset(book,0,sizeof(book));
	memset(dis,0x7f,sizeof(dis));
	b.push_front(s);
	book[s]=1;
	dis[s]=0;
	while(b.size())
	{
		int x=b.front();
		b.pop_front();
		book[x]=0;
		for(int i=head[x];i;i=edge[i].next)
			if(dis[edge[i].to]>dis[x]+edge[i].dis)
			{
				dis[edge[i].to]=dis[x]+edge[i].dis;
				if(!book[edge[i].to])
				{
					book[edge[i].to]=1;
					if(b.size()&&dis[edge[i].to]<dis[b.front()])
						b.push_front(edge[i].to);
					else
						b.push_back(edge[i].to);
				}
			}
	}

	return dis[t];
}

int main()
{
	int s,a,b;
	scanf("%d%d%d%d%d",&m,&n,&s,&a,&b);
	for(int i=1;i<=m;i++)
	{
		int u,v,w;
		scanf("%d%d%d",&u,&v,&w);
		add(u,v,w);
		add(v,u,w);
	}
	
	printf("%d",std::min(spfa(s,a),spfa(s,b))+spfa(a,b));
	return 0;
}
```



