# P9618 题解

建议评绿/蓝。

分析：

一看就是很明显的最短路问题。

观察到讯问中的 $c ≤ 20$，所以可以用 $O(qc)$ 的复杂度处理询问。

设 $dp_i,_j$ 表示到第 $i$ 个点，换乘了 $j$ 次的最短路径长度，于是答案就成为了所有 $a \times dp_n,_i + b \times i$ 的最小值。

由于有换乘，可以想到分层图。

由于 $m$ 可能会很大，所以不可能对一条地铁线路建一层。

建一个不到 $20$ 层的分层图，因为如果换乘次数超过 $20$ 的话询问不会考虑到。

用分层图跑一下最短路即可。为了节省内存，我们对 $n$ 个节点都建了一个虚点处理换乘。详细做法见代码。

code：
```cpp
#include<bits/stdc++.h>
using namespace std;

const int maxn=4e5+10;//注意数组范围，最大为sigma(ki)+n，即4e5 
int a[maxn];//输入顺序的第i个点的实际点为a[i] 
int tot=0;

struct edge{//边，to表示到哪个点，tran表示是否换乘，d表示边的长度 
	int to;
	int tran;
	int d;
};

vector<edge> G[maxn];//图 
int dist[maxn];
vector<int> belong[maxn];//输入顺序的第i个点的真实点 
int n,m,q;

struct point{//点，用于dijkstra算法。 
	int u;//节点编号 
	int tran;//换乘了几次 
	int d;//距离 
	
	bool operator <(const point &cmp) const{//重载运算符 
		return d>cmp.d;
	}
};

int dp[maxn][25];

void dij(){//dijkstra 
	priority_queue<point> q;
	while (!q.empty()) q.pop();
	
	for (int i=1;i<=4e5;i++){
		for (int j=0;j<25;j++) dp[i][j]=1e9+7;//初始化成极大值 
	}
	
	//将编号为1的点放入优先队列 
	for (int i=1;i<=tot;i++){
		if (a[i]==1){//a[i]的定义见主函数。 
			q.push((point){i,0,0});
			dp[i][0]=0;
		}
	}
	
	while (!q.empty()){
		point f=q.top(); q.pop();
		int u=f.u,tran=f.tran,d=f.d;
		
		if (d>dp[u][tran]) continue;//减少很多无用的松弛 
		
		for (int i=0;i<(int)G[u].size();i++){
			int v=G[u][i].to;
			if (tran+G[u][i].tran>21) continue;//特判，如果超过20则无意义 
			
			if (dp[v][tran+G[u][i].tran]>dp[u][tran]+G[u][i].d){//松弛 
				dp[v][tran+G[u][i].tran]=dp[u][tran]+G[u][i].d;
				q.push((point){v,tran+G[u][i].tran,dp[v][tran+G[u][i].tran]});
			}
		}
	}
}
int main(){
	scanf("%d%d%d",&n,&m,&q);
	 
	
	for (int i=1;i<=m;i++){
		int cnt;
		scanf("%d",&cnt);
		if (cnt==1){//如果地铁线路长度为1，则这条地铁没有意义 
			int unu; scanf("%d",&unu); continue;
		}
		
		int u;
		scanf("%d",&u);
		a[++tot]=u;//输入的第tot个点，真实点为u 
		belong[u].push_back(tot);
		cnt--;
		
		
		while (cnt--){//前面一个点向后面的点连边 
			int now;
			scanf("%d",&now);
			a[++tot]=now;
			belong[now].push_back(tot);//输入的第tot个点，真实点为now 
			G[tot-1].push_back((edge){tot,0,1});//路程为1，不需要换乘 
			
		}
	}
	
	for (int i=1;i<=n;i++){
		int to=i+tot;//虚点 
		for (int j=0;j<(int)belong[i].size();j++){
			int u=belong[i][j];
			G[u].push_back((edge){to,0,0});
			G[to].push_back((edge){u,1,0});
			//如果a[x]=a[y]，那么这两条单向边保证了从x到y需要换乘1次，距离为0 
		}
	}
	
	dij();
	for (int i=0;i<=30;i++) dist[i]=1e9+7;//dist[i]为到n点换乘i次的最短路径长度，初始化为极大值 
	for (int i=0;i<(int)belong[n].size();i++){
		int u=belong[n][i];
		
		for (int j=0;j<=20;j++) dist[j]=min(dist[j],dp[u][j]);//更新到n点换乘j次的最短距离 
	}
	
	while (q--){
		int k1,k2,c;
		scanf("%d%d%d",&k1,&k2,&c);
		long long ans=1e12;
		for (int i=0;i<=c;i++){//枚举换乘几次 
	//		printf("%d %d\n",dist[i],i);
			ans=min(ans,1ll*k1*dist[i]+1ll*k2*i);
		}
		printf("%lld\n",ans);
	}
	return 0;
} 
```
开 O2 就能过了。