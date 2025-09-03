# P2522 题解

我顺便来安利一下自己的博客[peng-ym's blog](http://www.cnblogs.com/peng-ym/)里面也有[莫比乌斯反演](http://www.cnblogs.com/peng-ym/p/8647856.html)与[整除分块](http://www.cnblogs.com/peng-ym/p/8661118.html)的介绍，不知道的可以看一看哦！
## 题目描述
- 对于给出的n个询问，每次求有多少个数对(x,y)，满足a≤x≤b，c≤y≤d，且gcd(x,y) = k，gcd(x,y)函数为x和y的最大公约数。

## 输入输出格式
- 输入格式：
第一行一个整数n，接下来n行每行五个整数，分别表示a、b、c、d、k
- 输出格式：
共n行，每行一个整数表示满足要求的数对(x,y)的个数

## 解题思路
- 这个题要求的其实就是:$Ans=\sum_{i=a}^{b}\sum_{j=c}^{d}[gcd(i,j)=k]$
- 如果做过一道叫:[[POI2007]ZAP-Queries](http://www.cnblogs.com/peng-ym/p/8660937.html )的题，那么这题就显得非常的简单了。因为那道题就是这道题的一个特殊情况$(a=1,c=d)$
- 我们可以发现本题所算的$a$~$b$,$c$~$d$的答案，实质上由一个简单的容斥就可以转换成:
$$Ans((1,b),(1,d))-Ans((1,b),(1,c-1))-Ans((1,a-1),(1,d))+Ans((1,a-1),(1,c-1))$$
- 也就是一种类似于前缀和的容斥。具体的原因，其实把$\sum$随便手写几项，就可以发现这一定是正确的。
- 至于如何求$1$~$n$,$1$~$m$，就按照那道题化简一下式子就可以了。
- 我们设：
$$f(k)=\sum_{i=1}^{a}\sum_{j=1}^{b}[gcd(i,j)=k]$$
$$F(n)=\sum_{n|k}f(k)=\lfloor\frac{a}{n}\rfloor\lfloor\frac{b}{n}\rfloor$$
则可以由莫比乌斯反演可以推出：
$$f(n)=\sum_{n|k}\mu(\lfloor\frac{k}{n}\rfloor)F(k)$$
- **(PS:如果不知道为什么要设这两个函数，可以点开我上面放的链接)**
- 设完这两个函数之后，我们便惊喜的发现，$Ans=f(d)$
- 于是就直接开始推答案：
$$Ans=\sum_{d|k}\mu(\lfloor\frac{k}{d}\rfloor)F(k)$$
枚举$\lfloor\frac{k}{d}\rfloor$设为$t$
$$Ans=\sum_{t=1}^{min(a,b)}\mu(t)\lfloor\frac{a}{td}\rfloor\lfloor\frac{b}{td}\rfloor$$
这时候，这个式子已经可以做到$O(n)$的时间复杂度了，但是因为有多组数据，所以我们再用一下**[整除分块](http://www.cnblogs.com/peng-ym/p/8661118.html)**，这式子就可以做到$O(\sqrt{n})$了。
- 我们只需要写一个这样的函数，每次询问调用四遍就可以了。

## 下附代码:

```cpp
// luogu-judger-enable-o2
#include<bits/stdc++.h>
#define N 60010
using namespace std;
inline void read(int &x)
{
    x=0;
    static int p;p=1;
    static char c;c=getchar();
    while(!isdigit(c)){if(c=='-')p=-1;c=getchar();}
    while(isdigit(c)) {x=(x<<1)+(x<<3)+(c-48);c=getchar();}
    x*=p;	
}
bool vis[N];
int prim[N],mu[N],sum[N],cnt,k;
void get_mu(int n)
{
    mu[1]=1;
    for(int i=2;i<=n;i++)
    {
        if(!vis[i]){mu[i]=-1;prim[++cnt]=i;}
        for(int j=1;j<=cnt&&i*prim[j]<=n;j++)
        {
            vis[i*prim[j]]=1;
            if(i%prim[j]==0)break;
            else mu[i*prim[j]]=-mu[i];
        }
    }
    for(int i=1;i<=n;i++)sum[i]=sum[i-1]+mu[i];
}
long long calc(int a,int b)
{
    static int max_rep;
    static long long ans;
    max_rep=min(a,b);ans=0;
    for(int l=1,r;l<=max_rep;l=r+1)
    {
        r=min(a/(a/l),b/(b/l));
        ans+=(1ll*a/(1ll*l*k))*(1ll*b/(1ll*l*k))*(sum[r]-sum[l-1]);
    }
    return ans;
}
int main()
{
//	freopen("P3455.in","r",stdin);
//	freopen("P3455.out","w",stdout);
    int t;
    read(t);
    get_mu(50000);
    while(t--)
    {
        static int a,b,c,d;
        read(a);read(b);read(c);read(d);read(k);
        printf("%lld\n",calc(b,d)-calc(b,c-1)-calc(a-1,d)+calc(a-1,c-1));
    }
    return 0;
}
```