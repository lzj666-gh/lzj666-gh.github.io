# P8733 题解

# P8733 [蓝桥杯 2020 国 C] 补给 题解
一道最短路加状压题。

首先，处理出每两个点 $i,j$ 之间的最短距离 $dis_{i,j}$。

然后，开始状压。

定义 $dp_{i,j}$ 为在状态为 $i$ 且停留在 $j$ 的最短距离。其中，状态 $i$ 在二进制下从后往前的第 $k$ 位表示第 $k$ 个点是否到达（$0$ 表示没到达，$1$ 表示到达了）。

初始：$dp_{1,0}=1$。

转移：$dp_{i,j} = \min dp_{i\oplus 2^j,k} + dis_{j,k}$（从状态 $i\oplus 2^j$ 来，答案为状态为 $i\oplus 2^j$ 且停留在 $k$ 的答案 $dp_{i\oplus 2^j,k}$ 加上从 $k$ 到 $j$ 的距离）。要求：$i\oplus 2^j$ 从后往前的第 $k$ 位不为 $0$。

答案：$\min\limits_{i=1}^{n-1}dp_{2^n-1,i}+dis_{i,0}$。

**注意：**

1. 别忘了最后得回去；

2. 最短路初始建边若边长大于 $D$，就不能建。

题外话：考场上最后几分钟才改成了状压的写法，没调出来（悲）。

代码：

```cpp
#include <bits/stdc++.h>
using namespace std ;
int n , d ;
double ans = DBL_MAX , x[25] , y[25] , dp[1 << 20][25] , dis[25][25] ;
bool vis[25] ;
double jl(int a , int b)
{
	return sqrt((x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b])) ;
}
int main()
{
	memset(dp , 0x7f , sizeof dp) ;
	memset(dis , 0x7f , sizeof dis) ;
	cin >> n >> d ;
	for(int i = 0 ; i < n ; i++)	cin >> x[i] >> y[i] ;
	for(int i = 0 ; i < n ; i++)	for(int j = 0 ; j < n ; j++)	if(jl(i , j) < d)	dis[i][j] = jl(i , j) ;
	for(int i = 0 ; i < n ; i++)
		for(int j = 0 ; j < n ; j++)
			for(int k = 0 ; k < n ; k++)
				dis[i][j] = min(dis[i][j] , dis[i][k] + dis[k][j]) ;
	dp[1][0] = 0 ;
	for(int i = 1 ; i < (1 << n) ; i++)
	{
		for(int j = 0 ; j < n ; j++)
		{
			if(!((i >> j) & 1))	continue ;
			int tmp = i ^ (1 << j) ;
			for(int k = 0 ; k < n ; k++)
			{
				if(!((tmp >> k) & 1))	continue ;
				dp[i][j] = min(dp[i][j] , dp[tmp][k] + dis[j][k]) ;
			}
		}
	}
	for(int i = 1 ; i < n ; i++)
		ans = min(ans , dp[(1 << n) - 1][i] + dis[i][0]) ;
	printf("%.2lf" , ans) ;
	return 0 ;
}
```