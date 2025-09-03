# P2158 题解

## [原文地址](https://i.cnblogs.com/EditPosts.aspx?postid=10293067)

发现这道题的题解大多都没有详细讲欧拉函数，所以本弱就来详细将讲欧拉函数

欧拉函数是小于$x$的整数中与$x$互质的数的个数，一般用$φ(x)$表示。特殊的，$φ(1)=1$。

如何计算出$1-n$欧拉函数呢？

~~我会GCD暴力枚举！~~

复杂度$O(n^2logn)$

~~我会递推~~

复杂度$O(n^2)$

递推式：

$φ(n)=n*∏(1-\frac{1}{pi})$（其中pi为n的所有质因数）

这个递推式的推到比较简单，因为$n$里面一定有$n*\frac{1}{pi}$个数是$pi$的倍数，所以我们就有$n*(1-\frac{1}{pi})$个数不是pi的个数

于是我们想知道$1-n$中有多少数不是所有$pi$倍数，我们自然可以想到乘法原理，就可以推出我们的递推式了。

其实我们也可以$O(1)$推出欧拉函数，即$φ(p)=p-1$,但是p要是质数，怎么证明呢？显然因为$p$是质数，所以他的质因数一定只有1和他本身，所以我们代入公式，即$φ(p)=p*(1-\frac{1}{p})=p*\frac{p-1}{p}=p-1$

我们有一个关于欧拉函数的性质，当$n>1$时，小于n的数中，与n互质的数的总和为：$\frac{φ(n)*n}{2}$。这个公式证明需要用到一个定理~~（其实是我太菜了不会证明）~~若$n$互质的数有一个是$m$，那么还存在另一个数$n-m$也与$n$互质。

所以与$n$互质的数的平均数是$\frac{n}{2}$，而个数又是$φ(n)$，可以得到这些数的和就是$\frac{φ(n)*n}{2}$。

其实根据上面那个定理，我们也可以得到另一个性质：当$n>2$时，$φ(n)$是偶数

那可不可以线性递推出$1-n$中所有的欧拉函数呢？

联想到我们是怎么筛出$1-n$中所有质数的呢？

### [不会的同学可以戳一戳](https://tbr-blog.blog.luogu.org/solution-p3912)

根据该链接的第一个算法，我们可以推出类比推出筛欧拉函数的方法

首先我们把所有的欧拉函数都设为它本身，然后再根据公式除以n所有的质因子（质因子可以靠筛法）

每当我们找到一个质数时，我们把它所有的倍数（即有质因子为该质数的数）乘以$(1-\frac{1}{pi})$即$(\frac{pi-1}{pi})$即可

以下算法复杂度为$O(nlogn)$
```cpp
il void work(int n) 
{ 
	for(re int i=1;i<=n;++i) 
    {
    	p[i]=i; 
    }
    for(re int i=2;i<=n;++i) 
    { 
    	if(p[i]==i)//如果i是质数
    	{ 
        	for(re int j=i;j<=n;j+=i) 
            { 
            	p[j]=p[j]/i*(i-1);//那么就把i的所有倍数筛出来 
            } 
        } 
    }
}
```

既然我们可以利用第一种筛法求出所有欧拉函数，那么我们可不可以根据欧拉筛推出所有的欧拉函数呢？显然是可以的。

我们需要计算的东西其实和上面的方法一样，下面给出代码。
```cpp
il void euler(int n) 
{
	p[1]=1;//1要特判 
    for(re int i=2;i<=n;++i) 
    { 
    	if(!b[i])//这代表i是质数 
        { 
        	prime[++num]=i; 
            p[i]=i-1; 
        } 
    	for(re int j=1;j<=num&&prime[j]*i<=n;++j)//经典的欧拉筛写法 
    	{ 
    		b[i*prime[j]]=1;//先把这个合数标记掉 
        	if (i%prime[j]==0) 
        	{ 
        		p[i*prime[j]]=p[i]*prime[j];//若prime[j]是i的质因子，则根据计算公式，i已经包括i*prime[j]的所有质因子 
           	 break;//经典欧拉筛的核心语句，这样能保证每个数只会被自己最小的因子筛掉一次 
        	} 
        	else 
        	{
        		p[i*prime[j]]=p[i]*p[prime[j]];//利用了欧拉函数是个积性函数的性质 
        	}
    	} 
    } 
}
```
## 例题：P2158 [SDOI2008]仪仗队 

