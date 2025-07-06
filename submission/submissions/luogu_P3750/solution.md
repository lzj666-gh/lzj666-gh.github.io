# P3750 题解

这道$dp$题感觉也挺神的。。我们考虑每个点按多次都可以归化成按或不按两种状态，而且很显然可以发现，每个按键都不可能被其他按键的组合键替代，于是我们实际上可以从大到小扫一遍，碰到亮的就按一遍，这样的话我们就可以找到所有必须要按的键，实际上就相当于除开这些键按了其他的键就还要必须按一个相同的键给按回来，这样我们就可以$dp$了。我们设$f[i]$表示从$i$个需要按的键到$i-1$个需要按的键的期望操作次数，这个转移方程是这样的：
$$f[i]=\frac{i}{n}+\frac{n-i}{n}\times(f[i]+f[i+1]+1)$$
这个的意思实际上是，有$\frac{i}{n}$的概率可以按到正确的键位，有另外$\frac{n-i}{n}$的概率是错误的位置，所以在之后的操作中需要将这个按键按回来，所以就多了一个需要按的键，按回来$i$之后还是需要$f[i]$的操作次数到$i-1$，这样就解释完了。。。

然后我们就可以把上面那个式子简化一下：
$$f[i]=\frac{n+(n-i)\times f[i+1]}{i}$$
然后求出这个东西之后，我们先比较一下必须按的按键个数（设为$cnt$）和$k$，如果还要小，就肯定是前者作为答案。不然我们就直接把$f[cnt]+f[cnt-1]+....+f[k+1]$作为答案即可，就相当于是从$cnt$到$k$的期望操作次数，然后，**记得要加个$k$!!!**，然后就乘上$n$的阶乘即可。

下面是代码
```cpp
// luogu-judger-enable-o2
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define maxn 100010
#define mod 100003
using namespace std;
typedef long long ll;
ll read()
{
    ll x=0,f=1;
    char ch=getchar();
    while(ch-'0'<0||ch-'0'>9){if(ch=='-') f=-1;ch=getchar();}
    while(ch-'0'>=0&&ch-'0'<=9){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
int n,k;
int a[maxn];
int cnt=0;
ll f[maxn];
ll quick_pow(ll x,ll p)
{
    ll an=1;
    ll po=x;
    while(p)
    {
        if(p%2)  an=(an*po)%mod;
        po=(po*po)%mod;
        p/=2;   
    }
    return an;
}
int main()
{
    n=read();k=read();
    for(int i=1;i<=n;i++)   a[i]=read();
    for(int i=n;i>=1;i--)
    {
        if(a[i])
        {
            cnt++;
            for(int j=1;j*j<=i;j++)
            {
                if(i%j==0)
                {
                    a[j]^=1;
                    if(j*j!=i)  a[i/j]^=1;
                }
            }
        }
    }
    f[n+1]=0;
    for(int i=n;i>=1;i--)
    {
        ll tmp=(ll)(n-i)*f[i+1]%mod;
        tmp=(tmp+(ll)n)%mod;
        tmp=tmp*quick_pow(i,mod-2)%mod;
        f[i]=tmp;
    }
    ll tmp=0;
    if(cnt<=k)   tmp=cnt;
    else{
        for(int i=cnt;i>k;i--)  tmp=(tmp+f[i])%mod;
        tmp=(tmp+k)%mod;
    }
    for(int i=1;i<=n;i++)  tmp=(tmp*(ll)i)%mod;
    printf("%lld\n",tmp);
    return 0;
}
```