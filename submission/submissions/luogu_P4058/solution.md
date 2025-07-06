# P4058 题解

$20$分思路：我们先模拟每棵树树每个月的高度，再看看这个数的高度是否大于或等于$L$，如果是就将当前截下的木材长度加上$L$，然后将这棵树的高度减去$L$即可，如果我们假设当前已经截下的木材长度为$da$，且现在是第$ans$个月的话，那么当$da>=L$时就要打印$ans$并跳出循环了。


$40$分思路：我们先模拟每棵树树每个月的高度，再看看这个数的高度是否大于或等于$L$，如果是就将当前截下的木材长度加上$h_i$，然后将这棵树的高度设为$0$即可，如果我们假设当前已经截下的木材长度为$da$，且现在是第$ans$个月的话，那么当$da>=L$时就要打印$ans$并跳出循环了。


$45$分思路：在模拟每棵树的高度之前我们需要先判断一下在第$0$个月时可否完成订单，若能够完成订单就输出$0$，否则就继续循环枚举。


$60$分思路：将我们的程序里的所有$int$类型的变量都转化为$long$ $long$类型的。因为$1<=S,L<=10^{18}$。


$75$分思路：使用二分查找，将$l$设为$0$，且将$r$设为∞，这样$mid$就是⌊$\frac{l+r}{2}$⌋。那么，在第$mid$个月时，$h_i$'=$h_i+a_i*mid$，统计一下在第$mid$个月是能否完成订单即可，若能够完成订单就将$r=mid$，否则就将$l=mid$，当$r-l>1$时进行循环，所以最终的答案就是$r$，如果你还不明白什么是二分查找下面将给出一个$l=1,r=10$的例子，其中浅绿色的格子代表$l$，深绿色的格子代表$r$，黄色的格子代表将要查找的点，浅蓝色的格子代表$mid$。


 ![](https://cdn.luogu.com.cn/upload/pic/12863.png) 

$85$分思路：将程序内的所有$long$ $long$转化为$unsigned$ $long$ $long$即可，其余同$75$分思路。


$100$分思路：先将$r$设为$max(S,L)$，再将$r$'设为$min(r$',$(r-h_i)/a_i+1)$即可，再将所有的$int$转化为$unsigned$ $long$ $long$即可。其余同$85$分思路。


$20$分代码：


```cpp
#include <cstdio>
int h[1000001],a[1000001];
int main()
{
    int ans=0,n=0,x=0,y=0;
    scanf("%d %d %d",&n,&x,&y);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&h[i]);
    }
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    while(++ans)
    {
        for(int i=1;i<=n;i++)
        {
            h[i]+=a[i];
            if(h[i]>=y)
            {
                x-=y;
                h[i]-=y;
            }
        }
        if(x<=0)
        {
            break;
        }
    }
    printf("%d",ans);
    return 0;
}
```
$40$分代码：

```cpp
#include <cstdio>
int h[1000001],a[1000001];
int main()
{
    int ans=0,n=0,x=0,y=0;
    scanf("%d %d %d",&n,&x,&y);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&h[i]);
    }
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    while(++ans)
    {
        for(int i=1;i<=n;i++)
        {
            h[i]+=a[i];
        }
        int da=0;
        for(int i=1;i<=n;i++)
        {
            if(h[i]>=y)
            {
                da+=h[i];
            }
        }
        if(da>=x)
        {
            break;
        }
    }
    printf("%d",ans);
    return 0;
}
```
$45$分代码：

```cpp
#include <cstdio>
int h[1000001],a[1000001];
int main()
{
    int ans=0,n=0,x=0,y=0;
    scanf("%d %d %d",&n,&x,&y);
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&h[i]);
    }
    for(int i=1;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    int da=0;
    for(int i=1;i<=n;i++)
    {
        if(h[i]>=y)
        {
            da+=h[i];
        }
    }
    if(da>=x)
    {
        printf("0");
        return 0;
    }
    while(++ans)
    {
        for(int i=1;i<=n;i++)
        {
            h[i]+=a[i];
        }
        int da=0;
        for(int i=1;i<=n;i++)
        {
            if(h[i]>=y)
            {
                da+=h[i];
            }
        }
        if(da>=x)
        {
            break;
        }
    }
    printf("%d",ans);
    return 0;
}
```
$60$分代码：

