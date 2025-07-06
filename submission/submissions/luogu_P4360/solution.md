# P4360 题解

~~这个题就是个简单的斜率优化DP的入门题~~  

我们先写出朴素的DP方程式：

$dp[i]=totsum-dis[j]*sum[j]-dis[i]*(sum[i]-sum[j])(j<i)$

其中$dp[i]$表示当前第二个工厂修到第$i$棵树的位置时的最小花费，$totsum$表示所有树一开始全部运送的山脚下的花费，$dis[i]$表示距离的后缀和(因为我们是从上运到下面)，$sum[i]$表示树的重量的前缀和。那么在$i,j$处修了工厂后花费就变成了总花费$totsum$减去从$j$厂运到山脚的额外花费$dis[j]*sum[j]$，再减去从$i$厂运到山脚下的额外花费$dis[i]*(sum[i]-sum[j])$。

形象的说，就是你先把$j$前面的木材运到$j$厂，然后减去这些木材运到山脚的花费，再把$i,j$之间的木材运到$i$厂，再减去它们到山脚的花费。

然后我们将DP方程式变形,令$j,k(j<k)$这两种决策转移到$i$的时候，$k$决策更优秀，那么就可以得到$totsum-dis[j]*sum[j]-dis[i]*(sum[i]-sum[j])>totsum-dis[k]*sum[k]-dis[i]*(sum[i]-sum[k])$

整理后可以得出：$\frac{dis[j]*sum[j]-dis[k]*sum[k]}{sum[j]-sum[k]}>dis[i]$

然后因为斜率$dis[i]$是随着$i$的增加而变小的，所以我们根据斜率维护一个上凸壳，因为是单调的，所以用一个队列就可以了。

丑陋代码新鲜出炉~~~

代码中的sum就是totsum，s[i]就是sum[i],d[i]就是dis[i].

```cpp

#include<cstdio>
#include<cstring>
#include<algorithm>
#define db double
using namespace std;
const int M=3e4+1;
int n;
int q[M],fi,la,ans=2e9+1;
int sum,s[M],d[M],w[M];
db calc(int j,int k){return 1.0*(d[j]*s[j]-d[k]*s[k])/(s[j]-s[k]);}
int count(int i,int j){return sum-d[j]*s[j]-d[i]*(s[i]-s[j]);}
int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++){scanf("%d%d",&w[i],&d[i]);}
    for(int i=n;i>=1;i--) d[i]+=d[i+1];
    for(int i=1;i<=n;i++) s[i]=s[i-1]+w[i],sum+=d[i]*w[i];
    for(int i=1;i<=n;i++){
        while(fi<la&&calc(q[fi],q[fi+1])>d[i]) ++fi;
        ans=min(ans,count(i,q[fi]));
        while(fi<la&&calc(q[la-1],q[la])<calc(q[la],i)) --la;
        q[++la]=i;
    }
    printf("%d\n",ans);
    return 0;
}
```