# P4266 题解

[题目传送门](https://www.luogu.org/problem/P4266)

思路：这题就是一个贪心，先将每个休息站按照美味值从大到小排序，然后从头到尾扫一遍，能吃就一直吃到FJ追上来为止。

细节：要开long long！！！~~别问我是怎么知道的~~

代码：
```
#include <bits/stdc++.h>
using namespace std;
long long l,n,v1,v2,ans,a2;//v1为FJ的速度，v2为Bessie的速度，a2记录Bessie吃了多久的草
struct sb
{
	long long a,b;
}a[100001];
bool cmp(const sb &sb1,const sb &sb2)
{
	return sb1.b>sb2.b;
}
int main()
{
	scanf("%lld%lld%lld%lld",&l,&n,&v1,&v2);
	for(long long i=1;i<=n;i++)scanf("%lld%lld",&a[i].a,&a[i].b);
	sort(a+1,a+n+1,cmp);//排序（C++党的优越感）
	for(long long i=1;i<=n;i++)//从头往后扫
	{
		if(a[i].a*v2+a2<=a[i].a*v1)//如果Bessie到这块草地的时间加上她已经用来吃草的时间小于等于FJ到这块草地的时间
		{
			ans+=(a[i].a*v1-a[i].a*v2-a2)*a[i].b;//吃个痛快！
			a2=a[i].a*v1-a[i].a*v2;//将吃草的时间加上
		}
	}
	printf("%lld",ans);//输出
}
```
![](https://www.luogu.org/images/congratulation.png)