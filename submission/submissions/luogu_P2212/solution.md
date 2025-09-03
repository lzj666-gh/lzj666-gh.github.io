# P2212 题解

- 题目链接：

  https://www.luogu.org/problemnew/show/P2212
  
- 思路：

  一道最小生成树裸题(最近居然变得这么水了),但是因为我太蒻,搞了好久,不过借此加深了对最小生成树的认识.
  
  首先这明显是个稠密图,有$\sum_{n-1}^{i=1}i=n*(n-1)/2$条边,看起来$Prim$会明显优于$Kruskal$,于是这道题我用了三种方法
  
  
- $Kruskal$

  简单易懂，简洁优美  耗时/内存 344ms, 24343KB
  
  代码：
  
```cpp
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cctype>
#define ri register int 
#define ll long long 
using namespace std;
const int maxn=2005;
const int inf=192681792;
struct Edge{
	int u,v,dis;
	bool operator <(const Edge& b)const{
		return dis<b.dis;
	}
}edge[19260817];//边数不要设小了 
int n,c,tot=0;
int px[maxn],py[maxn];
int fa[maxn];
int get(int x){
	if(fa[x]!=x)fa[x]=get(fa[x]);
	return fa[x];
}
inline void kruskal(){
	int u,v,dis;
	int cnt=0,ans=0;
	for(ri i=1;i<=n;i++){
		fa[i]=i;
	}
	for(ri i=1;i<=tot;i++){
		u=edge[i].u,v=edge[i].v;
		u=get(u),v=get(v);
		if(u!=v){
			fa[u]=v;
			ans+=edge[i].dis;
			cnt++;
	    }
	    if(cnt==n-1)break;
	}
	if(cnt==n-1)printf("%d",ans);
	else puts("-1");
	return ;
}
int main(){
	scanf("%d %d",&n,&c);
	for(ri i=1;i<=n;i++){
		scanf("%d %d",&px[i],&py[i]);
		for(ri j=1;j<i;j++){
			int d=(px[i]-px[j])*(px[i]-px[j])+(py[i]-py[j])*(py[i]-py[j]);
			if(d>=c){
				edge[++tot].u=i,edge[tot].v=j,edge[tot].dis=d;
			}
		}
	}
	sort(edge+1,edge+1+tot);
	kruskal();
	return 0;
}
```
  
- $Prim+Priority\_queue$优化

  说到$Prim$就不得不提，觉得网上挺多$Prim$堆优化代码都是假的。
  
  $Prim$的原理是找到连接生成树点集中一点与非生成树点集中一点的最小边权，将其加入答案,于是我们用$vis[]$数组标记该点是否处在生成树点集中,$d[x]$记录x到非生成树点集中一点的最短边权，或者是该点加入生成树点集中时的边权。
  
  于是我们将一个节点加入生成树点集中时，就要通过此点进行一次类似松弛的操作，更新该点出边的$d[]$值，最终答案就是所有点$d[]$值之和。
  
  然后网上很多代码都没有这种类似操作，我也不太懂他们的原理
  
  但是呢，在此题上运用上述算法的$Prim$会快100+ms,应该是更优的
  
  同时此题还要判断-1情况（即无法联通），我们只需判断非生成树点集集合大小
  与无法加入生成树点集集合大小是否相等(即$d[x]=INF$的点的个数)就可以了.
   
  代码： 耗时/内存 336ms, 46703KB
  
  有趣的是仅比$Kruskal$快了10ms左右
  
