# P1658 题解

思路：贪心

将面值从小到大排序

考虑用前$i$种面值可以凑出的最大价值

显然当且仅当$a_1\neq 1$时是无解的，因为凑不出$1$

这样就限定了$a_1=1$

假设已经凑出了$1$~$s$的面值，那么我们可以加入一张面值不超过$s+1$的硬币

如果超过$s+1$，那么就不可以凑出$s+1$面值

设这个面值是$a$，那么可以把$s$延伸到$s+a$

显然这个面值越大越好

所以就直接找出$a\leq s+1$的最大的$a$,然后把$s$更新为$s+a$,同时$ans++$即可

版本1如下

```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,x,a[2000],ans;
int getin()
{
	int x=0;char ch=getchar();
	while(ch<'0'||ch>'9')ch=getchar();
	while(ch>='0'&&ch<='9')x=x*10+ch-48,ch=getchar();
	return x;
}
int main()
{
	x=getin(),n=getin();
	for(int i=1;i<=n;i++)a[i]=getin();
	sort(a+1,a+n+1);
	if(a[1]!=1){cout<<-1;return 0;}
	int sum=0;
	while(sum<x)
	{
		int i;
		for(i=n;i>=1;i--)if(a[i]<=sum+1)break;
		ans++,sum+=a[i];
	}
	cout<<ans<<endl;
}
```
复杂度$O(nm)$，但是实际上一般跑不到这个上界

这样的效率对于这道题已经绰绰有余了，但是我们还是要想办法优化

注意到$a_i$单调递增，所以可以用一个二分来找出最大值

复杂度$O(mlogn)$的版本2
```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,x,a[2000],ans;
int getin()
{
	int x=0;char ch=getchar();
	while(ch<'0'||ch>'9')ch=getchar();
	while(ch>='0'&&ch<='9')x=x*10+ch-48,ch=getchar();
	return x;
}
int find(int x)
{
	int l=1,r=n,mid;
	while(l<r)
	{
		mid=(l+r+1)>>1;
		if(a[mid]<=x)l=mid;
		else r=mid-1;
	}
	return l;
}
int main()
{
	x=getin(),n=getin();
	for(int i=1;i<=n;i++)a[i]=getin();
	sort(a+1,a+n+1);
	if(a[1]!=1){cout<<-1;return 0;}
	int sum=0;
	while(sum<x)
	{
		int i=find(sum+1);
		ans++,sum+=a[i];
	}
	cout<<ans<<endl;
}
```
退回到版本1，注意到一个值可能会被重复累加，可不可以快速地找出累加次数呢？

显然是可以的

当$a_{i+1}\leq s+ka_i+1$时$a_i$就会被$a_{i+1}$代替

令$k$最小可以解出$k=\lceil\frac{a_{i+1}-s-1}{a_i}\rceil$

于是这样每次都可以使下标$i+1$，所以复杂度$O(n^2)$

和版本2结合可以得到一个复杂度$O(n\log n)$的做法

版本3
```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,x,a[2000],ans;
int getin()
{
	int x=0;char ch=getchar();
	while(ch<'0'||ch>'9')ch=getchar();
	while(ch>='0'&&ch<='9')x=x*10+ch-48,ch=getchar();
	return x;
}
int find(int x)
{
	int l=1,r=n,mid;
	while(l<r)
	{
		mid=(l+r+1)>>1;
		if(a[mid]<=x)l=mid;
		else r=mid-1;
	}
	return l;
}
int main()
{
	x=getin(),n=getin();
	for(int i=1;i<=n;i++)a[i]=getin();
	a[n+1]=1e9;//注意这里要赋一个极大值避免出现问题
	sort(a+1,a+n+1);
	if(a[1]!=1){cout<<-1;return 0;}
	int sum=0;
	while(sum<x)
	{
		int i=find(sum+1);
		int k=ceil((double)(min(x,a[i+1])-sum-1)/a[i]);//要和s取min
		ans+=k,sum+=a[i]*k;
	}
	cout<<ans<<endl;
}
```
版本4其实已经不难想到了

我们每次选取的i都是递增的，那么直接记录上次选取的i，复杂度$O(n)$

版本4
```cpp
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,x,a[2000],ans;
int getin()
{
	int x=0;char ch=getchar();
	while(ch<'0'||ch>'9')ch=getchar();
	while(ch>='0'&&ch<='9')x=x*10+ch-48,ch=getchar();
	return x;
}
int main()
{
	x=getin(),n=getin();
	for(int i=1;i<=n;i++)a[i]=getin();
	a[n+1]=1e9;
	sort(a+1,a+n+1);
	if(a[1]!=1){cout<<-1;return 0;}
	int sum=0,i=0;
	while(sum<x)
	{
		while(a[i+1]<=sum+1)i++;
		int k=ceil((double)(min(x,a[i+1])-sum-1)/a[i]);
		ans+=k,sum+=a[i]*k;
	}
	cout<<ans<<endl;
}
```
PS:可能正常人都是直接跳到版本4的只有我这种蒟蒻才会想这么多