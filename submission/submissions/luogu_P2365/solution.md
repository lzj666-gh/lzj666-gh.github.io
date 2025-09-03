# P2365 题解

看很多题解里面$O(n^2)$的dp状态都讲得不怎么清楚，我就再详细地讲解一下吧

我们定义：$dp[i][j]$为把前$i$个任务分成$j$组，所需要的最小费用

显然对于每一个i，都有两种情况：

**1.将i与i-1划分在同一组内**

**2.将i独立设为一组**

先看**第一种情况**：

此时第j个分组的左端点未知，所以我们可以枚举左端点

令第j个任务分组区间为$[l,i]$，则有：

$dp[i][j]=dp[l-1][j-1]+($第$j$个任务分组所需费用$)$

那么第j个任务分组所需费用怎么求呢？

因为此时为第j个任务分组，所以一定有j个启动时间(s)，此时完成第j个任务分组的时间节点为$j*s+sumt[i]$（这里$sumt[i]$为$t[1]+t[2]+…+t[i]$）,即前i个任务所需的总时间+j个准备时间

所以第j个任务所需费用为

$(j*s+sumt[i])*(sumf[i]-sumf[l-1])$

（$sumf[i]-sumf[l-1]$为区间$[l,i]$的费用系数和）

再来看**第二种情况**：

此时显而易见第j个任务分组区间为$[i,i]$，做法同上，只不过将上面的l换成了i，所以第j个任务所需费用为：

$(j*s+sumt[i])*(sumf[i]-sumf[i-1])$

两种情况的状态转移非常相似，所以对于第二种情况，我们只需设置l的上界为i即可完成转移。

故总的转移为：

$dp[i][j]=dp[l-1][j-1]+(j*s+sumt[i])*(sumf[i]-sumf[l-1])$$(1<=l<=i)$

代码如下：
```
#include <cstdio>
#include <cstring>
#include <iostream>
#define ll long long
using namespace std;
const int N=5011;
const int inf=0x7fffffff;
int n,s,t[N],f[N],sumt[N],sumf[N];//因为f[i],t[i]<=100,所以前缀和只需用int类型存储即可 
ll dp[N][N],ans;
int main(){
	scanf("%d%d",&n,&s);
	for(int i=1;i<=n;i++){
		scanf("%d%d",&t[i],&f[i]);
		sumt[i]=sumt[i-1]+t[i];
		sumf[i]=sumf[i-1]+f[i];
	}
	memset(dp,127,sizeof(dp));//赋最大值
	dp[0][0]=0; //初始化 
	ans=inf; 
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			for(int l=1;l<=i;l++){
				dp[i][j]=min(dp[i][j],dp[l-1][j-1]+(j*s+sumt[i])*(sumf[i]-sumf[l-1]));
			}
		}
	}
	for(int i=1;i<=n;i++){
		ans=min(ans,dp[n][i]);
	}//取最大值 
	printf("%lld\n",ans);
	return 0;
} 
```

时间复杂度$O(n^3)$,因为卡空间，所以期望得分0pts

把N改成可以过$O(n^3)$的400，期望得分50pts

我们考虑优化。

因为这题不限分成多少个组，所以j其实是多余的

我们回顾上面的状态转移方程，可以发现j在其中的作用仅仅是计算要加多少个启动时间而已。所以我们要想办法不通过j而计算出启动时间。

很抱歉，做不到。但是很显然，每多一个任务分组，后续任务的结束时间必定会延迟s秒。这会造成后续的费用多出$(sumf[n]-sumf[l-1])*s$,我们可以将其提前加在dp[i]里

所以，最终$dp[i]$表示（前i个任务分成若干组后的费用+分成若干组后多出的后续费用）的最小值

状态转移式为：

$dp[i]=min(dp[i],dp[l-1]+sumt[i]*(sumf[i]-sumf[l-1])+s*(sumf[n]-sumf[l-1]))(1<=l<=i)$

（[1,l-1]分为若干组的最小费用+[1,l-1]多出的后续费用+不算s的这个任务分组的费用+[l,i]多出的后续费用）

代码：
```
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int n,s,t[5001],f[5001];
int sumt[5001],sumf[5001];
long long dp[5001];
int main(){
	scanf("%d%d",&n,&s);
	for(int i=1;i<=n;i++){
		scanf("%d%d",&t[i],&f[i]);
		sumt[i]=sumt[i-1]+t[i];
		sumf[i]=sumf[i-1]+f[i];
	}
	memset(dp,127,sizeof(dp));
	dp[0]=0;
	for(int i=1;i<=n;i++){
		for(int l=1;l<=i;l++){
			dp[i]=min(dp[i],dp[l-1]+sumt[i]*(sumf[i]-sumf[l-1])+s*(sumf[n]-sumf[l-1]));
		}//前i个的最后一组为l~i 
	}
	printf("%lld\n",dp[n]);
	return 0;
}
```

时间复杂度$O(n^2)$,期望得分100pts