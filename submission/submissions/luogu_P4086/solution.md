# P4086 题解

此题，$emmmm...$

其实简化一下题目，就是在从$a_{k+1}$到$a_n$里找一个最小值，并把它去掉，再算剩下的几个数的平均值，求是这个平均值最大的$k$

那么，其实就是$3$部分：最小值、平均数、求平均数最大值。

一个一个看：

### $1.$

最小值的朴素解法是什么？$O(n)$扫一遍啊

但是我们还要遍历一次$k$从$1$到$n$，而且如果求平均值也是$O(n)$的话，总的来说就是$O(n^3)$了，绝对爆炸。

想一想，我们不用每次都求最小值啊，一开始就预处理掉不就好了，反正是静态的

于是就有了这份代码：

```
for(int i=n;i>=2;i--)mn[i]=min(mn[i+1],a[i]);
```
就这么一行？

对，就这么一行。

这样，我们就能$O(1)$求最小值啦~~

### $2.$

平均值。。。

要求平均值，就要知道一个区间的和

和最小值一样，朴素的方法是$O(n)$的

但是我们还要遍历一次$k$从$1$到$n$，总的来说又是$O(n^2)$了，还是炸了。

但是我们有什么？前缀和啊！

而且这里还不用前缀和，只要倒着一个一个加，还能合并到上面最小值代码里

于是就是这样了：

```
for(int i=n;i>=2;i--)mn[i]=min(mn[i+1],a[i]),sum[i]=sum[i+1]+a[i];
```
就这么一行？

对，还是就这么一行。

于是，$O(1)$求平均值也$OK$啦~~

### $2.5:$

其实平均数也能与处理啊，就是

```
(sum[i]-min[i])/(n-i)
```
嘛

于是就是这样了：

```
for(int i=n;i>=2;i--){
    mn[i]=min(mn[i+1],a[i]);
    sum[i]=sum[i+1]+a[i];
    if(i!=n)avr[i]=(sum[i]-mn[i])/(double)(n-i);
}
```
再就是比较了，此处不再说明。

完整代码：

```
#include<algorithm>
#include<bitset>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<map>
#include<iostream>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;
#define ll long long
#define f(i,a,b) for(int i=a;i<=b;i++)
inline ll read(){
   int s=0,w=1;
   char ch=getchar();
   while(ch<'0'||ch>'9'){if(ch=='-')w=-1;ch=getchar();}
   while(ch>='0'&&ch<='9') s=s*10+ch-'0',ch=getchar();
   return s*w;
}
#define d read()
ll n;
double a[1000010];
double avr[1000010];
double sum[1000010];
double mn[1000010];
double mx;
int main(){
	n=d;
	f(i,1,n+1)mn[i]=10010;
	f(i,1,n)scanf("%lf",&a[i]);
	for(int i=n;i>=2;i--){
		mn[i]=min(mn[i+1],a[i]);
		sum[i]=sum[i+1]+a[i];
		if(i!=n)avr[i]=(sum[i]-mn[i])/(double)(n-i);
	}
	f(i,2,n-1)mx=max(mx,avr[i]);
	f(i,2,n-1)if(mx==avr[i])printf("%lld\n",i-1);
	return 0;
}
```