通过观察发现，可以被看到的人必须满足$gcd(x,y)=1$，证明也很简单，如果$x,y$不互质的话，那么一定会有$(x/gcd(x,y),y/gcd(x,y))$把$(x,y)$挡住，换句话说，如果$gcd(x,y)$等于1，那么它一定可以把所有的$(kx,ky)$都挡住，所以我们只需要求出与$x,y$互质对的对数即可。

通过观察也可以发现，可以看到的人一定满足对称关系，所以我们只需要算出一个三角形（下面会提到）的对数在乘以$2+1$ ($2,2$也满足条件)

所以我们要算下图中为$1$的答案的对数即可
```
0000
0001
0011
0111
```
那我们怎么求呢？显然可以用欧拉函数来求出与每一个数互质的数的个数即可。

### 具体实现：

我们先算出$1~n$中所有的欧拉函数（$n$比较小，没必要用欧拉筛）,再把$1~n-1$所有的欧拉函数加起来就可以得到上图三角形内答案了。

为什么是$n-1$呢？我们不难发现，上图中小三角形只有$n-1$排，所以就是$n-1$啊

但这道题有一个坑点，如果$n==1$，那我们的答案应该是$0$而不是$1$，为什么呢？我们仔细回忆一下，我们为什么要$+1$呢？因为我们有一个$(2,2)$来特判（两个三角形的分界），如果$n==1$的话，显然就不需要$+1$了

时间复杂度：$O(n^2)->O(n)$

代码如下
```cpp
#include<bits/stdc++.h>
using namespace std;
#define re register
#define maxn 400005
int n,ans,p[maxn];
int main()
{
    cin>>n;
    for(re int i=1;i<=n;++i)
    {
        p[i]=i;
    }
    for(re int i=2;i<=n;++i)
    {
        if(p[i]==i)
        {
            for(re int j=i;j<=n;j+=i)
            {
                p[j]=p[j]*(i-1)/i;
            }
        }
    }
    for(re int i=1;i<n;++i)
    {
        ans+=p[i];
    }
    printf("%d\n",(n==1)?0:ans<<1|1);
    return 0;
}
```

后来学了莫比乌斯反演，发现这题还可以用莫比乌斯反演做。

题目所求即为：$\sum_{i=1}^{n-1}\sum_{j=1}^{n-1}[gcd(i,j)==1]$

按照莫比乌斯反演的套路，原式=$\sum_{i=1}^{n-1}\sum_{j=1}^{n-1}\sum_{g|gcd(i,j)}\mu(i)$

i,j同时除以g得：原式=$\sum_{g=1}^{n}\mu(i)\sum_{i=1}^{\frac{n-1}{g}}\sum_{j=1}^{\frac{n-1}{g}}=\sum_{g=1}^{n}\mu(i)*\frac{n-1}{g}*\frac{n-1}{g}$

时间复杂度：$O(n^2)->O(n)$，当然这个复杂度对于此题已经够用了

然后我们发现$\frac{n-1}{g}$在一定范围内是相等的，所以我们可以用整出分块优化，不算预处理时间复杂度：$O(n)->O(\sqrt{n})$
```cpp
#include<bits/stdc++.h>
using namespace std;
#define il inline
#define re register
#define debug printf("Now is Line : %d\n",__LINE__)
#define file(a) freopen(#a".in","r",stdin);freopen(#a".out","w",stdout)
#define mod 1000000007
il int read()
{
    re int x=0,f=1;re char c=getchar();
    while(c<'0'||c>'9') {if(c=='-') f=-1;c=getchar();}
    while(c>='0'&&c<='9') x=x*10+c-48,c=getchar();
    return x*f;
}
#define maxn 40000
int mu[maxn+5],prim[maxn+5],vis[maxn+5],cnt,n,ans;
signed main()
{
	n=read()-1;
	if(!n) return puts("0"),0;
    mu[1]=1;
    for(re int i=2;i<=n;++i)
    {
        if(!vis[i]) prim[++cnt]=i,mu[i]=-1;
        for(re int j=1;j<=cnt;++j)
        {
            if(prim[j]*i>n) break;
            vis[prim[j]*i]=1;
            if(i%prim[j]==0) break;
            mu[i*prim[j]]=-mu[i];
        }
    }	
	for(re int i=1;i<=n;++i) mu[i]+=mu[i-1];
	for(re int l=1,r;l<=n;l=r+1)
	{
		r=n/(n/l);
		ans+=(mu[r]-mu[l-1])*(n/l)*(n/r);
	}
	printf("%d",ans+2);
    return 0;
}
```