# P4315 题解

这道题目，如果把边权改为点权的话，那么就是一个树链剖分+线段树的裸题了，就是两遍dfs找出重儿子，对点进行重新编号，然后树链剖分即可。

但是！！——这题是边权，那怎么办呢？我们发现，一个点最多只有一个父亲结点，那么我们就可以考虑把这个点与其父亲结点之间边的边权转化为这个点的点权！那，之后，就变成了我们一开始说的树链剖分裸题了呀！还有一个非常重要的细节就是树链剖分查询和修改路径的时候，父亲结点是不在路径上的！因为父亲结点的点权代表的是它与它的父亲之间的边权，因此，在查询和修改的时候，最后左端点为$id[x]$+$1$。

具体实现看代码：

```cpp
#include<cstdio>
#include<algorithm>
#include<cctype>
#define maxn 100007
#define ll long long
#define ls rt<<1
#define rs rt<<1|1
using namespace std;
int n,head[maxn],d[maxn],size[maxn],son[maxn],a[maxn],tag[maxn<<2];                             //tag是把区间改为一个数时的lazy数组。
int p[maxn],id[maxn],top[maxn],num,cnt,lazy[maxn<<2],fa[maxn],maxx[maxn<<2];              
char s[10];
inline int qread() {
  char c=getchar();int num=0,f=1;
  for(;!isdigit(c);c=getchar()) if(c=='-') f=-1;
  for(;isdigit(c);c=getchar()) num=num*10+c-'0';
  return num*f;
}
struct node {
  int v,w,nxt;
}e[maxn<<1];
inline void ct(int u, int v, int w) {  
  e[++num].v=v;
  e[num].w=w;
  e[num].nxt=head[u];
  head[u]=num;
}
inline void pushup(int rt) {
  maxx[rt]=max(maxx[ls],maxx[rs]);
}
inline void pushdown(int rt) {
  if(tag[rt]>=0) {
    lazy[ls]=lazy[rs]=0;
    maxx[ls]=maxx[rs]=tag[ls]=tag[rs]=tag[rt];
    tag[rt]=-1;
  }
  if(lazy[rt]) {
    lazy[ls]+=lazy[rt];
    lazy[rs]+=lazy[rt];
    maxx[ls]+=lazy[rt];
    maxx[rs]+=lazy[rt];
    lazy[rt]=0;
  }
}
void build(int rt, int l, int r) {
  tag[rt]=-1;
  if(l==r) {
    maxx[rt]=a[l];
    return;
  }
  int mid=(l+r)>>1;
  build(ls,l,mid);
  build(rs,mid+1,r);
  pushup(rt);
}
void modify1(int rt, int l, int r, int L, int R, int val) {
  if(L>r||R<l) return;
  if(L<=l&&r<=R) {
    lazy[rt]+=val;
    maxx[rt]+=val;
    return;
  }
  pushdown(rt);
  int mid=(l+r)>>1;
  if(L<=mid) modify1(ls,l,mid,L,R,val);
  if(R>mid) modify1(rs,mid+1,r,L,R,val);
  pushup(rt);
}
void modify2(int rt, int l, int r, int L, int R, int val) {
  if(L>r||R<l) return;
  if(L<=l&&r<=R) {
    maxx[rt]=tag[rt]=val;
    lazy[rt]=0;
    return;
  }
  pushdown(rt);
  int mid=(l+r)>>1;
  modify2(ls,l,mid,L,R,val),modify2(rs,mid+1,r,L,R,val);
  pushup(rt);
}
int cmax(int rt, int l, int r, int L, int R) {
  if(L<=l&&r<=R) return maxx[rt];
  int ans=0;
  int mid=(l+r)>>1;
  pushdown(rt);
  if(L<=mid) ans=max(ans,cmax(ls,l,mid,L,R));
  if(R>mid) ans=max(ans,cmax(rs,mid+1,r,L,R));
  return ans;
}
void dfs1(int u, int f) {
  size[u]=1;
  for(int i=head[u];i;i=e[i].nxt) {
    int v=e[i].v;
    if(v!=f) {
      d[v]=d[u]+1;
      fa[v]=u;
      p[v]=e[i].w;
      dfs1(v,u);
      size[u]+=size[v];
      if(size[v]>size[son[u]]) son[u]=v;
    }
  }
}
void dfs2(int u, int t) {
  id[u]=++cnt;
  top[u]=t;
  a[cnt]=p[u];
  if(son[u]) dfs2(son[u],t);
  for(int i=head[u];i;i=e[i].nxt) {
    int v=e[i].v;
    if(v!=fa[u]&&v!=son[u]) dfs2(v,v);
  }
}
void cal1(int x, int y, int val) {
  int fx=top[x],fy=top[y];
  while(fx!=fy) {
    if(d[fx]<d[fy]) swap(x,y),swap(fx,fy);
    modify1(1,1,n,id[fx],id[x],val);
    x=fa[fx],fx=top[x];
  }
  if(id[x]>id[y]) swap(x,y);
  modify1(1,1,n,id[x]+1,id[y],val);
}
void cal2(int x, int y, int val) {
  int fx=top[x],fy=top[y];
  while(fx!=fy) {
    if(d[fx]<d[fy]) swap(x,y),swap(fx,fy);
    modify2(1,1,n,id[fx],id[x],val);
    x=fa[fx],fx=top[x];
  }
  if(id[x]>id[y]) swap(x,y);
  modify2(1,1,n,id[x]+1,id[y],val);
}
int query(int x, int y) {
  int ans=0,fx=top[x],fy=top[y];
  while(fx!=fy) {
    if(d[fx]<d[fy]) swap(x,y),swap(fx,fy);
    ans=max(ans,cmax(1,1,n,id[fx],id[x]));
    x=fa[fx],fx=top[x];
  }
  if(id[x]>id[y]) swap(x,y);
  ans=max(ans,cmax(1,1,n,id[x]+1,id[y]));
  return ans;
}
int main() {
  n=qread();
  for(int i=1,u,v,w;i<n;++i) {
    u=qread(),v=qread(),w=qread();
    ct(u,v,w);ct(v,u,w);
  }
  dfs1(1,0),dfs2(1,1);build(1,1,n);
  while(1) {
    scanf("%s",s);
    if(s[0]=='S') break;
    int x=qread(),y=qread();
    if(s[1]=='h') {
      x=d[e[x*2-1].v]<d[e[x<<1].v]?e[x<<1].v:e[x*2-1].v;
      modify2(1,1,n,id[x],id[x],y);        //这里必须要加这句话！因为我们dfs时没有记录哪个边具体对应哪个点。
    }
    if(s[1]=='o') {
      int zrj=qread();
      cal2(x,y,zrj);
    }
    if(s[1]=='d') {
      int zrj=qread();
      cal1(x,y,zrj);
    }
    if(s[1]=='a') printf("%d\n",query(x,y)); 
  }
  return 0;
}
```

代码量有点大，调起来也挺难的，本蒟蒻调了一下午……可能我太弱了，祝大家一遍AC啊！！！