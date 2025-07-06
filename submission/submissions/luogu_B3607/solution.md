# B3607 题解

~~来一个 HLPP 的题解~~

HLPP （最高标号预流推进）应该是常见最大流算法里效率最高的，最差复杂度为 $O(n^2\sqrt m)$（然而随机数据下跑的没 dinic 快），虽然裸的 HLPP 很容易被卡到这个上界，但是经过一些优化的 HLPP 还是基本能做到平均速度和 dinic 持平。

------------

### 基本思想

EK、FF、dinic、ISAP 等算法都属于**增广路算法**。而 HLPP 是一种**推送-重贴标签**算法（又称预流推进）。现在效率最高的几种最大流算法几乎都是推送-重贴标签算法。推送-重贴标签算法在算法过程中并不满足网络的流量守恒性质，即存在流入一个节点的流量大于流出该节点流量的情况，因为在执行过程中，推送-重贴标签算法始终维护着一个函数**预流**（preflow）。

众所周知，网络的流量守恒性质是：在网络 $G(E,V)$ 中，对于 $u\in V-\{s,t\}$ 有：

$$\sum_{v\in V}f(v,u)-\sum_{v\in V}f(u,v)=0$$

而在推送-重贴标签算法过程中，则弱化了这个条件：

$$\sum_{v\in V}f(v,u)-\sum_{v\in V}f(u,v)\geq0$$

即每个节点可以暂时储存一定的流量（但不能透支），而我们称：

$$e(u)=\sum_{v\in V}f(v,u)-\sum_{v\in V}f(u,v)$$

为 $u$ 的**超额流**（excess flow）。

不难发现，在最大化流量且 $u\in V-\{s,t\}$ 的 $e(u)$ 都为 $0$ 时，$e(t)$ 即为整张网络的最大流。

那么我们的目标就是不断推送流量，且保证最终 $e(u)$ 为 $0$。



------------

### 算法流程
大家可能就立刻会想到一种做法：

每个节点都把流向自己的边流满，多余的流量作为超额流暂时储存，一旦有机会就马上推向周围的节点；因为有反向边的存在，从 $s$ 流出的多余流量最终一定也会回到 $s$，那么最终整张网络也能平衡。

但是，设想一种情况：如果 $u$ 把超额流推给了 $v$，但 $v$ 不讲武德，接化发把流量原封不动的还了回去，然后 $u$ 再推，$v$ 再还……一直推到 TLE。

那么我们就考虑和 dinic 差不多，将整张网络进行分层，每一层节点的超额流只能推给下一层节点。

令 $h(u)$ 为高度函数，表示节点 $u$ 的高度（height），预流推进的操作只允许推给 $v\in V$ 且 $h(v)=h(u)-1$ 的节点，那么流量就不会来回推了， $h(s)$ 设为最高。

但是，这样又会有另一种情况：在流量推来推去的过程中，有个节点 $u$ 特别惨，满足 $v\in V$ 且 $h(v)=h(u)-1$ 的边 $(u,v)$ 要么就没有，要么已经满流了，而此时她上一层的节点又推给她很多超额流，而这些超额流在她手里无论如何都推不出去了。

怎么办？

我们的算法叫推送-**重贴标签**算法。

那就强行把她抬起来，把流量推回去。

（你可以想象一个场面，一个盆地或一个断层被顶出，变成一座山）

每次遇到流不动的情况，那么就找到一个最低的高度，让她恰好能流掉自己的超额流。

这就是重贴标签（relabel）的过程

然后呢？没有然后了。

------------
### 关于 HLPP 的细节

上面的都是推送-重贴标签算法的基础模型，如果不加优化可以轻松的达到 $O(n^2m)$ 的~~优秀~~复杂度，距离我们 HLPP 的 $O(n^2\sqrt m)$ 还有一段距离。

那么还要注意什么？

1. 关于 $h$ 函数初值的处理。

如何给 $h$ 赋一个合适的初值？可以直接将 $h(s)\gets n$ ，其它的都是 $0$，在重贴标签的过程中不断调整。

但这样不够优秀，在初始时可以像 dinic 一样 bfs 一遍，将分层图的层次作为 $h$。这样可以节省大量时间

2. 关于怎么让流量从高处向低处流？

这个问题由 R·E·Tarjan （怎么又是他）在 1986 年解决，这也是 HLPP 名字的由来。bfs 可以有层次的处理信息。我们可以建立一个以 $h$ 为键值的优先队列，每次取最高的节点进行预流推进。因为其它节点都比当前节点矮，不会被重贴标签，处理起来方便；而且这样能保证每个点入队的次数最少，因为矮的节点会在队列中被反复推进，而不是出队又进队。

3. 关于重贴标签的 gap 优化。

学过 ISAP 的人大概都知道 gap 优化，HLPP 的 gap 优化和 ISAP 有点像。假设我们给 $u$ 重贴标签的过程中，$h(u)$ 这一高度没有其它节点了，由于只有满足 $h(v)=h(u)-1$ 的边 $(u,v)$ 的边才会被预流推进，那么高度为 $h(u)+1$ 就永远无法把自己的超额流向下推了，以此类推，所有 $h(v)>h(u)$ 的节点的超额流都流不动了，这些节点未来都需要重贴标签，不知情的节点还会互相推流量，然而这些流量都流不动。那么还不如现在就重贴。把她们的高度设为 $n+1$ ，这样一来，她们的流量就可以直接还给 $s$ 节点。

