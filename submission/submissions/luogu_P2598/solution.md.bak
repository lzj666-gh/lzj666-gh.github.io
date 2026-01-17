# P2598 题解

其实这题根本没有其它题解说的那么复杂。

建图方式：

1、原点向所有狼连流量 $inf$ 的边

2、所有羊向汇点连流量 $inf$ 的边

3、所有点向四周连流量为 $1$ 的边。

然后下面就没了。

求出最小割就是答案，不用考虑题解说的什么 $0$ 的归属问题。

为什么是对的？

所有狼和羊之间的边都被割掉了，相当于修了栅栏，所以是对的。


~~死因：n,m写反调了一个小时~~

```cpp
#include<bits/stdc++.h>
#define N 100005
#define INF 1<<29
#define num(i,j) ((i-1)*m+j)
using namespace std;

inline void rd(int &X){
    X=0;int w=0;char ch=0;
    while(!isdigit(ch))w|=ch=='-',ch=getchar();
    while(isdigit(ch))X=(X<<3)+(X<<1)+(ch^48),ch=getchar();
    X=w?-X:X;
}

int n,m,s,t,ans,f,k;
int head[N],cnt=1,d[N];
struct nd{int nxt,to,v;}e[N<<1];
#define For(x) for(int y,i=head[x];(y=e[i].to);i=e[i].nxt)

void add(int x,int y,int w){
    e[++cnt]=(nd){head[x],y,w};head[x]=cnt;
    e[++cnt]=(nd){head[y],x,0};head[y]=cnt;
}
bool bfs()
{
    queue<int> q; q.push(s);
    memset(d,0,sizeof d); d[s]=1;
    while(!q.empty()){
        int x=q.front();q.pop();
        For(x) if(e[i].v&&!d[y]){
            q.push(y); d[y]=d[x]+1;
            if(y==t) return 1;
        }
    } return 0;
}

int dinic(int x,int flow)
{
    if(x==t) return flow; int re=flow;

    for(int y,i=head[x];(y=e[i].to)&&re;i=e[i].nxt)
        if(e[i].v&&d[y]==d[x]+1)
        {
            k=dinic(y,min(re,e[i].v));
            if(!k) d[y]=0;
            e[i].v-=k;e[i^1].v+=k;re-=k; 
        }
    return flow-re;
}
int a[105][105];
int mx[]={1,-1,0,0};
int my[]={0,0,1,-1};
void build()
{
    rd(n);rd(m);s=n*m+1;t=n*m+2;
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            rd(a[i][j]);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            if(a[i][j]==1)
                add(s,num(i,j),INF);
            else if(a[i][j]==2)
                add(num(i,j),t,INF);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            for(int k=0;k<4;k++)	
            {
                int tx=i+mx[k];
                int ty=j+my[k];
                if(tx<=n and ty<=m and tx>=1 and ty>=1)
                    add(num(i,j),num(tx,ty),1);
            }
}
int main()
{
    build();
    while(bfs())
        while(f=dinic(s,INF))
            ans+=f;
    cout<<ans;
}
```