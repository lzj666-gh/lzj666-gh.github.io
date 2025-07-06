# P1395 题解

题解在博客食用效果更佳哦~[YoungNeal](http://www.cnblogs.com/YoungNeal/p/8629717.html)  
Solution

第一想法是求出每个点到根节点的距离，然后 $O(n^2)$
lca 瞎搞，但是会 T。

所以换 O(n) 的树形 dp。

不妨钦定以 1 为根。

记录 $size[i]$ 表示 i 与 i 的子树的结点个数之和。

定义 $d[i]$ 表示在点 i 开会的距离和。

定义 $subtree(x)$ 表示以 x 为根的子树中点的集合。显然 $subtree(x)∈n$

那么对于树上的非根节点 x，设它的父亲为 y。

所以转移方程 $d[x]=d[y]+(n-size[x])-size[x]=d[y]+n-2*size[x]$

意思是，

① 考虑不在 $subtree(x)$ 中的点，它们到 x 的距离和是 它们到 y 的距离和加上 $(n-size[x])$

② 而对于那些在 $subtree(x)$ 中的点，它们到 x 的距离和就是 它们到 y 的距离和再减去 $(size[x])$

所以合并两式，$d[x]=d[y]+n-2*size[x]$

时间复杂度 $O(n)$

```
// By YoungNeal
#include<cstdio>
#define N 50005

int d[N];
int f[N];
int n,cnt;
int size[N];
bool vis[N];
int head[N];

struct Edge{
    int to,nxt;
}edge[N<<1];

void add(int x,int y){
    edge[++cnt].to=y;
    edge[cnt].nxt=head[x];
    head[x]=cnt;
}

void dfs1(int now){
    size[now]=1;
    for(int i=head[now];i;i=edge[i].nxt){
        int to=edge[i].to;
        if(d[to]) continue;
        d[to]=d[now]+1;
        dfs1(to);
        size[now]+=size[to];
    }
}

void dfs(int now,int fa){
    f[now]=f[fa]+n-2*size[now];
    for(int i=head[now];i;i=edge[i].nxt){
        int to=edge[i].to;
        if(to==fa) continue;
        dfs(to,now);
    }
}

signed main(){
    scanf("%d",&n);
    for(int x,y,i=1;i<n;i++){
        scanf("%d%d",&x,&y);
        add(x,y);add(y,x);
    }
    d[1]=1;
    dfs1(1);
    int maxn=0,idx=1;
    for(int i=1;i<=n;i++) maxn+=d[i];
    maxn-=n;
    f[1]=maxn;
    for(int i=head[1];i;i=edge[i].nxt){
        int to=edge[i].to;
        dfs(to,1);
    }
    for(int i=2;i<=n;i++){
        if(f[i]<maxn) maxn=f[i],idx=i;
    }
    printf("%d %d",idx,maxn);
    return 0;
}
```