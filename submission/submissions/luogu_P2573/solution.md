# P2573 题解

/\*
题目大意为：在只能从点权大的点到点权小的点（可以相等）的情况下，从1点出发建立一棵尽可能有更多点的最小生成树

显然我们不能直接求最小生成树，因为有些点应为高度原因无法到达。

为保证我们只会由高到低，我们就只建立由高向低的单向边即可。

对于建立出来的图A，由1点开始宽搜，将扩展到的点和边加入一个新图B，所有扩展到的点便是能到达的最多点。

我们再在这个新图上跑Kruskal求最小生成树，求得最短距离。

对于排序部分，为保证有尽可能多的点在最小生成树里，我们按终点的高度为第一关键字从大到小排序，边长为第二关键字从小到大排序；

这样就能保证拓展的点最多，进而再用最小生成树求最短距离。

\*/





```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<queue>
#include<map>
#include<vector>
#define ll long long
#define R register
#define Rf(a,b,c) for(R int (a)=(b);(a)<=(c);++(a))
#define Tf(a,b,c) for(R int (a)=(b);(a)>=(c);--(a))
using namespace std;
const int N=2000000+5,M=100000+5;
ll n,m,tot,ans,num,sum,cnt,ql,qr;
struct it{
    ll u,v,w;//新图 
};
struct node {
    ll to,nx,val;//初始图（链式前向星） 
};
it a[N];node b[N];
ll fa[M],h[M],head[M],q[M];
bool vis[M];
inline ll read()//读入优化 
{
    ll x=0,f=1;char ch=getchar();
    while(ch>'9'||ch<'0'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x*=10;x+=(ch-'0');ch=getchar();}
    return x*f;
}
bool cmp1(it x,it y) {
//比较函数，以终点的高度为第一关键字从大到小排序，边长为第二关键字从小到大排序 
    if(h[x.v]!=h[y.v]) return h[x.v]>h[y.v];
    return x.w<y.w;
}
inline ll find(ll x) {//并查集找父亲 
    if(fa[x]!=x) fa[x]=find(fa[x]);
    return fa[x];
}
inline void add(int u,int v,int c) {//链式前向星加边 
    b[++num].to=v;
    b[num].nx=head[u];
    head[u]=num;
    b[num].val=c;
}
void bfs(){//宽搜，拓展可到达的点，建新图 
    q[++qr]=1;vis[1]=1;
    while(ql<qr) {
        int now=q[++ql];
        for(int i=head[now];i;i=b[i].nx) {
            a[++cnt].u=now;a[cnt].v=b[i].to;a[cnt].w=b[i].val;//建立新图的边 
            if(!vis[b[i].to]) {
                vis[b[i].to]=1;sum++;//sum计数器计可到达的点 
                q[++qr]=(b[i].to);
            }
        }
    }
}
int main()
{
//    freopen("steep.in","r",stdin);
//    freopen("steep.out","w",stdout);
    n=read();m=read();//读入数据 
    Rf(i,1,n) h[i]=read(),fa[i]=i;
    Rf(i,1,m) {
        R int u=read(),v=read(),c=read();
        if(h[u]>=h[v]) add(u,v,c);//根据边两边的点的高度，建立一条由高到低的单向边 
        if(h[u]<=h[v]) add(v,u,c);//当高度相等时会建两条边 
    }
    bfs();//广搜拓展点 
    sort(a+1,a+1+cnt,cmp1);//对新图的点跑Kruskal求最小生成树 
    Rf(i,1,cnt) {
        R int rx=find(a[i].u),ry=find(a[i].v);
        if(rx!=ry) {
            fa[rx]=ry;ans+=a[i].w;//求最短距离 
        }
    }
    printf("%lld %lld",sum+1,ans);//sum+1，还有初始的1点可到 
    return 0;
}

```