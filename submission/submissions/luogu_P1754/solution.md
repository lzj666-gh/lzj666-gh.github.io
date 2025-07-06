# P1754 题解

我想发两篇，。。。强制自己学下卡特兰数。

本片考虑dp

dp的是后  dp【i】【j】表示后面还有i个50元j个100元的时候，的方案数

考虑在前一步的时候可以拿到50或100所以

dp[i][j]=dp[i-1][j]+dp[i][j-1];

下面是代码

    
        
```cpp
#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
long long n,m,dp[100][100];
int main()
{
cin>>n;
for(int i=1;i<=n;i++)
{
    dp[i][0]=1;
}
for(int i=1;i<=n;i++)
{
    for(int j=1;j<=i;j++)
    {
            dp[i][j]=dp[i-1][j]+dp[i][j-1];
    }
}
cout<<dp[n][n];
    return 0;
}

```