# P1843 题解

标准的二分答案。

首先考虑暴力做法，即枚举最终答案ans，对于第一个可行的ans一定是最优解（在ans时间内可以烘干在ans+t(t>=0)的时间内也就一定可以烘干）由于N<=500000的数据范围绝对会TLE，因此需要优化。

接下来考虑优化，由于之前提到的性质，设f(i)表示在i时间内有无可能烘干，那么f数组必定满足**单调性**。那么我们可以二分最终答案ans，对于每一个ans对其进行暴力check：对于每一件衣服，如果它能在ans天内烘干（湿度<=ans*a），那么就不必使用烘干机，接下来处理必须使用烘干机的情况，当i号衣服不能被直接烘干时，我们需要用```((clothes[i]-a*mid)%b==0?(clothes[i]-a*mid)/b:(clothes[i]-a*mid)/b+1;)```次烘干机进行烘干（实际写代码的过程中我更推荐if-else），最后只需看烘干机使用总数是否小于等于mid即可。

下面给出参考代码：
```cpp
#include<iostream>
#define int long long
using namespace std;
int n,a,b,clothes[600006];
bool check(int mid)
{
	int tot=0;
	for(int i=1;i<=n;i++)
	{
		if(clothes[i]<=mid*a)continue;
		else 
		{
			
			if((clothes[i]-mid*a)%b==0)tot+=(clothes[i]-mid*a)/b;
			else tot+=((clothes[i]-mid*a)/b+1);
		}
	}
	return tot<=mid;
}
signed main()
{
	ios::sync_with_stdio(0);
	cin>>n>>a>>b;
	for(int i=1;i<=n;i++)cin>>clothes[i];
	int l=0,r=1e9,mid;
	while(l<=r)
	{
		mid=(l+r)/2;
		if(check(mid))r=mid-1;
		else l=mid+1;
	}
	cout<<l<<endl;
	return 0;
} 
```
喜欢我的题解别忘了点个赞哦~