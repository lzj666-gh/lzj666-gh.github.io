# CF10D 题解

对于这类问题我们通常有两种转移方式，一种是以i结尾的数列，另一种是前i个数中选择一些组成的数列。
 
此题中我们选用a数组前i个元素，b数组以j结尾来转移，空间为O(n^2)，时间为O(n^3).

再来说方案：维护一个LICS[i][]，代表以j结尾的LICS方案，每更新一次答案，则将方案也迁移过来。这将额外带来一个O(n)的复杂度，但是对于本题来说足够了，而且转移也相当简明直白。

Code：

```
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define maxn 505
using namespace std;
int n,m,a[maxn],b[maxn],f[maxn][maxn],lics[maxn][maxn],tot[maxn];
int ans,pos;
int main()
{
    ios::sync_with_stdio(false);
    cin>>n;
    for(int i=1;i<=n;++i)cin>>a[i];
    cin>>m;
    for(int i=1;i<=m;++i)cin>>b[i];
    f[0][0]=0;
    for(int i=1;i<=n;++i)
        for(int j=1;j<=m;++j)
        {
            if(a[i]!=b[j])f[i][j]=f[i-1][j];
            else {
                f[i][j]=1;tot[j]=1;
                for(int k=1;k<j;++k){
                    if(b[k]<b[j])
                    {
                        if(f[i-1][k]+1>f[i][j]){
                            f[i][j]=f[i-1][k]+1;
                            tot[j]=tot[k]+1;
                            for(int p=1;p<=tot[k];++p)lics[j][p]=lics[k][p];
                        }
                    }
                }
                lics[j][tot[j]]=b[j];
            }
        }
    for(int i=1;i<=m;++i){
        if(f[n][i]>ans)ans=f[n][i],pos=i;
    }
    printf("%d\n",ans);
    for(int i=1;i<=tot[pos];++i)printf("%d ",lics[pos][i]);
    return 0;
}
```