# P2296 题解

### 更新
- $2024.12.31$ 删除部分粗体。
- $2025.04.09$ 更新代码。

---
### 思路
如果我们知道哪些点满足**出边所指向的点都直接或间接与终点连通**，那么这道题就变成了最简单的 bfs 单源最短路。  
所以我们先预处理出哪些点满足出边所指向的点都直接或间接与终点连通，再进行 bfs 单源最短路。  
想要求出哪些点满足出边所指向的点都直接或间接与终点连通，就得先求出哪些点直接或间接与终点连通。可以建反图，然后从终点开始 dfs 遍历所有和他连通的点。  
在遍历反图的过程中，遍历到一个点就删掉一个点，如果某个点的入度从因为删点变成了 $0$，就说明他满足出边所指向的点都直接或间接与终点连通。  

一共进行了 dfs 和 bfs 两次遍历，时间复杂度为 $O(n+m)$。  

---
### 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
int n,m;
int s,t;
vector<int>edg[10003],fedg[10003];
int out[10003];
bool vis[10003],f[10003];
int dis[10003];
queue<int>q;

void col(int p){
	if(vis[p])return;
	vis[p]=1;
	for(int i=0;i<fedg[p].size();i++){
		int to=fedg[p][i];
		out[to]--;
		if(!out[to])f[to]=1;
		col(to);
	}
}

int main(){
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++){
		int u,v; scanf("%d%d",&u,&v);
		edg[u].push_back(v);
		fedg[v].push_back(u);
		out[u]++;
	}
	scanf("%d%d",&s,&t);
	col(t);
	f[t]=1;
    if(!f[s]){
        cout<<-1;
        return 0;
    }
	memset(dis,0x3f,sizeof(dis));
	q.push(s);
	dis[s]=0;
	while(!q.empty()){
		int x=q.front();
		q.pop();
		for(int i=0;i<edg[x].size();i++){
			int to=edg[x][i];
			if(!f[to])continue;
			if(dis[to]>dis[x]+1){
				q.push(to);
				dis[to]=dis[x]+1;
			}
		}
	}
	if(dis[t]<=1e4)cout<<dis[t];
	else cout<<-1;
	return 0;
}
```