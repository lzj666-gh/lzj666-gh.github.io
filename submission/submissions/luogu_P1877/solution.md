# P1877 题解

到达型的01背包问题

f[i][j]:前i首歌曲能否达到音量j,f[i][j]=0不能达到,f[i][j]=1表示可以达到

音量调高表示取第i件物品，音量调低表示不取第i件物品

音量为背包容量，01背包模板题（调高调低带约束）

初始条件：f[0][beginlevel]=1,没演奏前可以到达beginlevel









```cpp
#include<bits/stdc++.h>
using namespace std;
int n,begin,maxlevel;
int ans;
int a[51];
int f[51][1001];
int main()
{
    scanf("%d%d%d",&n,&begin,&maxlevel);
    f[0][begin]=1;
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=1;i<=n;i++)
        for(int j=maxlevel;j>=0;j--)
        {
            if(j-a[i]>=0)
                f[i][j]=f[i][j]||f[i-1][j-a[i]];
            if(j+a[i]<=maxlevel)
                f[i][j]=f[i][j]||f[i-1][j+a[i]];
        }
    for(int i=maxlevel;i>=1;i--)
        if(f[n][i]==1)
        {
            printf("%d",i);
            return 0;
        }
    printf("-1");
    return 0;
}

```