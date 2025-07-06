# P1576 题解

算法：Dijkstra+堆优化（题解里为什么没有啊。。。，spfa能不用就千万别用，这个算法非常地危险）
思路其他题解都已经讲的很清楚了，我们来讲一下具体代码如何实现：
```cpp
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
using namespace std;
int n,m,A,B;
double dis[2010];
bool mark[2010];
struct Node//固定格式：因为最短路里面是从小到大，那么最长路就要反过来，从大到小 
{
	int Num;
	double dis;
	bool operator<(const Node &a) const
	{
		return a.dis>dis;//再次提醒 
	}
};
struct node
{
	int Num;
	double dis;
};
vector<node> G[2010];
inline void Dij()
{
	priority_queue<Node> q;//建立优先队列 
	Node temp;
	temp.Num=A;
	temp.dis=1;
	q.push(temp);//初始化 
	while(!q.empty())//Dij算法，不会请自行百度了解基本思想 
	{
		int u=q.top().Num;//取出队首的元素 
		q.pop();
		if(mark[u]==1) continue;
		mark[u]=1;
		for(int i=0;i<G[u].size();i++)//讨论与队首元素相关的点 
		{
			int v=G[u][i].Num;
			double l=G[u][i].dis;
			if(mark[v]==0&&dis[v]<dis[u]*l)//最长路更新 
			{
				dis[v]=dis[u]*l;
				temp.Num=v;
				temp.dis=dis[v];
				q.push(temp);//入队 
			}
		}
	}
}
int main()
{
	node temp;
	scanf("%d%d",&n,&m);//输入点，边 
	memset(dis,-0x3f,sizeof(dis));//因为是求最长路，所以初始化为负无穷 
	for(int i=1;i<=m;i++)
	{
		int x,y;
		double z;
		scanf("%d%d%lf",&x,&y,&z);//输入一条线的两端以及长度 
		temp.Num=y;
		temp.dis=1-z/100;
		G[x].push_back(temp);
		temp.Num=x;
		G[y].push_back(temp);//双向边，用的vector存图，链式前向星同理 
	}
	scanf("%d%d",&A,&B);//输入起始点，终止点 
	dis[A]=1;//起始点到自己的距离要初始化为1，不能是0，否则等下与之相乘的数就会是0了 
	Dij();//跑 
	printf("%.8lf",100/dis[B]);//输出答案 
	return 0;
}
```