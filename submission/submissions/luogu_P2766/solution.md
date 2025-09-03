# P2766 题解

题解来自网络流24题：

【问题分析】


第一问时LIS，动态规划求解，第二问和第三问用网络最大流解决。


【建模方法】


首先动态规划求出F[i]，表示以第i位为开头的最长上升序列的长度，求出最长上升序列长度K。


1、把序列每位i拆成两个点<i.a>和<i.b>，从<i.a>到<i.b>连接一条容量为1的有向边。

2、建立附加源S和汇T，如果序列第i位有F[i]=K，从S到<i.a>连接一条容量为1的有向边。

3、如果F[i]=1，从<i.b>到T连接一条容量为1的有向边。

4、如果j>i且A[i] < A[j]且F[j]+1=F[i]，从<i.b>到<j.a>连接一条容量为1的有向边。


求网络最大流，就是第二问的结果。把边(<1.a>,<1.b>)(<N.a>,<N.b>)(S,<1.a>)(<N.b>,T)这四条边的容量修改为无穷大，再求一次网络最大流，就是第三问结果。


【建模分析】


上述建模方法是应用了一种分层图的思想，把图每个顶点i按照F[i]的不同分为了若干层，这样图中从S出发到T的任何一条路径都是一个满足条件的最长上升子序列。

由于序列中每个点要不可重复地取出，需要把每个点拆分成两个点。单位网络的最大流就是增广路的条数，所以最大流量就是第二问结果。

第三问特殊地要求x1和xn可以重复使用，只需取消这两个点相关边的流量限制，求网络最大流即可。

```cpp
#include<bits/stdc++.h>
#define inf 1000000007
#define N 2000005
#define M 505
using namespace std;
struct Edge{
    int u,v,next,f;
}G[N];
int head[N],tot=0,a[M],dp[M],n,len,s,t,ans;
void addedge(int u,int v,int f){
    G[tot].u=u;G[tot].v=v;G[tot].f=f;G[tot].next=head[u];head[u]=tot++;
    G[tot].u=v;G[tot].v=u;G[tot].f=0;G[tot].next=head[v];head[v]=tot++;
}
int level[100*M];
bool bfs(int s,int t){
    memset(level,0,sizeof(level));
    queue<int>q;q.push(s);level[s]=1;
    while(!q.empty()){
        int u=q.front();q.pop();
        if(u==t)return 1;
        for(int i=head[u];i!=-1;i=G[i].next){
            int v=G[i].v,f=G[i].f;
            if(level[v]==0&&f)q.push(v),level[v]=level[u]+1;
        }
    }
    return 0;
}
int dfs(int u,int maxf,int t){
    if (u==t)return maxf;
    int rat=0;
    for (int i=head[u];i!=-1&&rat<maxf;i=G[i].next){
        int v=G[i].v;int f=G[i].f;
        if (level[v]==level[u]+1&&f){
            int Min=min(maxf-rat,f);
            f=dfs(v,Min,t);
            G[i].f-=f;G[i^1].f+=f;rat+=f;
        }
    }
    if (!rat)level[u]=N;
    return rat;
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]),dp[i]=1;
    for(int i=1;i<=n;i++)
    for(int j=1;j<i;j++)
    if(a[j]<=a[i])dp[i]=max(dp[i],dp[j]+1);
    for(int i=1;i<=n;i++)len=max(len,dp[i]);
    printf("%d\n",len);
    s=0;t=5000;
    memset(head,-1,sizeof(head));
    for(int i=1;i<=n;i++)if(dp[i]==1)addedge(s,i,1);
    for(int i=1;i<=n;i++)if(dp[i]==len)addedge(i+n,t,1);
    for(int i=1;i<=n;i++)addedge(i,i+n,1);
    for(int i=1;i<=n;i++)
    for(int j=1;j<i;j++)
    if(a[j]<=a[i]&&dp[j]+1==dp[i])addedge(j+n,i,1);
    while(bfs(s,t))ans+=dfs(s,inf,t);printf("%d\n",ans);
    addedge(1,1+n,inf);addedge(s,1,inf);
    if(dp[n]==len)addedge(n,n*2,inf),addedge(n*2,t,inf);
    while(bfs(s,t))ans+=dfs(s,inf,t);
    printf("%d\n",ans);
    return 0;
}
```