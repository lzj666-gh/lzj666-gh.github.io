# P13823 题解

出题人题解。

首先显然能注意到：将图看成连通图后，同一个连通块里的就能相互转移。于是，每个点的答案肯定是连通块里的最大值之一转移到的。

这个题中，一条边相对于某个点来说是入边还是出边已经不重要了，因为都可以通过这条边进入或走出某个点。于是为了方便并不产生误导，将原来的某个点的入边称为 A 边，原来某个点的出边称为 B 边。

不难发现，从一个点的 A 边进入某个点，再从 B 边出去，这种情况不消耗代价，B 边进入、A 边出去也一样。只有从一个点的 A 边进入、A 边出去，或者 B 边进入、B 边出去，才会消耗 $1$ 步。

于是，对于每个点，我们需要考虑的边有四类：从 A 边或 B 边进来或出去都需要考虑。于是不难想到拆点：

![](https://cdn.luogu.com.cn/upload/image_hosting/67woxwu1.png)

然后，所有原图中的边 $u\rarr v$ 可以拆成两条：$u$ 的 B2 连向 $v$ 的 A1、从 $v$ 的 A2 连向 $u$ 的 B1。

显然这样的拆点方式，仅仅使得点和边的规模都扩大了常数倍。其实可以合并 A1 和 B2，再合并 A2 和 B1，做到一个点仅拆成两个点。但是为了较好理解还是选择了上面的方法。

最后每个连通块独立，在新图中跑 01bfs 即可。因为最大值可能有多个，所以把它们都设为起点。

时间复杂度 $O(n+m)$。

以下是由 @[jasmine0201](/user/476922) 编写的代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=5e5+5,M=2*N;
int n,m,d[4*N],a[4*N],b[4*N],s[4*N];
struct edge1 {int cnt,head[4*N],nxt[4*M],to[4*M],w[4*M]; } ed;
struct edge2 {int cnt,head[N],nxt[M],to[M]; } Ed;
void addedge(int u,int v,int p){
	ed.to[++ed.cnt] = v;
	ed.nxt[ed.cnt] = ed.head[u];
	ed.head[u] = ed.cnt;
    ed.w[ed.cnt] = p;
}
void addEdge(int u,int v){
	Ed.to[++Ed.cnt] = v;
	Ed.nxt[Ed.cnt] = Ed.head[u];
	Ed.head[u] = Ed.cnt;
}
int dfs(int x){
	if(b[x]) return s[x];
	b[x]=1;
	s[x]=a[x];
	// for(int i=0;i<Ed[x].size();i++) s[x]=max(s[x],dfs(Ed[x][i]));
    for(int i=Ed.head[x];i;i=Ed.nxt[i]) s[x]=max(s[x],dfs(Ed.to[i]));
	return s[x];
}
void dfs1(int x,int num){
	if(s[x]==-1) return;
	s[x]=-1;
	if(a[x]<num) b[x]=0;
	// for(int i=0;i<Ed[x].size();i++) dfs1(Ed[x][i],num);
    for(int i=Ed.head[x];i;i=Ed.nxt[i]) dfs1(Ed.to[i],num);
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);
	int n;
	cin>>n>>m;
	for(int i=1;i<=n;i++) cin>>a[i];
	for(int i=1;i<=n;i++){
		addedge(i*4+1,i*4+3,0);
		addedge(i*4+2,i*4+4,0);
		addedge(i*4+1,i*4+4,1);
		addedge(i*4+2,i*4+3,1);
	}
	int u,v;
	for(int i=1;i<=m;i++){
		cin>>u>>v;
		addedge(u*4+3,v*4+1,0);
		addedge(v*4+4,u*4+2,0);
		addEdge(u,v);
		addEdge(v,u);
	}
	for(int i=1;i<=n;i++) dfs(i);
	for(int i=1;i<=n;i++) dfs1(i,s[i]);
	deque<int> q;
	for(int i=1;i<=n;i++){
		if(b[i]){
			q.push_back(i*4+1); d[i*4+1]=1;
			q.push_back(i*4+2); d[i*4+2]=1;
		}
	}
	while(!q.empty()){
		int x=q.front();q.pop_front();
		for(int i=ed.head[x];i;i=ed.nxt[i]){
			int v=ed.to[i];
			if(d[v]<=d[x]+ed.w[i]&&d[v]!=0) continue;
			d[v]=d[x]+ed.w[i];
			if(ed.w[i]==0) q.push_front(v);
			else q.push_back(v);
		}
	}
	for(int i=1;i<=n;i++){
		if(b[i]) cout<<0<<' ';
		else cout<<min(d[i*4+3],d[i*4+4])<<' ';
	}
}
```