# P13824 题解

`if(vs[i]!=lca(vs[i],x))` 写成 `if(vs[i]!=1)` 痛失 100pts.

另外的，倒序开题，所以这题写了 3h 左右。

怎么有人用小号打基础赛还掉分啊。

---

先对于每个点对，计算其作为可行解时 $d$ 的范围。

考虑 dp。

定义 $f_{i,j}$ 表示当 $d\ge f_{i,j}$ 时点对 $(i,j)$ 才是一个可能的解。

转移式：

+ 当 $i$ 是 $j$ 的祖先，$f_{i,j}=\max(dis_{i,j},f_{i,fa_j})$。
+ 否则，$f_{i,j}=\max(dis_{i,j},\min(f_{i,fa_j},f_{fa_i,fa_j},f_{fa_i,fa}))$。

其中 $dis_{i,j}$ 表示 $(i,j)$ 的树上距离，$fa_i$ 表示 $i$ 的父亲。

然后我们有 $f_{i,j}=f_{j,i}$，并且 $f_{i,i}=0$。

现在我们要求所有的 $f_{i,j}$。

由于每一个点都是从父亲转移而来，考虑 DAG DP。

按照拓扑序转移容易做到 $O(n^2)$。

然后我们把每一个 $d$ 的最优解放到桶里，用类似于单调队列的处理，按顺序拿出来，如果没有前面优就扔掉。

查询时二分就做完了。这个部分容易做到 $O(q\log n^2)$。

实现较困难。

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
vector<pair<int,int> >ve[1005];
int fa[1005],dep[1005];
void dfs(int x){
    for(int i=0;i<ve[x].size();i++)
    if(ve[x][i].first!=fa[x])
    fa[ve[x][i].first]=x,
    dep[ve[x][i].first]=dep[x]+ve[x][i].second,
    dfs(ve[x][i].first);
}
int mi[25][1005],dfn[1005],dfnn;
int get(int u,int v){
    if(dfn[u]<dfn[v])return u;
    else return v;
}
void dfs1(int id,int f){
    mi[0][dfn[id]=++dfnn]=f;
    for(pair<int,int> it:ve[id])
    if(it.first!=f)dfs1(it.first,id); 
}
int lca(int u,int v){
    if(u==v)return u;
    if((u=dfn[u])>(v=dfn[v])) swap(u, v);
    int d=__lg(v-u++);
    return get(mi[d][u],mi[d][v-(1<<d)+1]);
}
struct fish{
    int x,y;
}a[1005];
int F(int i,int j){
    return (a[i].x-a[j].x)*(a[i].x-a[j].x)+(a[i].y-a[j].y)*(a[i].y-a[j].y);
}
int f[1005][1005];
vector<int>vs;
int jl(int i,int j){
    return dep[i]+dep[j]-2*dep[lca(i,j)];
}
map<int,int>qwq;
map<int,pair<int,int>>mp;
vector<int>ansid;
vector<pair<int,int>>ret;
signed main(){
    int n,t;
    cin>>n>>t;
    for(int i=1;i<=n;i++)
    cin>>a[i].x>>a[i].y;
    for(int i=1;i<n;i++){
        int u,v;
        cin>>u>>v;
        ve[u].push_back({v,F(u,v)});
        ve[v].push_back({u,F(u,v)});
    }
    dfs1(1,0);
    for(int i=1;i<=__lg(n);i++)
    for(int j=1;j<=n-(1<<i)+1;j++)
    mi[i][j]=get(mi[i-1][j],mi[i-1][j+(1<<(i-1))]);
    dfs(1);
    queue<int>q;
    q.push(1);
    while(!q.empty()){
        int x=q.front();q.pop();
        for(int i=0;i<vs.size();i++){
            f[x][vs[i]]=f[fa[x]][vs[i]];
            if(vs[i]!=lca(vs[i],x))
            f[x][vs[i]]=min({f[x][vs[i]],f[x][fa[vs[i]]],f[fa[x]][fa[vs[i]]]});
            f[x][vs[i]]=max(f[x][vs[i]],F(x,vs[i]));
            f[vs[i]][x]=f[x][vs[i]];
        }
        vs.push_back(x);
        for(int i=0;i<ve[x].size();i++){
            if(ve[x][i].first==fa[x])continue;
            q.push(ve[x][i].first);
        }
    }
    for(int i=1;i<=n;i++)
    for(int j=i;j<=n;j++){
        if(!mp[f[i][j]].first||qwq[f[i][j]]<jl(i,j))
        mp[f[i][j]]={i,j},qwq[f[i][j]]=jl(i,j);
    }
    for(auto i:mp){
        int x=i.first;
        if(!ansid.empty()){
            if(qwq[ansid[ansid.size()-1]]<qwq[x])
            ansid.push_back(x),ret.push_back(mp[x]);
            else if(qwq[ansid[ansid.size()-1]]==qwq[x]&&mp[ansid[ansid.size()-1]]>mp[x])
            ansid.push_back(x),ret.push_back(mp[x]);
        }else ansid.push_back(x),ret.push_back(mp[x]);
    }
    while(t--){
        int d;
        cin>>d;
        int x=upper_bound(ansid.begin(),ansid.end(),d)-ansid.begin()-1;
        cout<<ret[x].first<<' '<<ret[x].second<<'\n';
    }
    return 0;
}
// 「在这个太阳西斜的世界里」
```