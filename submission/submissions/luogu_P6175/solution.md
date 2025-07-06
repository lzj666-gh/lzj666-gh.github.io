# P6175 题解

无向图的最小环。

这里主要来讲一下利用Floyd求解的具体原理

要想用Floyd求解无向图最小环问题，我们首先要深入里了解Floyd每一步的意义。

~~虽然四层代码很好背~~

```cpp
for(int k=1;k<=n;k++){
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);
```
但是在这个过程发生了什么呢，为什么可以用来求最小环呢？

考虑一个图中的最小环 **/ u-v-k-u /**

如果我们随意去掉其中一条边 **/ u-v /**

那么剩下的 **/ v-k-u /** 一定是图中 **( u , v )** 间的最短路径

那么这怎么和Floyd算法联系呢？

我们知道，

$\color{red}\text{在Floyd算法枚举} k_i \text{的时候，已经得到了前 k-1 个点的最短路径}$

$\color{red}\text{这 k-1 个点不包括点 k，并且他们的最短路径中也不包括 k 点}$

那么我们便可以从这前 k-1 个点中选出两个点 **i , j** 来

因为 **/ i-j /** 已经是 **( i , j )** 间的最短路径，且这个路径不包含 **k** 点

##### **注解：这里 / i-j / 这样表达只是为了直观，实际中 ( i , j ) 间的最短路很可能不仅仅只有 / i-j / ，还有可能会有其他点，但是这条路径一定是 ( i , j ) 间的最短路**

所以连接 **/ i-j-k-i /** ，我们就得到了一个经过 **i , j , k** 的最小环

最后每次更新 ans 的最小值即可。

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
const int inf = 1e13;
int n,m,u,v,w,ans = inf;
int dis[128][128];
int mp[128][128];
signed main(void){
	cin>>n>>m;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			if(i!=j)dis[i][j]=mp[i][j]=inf;
	for(int i=1;i<=m;i++){
		cin>>u>>v>>w;
		dis[u][v]=min(dis[u][v],w);
		dis[v][u]=min(dis[v][u],w);
		mp[u][v]=min(mp[u][v],w);
		mp[v][u]=min(mp[v][u],w);
  		//判断重边，因为这个卡了我好几次，最后来瞅了眼题解才明白，囧
	}
	for(int k=1;k<=n;k++){
		for(int i=1;i<k;i++)
			for(int j=i+1;j<k;j++)
				ans = min(ans,dis[i][j]+mp[i][k]+mp[k][j]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++){
				dis[i][j] = min(dis[i][j],dis[i][k]+dis[k][j]);
				dis[j][i] = dis[i][j];
			}
		
	}
	if(ans==inf)cout<<"No solution.";
	else cout<<ans;
	return 0;
}
```
