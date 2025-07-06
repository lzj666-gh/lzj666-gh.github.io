# P1855 题解

####其实这道题很简单的呀(题解 By Plue Jheng/InfoEoR)

在完成这道题之前,首先要保证:

- 1.了解并熟练掌握 0/1背包问题.

- 2.对多维动规/多维背包问题有一定了解

- 3.会C/C++/Pascal/中文

那就很简单那!

```cpp
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,M,T,dp[1010][1010];
int m[1010],t[1010];
int main()
{
    scanf("%d%d%d",&n,&M,&T);
    for(int i=1;i<=n;i++)
    {
        //仅仅只是多了一维而已 
        scanf("%d%d",&m[i],&t[i]);
        for(int j=M;j>=m[i];j--)
        for(int k=T;k>=t[i];k--)
        {
            dp[j][k]=max(dp[j][k],dp[j-m[i]][k-t[i]]+1);
        }
    }
    printf("%d\n",dp[M][T]);
}
```