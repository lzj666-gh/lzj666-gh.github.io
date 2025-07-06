# P1722 题解

### [题目传送门](https://www.luogu.org/problemnew/show/P1722)

题目貌似没说清楚，总的红色算筹个数必须与黑色算筹相等。

这一题因为n<=100,所以可以放心大胆地用二维DP

令dp[i][j]表示前i个算筹中放j个红色算筹的方案数

则可以得出dp[i][j]=dp[i-1][j]+dp[i-1][j-1]

**注意：j必须大于等于i/2上取整 **

不说了，下面是[本蒟蒻](https://www.luogu.org/space/show?uid=40985)的代码：
```cpp
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
int n,f[505][505];
int main(){
	scanf("%d",&n);
	f[1][1]=1;
	for (int i=2;i<=n+n;i++)
		for (int j=(i+1)>>1;j<=i;j++)
			f[i][j]=(f[i-1][j]+f[i-1][j-1])%100;
	printf("%d",f[n+n][n]);
	return 0;
}
```