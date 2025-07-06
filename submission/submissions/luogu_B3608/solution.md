# B3608 题解

这道题对 `EK+spfa` 算法不太友好，需要卡常才能通过。

（但是好歹卡过去了）

学习费用流（最小费用最大流）首先要学习网络流，可以看我的[题解](https://www.luogu.com.cn/blog/I-do-not-want-TLE/solution-b3606)，当然可以参考[经典日报](https://www.luogu.com.cn/blog/ONE-PIECE/wang-lao-liu-di-zong-jie)。

费用流和网络流的形态很类似，主体还是根据网络流。下面举一个例子（又是借鉴日报）。

假设 `s` 城有 `inf`个（穷）人想去 `t` 城，但是从 `s`到`t` 要经过一些城市才能到达，每条路有最大流量和权值（流量通过 `1` 所花费的代价），问最终最多能有多少人能到达 `t` 城。（由于是穷人）他们希望能在最多人到达 `t` 城的同时花最少的钱，问最少的钱是多少。

费用流就是在流量最大的情况下所花费的最小费用。

相较于网络流，费用流只是增加了权值，我们只需要解决权值问题即可。

这你想到了什么？代价最小？那就最短路！

因为有负权边，所以 `spfa` 是最方便的！而且需要进行多次 `spfa` 所以基本上不会全都卡成 $n^2$ 。

关于 `spfa` 它诈尸了！（大雾）

再详细一点，就是把 `bfs` 改成 `spfa` ,再松弛过程中记录路径即可。

这道板子题会卡一下 `EK+SPFA`，所以需要进行卡常。

下面是代码：

```
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
namespace in{
    #ifdef faster
    char buf[1<<21],*p1=buf,*p2=buf;
    inline int getc(){return p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++;}
    #else
    inline int getc(){return getchar();}
    #endif
    template <typename T>inline void read(T& t){
        t=0;int f=0;char ch=getc();while (!isdigit(ch)){if(ch=='-')f = 1;ch=getc();}
        while(isdigit(ch)){t=t*10+ch-48;ch = getc();}if(f)t=-t;
    }
    template <typename T,typename... Args> inline void read(T& t, Args&... args){read(t);read(args...);}
}
namespace out{
    char buffer[1<<21];int p1=-1;const int p2 = (1<<21)-1;
    inline void flush(){fwrite(buffer,1,p1+1,stdout),p1=-1;}
    inline void putc(const char &x) {if(p1==p2)flush();buffer[++p1]=x;}
    template <typename T>void write(T x) {
        static char buf[15];static int len=-1;if(x>=0){do{buf[++len]=x%10+48,x/=10;}while (x);}else{putc('-');do {buf[++len]=-(x%10)+48,x/=10;}while(x);}
        while (len>=0)putc(buf[len]),--len;
    }
}
const int inf=2147483647;
int maxn,cost;
int top=1,head[5001];
int dis[5001];
int n,m,s,t,book[5001];
int min(int a,int b){
	return a>b?b:a;
}
struct point{
    int v,w,val,next;
}a[100001];
struct b{
    int fa;
    int v;
}b[5001];
inline void add(int u,int v,int val,int w){
    a[++top].v=v;
    a[top].val=val;
    a[top].w=w;
    a[top].next=head[u];
    head[u]=top;
}
queue<int> q;
inline bool spfa(){
    for(register int i=1;i<=n;i++)
    	dis[i]=inf,b[i].fa=b[i].v=book[i]=0;
    dis[s]=0;
    q.push(s);
    book[s]=1;
    while(!q.empty()){
        int u=q.front();
        book[u]=0;
        q.pop();
        for(register int i=head[u];i;i=a[i].next){
            int v=a[i].v,w=a[i].w;
            if(a[i].val>0&&dis[v]>dis[u]+w){
                dis[v]=dis[u]+w;
                b[v].fa=u,b[v].v=i;
                if(book[v]==0){
                    q.push(v);
                    book[v]=1;
                }
            }
        }
    }
    return dis[t]!=inf;
}
void EK(){
    while(spfa()){
        int minn=inf;
        for(register int i=t;i!=s;i=b[i].fa)
			minn=min(minn,a[b[i].v].val);
        for(register int i=t;i!=s;i=b[i].fa){
            a[b[i].v].val-=minn;
            a[b[i].v^1].val+=minn;
        }
        maxn+=minn;
        cost+=minn*dis[t];
    }
    return;
}
int main()
{
    in::read(n,m);
    s=1,t=n;
    int u,v,val,w;
    for(register int i=1;i<=m;i++){
        in::read(u,v,val,w);
        add(u,v,val,w);
        add(v,u,0,-w);
    }
    EK();
    printf("%d %d",maxn,cost);
    return 0;
}
```