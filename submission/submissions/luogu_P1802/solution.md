# P1802 题解

一个变形版的01背包。

dp[i]表示用i瓶药获得的最多经验。

**决策？**

当i>=use时，可以选择打败或者不打败

dp[i]=max(dp[i]+lose,dp[i-use]+win)。

当i<use时，无法战胜对方。

dp[i]+=lose

至于数据范围，最后输出时强制转换一下就行了。

    
    
```cpp
#include <cstdio>
#include <iostream>
using namespace std;
int dp[1100];
int win[1100],lose[1100],use[1100];
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
     scanf("%d%d%d",lose+i,win+i,use+i);
    for(int i=1;i<=n;i++)
     {
         for(int j=m;j>=use[i];j--)
          dp[j]=max(dp[j]+lose[i],dp[j-use[i]]+win[i]);
         for(int j=use[i]-1;j>=0;j--)
          dp[j]+=lose[i];
     }
     printf("%lld",5ll*dp[m]);
}
```