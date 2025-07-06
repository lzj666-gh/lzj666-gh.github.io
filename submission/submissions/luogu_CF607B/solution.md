# CF607B 题解

区间dp

其它的题解做法比较玄学 ~~至少我是没有看懂~~，或者是用递归实现转移的 ~~于是我决定发篇题解~~

------------

题意：从一个序列中每次取出一个回文串，求最少取几次（取出后两端外的数会相接）

------------

设$dp[i][j]$为在$[i,j]$的闭区间内最少的花费

显然
$\begin{cases}dp[i][i]=1\\dp[i][i+1]=1\quad (a[i]=a[i+1])\\dp[i][i+1]=2\quad (a[i]\ne a[i+1])\end{cases}$

~~原因请读者自行脑补~~

于是可以推出转移方程：

$\begin{cases}dp[i][j]=dp[i+1][j-1]\quad (a[i]=a[j])\\\\dp[i][j]=min_{k=i}^{j-1}dp[i][k]+dp[k+1][j]\end{cases}$

然后就可以愉快的dp辣

```cpp
#include<bits/stdc++.h>
using namespace std;
const int N=505;
const int inf=233333333;

int n,a[N],dp[N][N];

int main()
{
	scanf("%d",&n);
	for (int i=1;i<=n;i++) scanf("%d",&a[i]);
	for (int i=1;i<=n;i++)
	for (int j=1;j<=n;j++) dp[i][j]=inf;  //开始全赋inf，否则转移取min时就会挂掉
	for (int i=1;i<=n;i++) dp[i][i]=1;  //直接取一个数，花费一个代价
	for (int i=1;i<n;i++) dp[i][i+1]=1+(a[i]!=a[i+1]);  //取两个数的情况，如果相等取一次就好了，否则取两次
	for (int i=3;i<=n;i++)  //注意转移时需要先枚举区间长度
	for (int j=1;i+j-1<=n;j++)
	{
		int l=j,r=i+j-1;  //计算区间左右端点
		if (a[l]==a[r]) dp[l][r]=dp[l+1][r-1];
		for (int k=l;k<r;k++) dp[l][r]=min(dp[l][r],dp[l][k]+dp[k+1][r]);  //转移
	}
	printf("%d",dp[1][n]);

	return 0;
}
```