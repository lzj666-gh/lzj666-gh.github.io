# P4114 题解

第一次写边权树剖的题目，写篇题解造(bao)福(fu)社会

这题要搞的是对边权的操作，不是点权，怎么搞？  我们注意到一棵$n$个节点的树，有$n-1$个节点(废话)，且每个节点只有**唯一**的父节点。  
那就可以考虑把$u$到其父节点$v$的边权，转移到$u$上存储，这样就可以开开心心的树剖了。   
对于权值的转移，在树剖的第一遍dfs时就能搞定。 

另外，这里要求$u$到$v$节点之间所有**边**的最大权值，不是点。  
不难发现：对于$\text{lca}(u,v)$记录的边权，是不在$u$到$v$的路径上的。所以在计算最大值时，自然不能算进这个节点。   
搞树上路径查询的时候，我们是这样做的：  
$u$和$v$节点不断地跳到其重链顶端，直到一条重链为止。  

此时，若假设$u$比$v$的深度小，那么显然$\text{lca}(u,v)=u$。这个$u$节点时不能算进答案里的，要避开它，我们可以根据树剖的性质：  
>同一条重链上的节点编号连续  

所以在最后一步查询的时候，$\text{query}(\text{id}[u]+1,\text{id}[v])$就行了，因为比$u$的编号大$1$的节点，一定是它的儿子。如此一来，就不会将$\text{lca}$算入结果了。 

是不是很简单啊？  
```cpp
#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#include<vector>
#include<ctime>
#define N 100003
#define inf 0x3f3f3f3f
#define ll long long
#define ls(u) (u<<1)
#define rs(u) (u<<1|1)
#define mid ((l+r)>>1)
using namespace std;

struct edge{
    int u,v,w;
    edge(int u=0,int v=0,int w=0):u(u),v(v),w(w){}
};

int wl[N],son[N],size[N],top[N],b[N],id[N];
int a[N<<2],tag[N<<2],depth[N],fa[N],mx[N<<2];
edge e[N];
int n,m,r,cnt;
vector<edge> adj[N];

inline void read(int &x){
    x = 0;
    char c = getchar();
    while(!isdigit(c)) c = getchar();
    while(isdigit(c)){
        x = (x<<3)+(x<<1)+c-'0';
        c = getchar();
    }
}

void print(int x){
    if(x>9) print(x/10);
    putchar(x%10+'0');
}

inline int max(int a,int b){
    return a>b?a:b;
}

//以下为线段树

inline void push_up(int u){
    a[u] = a[ls(u)]+a[rs(u)];
    mx[u] = max(mx[ls(u)],mx[rs(u)]);
}

void build(int u,int l,int r){
    if(l==r){
        a[u] = mx[u] = wl[l];
        return;
    }
    build(ls(u),l,mid);
    build(rs(u),mid+1,r);
    push_up(u);
}

void update(int u,int l,int r,int q,int k){
    if(l==r){
        a[u] = mx[u] = k;
        return;
    }
    if(q<=mid) update(ls(u),l,mid,q,k);
    else update(rs(u),mid+1,r,q,k);
    push_up(u);
}

int qaq(int nl,int nr,int l,int r,int u){
    int res = -inf;
    if(nl<=l&&r<=nr) return mx[u];
    if(nl<=mid) res = max(res,qaq(nl,nr,l,mid,ls(u)));
    if(nr>mid) res = max(res,qaq(nl,nr,mid+1,r,rs(u)));
    push_up(u);
    return res;
}

inline int qmax(int l,int r){
    return qaq(l,r,1,n,1);
}

//以上为线段树

void dfs1(int u,int f){
    fa[u] = f;
    depth[u] = depth[f]+1;
    size[u] = 1;
    int v,t = -1,l = adj[u].size();
    for(int i=0;i<l;++i){
        v = adj[u][i].v;
        if(v==f){
            b[u] = adj[u][i].w;
            continue;
        }
        dfs1(v,u);
        size[u] += size[v];
        if(size[v]>t){
            t = size[v];
            son[u] = v;
        }
    }
}

void dfs2(int u,int f){
    top[u] = f;
    id[u] = ++cnt;
    wl[cnt] = b[u];
    if(son[u]==0) return;
    dfs2(son[u],f);
    int v,l = adj[u].size();
    for(int i=0;i<l;++i){
        v = adj[u][i].v;
        if(v==fa[u]||v==son[u]) continue;
        dfs2(v,v);
    }
}

int pathMax(int u,int v){
    int res = -inf;
    while(top[u]!=top[v]){
        if(depth[top[u]]<depth[top[v]])
            swap(u,v);
        res = max(res,qmax(id[top[u]],id[u]));
        u = fa[top[u]];
    }
    if(depth[u]>depth[v]) swap(u,v);
    res = max(res,qmax(id[u]+1,id[v])); //上面提到的避开lca的方法
    return res;
}

int main(){
    int u,v,w,q;
    string str;
    read(n);
    for(int i=1;i<n;++i){
        read(u),read(v),read(w);
        adj[u].push_back(edge(u,v,w));
        adj[v].push_back(edge(v,u,w));
        e[i] = edge(u,v,w);
    }
    dfs1(1,0);
    dfs2(1,1);
    build(1,1,n);
    string op;
    while(1){
        op = "";
        char c = getchar();
        while(c<'A'||c>'Z') c = getchar();
        while(c>='A'&&c<='Z'){
            op.push_back(c);
            c = getchar();
        }
        if(op=="DONE") break;
        read(u),read(v);
        if(op=="QUERY"){
            if(u==v) putchar('0');
            else print(pathMax(u,v));
            putchar('\n');
        }else{
            if(depth[e[u].u]>depth[e[u].v]) u = e[u].u;
            else u = e[u].v;
            update(1,1,n,id[u],v);
        }
    }
    return 0;
}
```
