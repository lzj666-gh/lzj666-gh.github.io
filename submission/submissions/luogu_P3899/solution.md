# P3899 题解

**蒟蒻博客**：[QwQ](https://www.cnblogs.com/GoldenPotato/p/9801317.html)


------------

## Solution

你们搞的这道题啊，exciting！

 .

这题真的很有意思。

首先，我们可以先理解一下题面：固定一个a，找到一个b，c就是a与b的公共子树中的某个点。

那么，我们显然可以把这个b分成两类，第一种是在a上面的，第二种在a下面的。


对于b在a上面的情况，显然，c一定是a的子树中的某个点，答案即$min(K,depth[a])*size[a]$

.

对于b在a下面的情况，问题就会变得比较exciting了。

我们可以考虑使用主席树来搞这个问题。

考虑建一颗这样的主席树，**以节点深度为主席树下标**。

对于一个节点，如果B在这个节点上，那么，它对答案的贡献显然是它的size-1。

那么，我们把它的贡献插入到它对应的主席树中（以深度为下标）。

每一个子节点开一颗主席树，记录到它为止所有的深度的答案和，有点类似前缀和，**以dfs序为时间轴**。

这样，我们可以用一种类似树上差分的办法来“抠”出一颗子树对应的线段数（以深度为下标），**这颗线段数中的[depth[x]+1,depth[x]+K]区间的sum就是这个x点的答案啦**。

 
.

就酱，这题就被我们切掉啦٩(๑>◡<๑)۶


------------
## Code
```cpp
#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
long long read()
{
    long long x=0,f=1; char c=getchar();
    while(!isdigit(c)){if(c=='-') f=-1;c=getchar();}
    while(isdigit(c)){x=x*10+c-'0';c=getchar();}
    return x*f;
}
const long long N=300000+100;
const long long M=N*30;
struct SegmentTree
{
    #define mid ((now_l+now_r)>>1)
    long long son[M][2],cnt;
    long long sum[M];
    inline void update(long long now)
    {
        sum[now]=sum[son[now][0]]+sum[son[now][1]];
    }
    void Build(long long now,long long now_l,long long now_r)
    {
        if(now_l==now_r) 
            return;    
        Build(son[now][0]=++cnt,now_l,mid);
        Build(son[now][1]=++cnt,mid+1,now_r);
    }
    void Add(long long x,long long num,long long now,long long pre,long long now_l,long long now_r)
    {
        if(now_l==now_r)
        {
            sum[now]=sum[pre];
            sum[now]+=num;
            return ;
        }
        if(x<=mid) son[now][1]=son[pre][1],Add(x,num,son[now][0]=++cnt,son[pre][0],now_l,mid);
        else son[now][0]=son[pre][0],Add(x,num,son[now][1]=++cnt,son[pre][1],mid+1,now_r);
        update(now);
    }
    long long Query(long long L,long long R,long long now,long long pre,long long now_l,long long now_r)
    {
        if(now_l>=L and now_r<=R)
            return sum[now]-sum[pre];
        long long ans=0;
        if(L<=mid) ans+=Query(L,R,son[now][0],son[pre][0],now_l,mid);
        if(R>mid) ans+=Query(L,R,son[now][1],son[pre][1],mid+1,now_r);
        return ans;
    }
    void Print(long long now,long long now_l,long long now_r)
    {
        cerr<<"no."<<now<<" now_l&r:"<<now_l<<" "<<now_r<<" sonl&r"<<son[now][0]<<" "<<son[now][1]<<" sum:"<<sum[now]<<endl;
        if(now_l!=now_r)
        {
            Print(son[now][0],now_l,mid);
            Print(son[now][1],mid+1,now_r);    
        }
    }    
    #undef mid
}sgt;
vector <long long> e[N];
long long n,m,depth[N],size[N],dfn[N],dfn_to,r[N];
void dfs2(long long now)
{
    dfn[now]=++dfn_to;
    size[now]=1;
    for(long long i=0;i<(long long)(e[now].size());i++)
        if(depth[e[now][i]]==0)    
        {
            depth[e[now][i]]=depth[now]+1;
            dfs2(e[now][i]);
            size[now]+=size[e[now][i]];    
        }
}
void dfs(long long now)
{
    r[dfn[now]]=++sgt.cnt;
    sgt.Add(depth[now],size[now]-1,r[dfn[now]],r[dfn[now]-1],1,n);
    //sgt.Print(r[dfn[now]],1,n);
    //cerr<<endl;
    for(long long i=0;i<(long long)(e[now].size());i++)
        if(depth[e[now][i]]>depth[now])
            dfs(e[now][i]);
}
int main()
{
    n=read(),m=read();
    for(long long i=1;i<=n;i++)
        e[i].reserve(4);
    for(long long i=1;i<n;i++)
    {
        long long s=read(),t=read();
        e[s].push_back(t);
        e[t].push_back(s);    
    }
    
    sgt.Build(0,1,n);
    //sgt.Print(0,1,n);
    //cerr<<endl;
    depth[1]=1;
    dfs2(1);
    dfs(1);
    
    for(long long i=1;i<=m;i++)
    {
        long long p=read(),K=read();
        long long ans=sgt.Query(depth[p]+1,depth[p]+K,r[dfn[p]+size[p]-1],r[dfn[p]-1],1,n);
        ans+=min(K,depth[p]-1)*(size[p]-1);
        printf("%lld\n",ans);
    }
    return 0;
}
```