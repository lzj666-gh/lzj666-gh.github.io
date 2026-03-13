# P6145 题解

对于每个三元组 $(a,b,x)$，从 $a$ 向 $b$ 连一条长度为 $x$ 的边。同时新建一个超级源点 $0$，从 $0$ 向 $i$ 连长度为 $S_i$ 的边。

容易发现这张图是一个 DAG。

直接拓扑排序递推计算即可。

```cpp
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
struct edge
{
 int v,w,next;
}e[100005];
int s[100005],t[100005],head[100005],cnt;
queue<int> q;
void addedge(int u,int v,int w)
{
 e[++cnt].v=v;
 e[cnt].w=w;
 e[cnt].next=head[u];
 head[u]=cnt;
}
int main()
{
 freopen("timeline.in","r",stdin);
 freopen("timeline.out","w",stdout);
 ios::sync_with_stdio(false);
 int n,m,c;
 cin>>n>>m>>c;
 for(int i=1;i<=n;i++)
  cin>>s[i];
 for(int i=1;i<=c;i++)
 {
  int u,v,w;
  cin>>u>>v>>w;
  addedge(u,v,w);
  t[v]++;
 }
 for(int i=1;i<=n;i++)
  if(!t[i])q.push(i);
 while(!q.empty())
 {
  int u=q.front();
  q.pop();
  for(int i=head[u];i;i=e[i].next)
  {
   int v=e[i].v,w=e[i].w;
   s[v]=max(s[v],s[u]+w);
   t[v]--;
   if(!t[v])q.push(v);
  }
 }
 for(int i=1;i<=n;i++)
  cout<<s[i]<<endl;
 return 0;
}
```