代码（细节比较多，可以对照查看）：
```cpp
#include<bits/stdc++.h>
using namespace std;
#define rg register
#define ll long long
#define ull unsigned ll
#define inf 0x7f7f7f7f
#define sit set<int>::iterator
inline void file(){
	freopen("test.in","r",stdin);
}
char buf[1<<21],*p1=buf,*p2=buf;
inline int getc(){
    return p1==p2&&(p2=(p1=buf)+fread(buf,1,1<<21,stdin),p1==p2)?EOF:*p1++;
}
inline ll read(){
	rg ll ret=0,f=0;char ch=getc();
    while(!isdigit(ch)){if(ch=='-')f=1;ch=getc();}
    while(isdigit(ch)){ret=ret*10+ch-48;ch=getc();}
    return f?-ret:ret;
}
struct node{
	int nex,to;
	ll val;
}e[500005<<1];
int n,m,u,v,w,s,t,cnt=1,head[50005];
int h[50005],gap[50005];  //h 表示高度，gap 表示该高度的节点数。 
bool vis[50005];  //vis 表示是否在队中。 
ll maxflow,excess[50005];  //excess 表示超额流 
inline void add(int u,int v,ll w){
	e[++cnt].nex=head[u];
	e[cnt].to=v;
	e[cnt].val=w;
	head[u]=cnt;
}
bool init(){  //初始 bfs 给图分层，注意是从 t 倒着搜。 
	queue<int> q; 
	memset(h,0x7f,sizeof(h));
	h[t]=0; q.push(t);
	while(!q.empty()){
		int now=q.front(); q.pop();
		for(rg int i=head[now];i;i=e[i].nex){
			if(e[i^1].val&&h[e[i].to]-1>h[now]){
				q.push(e[i].to);
				h[e[i].to]=h[now]+1;
			}
		}
	}
	return h[s]!=inf;
}
struct ty{
	int v;
	bool operator<(const ty& __)const{
		return h[v]<h[__.v]; 
	}
};
inline ty make(int x){
	return (ty){x};
}
priority_queue<ty> pq;  //以 h 为键值的优先队列。 
inline void push(int x){  //预流推进操作。 
	for(rg int i=head[x];i;i=e[i].nex){
		if(!excess[x]) break;  //推完了。 
		if(!e[i].val||h[e[i].to]!=h[x]-1) continue;  //不能推。 
		ll tmp=min(e[i].val,excess[x]);  //尽可能的推。 
		e[i].val-=tmp;
		e[i^1].val+=tmp;
		excess[x]-=tmp;
		excess[e[i].to]+=tmp;
		if(e[i].to!=s&&e[i].to!=t&&!vis[e[i].to]){  //被推的节点自己也会超额，入队等待推别人的机会。 
			vis[e[i].to]=1;
			pq.push(make(e[i].to));
		}
	}
}
inline void relabel(int x){
	h[x]=inf;
	for(rg int i=head[x];i;i=e[i].nex)
		if(e[i].val&&h[e[i].to]<h[x]-1)
			h[x]=h[e[i].to]+1;  //找到最矮的能推别人的位置。 
}
void HLPP(){
	if(!init())  //不连通。 
		return maxflow=0,void();
	h[s]=n;
	for(rg int i=1;i<=n;++i)
		if(h[i]!=inf) ++gap[h[i]];
	for(rg int i=head[s];i;i=e[i].nex){
		if(!e[i].val||h[e[i].to]==inf) continue;
		ll tmp=e[i].val;
		e[i].val-=tmp; 
		e[i^1].val+=tmp;
		excess[s]-=tmp;
		excess[e[i].to]+=tmp;
		if(e[i].to!=s&&e[i].to!=t&&!vis[e[i].to]){  
			vis[e[i].to]=1;
			pq.push(make(e[i].to));
		}
	} //同 push 函数，对于 s 的 push 特殊处理。 
	while(!pq.empty()){
		int now=pq.top().v; pq.pop();
		vis[now]=0;
		push(now);
		if(!excess[now]) continue; //超额流推完了。 
		if(!--gap[h[now]])  //gap 优化。 
			for(rg int i=1;i<=n;++i)
				if(i!=s&&i!=t&&h[i]>h[now]&&h[i]<n+1)
					h[i]=n+1;
		relabel(now); 
		++gap[h[now]];  //重贴标签。 
		vis[now]=1;
		pq.push(make(now)); //没推完，入队继续等待推别人的机会。 
	}
	maxflow=excess[t];
}
int main(){
    n=read(); m=read(); s=read(); t=read();
    for(rg int i=1;i<=m;++i){
    	u=read(); v=read(); w=read(); 
    	add(u,v,w);
    	add(v,u,0);
	}
	HLPP();
	printf("%lld",maxflow);
    return 0;
}
//If you're gonna replace me,at least have the audacity to kill me thoroughly.
```
