# P1164 题解

感觉DP实在白学了，因为我连自己敲的代码都不知道是用的DP还是递推。

开个玩笑，这是一道简单的动规题，定义f[i][j]为用前i道菜用光j元钱的办法总数，其状态转移方程如下：

（1）if(j==第i道菜的价格)f[i][j]=f[i-1][j]+1;

（2）if(j>第i道菜的价格) f[i][j]=f[i-1][j]+f[i-1][j-第i道菜的价格];

（3）if(j<第i道菜的价格) f[i][j]=f[i-1][j];

说的简单一些，这三个方程，每一个都是在吃与不吃之间抉择。若钱充足，办法总数就等于吃这道菜的办法数与不吃这道菜的办法数之和；若不充足，办法总数就只能承袭吃前i-1道菜的办法总数。依次递推，在最后，我们只要输出f[n][m]的值即可。

```cpp
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int a[101],f[101][10001]={0};
int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;++i)cin>>a[i];
    for(int i=1;i<=n;++i)
      for(int j=1;j<=m;++j)
      {
          if(j==a[i])f[i][j]=f[i-1][j]+1;
          if(j>a[i]) f[i][j]=f[i-1][j]+f[i-1][j-a[i]];
          if(j<a[i]) f[i][j]=f[i-1][j];
      }
    cout<<f[n][m];
    return 0;
}
```