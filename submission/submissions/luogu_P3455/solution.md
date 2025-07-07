# P3455 题解

#### 曾经我好几次想学莫比乌斯反演，但是写完题后还是一脸懵逼，又因为我比较懒，所以已知没有学会，不断摸索摸索，现在已经有了初步的理解。

#### 我决定用初学者的角度写一篇总结，以免我再忘掉。

***
例题：[P3455 [POI2007]ZAP-Queries](https://www.luogu.org/problemnew/show/P3455)

实际上就是求

$\sum_{i=1}^{n}\sum_{j=1}^{m}[gcd(i,j)=k]$

(这里我们让$n>=m$)

我们首先把$k$提出来。为什么呢，因为莫比乌斯反演的条件之一是出现$[...=1]$。即：

$\sum_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{k}\rfloor}[gcd(i,j)=1]$

这是因为$k|i$且$k|j$时才对答案有贡献。

***
现在我们先介绍莫比乌斯反演
***
**定义**

$\mu(x)=\begin{cases} 1 & x=1 \\ 0 & \textrm{存在} p^2|x,p \in Prime \\ (-1)^k & k\textrm{为质因数个数}\end{cases}$

非常奇怪的一个定义$...$

我当初也不太理解为什么要定义成这个鬼样子$...$

***
**定义**

$f_1*f_2(x)=\sum_{i|x}f_1(i)f_2(\frac{n}{i})$

为数论函数(定义域为正整数的函数)$f_1$和$f_2$的**迪利克雷卷积**

那么实际上我们可以把$*$看作两个函数之间的作用，返回一个函数
***
**引理1:**

**若**$f_1$和$f_2$**为积性函数，那么**$f_1*f_2$**也为积性函数**

_证明：_

$(gcd(x,y)=1)$

$\begin{aligned} f_1*f_2(xy)=&\sum_{i|xy}f_1(i)f_2(\frac{xy}{i}) -\textrm{定义}\\ =& \sum_{i|x}\sum_{j|y}f_1(ij)f_2(\frac{xy}{ij})-\textrm{把上一步的}i\textrm{变为这一步的ij}\\  =&\sum_{i|x}\sum_{j|y}f_1(i)f_1(j)f_2(\frac{x}{i})f_2(\frac{y}{j}) -f_1\textrm{和}f_2\textrm{是积性函数}\\ =&(\sum_{i|x}f_1(i)f_2(\frac{x}{i}))(\sum_{j|y}f_1(j)f_2(\frac{y}{j}))\ -\textrm{不理解这步的话可以倒推到上一步}\\ =&f_1(x)*f_2(y)\end{aligned}$


***
**定义**

$\epsilon(x)=[x=1]$

叫做单位函数

***
**定理1：**$($反演本质$)$

$1*\mu=\epsilon$

即：
$\sum_{i|x}\mu(i)=\epsilon(x)$

_证明：_

_若_$x=1$_，显然成立_

_否则，我们让_$t=\Pi_{i=1} p_i^{a_i}$

_如果_$a$_中有一个不为_$1$，_则_$\mu(t)=0$

_所以对_$1*\mu$_真正有贡献的的只有_$a$_全为_$0$_或_$1$_的因数。_

_假设有_$p_{1-n}$，_那么有且仅有_$i$_个_$a$_的值为_$1$_的因数个数为_$C_{n}^{i}$

_根据_$\mu$_的定义，我们可以得到以下式子_

$1*\mu=\sum_{i=0}^{n}(-1)^iC_{n}^{i}$

_而_

$(x-1)^n=\sum_{i=0}^{n}(-1)^iC_{n}^{i}x^{n-i}$

_令_$x=1$_，等式左边为_$0$_，等式右边为上式。所以，这种情况下，_

$1*\mu=\sum_{i=0}^{n}(-1)^iC_{n}^{i}=0$

_综上，_

$1*\mu=\epsilon$

***
**引理2：**

$\mu$为积性函数

_证明：_

$(gcd(x,y)=1)$

_若_$x$_和_$y$_有一个为_$1$_，显然成立_

_若_$\mu(x)$_和_$\mu(y)$_有一个为_$0$_，显然成立_

_否则：_

$\begin{aligned}\mu(x)\mu(y)=&(-1)^{k_x}(-1)^{k_y} -\textrm{定义} \\ =& (-1)^{k_x+k_y} \\ =&\mu(xy) -\textrm{质因数个数函数是加性函数}\end{aligned}$

