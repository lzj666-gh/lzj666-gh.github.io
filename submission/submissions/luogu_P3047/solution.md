# P3047 题解

我记得我调这道题时中耳炎，发烧，于是在学长的指导下过了也没有发题解

发现我自己的思路蛮鬼畜的

常规操作：$f[i][j]$ 表示到$i$的距离为$j$的奶牛有多少只，但注意这只是在第二遍dfs之后

在我的第一遍dfs中(就是下面那个叫build的函数）,$f[i][j]$的含义是在i这课子树中到$i$的距离为$j$的奶牛有多少只，所以在第一遍dfs的时候，$f[i][j]$的状态只会来自它的儿子们

于是在第一遍dfs就有一个异常简单的方程

$$f[i][j]=\sum_{}f[k][j-1]$$

其中$k$是 $i$的儿子

如果我们钦定以1为根建树的话，那么1的子树就是整棵树，于是这个时候的$f[1]$就是全树意义下的答案了

而这个时候第二遍dfs就要登场了，第二遍dfs的意义就是利用父亲去更新儿子，于是我们就又有一个简单的方程了

$$f[k][j]=\sum_{}f[i][j-1]$$

其中$k$是 $i$的儿子

这样的话肯定会有重复的，因为到$i$的距离为2的点包含到$k$距离为1的k的儿子们,而这些点位于$k$的子树中的点已经在第一遍dfs的时候被加上了，于是我们在这里简单容斥就好了

于是就是代码了
```cpp
#include<iostream>
#include<cstring>
#include<cstdio>
#define re register
#define maxn 100001
using namespace std;
struct node
{
    int v,nxt;
}e[maxn<<1];
int f[maxn][21],s[maxn],head[maxn],deep[maxn];
int n,num,k;
inline int read()
{
    char c=getchar();
    int x=0;
    while(c<'0'||c>'9') c=getchar();
    while(c>='0'&&c<='9')
      x=(x<<3)+(x<<1)+(c^48),c=getchar();
    return x;
}
inline void add(int x,int y)
{
    e[++num].v=y;
    e[num].nxt=head[x];
    head[x]=num;
}
inline void build(int r)
{
    for(re int i=head[r];i;i=e[i].nxt)
    if(!deep[e[i].v])
    {
        deep[e[i].v]=deep[r]+1;
        build(e[i].v);
        for(re int j=1;j<=k;j++)
        f[r][j]+=f[e[i].v][j-1];
    }
}
inline void dfs(int r)
{
    for(re int i=head[r];i;i=e[i].nxt)
    if(deep[e[i].v]>deep[r])
    {
        for(re int j=k;j>=2;j--)
            f[e[i].v][j]-=f[e[i].v][j-2];//简单的容斥原理了
          //这里的循环一定要倒序
        for(re int j=1;j<=k;j++)
            f[e[i].v][j]+=f[r][j-1];
        dfs(e[i].v);
    }
}
int main()
{
    n=read();
    k=read();
    int x,y;
    for(re int i=1;i<n;i++)
    {
        x=read();
        y=read();
        add(x,y);
        add(y,x);
    }
    for(re int i=1;i<=n;i++)
        s[i]=read(),f[i][0]=s[i];
    deep[1]=1;
    build(1);
    dfs(1);
    for(re int j=1;j<=n;j++)
    {
        int ans=0;
        for(re int i=0;i<=k;i++)
        ans+=f[j][i];
        printf("%d\n",ans);
    }
}
```