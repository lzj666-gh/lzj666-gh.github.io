# P4644 题解

大多数人用的线段树，好写好调的最短路居然没什么人写？

最短路的唯一一篇题解没判无解，码风毒瘤？

是时候来一篇认真的最短路题解了！

考虑转化题意。

要让起点到终点之间的全部点被覆盖，

我们就可以把每一头奶牛视为从起始时间到终止时间连一条边权为工资的边。

同时，每一个时间点向前一条时间点连一条边权为零的边。

~~感性理解一下，~~ 我们发现用这种方式建图，当某个点能够被到达时，从起点到它之间的每一个点都必定已被覆盖。

因为对任何一个点而言，只有当一条起点被覆盖的边以它为终点或越过它，它才是被覆盖的；而一条边的起点要被覆盖，同样要满足上述条件。以此类推，从起点到它之间的所有点都应该被覆盖了。

于是当终点能被到达时，就满足了所有时间点都被覆盖的要求。

由于向后的边权就是工资，向前的边权为零不影响答案，

所以起点到终点的最短路就是答案。。。

终点无法到达就是无解。。。

还有一点很重要，题中给的是时间点，而这个算法需要时间段。

那么我们把每条边的终点加一，就把一个时间点拆出了起点和终点，变成了时间段。

于是代码就出来了。

```cpp
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>

char gc()
{
    static char buf[1<<16],*p1=buf,*p2=buf;
    if(p1==p2)
    {
        p2=(p1=buf)+fread(buf,1,1<<16,stdin);
        if(p1==p2)return EOF;
    }
    return *p1++;
}

//#define gc getchar

template<typename _Tp>
void read(_Tp& x)
{
    x=0;
    char c=gc();
    while(c<'0'||c>'9')c=gc();
    while(c>='0'&&c<='9')
    {
        x=(x<<1)+(x<<3)+(c^48);
        c=gc();
    }
}

const int N=100005,M=300005;

int head[N];
long long dis[N];
bool vis[N];

struct Edge
{
    int next,to;
    long long w;
};
Edge E[M];
void add(int u,int v,int w)
{
    static int tot=0;
    E[++tot].next=head[u];
    E[tot].to=v;
    E[tot].w=w;
    head[u]=tot;
}

typedef std::pair<long long,int> Node;

void dijkstra(int s)
{
    memset(dis,0x3f,sizeof(dis));
    std::priority_queue<Node,std::vector<Node>,std::greater<Node> > q;
    dis[s]=0;
    q.push(Node(0,s));
    while(!q.empty())
    {
        int u=q.top().second;
        if(vis[u])
        {
            q.pop();
            continue;
        }
        q.pop();
        vis[u]=1;
        for(int i=head[u];i;i=E[i].next)
        {
            int v=E[i].to;
            if(dis[v]>dis[u]+E[i].w)
            {
                dis[v]=dis[u]+E[i].w;
                q.push(Node(dis[v],v));
            }
        }
    }
}

int main()
{
    int n,S,E;
    read(n),read(S),read(E);
    for(int i=S;i<E;++i)
    {
        add(i+1,i,0);
    }
    for(int i=0;i<n;++i)
    {
        int u,v,w;
        read(u),read(v),read(w);
        if(u<S)u=S;
        if(v>E)v=E;
        add(u,v+1,w);
    }
    dijkstra(S);
    printf("%lld",dis[E+1]==0x3f3f3f3f3f3f3f3f?-1:dis[E+1]);
}

```