```cpp
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <vector>
#include <queue>
#define ri register int 
#define ll long long 
using namespace std;
const int maxn=2005;
const int inf=192681792;
int n,c;
int px[maxn],py[maxn];
struct Edge{
	int ne,to,dis;
}edge[19260817];
int h[maxn],num_edge=0;
struct Ele{
	int ver,dis;
	bool operator <(const Ele &b)const{
		return dis>b.dis;
	}
	Ele(int x,int y){ver=x,dis=y;}
};
inline void add_edge(int f,int t,int dis){
	edge[++num_edge].ne=h[f];
	edge[num_edge].to=t;
	edge[num_edge].dis=dis;
	h[f]=num_edge;
}
inline void prim(){
	priority_queue<Ele>a;
	int d[maxn],u,v,dis,cnt=0,ans=0,q=n-1;
	bool vis[maxn];
	for(ri i=1;i<=n;i++){d[i]=inf,vis[i]=0;}
	d[1]=0;
	while(a.size())a.pop();
    a.push(Ele(1,0));
	while(a.size()){
		u=a.top().ver,dis=a.top().dis,a.pop();
		while(vis[u]){
			u=a.top().ver,dis=a.top().dis,a.pop();
		}
		//ans+=dis,
		cnt++,vis[u]=1;
		//cout<<cnt<<endl;
		if(cnt==n-1)break;
		for(ri i=h[u];i;i=edge[i].ne){
			v=edge[i].to;
			if(!vis[v]&&d[v]>edge[i].dis){
				if(d[v]==inf)q--;
				d[v]=edge[i].dis;
				a.push(Ele(v,d[v]));
			}
		}
		if(q==n-cnt)break;
	}
	for(ri i=1;i<=n;i++)ans+=d[i];
	if(cnt==n-1)printf("%d\n",ans);
	else puts("-1");
	return ;
}
int main(){
	scanf("%d %d",&n,&c);
	for(ri i=1;i<=n;i++){
		scanf("%d %d",&px[i],&py[i]);
		for(ri j=1;j<i;j++){
			int d=(px[i]-px[j])*(px[i]-px[j])+(py[i]-py[j])*(py[i]-py[j]);
			if(d>=c){
				add_edge(i,j,d);
				add_edge(j,i,d);//edge[++tot].u=i,edge[tot].v=j,edge[tot].dis=d;
			}
		}
	}
	prim();
	return 0;
}
```
  
- $Prim+$手写堆

  其他一样，将POI改成了手写堆,同时我发现手写堆$Heap[]$若用结构体时用$swap()$会出现玄学错误
  
  代码：耗时/内存 424ms, 46867KB
  
  比POI还更慢，可见O2的力量
  
```cpp
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#define ri register int 
#define ll long long 
using namespace std;
const int maxn=2005;
const int inf=192681792;
int n,c;
int px[maxn],py[maxn];
struct Edge{
	int ne,to,dis;
}edge[19260817];
int h[maxn],num_edge=0;
struct Ele{
	int ver,dis;
	Ele(int x,int y){ver=x,dis=y;}
	Ele(){;}
};
struct S_Heap{
	int heap[1926817],ver[1926817];
	int n;
	inline void up(int k){
		int f=(k>>1);
		while(k>1){
			if(heap[k]<heap[f]){
				swap(heap[k],heap[f]);
				swap(ver[k],ver[f]);
				k=f,f=(k>>1);
			}
			else  break;
		}
		return ;
	}
	inline void push(int v,int di){
		ver[++n]=v;
		heap[n]=di;
		up(n);
	}
	inline void down(int fa){
		int s=(fa<<1);
		while(s<=n){
			if(s<n&&heap[s]>heap[s+1])s++;
			if(heap[s]<heap[fa]){
				swap(heap[s],heap[fa]);
				swap(ver[s],ver[fa]);
				fa=s,s=(fa<<1);
			}
			else break;
		}
		return ;
	}
	inline void pop(){
		heap[1]=heap[n];
		ver[1]=ver[n--];
		down(1);
		return ;
	}
};
inline void add_edge(int f,int t,int dis){
	edge[++num_edge].ne=h[f];
	edge[num_edge].to=t;
	edge[num_edge].dis=dis;
	h[f]=num_edge;
}
inline void prim(){
	S_Heap a;//priority_queue<Ele>a;
	int d[maxn],u,v,dis,cnt=0,ans=0,q=n-1;
	bool vis[maxn];
	for(ri i=1;i<=n;i++){d[i]=inf,vis[i]=0;}
	d[1]=0;
    a.push(1,0);
	while(a.n){
		u=a.ver[1],dis=a.heap[1],a.pop();
		while(vis[u]){
			u=a.ver[1],dis=a.heap[1],a.pop();
		}
		cnt++,vis[u]=1;
		if(cnt==n-1)break;
		for(ri i=h[u];i;i=edge[i].ne){
			v=edge[i].to;
			if(!vis[v]&&d[v]>edge[i].dis){
				if(d[v]==inf)q--;
				d[v]=edge[i].dis;
				a.push(v,d[v]);
			}
		}
		if(q==n-cnt)break;
	}
	for(ri i=1;i<=n;i++)ans+=d[i];
	if(cnt==n-1)printf("%d\n",ans);
	else puts("-1");
	return ;
}
int main(){
	scanf("%d %d",&n,&c);
	for(ri i=1;i<=n;i++){
		scanf("%d %d",&px[i],&py[i]);
		for(ri j=1;j<i;j++){
			int d=(px[i]-px[j])*(px[i]-px[j])+(py[i]-py[j])*(py[i]-py[j]);
			if(d>=c){
				add_edge(i,j,d);
				add_edge(j,i,d);//edge[++tot].u=i,edge[tot].v=j,edge[tot].dis=d;
			}
		}
	}
	prim();
	return 0;
}
```
  