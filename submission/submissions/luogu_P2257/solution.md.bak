# P2257 题解

说实话，个人认为这道题不适合作为第一道莫比乌斯反演的题。因为这道题蕴含着一些奇妙的数学技巧。对于莫比乌斯反演的初学者，建议看看我的一篇博客[**莫比乌斯反演-让我们从基础开始**](https://www.luogu.org/blog/An-Amazing-Blog/mu-bi-wu-si-fan-yan-ji-ge-ji-miao-di-dong-xi)。我在这篇博客中详细地介绍了推导莫比乌斯反演的思维过程以及各种常用方法，由浅入深。

下面开始吧

首先我们理一下题意，这道题实际上是求

$$\sum_{i=1}^{n}\sum_{j=1}^{m}[gcd(i,j)\in prime]$$

根据常规思路，我们不妨枚举一下这里的$gcd(i,j)$，就假设它叫$k$吧。顺便令$n\leq m$，显然有$k\leq n$

$$=\sum_{k=1}^{n}\sum_{i=1}^{n}\sum_{j=1}^{m}[gcd(i,j)=k]\ \ \ (k\in prime)$$

同时除以$k$，将$[gcd(i,j)=k]$化成$[gcd(i,j)=1]$

$$=\sum_{k=1}^{n}\sum_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{k}\rfloor}[gcd(i,j)=1]\ \ \ (k\in prime)$$

下面有请~~我们喜闻乐见的~~莫比乌斯反演

和下面的大佬们不一样，我一看到那个需要设函数的莫比乌斯反演公式就头大，所以我决定，不用那个公式。

我们知道莫比乌斯函数的性质

$$\sum_{d|n}\mu(d)=[n=1]$$

我们把这个$n$换成$gcd(i,j)$

$$[gcd(i,j)=1]=\sum_{d|gcd(i,j)}\mu(d)$$

把这个东西扔到原式中去，于是原式

$$=\sum_{k=1}^{n}\sum_{i=1}^{\lfloor\frac{n}{k}\rfloor}\sum_{j=1}^{\lfloor\frac{m}{k}\rfloor}\sum_{d|gcd(i,j)}\mu(d)\ \ \ (k\in prime)$$

套路一下，我们枚举$d$，顺便把$d$提到前面来。
由于$d|gcd(i,j)$，可得$i,j$都是$d$的倍数，要满足这个条件，不妨将$i,j$的上限都除以$d$。相当于把$i$变成$\lfloor\frac{i}{d}\rfloor *d$，$j$变成$\lfloor\frac{j}{d}\rfloor *d$

于是我们就跟中间的那两个$\sum$说再见了

$$=\sum_{k=1}^{n}\sum_{d=1}^{\lfloor\frac{n}{k}\rfloor}\mu(d)*\lfloor\frac{n}{kd}\rfloor*\lfloor\frac{m}{kd}\rfloor\ \ \ (k\in prime)$$

我最开始就是推到这里，然后开心地枚举了一下$k$，结果T掉了

然后仔细地想了一想

对于这种看似已经化成最简的式子，我们有一个常用方法可以降低时间复杂度

我们设$T=kd$，有

$$=\sum_{k=1}^{n}\sum_{d=1}^{\lfloor\frac{n}{k}\rfloor}\mu(d)*\lfloor\frac{n}{T}\rfloor*\lfloor\frac{m}{T}\rfloor\ \ \ (k\in prime)$$

枚举一下$T$，提到前面去

$$=\sum_{T=1}^{n}\lfloor\frac{n}{T}\rfloor*\lfloor\frac{m}{T}\rfloor\sum_{k|T,k\in pimre}\mu(\frac{T}{k})$$

我们惊喜地发现，最后那个东西，是可以预处理的！

考虑每一个质数$k$，对于$k$的倍数$T$，将它的值加上$\mu(\frac{T}{k})$

代码实现如下

``` cpp 
void sieve() {
    mu[1]=1;
    for (int i=2;i<=10000000;i++) {
        if (!flag[i]) prime[++cnt]=i,mu[i]=-1;
        for (int j=1;j<=cnt&&i*prime[j]<=10000000;j++) {
            flag[i*prime[j]]=1;
            if (i%prime[j]==0) break;
            mu[i*prime[j]]=-mu[i];
        }
    }
    for (int i=1;i<=cnt;i++)
        for (int j=1;prime[i]*j<=10000000;j++)
            f[j*prime[i]]+=mu[j];
    for (int i=1;i<=10000000;i++)
        sum[i]=sum[i-1]+f[i];
}
```

处理一下前缀和$sum$，就可以$AC$啦

分享完整代码

``` cpp
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define LL long long
LL mu[10000010];int flag[10000010],prime[10000010],cnt,f[10000010],sum[10000010];
void sieve() {
    mu[1]=1;
    for (int i=2;i<=10000000;i++) {
        if (!flag[i]) prime[++cnt]=i,mu[i]=-1;
        for (int j=1;j<=cnt&&i*prime[j]<=10000000;j++) {
            flag[i*prime[j]]=1;
            if (i%prime[j]==0) break;
            mu[i*prime[j]]=-mu[i];
        }
    }
    for (int i=1;i<=cnt;i++)
        for (int j=1;prime[i]*j<=10000000;j++)
            f[j*prime[i]]+=mu[j];
    for (int i=1;i<=10000000;i++)
        sum[i]=sum[i-1]+f[i];
}
LL solve(int a,int b) {
    LL ans=0;
    if (a>b) swap(a,b);
    for (int l=1,r=0;l<=a;l=r+1) {
        r=min(a/(a/l),b/(b/l));
        ans+=(LL)(sum[r]-sum[l-1])*(LL)(a/l)*(LL)(b/l);
    }
    return ans;
}
int main() {
    sieve();
    int n,m,T;scanf("%d",&T);
    while (T--) {
        scanf("%d%d",&n,&m);
        if (n>m) swap(n,m);
        printf("%lld\n",solve(n,m));
    }
}
```