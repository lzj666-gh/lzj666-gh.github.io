# P4427 题解

大概是树上差分的题？

先介绍下什么是树上差分……(说实在的应该叫树上前缀和比较好)

大概是我们要算路径上的一些数(通常是求和)，然后计算路径信息的时候我们处理一些信息，然后通过算$Dep_{u}+Dep_{v}-2Dep_{lca(u,v)}$来计算路径上的信息

题目看起来非常有树链剖分的感觉……但是问题是，这道题没有修改这就导致题目难度大幅度下降了，所以我们先把每个点深度的k次方打一个表，之后我们因为要做减法，所以我们令$val_{i,k}$表示i到1号点路径上点深度的k次方之和……

然后问题来了，我们维护的是点权和，所以呢我们发现直接减的话会导致lca这个点没算，所以略微改一下公式，使lca这个点也被算一次

然后我们询问$u,v,k$的时候输出$val_{u,k}+val_{v,k}-val_{lca(u,v)}-val_{fa_{lca(u,v)}}$即可

问题就是如何找lca了……~~(欢迎使用TarjanO(n)求lca)~~

~~欢迎使用st表O(1)查询~~

然而最粗暴，可靠性最强，常数小而不会被轻易卡的算法还是倍增，所以这道题上一个倍增板子即可通过此题了~(不会倍增法求lca的话出门左转你站膜板区，包教包会~)

上代码~

```C
#include<cstdio>
#include<algorithm>
using namespace std;typedef long long ll;const ll mod=998244353;const int N=3*1e5+10;const int M=60;
int n;int m;int v[2*N];int x[2*N];int al[N];int ct;ll dep[N];int fa[N][22];int book[N];ll val[N][M];
inline void add(int u,int V){v[++ct]=V;x[ct]=al[u];al[u]=ct;}ll mi[M];
inline void dfs(int u)//处理val的信息以及倍增的信息 
{
    book[u]=true;for(int i=0;fa[u][i];i++){fa[u][i+1]=fa[fa[u][i]][i];}
    for(int i=al[u];i;i=x[i])
    {
        if(book[v[i]]){continue;}
        fa[v[i]][0]=u;dep[v[i]]=dep[u]+1;
        for(int j=1;j<=50;j++){mi[j]=mi[j-1]*dep[v[i]]%mod;}
        for(int j=1;j<=50;j++){val[v[i]][j]=(mi[j]+val[u][j])%mod;}
        dfs(v[i]);
    }
}
inline int lca(int u,int v)//倍增求lca 
{
    if(dep[u]<dep[v]){swap(u,v);}int d=dep[u]-dep[v];
    for(int i=0;d;d>>=1,i++){if(d&1){u=fa[u][i];}}if(u==v){return u;}
    for(int i=20;i>=0;i--){if(fa[u][i]!=fa[v][i]){u=fa[u][i];v=fa[v][i];}}
    return fa[u][0]; 
}
int main()
{
    scanf("%d",&n);mi[0]=1;
    for(int i=1,u,v;i<n;i++){scanf("%d%d",&u,&v);add(u,v);add(v,u);}dfs(1);//dfs处理 
    scanf("%d",&m);
    for(int i=1,u,v,k;i<=m;i++)
    {
        scanf("%d%d%d",&u,&v,&k);int l=lca(u,v);//然后我们就直接减了，注意lca只算但是要算一次 
        printf("%lld\n",(val[u][k]+val[v][k]+2*mod-val[fa[l][0]][k]-val[l][k])%mod);
    }return 0;//拜拜程序~ 
}

```