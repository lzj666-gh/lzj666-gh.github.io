# CF453A 题解

一道期望DP

如果投$n$次，最大点数是$k$，那么情况共有$k^n-(k-1)^n$种。

若$n$次投掷的点数都在$1$到$k$内，共有$k^n$种情况。

若$n$次投掷的点数都在$1$到$k-1$内，共有$(k-1)^n$种情况。

这两个数值相减即可得到最大值是$k$的情况。

所以我们的期望$ans=\frac{\sum_{i=1}^mi\times (i^n-(i-1)^n)}{m^n}=\sum_{i=1}^mi\times((\frac{i}{m})^n-(\frac{i-1}{m})^n).$


```
#include<cstdio>
#include<cmath>
using namespace std;
double n,m,ans;
int main(){
	scanf("%lf%lf",&m,&n);
	for(double i=1;i<=m;i++)
	ans+=i*(pow(i/m,n)-pow((i-1)/m,n));
	printf("%.12lf\n",ans);
}
```