```cpp
#include <cstdio>
long long h[1000001],a[1000001];
int main()
{
    long long ans=0,n=0,x=0,y=0;
    scanf("%lld %lld %lld",&n,&x,&y);
    for(long long i=1;i<=n;i++)
    {
        scanf("%lld",&h[i]);
    }
    for(long long i=1;i<=n;i++)
    {
        scanf("%lld",&a[i]);
    }
    long long da=0;
    for(long long i=1;i<=n;i++)
    {
        if(h[i]>=y)
        {
            da+=h[i];
        }
    }
    if(da>=x)
    {
        printf("0");
        return 0;
    }
    while(++ans)
    {
        for(long long i=1;i<=n;i++)
        {
            h[i]+=a[i];
        }
        long long da=0;
        for(long long i=1;i<=n;i++)
        {
            if(h[i]>=y)
            {
                da+=h[i];
            }
        }
        if(da>=x)
        {
            break;
        }
    }
    printf("%lld",ans);
    return 0;
}
```
$75$分代码：

```cpp
#include <cstdio>
long long h[1000001],a[1000001];
int main()
{
    long long ans=0,l=0,r=0,n=0,x=0,y=0;
    scanf("%lld %lld %lld",&n,&x,&y),r=999999999;
    for(long long i=1;i<=n;i++)
    {
        scanf("%lld",&h[i]);
    }
    for(long long i=1;i<=n;i++)
    {
        scanf("%lld",&a[i]);
    }
    long long da=0;
    for(long long i=1;i<=n;i++)
    {
        if(h[i]>=y)
        {
            da+=h[i];
        }
    }
    if(da>=x)
    {
        printf("0");
        return 0;
    }
    long long nh[200001];
    while(r-l>1)
    {
        long long mid=(l+r)/2;
        for(long long i=1;i<=n;i++)
        {
            nh[i]=h[i]+mid*a[i];
        }
        long long da=0;
        for(long long i=1;i<=n;i++)
        {
            if(nh[i]>=y)
            {
                da+=nh[i];
            }
        }
        if(da>=x)
        {
            r=mid;
        }
        else
        {
            l=mid;
        }
    }
    printf("%lld",r);
    return 0;
}
```
$85$分代码：

```cpp
#include <cstdio>
unsigned long long h[1000001],a[1000001];
int main()
{
    unsigned long long l=0,r=0,n=0,x=0,y=0;
    scanf("%llu %llu %llu",&n,&x,&y),r=999999999;
    for(unsigned long long i=1;i<=n;i++)
    {
        scanf("%llu",&h[i]);
    }
    for(unsigned long long i=1;i<=n;i++)
    {
        scanf("%llu",&a[i]);
    }
    unsigned long long da=0;
    for(unsigned long long i=1;i<=n;i++)
    {
        if(h[i]>=y)
        {
            da+=h[i];
        }
    }
    if(da>=x)
    {
        printf("0");
        return 0;
    }
    unsigned long long nh[200001];
    while(r-l>1)
    {
        unsigned long long mid=(l+r)/2;
        for(unsigned long long i=1;i<=n;i++)
        {
            nh[i]=h[i]+mid*a[i];
        }
        unsigned long long da=0;
        for(unsigned long long i=1;i<=n;i++)
        {
            if(nh[i]>=y)
            {
                da+=nh[i];
            }
        }
        if(da>=x)
        {
            r=mid;
        }
        else
        {
            l=mid;
        }
    }
    printf("%llu",r);
    return 0;
}
```
$100$分代码：
```cpp
#include <cstdio>
unsigned long long h[1000001],a[1000001];
unsigned long long min(unsigned long long x,unsigned long long y)
{
    return x<y?x:y;
}
unsigned long long max(unsigned long long x,unsigned long long y)
{
    return x>y?x:y;
}
int main()
{
    unsigned long long now=0,l=0,r=0,n=0,x=0,y=0;
    scanf("%llu %llu %llu",&n,&x,&y),now=r=max(x,y);
    for(unsigned long long i=1;i<=n;i++)
    {
        scanf("%llu",&h[i]);
    }
    for(unsigned long long i=1;i<=n;i++)
    {
        scanf("%llu",&a[i]);
        r=min(r,(now-h[i])/a[i]+1);
    }
    unsigned long long da=0;
    for(unsigned long long i=1;i<=n;i++)
    {
        if(h[i]>=y)
        {
            da+=h[i];
        }
    }
    if(da>=x)
    {
        printf("0");
        return 0;
    }
    unsigned long long nh[200001];
    while(r-l>1)
    {
        unsigned long long mid=(l+r)/2;
        for(unsigned long long i=1;i<=n;i++)
        {
            nh[i]=h[i]+mid*a[i];
        }
        unsigned long long da=0;
        for(unsigned long long i=1;i<=n;i++)
        {
            if(nh[i]>=y)
            {
                da+=nh[i];
                if(da>=x)
                {
                    break;
                }
            }
        }
        if(da>=x)
        {
            r=mid;
        }
        else
        {
            l=mid;
        }
    }
    printf("%llu",r);
    return 0;
}
```