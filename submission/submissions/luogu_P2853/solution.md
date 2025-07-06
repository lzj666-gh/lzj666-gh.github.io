# P2853 题解

从k个奶牛分别dfs，用mk[i]表示第i个牧场被遍历过多少次，最后只有mk[i]==k的牧场满足条件。无权的有向图也可以用vector存储。

```cpp
#include <queue>
#include <cstdio>
#include <iostream>
using namespace std;
bool vis[1010];
int k,n,m,ans;
int mk[1010],a[1010];
vector <int> b[1010];
void dfs(int x)
{
     vis[x]=1;  mk[x]++;
     for(int i=0;i<b[x].size();i++)
         if(!vis[b[x][i]])
             dfs(b[x][i]);
}
int main()
{
    int x,y;
    cin>>k>>n>>m;
    for(int i=1;i<=k;i++) cin>>a[i];
    for(int i=1;i<=m;i++) 
    {
        cin>>x>>y;
        b[x].push_back(y);
    }
    for(int i=1;i<=k;i++) { for(int j=1;j<=n;j++) vis[j]=0;  dfs(a[i]);}
    for(int i=1;i<=n;i++) if(mk[i]==k) ans++;
    cout<<ans;
    return 0;
}
```