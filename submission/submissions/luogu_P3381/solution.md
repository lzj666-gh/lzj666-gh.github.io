# P3381 题解

发了网络流，再来一发费用流

能做费用流的，网络流自然做得来，但在这还是~~不要脸的~~安利一下自己的博客（里面也有网络流的题解）：

[点我](https://www.luogu.org/blog/71403/)

扯远了...

费用流，就是在不炸水管的情况下求源点到汇点的最小费用。

有没有想起什么？

思考一下......

对，最短路径！

所以我们完全可以用已死的SPFA求出不炸水管的最短路径（当然，实在有心理阴影的可以用dijkstra）。

如果你最短路径都不会，还是去 [这儿](https://www.luogu.org/problemnew/show/P3371)
和 [这儿](https://www.luogu.org/problemnew/show/P4779)

然后再一把增广路求出最大流与最小费用就好了（我觉得很OK）

献上本蒟蒻的代码：

```cpp
#include<cstdio>
#define maxn 5050
#define maxm 50005
#define INF 0x3f3f3f3f
inline int read(){
	int r=0,f=1;
	char c=getchar();
	while(c<'0'||c>'9'){if(c=='-')f=-1;c=getchar();}
	while(c>='0'&&c<='9'){r=(r<<3)+(r<<1)+c-'0';c=getchar();}
	return r*f;
}
int s,t,n,m,head[maxn],pre[maxn],dis[maxn],q[maxn];
bool vis[maxn];
int s_e;
struct E{
	int v,c,w,nxt;
}e[maxm*2];
struct Max_fei{//本人喜欢结构体
	inline void a_e(int u,int v,int c,int w){
		e[s_e]=(E){v,c,w,head[u]};
		head[u]=s_e++;
	}
	inline void add(int u,int v,int c,int w){
		a_e(u,v,c,w);
		a_e(v,u,0,-w);
	}
	inline bool spfa(){
		for(int i=1;i<=n;i++){
			dis[i]=INF;
			vis[i]=false;
		}
		dis[s]=0;
		vis[s]=true;
		q[0]=s;
		int hd=0,tl=1;
		while(hd^tl){
			int u=q[hd++];//循环队列
			hd%=maxn;
			for(int i=head[u];i!=-1;i=e[i].nxt){
				int v=e[i].v;
				if(dis[v]>dis[u]+e[i].w&&e[i].c){//判断水管还能运水吗
					dis[v]=dis[u]+e[i].w;//更新
					pre[v]=i;//记录位置
					if(vis[v])continue;//如果在队里，那就不进队
					vis[v]=true;
					q[tl++]=v;
					tl%=maxn;
				}
			}
			vis[u]=false;
		}
		if(dis[t]==INF)return false;
		return true;
	}
	inline int min(int a,int b){//原谅我的手写min
		return a<b?a:b;
	}
	inline int end(int &flow){//flow求最大流
		int p,u,Min=1e9,ans=0;
		for(u=t;u!=s;u=e[p^1].v){//因为开始值为0，可以用xor来找反边
			p=pre[u];//往前找
			Min=min(Min,e[p].c);//找全部经过水管都能流过的最大流
            
		}
		for(u=t;u!=s;u=e[p^1].v){
			p=pre[u];
			e[p].c-=Min;
			e[p^1].c+=Min;
			ans+=e[p].w*Min;//加费用
		}
		flow+=Min;//加最大流
		return ans;
	}
	inline int solve(int &flow){
		int ans=0;
		while(spfa()){
			ans+=end(flow);
		}
		return ans;
	}
}Flow;
inline void work(){
	n=read();m=read();
	s=read();t=read();
	for(int i=1;i<=n;i++)head[i]=-1;//初始值为-1，方便xor
	for(int i=1;i<=m;i++){
		int u=read(),v=read(),c=read(),w=read();
		Flow.add(u,v,c,w);
	}
	int flow=0;
	int ans=Flow.solve(flow);
	printf("%d %d\n",flow,ans);
}
int main(){
	work();
	return 0;
}
```
到此结束~~（偷偷撒花）~~