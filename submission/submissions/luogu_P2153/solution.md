# P2153 题解

[$$\Large\texttt{My Blog}$$](https://hydingsy.github.io/)

---

## Description

> 题目链接：[Luogu 2153](https://www.luogu.org/problemnew/show/P2153)

Elaxia 最近迷恋上了空手道，他为自己设定了一套健身计划，比如俯卧撑、仰卧起坐等 等，不过到目前为止，他坚持下来的只有晨跑。现在给出一张学校附近的地图，这张地图中包含 $n$ 个十字路口和 $m$ 条街道，Elaxia 只能从一个十字路口跑向另外一个十字路口，街道之间只在十字路口处相交。Elaxia 每天从寝室出发跑到学校，保证寝室编号为 $1$，学校编号为 $n$。Elaxia 的晨跑计划是按周期（包含若干天）进行的，由于他不喜欢走重复的路线，所以在一个周期内，每天的晨跑路线都不会相交（在十字路口处），寝室和学校不算十字路口。Elaxia 耐力不太好，他希望在一个周期内跑的路程尽量短，但是又希望训练周期包含的天数尽量长。

数据范围：$1\le n\le 200$，$1\le m\le 2\times 10^4$

------

## Solution

首先我们发现需要求**路程最短，天数尽量长**。那么我们可以考虑**最小费用最大流**，其中路程为费用，天数为流量。

由于每个点只能被访问 $1$ 次，那么我们进行拆点，将 $i$ 拆成 $i_1$ 和 $i_2$，其中 $i_1$ 和 $i_2$ 之间连边 $(i_1,i_2,1,0)$（容量为 $1$，费用为 $0$），对于有向图的每条边 $(u,v,w)$ 连边 $(u_2,v_1,1,w)$ 和其反向边 $(v_1,u_2,0,-w)$。

又因为 $1$ 和 $n$ 可以多次经过，那么源点和汇点分别为 $s_2$ 和 $t_1$，然后直接跑网络流即可。

**时间复杂度**：$O(nmf)$

------

## Code

```cpp
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>

const int N=4e2+5,M=1e5+5;
const int INF=0x3f3f3f3f;
int n,m,tot=1,lnk[N],cnr[N],ter[M],nxt[M],cap[M],cost[M],dis[N],ret;
bool vis[N];

void add(int u,int v,int w,int c) {
    ter[++tot]=v,nxt[tot]=lnk[u],lnk[u]=tot,cap[tot]=w,cost[tot]=c;
}
void addedge(int u,int v,int w,int c) {
    add(u,v,w,c),add(v,u,0,-c);
}
int spfa(int s,int t) {
    memset(dis,0x3f,sizeof(dis));
    memcpy(cnr,lnk,sizeof(lnk));
    std::queue<int> q;
    q.push(s),dis[s]=0,vis[s]=1;
    while(!q.empty()) {
        int u=q.front(); q.pop(),vis[u]=0;
        for(int i=lnk[u];i;i=nxt[i]) {
            int v=ter[i];
            if(cap[i]&&dis[v]>dis[u]+cost[i]) {
                dis[v]=dis[u]+cost[i];
                if(!vis[v]) q.push(v),vis[v]=1;
            }
        }
    }
    return dis[t]!=INF;
}
int dfs(int u,int t,int flow) {
    if(u==t) return flow;
    vis[u]=1;
    int ans=0;
    for(int i=cnr[u];i;i=nxt[i]) {
        cnr[u]=i;
        int v=ter[i];
        if(!vis[v]&&cap[i]&&dis[v]==dis[u]+cost[i]) {
            int x=dfs(v,t,std::min(cap[i],flow-ans));
            if(x) ret+=x*cost[i],cap[i]-=x,cap[i^1]+=x,ans+=x;
        }
    }
    vis[u]=0;
    return ans;
}
int mcmf(int s,int t) {
    int ans=0;
    while(spfa(s,t)) {
        int x;
        while((x=dfs(s,t,INF))) ans+=x;
    }
    return ans;
}
int main() {
    scanf("%d%d",&n,&m);
    while(m--) {
        int u,v,c;
        scanf("%d%d%d",&u,&v,&c);
        addedge(u+n,v,1,c);
    }
    for(int i=1;i<=n;++i) addedge(i,i+n,1,0);
    int s=1+n,t=n;
    int ans=mcmf(s,t);
    printf("%d %d\n",ans,ret);
    return 0;
}
```