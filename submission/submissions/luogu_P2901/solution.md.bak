# P2901 题解

## $\color{green}{\text{Front Knowledge - A}^{*} \text{ algorithm}}$

`A* 算法`，就是启发式的 `BFS` 算法。它依赖于以下几个函数：

- $g$ 函数：即从开始到当前状态的花费。
- $g^*$ 函数：估计的从开始到当前状态的花费。由于 `BFS` 的特殊性，我们一定有 $g=g^*$。
- $h$ 函数：从当前状态到结束状态的**实际**花费。
- $h^*$ 函数：从当前状态到结束状态的**估计**花费。
- $f$ 函数：从起始状态到当前状态再到结束状态的总花费。即 $f=g+h$。
- $f^*$ 函数：从起始状态到当前状态再到结束状态的估计花费。即 $f^* = g^*+h^* = g +h^*$。

我们的 `A*算法` 就是根据 $f^*$ 从小到大来遍历搜索节点（因为它最有可能最优）。

为了保证正确性，我们要求 $h^* \leq h$。同时 $h^*$ 越大，`A*算法` 速度越快，所以 $h^*$ 函数的好坏决定了整个算法的好坏。

---------------------------------------------------------------

## $\color{green}{\text{K}^{\text{th}} \text{ Shortest Path}}$

顾名思义，就是求一张图的第 $K$ 短的路径。

考虑暴力，我们可以求出所有的可能路径，然后排序，取第 $K$ 小值即答案。但是，求所有可能路径的算法会 `TLE`。

考虑如何用 $\text{A}^{*}%$ 优化这个过程。我们先求出所有的点到终点的距离 $dis_i$，然后跑一遍 `A*` 算法。$d^{*}$ 函数就是当前状态（点）的 $dis$ 值，记从起点到当前点的花费为 $t$，故而 $f^{*} = d^{*} + g = dis + t$。

我们发现这个 $d^{*}$ 函数是相当优秀的。首先，它一定 $\leq d$，为什么？因为从一个点到终点的花费肯定 $\geq dis$（否则 $dis$ 就不是最短路径了呀）。其次，它足够优秀，足够大，是我们暂时能想到的，最好求，最大的 $d^{*}$ 函数了。

这么做还有一个好处，就是第 $u$ 次到达终点就是第 $u$ 短路。

```
1.求出所有的 dis (一遍SPFA/dijkstra) 搞定
2.把起点入队列
3.扩展 dis + t 最小的点
4.然后它是终点，则记录，如果求出 K 短路，再见
5.不断进行 3 直至出解
```

------------------------------------------------------------

## $\color{green}{\text{P2901\ \ \ \ \ [USACO08MAR]Cow Jogging G}}$

$\color{blue}{\text{【题意】：}}$ 输出一张 $n$ 个点，$m$ 条边，输出其 $K$ 短路，若无，就输出 `-1`。

$\color{blue}{\text{【思路】：}}$ `K 短路` 的模板题。

$\color{blue}{\text{【代码】：}}$
```cpp
typedef long long ll;int n,m,k;
const int N=1e3+100,M=1e6+100;
struct edge{int next,to;ll len;};
edge e[M],E[M];int h[N],H[N],tot,Tot;
inline void add(int a,int b,int c){
	e[++tot]=(edge){h[a],b,c};h[a]=tot;
}//链式前向星——正向图 
inline void Add(int a,int b,int c){
	E[++Tot]=(edge){H[a],b,c};H[a]=Tot;
}//链式前向星——反向图 
int dis[N];//点到终点的长度 
bool vis[N];//SPFA判重用数组 
inline void spfa_algorithm(){
	queue<int> q;q.push(1);
	memset(dis,127,sizeof(dis));
	memset(vis,true,sizeof(vis));
	vis[1]=false;dis[1]=0;
	while (q.size()){
		int u=q.front();q.pop();vis[u]=1;
		for(int i=H[u];i;i=E[i].next){
			register int to=E[i].to;
			if (dis[to]>dis[u]+E[i].len){
				dis[to]=dis[u]+E[i].len;//updata
				if (vis[to]){vis[to]=0;q.push(to);}
			}//单源最短路的松弛操作 
		}//特别注意，我们跑的是反向图 
	}
}
struct node{int pos;ll len;};
bool operator < (node a,node b){
	return a.len+dis[a.pos]>b.len+dis[b.pos];
}//特别注意，因为使用了STL的优先队列
 //所以这里的“小于”必须定义为“大于” 
int A_star_algorithm(int &ret){
	priority_queue<node> q;
	q.push((node){n,0});
	while (q.size()){
		node z=q.top();q.pop();
		if (z.pos==1){//又到终点了 
			printf("%lld\n",z.len);
			if ((--ret)==0) return 0;
		}
		register int u=z.pos,i;
		for(i=h[u];i;i=e[i].next){
			register int to=e[i].to;
			q.push((node){to,z.len+e[i].len});
		}
	}
	return ret;
}
int main(){
	n=read();m=read();k=read();
	for(int i=1,u,v,w;i<=m;i++){
		u=read();v=read();w=read();
		add(u,v,w);Add(v,u,w);
	}
	spfa_algorithm();
	A_star_algorithm(k);
	while (k--) printf("-1\n");
	return 0;
}



read() 函数就是快读函数（我写得丑，就不给大家了）
```

--------------------------------------

大家有空可以做做这题：[模板】k短路 / [SDOI2010]魔法猪学院](https://www.luogu.com.cn/problem/P2483)。它卡 `STL` 哦·！！！