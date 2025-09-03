# P5322 题解

[$\text{My Blog}$](https://www.cnblogs.com/santiego/p/11184624.html)

比较好想的DP，设$dp[i][j]$表示第$i$个城堡时，已派出$j$个士兵。决策时，贪心派出恰好严格大于某一玩家派出的数量的两倍（不然浪费）。我们发现又可以排序预处理出$a[i][j]$表示第$i$个城堡，出兵数量第$j$大的人出兵数量（因为这样可以很容易算出贡献，即为$k\times i$）

dp转移方程即为：
$dp[j]=MAX(dp[j-a[i][k]*2-1]+k*i, dp[j]);$


*AC Code:*

```cpp
#include <cstdio>
#include <algorithm>
#define MAX(A,B) ((A)>(B)?(A):(B))
using namespace std;
int s,n,m,dp[20002],a[110][110],ans;
signed main(){
    scanf("%d %d %d", &s, &n, &m);
    for(int i=1;i<=s;++i)
        for(int j=1;j<=n;++j)
            scanf("%d", &a[j][i]);
    for(int i=1;i<=n;++i)
        sort(a[i]+1, a[i]+1+s);
    for(int i=1;i<=n;++i)
        for(int j=m;j>=0;--j) //倒序枚举已派出兵
            for(int k=1;k<=s;++k) //对s个玩家决策
                if(j>a[i][k]*2)
                    dp[j]=MAX(dp[j-a[i][k]*2-1]+k*i, dp[j]);
    for(int i=0;i<=m;++i) ans=MAX(ans, dp[i]);
    printf("%d\n", ans);
    return 0;
}
/*
 dp[i][j]第i个城堡时，已派出j个士兵
 a[i][j]第i个城堡，第j个人出的兵
 */
```