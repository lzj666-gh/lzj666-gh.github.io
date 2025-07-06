# P8269 题解

## 题意
一共有 $n$ 头奶牛，每一头奶牛都有自己想拜访的奶牛，用 $a_i$ 表示牛 $i$ 想拜访的牛。对于每一头牛 $i$，如果它想拜访的牛在家，就会离开家并拜访它，还会增加 $v_i$ 的欢乐值，最后求欢乐值的最大值。
## 思路
我们可以将这个问题看作一个一个图，且每一个节点的出度都是 $1$。 我们可以发现除了每个环中会有一个奶牛无法获得高兴值，其他的奶牛都可以获得高兴值。

我们可以用拓扑排序来找到所有不在环上的奶牛，将答案加上他们的高兴值。接下用 dfs 找出每个环。对于每个环中的无法获得高兴值的奶牛，我们肯定选高兴值最小的。找到每个环的奶牛的非小值并加上它们。

最后在贴上代码:

```cpp
#include<bits/stdc++.h>
using namespace std;
#define inf 1e18+10
#define int long long
const int maxn=100010;
int n,a[maxn],v[maxn],rd[maxn],ans,minn=inf;
bool vis[maxn];
queue<int>q;
void topo(){
    for(int i=1;i<=n;i++){
        if(!rd[i])q.push(i);
    }
    while(!q.empty()){
        int x=q.front();q.pop();
        ans+=v[x];rd[a[x]]--;
        vis[x]=1;
        if(!rd[a[x]])q.push(a[x]);
    }
    return;
}
void dfs(int x){
    vis[x]=1;
    minn=min(minn,v[x]);
    if(vis[a[x]])return;
    dfs(a[x]);
    return;
}
signed main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%lld%lld",&a[i],&v[i]);
        rd[a[i]]++;
    }
    topo();
    for(int i=1;i<=n;i++){
        if(!vis[i])ans+=v[i];
    }
    for(int i=1;i<=n;i++){
        if(vis[i])continue;
        minn=inf;dfs(i);
        ans-=minn;
    }
    printf("%lld",ans);
    return 0;
}
```
