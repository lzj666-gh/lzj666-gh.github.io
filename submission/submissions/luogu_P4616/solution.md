# P4616 题解

### PS.
看了一下题解区，发现大多数题解都用树剖做的，但是我感觉根本不用树剖啊。。。用LCA就够了。  
此题其实没有紫色的qwq，个人感觉蓝~绿差不多了。

### Problem.
有$n$座城市。  
有$m$个时刻，在第$i$个时刻，所有$m-i+1$的倍数之间连边。  
有$q$个询问，询问第$x_i$座城市和$y_i$座城市什么时候联通。  

### Solution.
感觉这题根本不用树剖，而且一般dfs也就能搞定了。  
但是看题解区，基本上全都用树剖的。  
所以贡献一发LCA的题解。  

首先我们可以考虑如何把这棵树建出来。  
每一个时刻，**显然**可以直接考虑第$m-i+1$座城市和所有$m-i+1$的倍数连边。  
这两张图是等价的。（在只需要判断联通性的情况下  
那么就可以直接这样暴力枚举，然后用一个并查集记录两个点是否在同一个集合里。  
暴力枚举的复杂度是$\frac{N}{1}+\frac{N}{2}+...+\frac{N}{N}$的，所以复杂度是$O(N\times log_N)$的

这棵树建出来了，我们可以给这棵树附上权值。  
每条边的边权就是当前的时刻，从小到大加边。  
然后直接查两个点之间的路径上的瓶颈就好了。  
这个贪心**显然**是对的，笔者不证。  

然后，这棵树**显然**是一棵无根数。  
那么如何转化成一个有根数呢？  
方法很简单，直接钦定1为根就好了。  

然后这棵树建出来之后，接下来也没有修改操作。  
我就很想不通为什么楼上楼下都要用树剖做。  
这不是很**显然**一个lca的问题吗，真是令人谔谔。  
我相信，想来做这题的应该都会ST表求LCA了吧。  
笔者在这里也就不赘述方法了，如果不懂可以看代码注释。  

笔者不才，倍增用的st表，压行在这一行代码中也没有很体现。  
完结撒花，无耻求赞。  

### Coding.
```cpp
#include<bits/stdc++.h>
using namespace std;
struct edge{int to,wei,nxt;}e[200005];//边的结构体
int n,m,q,tot,head[100005],fa[100005],dep[100005],f[100005][35],dis[100005][35];
inline int getf(int x) {return fa[x]==x?x:fa[x]=getf(fa[x]);}//并查集找父亲
inline void adde(int x,int y,int w) {e[++tot]=(edge){y,w,head[x]},head[x]=tot;}//加边
inline void ready() {for(int i=m;i>=1;i--) for(int j=i+i,u=getf(i),v=getf(j);j<=n;j+=i,u=getf(i),v=getf(j)) if(u!=v) fa[u]=v,adde(i,j,m-i+1),adde(j,i,m-i+1);}//建树，直接暴力枚举
inline void dfs(int x,int fa=0,int val=0)
{//求出倍增数组，由于这题是边权，所以还需要一个val表示之前的边。
	f[x][0]=fa,dis[x][0]=val,dep[x]=dep[fa]+1;//f是father，dis是向上跳的最小值，dep是深度
	for(int i=1;(1<<i)<=dep[x];i++) f[x][i]=f[f[x][i-1]][i-1],dis[x][i]=max(dis[x][i-1],dis[f[x][i-1]][i-1]);//倍增处理
	for(int i=head[x];i;i=e[i].nxt) if(e[i].to!=fa) dfs(e[i].to,x,e[i].wei);//继续dfs
}
inline int lca(int x,int y)
{//求x到y的距离，lca模板
	int ans=0;if(dep[x]<dep[y]) swap(x,y);
	for(int i=25;i>=0;i--) if(dep[x]-(1<<i)>=dep[y]) ans=max(ans,dis[x][i]),x=f[x][i];
	if(x==y) return ans;
	for(int i=25;i>=0;i--) if(f[x][i]!=f[y][i]) ans=max(ans,max(dis[x][i],dis[y][i])),x=f[x][i],y=f[y][i];
	return max(ans,max(dis[x][0],dis[y][0]));
}
int main()
{
	for(int i=1;i<=100000;i++) fa[i]=i;//并查集初始化
	scanf("%d%d%d",&n,&m,&q),dep[0]=0,memset(dis,0x3f,sizeof(dis)),ready(),dfs(1);//一大堆初始化
	for(int x,y;q--;) scanf("%d%d",&x,&y),printf("%d\n",lca(x,y));//处理询问
	return 0;//完结撒花
}
```