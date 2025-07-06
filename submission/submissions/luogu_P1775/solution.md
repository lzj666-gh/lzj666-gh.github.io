# P1775 题解

令```dp[i][j]```表示区间```[i,j]```的最小价值。

不妨从终点考虑问题，即结果为两个子区间合并的最小值再加上合并需要的代价即可。

枚举两个子区间，即枚举这个区间的中间点k，使这个区间被分为```[i,k]```和```[k+1,j]```两个区间，取一遍最小值加上合并的即为当前区间所求。

至于合并的代价，用前缀和即可。

所以```dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+sum[j]-sum[i-1])```

```cpp
#include<bits/stdc++.h>
using namespace std;
int dp[310][310],len,a[310],n,sum[310];
int main()
{
	cin>>n;
	memset(dp,0x3f,sizeof(dp));//初始化1，因为是求最小代价，所以初始化设为很大的一个数，为了后面更新。
	for(int i=1;i<=n;i++)
	{
		cin>>a[i];
		sum[i]=sum[i-1]+a[i];
		dp[i][i]=0;//初始化2，他自己本身的代价为0。
	}
	for(int len=2;len<=n;len++)
	{
		for(int i=1;i<=n-len+1;i++)
		{
			int j=i+len-1;
			for(int k=i;k<j;k++)
			{
				dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+sum[j]-sum[i-1]);
			}
		}
	}
	cout<<dp[1][n];
}
```