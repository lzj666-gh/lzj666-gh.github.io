# P4568 题解

套路题，分层图。

以样例为例（使用 @EternalAlexander 这位dalao的OI Painter绘制）：

![](https://cdn.luogu.com.cn/upload/pic/19106.png)

各层内部正常连边，各层之间从上到下连权值为0的边。每向下跑一层，就相当于免费搭一次飞机。跑一遍从$s$到$t+n*k$的最短路即可。

```
#include<cstdio>
#include<cctype>
#include<cstring>
#include<queue>
#include<algorithm>
#include<vector>
#include<utility> 
#include<functional>

int Read()
{
    int x=0;char c=getchar();
    while(!isdigit(c))
    {
        c=getchar();
    }
    while(isdigit(c))
    {
        x=x*10+(c^48);
        c=getchar();
    }
    return x;
}

using std::priority_queue;
using std::pair;
using std::vector;
using std::make_pair;
using std::greater;

struct Edge
{
    int to,next,cost;
}edge[2500001];
int cnt,head[110005];

void add_edge(int u,int v,int c=0)
{
    edge[++cnt]=(Edge){v,head[u],c};
    head[u]=cnt;
}

int dis[110005];
bool vis[110005];
void Dijkstra(int s)
{
    memset(dis,0x3f,sizeof(dis));
    dis[s]=0;
    priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > points;
    points.push(make_pair(0,s));
    while(!points.empty())
    {
        int u=points.top().second;
        points.pop();
        if(!vis[u])
        {
            vis[u]=1;
            for(int i=head[u];i;i=edge[i].next)
            {
                int to=edge[i].to;
                if(dis[to]>dis[u]+edge[i].cost) 
                {
                    dis[to]=dis[u]+edge[i].cost;
                    points.push(make_pair(dis[to],to));
                }
            }
        }
    }
}

int main()
{
    int n=Read(),m=Read(),k=Read(),s=Read(),t=Read();
    int u,v,c;
    for(int i=0;i<m;++i)
    {
        u=Read(),v=Read(),c=Read();
        add_edge(u,v,c);
        add_edge(v,u,c);
        for(int j=1;j<=k;++j)
        {
            add_edge(u+(j-1)*n,v+j*n);
            add_edge(v+(j-1)*n,u+j*n);
            add_edge(u+j*n,v+j*n,c);
            add_edge(v+j*n,u+j*n,c);
        }
    }
    for(int i=1;i<=k;++i)
	{
		add_edge(t+(i-1)*n,t+i*n);
	}//预防奇葩数据
    Dijkstra(s);
    printf("%d",dis[t+k*n]);
    return 0;
}
```