***
好，说完了一大堆东西，我们继续来看题

$\sum_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{k}\rfloor}[gcd(i,j)=1]$

我们使用莫比乌斯反演得到

$\sum_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{k}\rfloor}\sum_{d|gcd(i,j)}\mu(d)$

我们又发现可以直接让$i$变成$i/d$，$j$变成$j/d$，这样就不用考虑$d$是否是$gcd(i,j)$的因数，于是我们枚举$d$，即

$\sum_{d=1}^{n}\sum_{i=1}^{\lfloor\frac{n}{kd}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{kd}\rfloor}\mu(d)$

此时我们发现，诶！$\mu(d)$和里面俩$\sum$没关系了，赶紧提出来

$\sum_{d=1}^{n}\mu(d)\sum_{i=1}^{\lfloor\frac{n}{kd}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{kd}\rfloor}1$

然后，我们就可以顿时消去两个$\sum$!

$\sum_{d=1}^{n}\mu(d)\lfloor\frac{n}{kd}\rfloor\lfloor\frac{m}{kd}\rfloor$

所以我们可以通过线性筛求出$\mu(1)-\mu(n)$，然后就可以$O(n)$求了！

但是我们又发现，询问组数$T=50000$，即使是$O(n)$也过不去。

此时，我们就需要另外一个数论处理工具：整除分块（数论分块）

***
对于$\sum_{i=1}^{n}f(i)$，$f(i)$单调，$f(i)$的取值有$k$种的某些函数，我们可以做到$O(k)$的复杂度

做法：

* 每次求出$f(x)=i$的终点
* 统计起点与终点之间的值
* 把$i$的终点$+1$为下一个值的起点

为什么说某些函数呢，因为有一些函数你不太好确定终点在哪里。

***
**引理3：**

$\lfloor\frac{n}{kd}\rfloor$的取值不会多于$2\sqrt {\lfloor\frac{n}{k}\rfloor}$种

_证明:_

* _若_$d<=\sqrt {\lfloor\frac{n}{k}\rfloor}$_，最多有_$\sqrt {\lfloor\frac{n}{k}\rfloor}$_种取值_

* _若_$d>=\sqrt {\lfloor\frac{n}{k}\rfloor}$，$\lfloor\frac{n}{kd}\rfloor<=\sqrt {\lfloor\frac{n}{k}\rfloor}$_，最多有_$\sqrt {\lfloor\frac{n}{k}\rfloor}$_种取值_

***
于是我们可以$O(n)$预处理，单次询问$O(\sqrt n)$求$\sum_{d=1}^{n}\mu(d)\lfloor\frac{n}{kd}\rfloor\lfloor\frac{m}{kd}\rfloor$啦！注意$\lfloor\frac{n}{kd}\rfloor\lfloor\frac{m}{kd}\rfloor$要分成$\lfloor\frac{n}{kd}\rfloor$和$\lfloor\frac{m}{kd}\rfloor$取值**都一样**的为一段。

代码：

```cpp
#include <bits/stdc++.h>
using namespace std;
const int Maxn=50005;
long long ans;
int T,n,m,k,cnt,mu[Maxn],prim[Maxn],sum[Maxn];
bool vis[Maxn];
void init(void)
{
	mu[1]=1;
	for(int i=2;i<=50000;i++)
	{
		if(!vis[i]) prim[++cnt]=i,mu[i]=-1;
		for(int j=1;j<=cnt&&i*prim[j]<=50000;j++)
		{
			vis[i*prim[j]]=true;
			if(i%prim[j]==0)
			{
				mu[i*prim[j]]=0;
				break;
			}
			mu[i*prim[j]]=-mu[i];
		}
	}
	for(int i=1;i<=50000;i++)
		sum[i]=sum[i-1]+mu[i];
}
int main()
{
	scanf("%d",&T);
	init();
	while(T--)
	{
		ans=0;
		scanf("%d%d%d",&n,&m,&k);
		int End=0,N=n/k,M=m/k;
		if(N<M) swap(N,M);
		for(int Start=1;Start<=M;Start=End+1)
		{
			End=min(N/(N/Start),M/(M/Start));
			ans+=(sum[End]-sum[Start-1])*(long long)(N/Start)*(M/Start);
		}
		printf("%lld\n",ans);
	}
	return 0;
}
```
