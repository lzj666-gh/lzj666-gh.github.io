# P2590 题解

<http://www.lydsy.com/JudgeOnline/problem.php?id=1036>

直接树链剖分线段树维护好了，神犇会写lct，然而我不会23333

树链剖分入门题，建议一做。

```cpp
#include<bits/stdc++.h>
#define N 100005
#define inf 1000000000
using namespace std;
int n,q,a[4*N];
struct Edge{
    int u,v,next;
}G[N];
int tot=0,head[N];
int size[100005],wson[100005],fa[100005],d[100005],top[100005];
int tpos[100005],pre[100005],cnt=0;
inline void addedge(int u,int v){
    G[++tot].u=u;G[tot].v=v;G[tot].next=head[u];head[u]=tot;
    G[++tot].u=v;G[tot].v=u;G[tot].next=head[v];head[v]=tot;
}
void dfs1(int u,int f){
    size[u]=1;
    for (int i=head[u];i;i=G[i].next){
        int v=G[i].v;if (v==f)continue;
        d[v]=d[u]+1;fa[v]=u;
        dfs1(v,u);
        size[u]+=size[v];
        if (size[v]>size[wson[u]])wson[u]=v;
    }
}
void dfs2(int u,int TP){
    tpos[u]=++cnt;pre[cnt]=u;top[u]=TP;
    if (wson[u])dfs2(wson[u],TP);
    for (int i=head[u];i;i=G[i].next){
        int v=G[i].v;
        if (v==fa[u]||v==wson[u])continue;
        dfs2(v,v);
    }
}
int sumv[4*N],maxv[4*N];
inline void pushup(int o){
    sumv[o]=sumv[o*2]+sumv[o*2+1];
    maxv[o]=max(maxv[o*2],maxv[o*2+1]);
}
void build(int o,int l,int r){
    int mid=(l+r)/2;
    if (l==r){sumv[o]=maxv[o]=a[pre[l]];return;}
    build(o*2,l,mid);build(o*2+1,mid+1,r);
    pushup(o);
}
void update(int o,int l,int r,int q,int v){
    int mid=(l+r)/2;
    if (l==r){sumv[o]=maxv[o]=v;return;}
    if (q<=mid)update(o*2,l,mid,q,v);
    else update(o*2+1,mid+1,r,q,v);
    pushup(o);
}
int querysum(int o,int l,int r,int ql,int qr){
    int mid=(l+r)/2,ans=0;
    if (ql<=l&&r<=qr)return sumv[o];
    if (ql<=mid)ans+=querysum(o*2,l,mid,ql,qr);
    if (qr>mid)ans+=querysum(o*2+1,mid+1,r,ql,qr);
    pushup(o);
    return ans;
}
int querymax(int o,int l,int r,int ql,int qr){
    int mid=(l+r)/2,ans=-inf;
    if (ql<=l&&r<=qr)return maxv[o];
    if (ql<=mid)ans=max(ans,querymax(o*2,l,mid,ql,qr));
    if (qr>mid)ans=max(ans,querymax(o*2+1,mid+1,r,ql,qr));
    pushup(o);
    return ans;
}
int qsum(int u,int v){
    int ans=0;
    while (top[u]!=top[v]){
        if (d[top[u]]<d[top[v]])swap(u,v);
        ans+=querysum(1,1,n,tpos[top[u]],tpos[u]);
        u=fa[top[u]];
    }
    if (d[u]<d[v])swap(u,v);
    ans+=querysum(1,1,n,tpos[v],tpos[u]);
    return ans;
}
int qmax(int u,int v){
    int ans=-inf;
    while (top[u]!=top[v]){
        if (d[top[u]]<d[top[v]])swap(u,v);
        ans=max(ans,querymax(1,1,n,tpos[top[u]],tpos[u]));
        u=fa[top[u]];
    }
    if (d[u]<d[v])swap(u,v);
    ans=max(ans,querymax(1,1,n,tpos[v],tpos[u]));
    return ans;
}
int main(){
    memset(head,0,sizeof(head));
    memset(a,0,sizeof(a));
    scanf("%d",&n);
    for (int i=1;i<n;i++){
        int u,v;
        scanf("%d%d",&u,&v);
        addedge(u,v);
    }
    for (int i=1;i<=n;i++)scanf("%d",&a[i]);
    d[1]=1;fa[1]=1;dfs1(1,-1);dfs2(1,1);build(1,1,n);
    scanf("%d",&q);
    while (q--){
        int x,y;
        char s[10];
        scanf("%s%d%d",s,&x,&y);
        if (s[1]=='H')update(1,1,n,tpos[x],y);
        if (s[1]=='M')printf("%d\n",qmax(x,y));
        if (s[1]=='S')printf("%d\n",qsum(x,y));
    }
    return 0;
}
```