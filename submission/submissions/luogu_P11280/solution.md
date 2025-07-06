# P11280 题解

### 题意
Terry 和 Jom 一起在图上玩一个游戏，每次两人可以选择移动一条边或者不动，当 Terry 移动到 Jom 所在的点他就输了，当 Terry 移动到给定节点 $r$ 他就赢了。（当 Jom 先到 $r$ 节点 Jerry 后到也算 Jerry 输）给出一个有 $n$ 个节点 $m$ 条边的图和目标节点 $r$，$q$ 次询问，每次给出 Jerry 和 Jom 的出发节点 $a,b$，Jerry 先手，求胜者是谁。
### 思路
靠虑 Jom 的必胜策略，当他去追逐 Jerry 肯定是没用的，因为 Jerry 肯定是不会自投罗网的。所以 Jom 唯一的策略只有两种，一种是挡在 Jerry 前往 $r$ 的路径上睡大觉，另一种是在 $r$ 上睡大觉。对于第一种情况，当 Jom 能先 Jerry 到达路径上的某一点那么 Jom 也一定能先比 Jerry 到达 $r$。因此，第一种情况也能够化作第二种情况。
### 代码
从 $r$ 开始 bfs 求每个点距离 $r$ 的最短路径，然后在每个问题比一下 $dis_a,dis_b$ 的大小就行了。

由于是 Jerry 先手，比大小那里要取等。
```cpp
#include<bits/stdc++.h>
#define N 1000005
//#define int long long
using namespace std;
inline int rint(){
	int x;
	cin>>x;
	return x;
}
//int js[26];
int n,m,r;
vector<int>a[N];
int dis[N];
struct Node{
	int i,w;
};
queue<Node>q;
void bfs(int p,int w){
	dis[p]=w;
	for(auto it:a[p]){
		if(dis[it]==1e9){
			q.push({it,w+1});
			dis[it]=w+1; 
		}
	}
}
signed main(){
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	cout<<"I'm here!\n";
	n=rint(),m=rint(),r=rint();
	for(int i=1;i<=m;i++){
		int u,v;
		cin>>u>>v;
		a[u].push_back(v);
		a[v].push_back(u);
	}
	for(int i=1;i<=n;i++){
		dis[i]=1e9;
	}
	q.push({r,0});
	while(!q.empty()){
		bfs(q.front().i,q.front().w);
		q.pop(); 
	}
	int t=rint();
	while(t){
		--t;
		int s=rint(),t=rint();
		if(dis[s]<=dis[t]){
			cout<<"Terry\n";
		}
		else{
			cout<<"Jom\n";
		}
	}
	return 0;
} 
```
[AC 记录](https://www.luogu.com.cn/record/189103931)。