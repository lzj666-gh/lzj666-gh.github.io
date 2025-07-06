# P1390 题解

其实这题和P2389差不多还简单一些

这里介绍一种nlogn的做法

设f[d]=∑∑gcd(i,j)=d

F[d]=∑∑d|gcd(i,j)

不难看出F[d]=n/d\*(n/d)

那么f[d]=F[d]-∑f[kd]

所以o(nlogn)扫一下就好了（主要是代码特别短）

然后ans=(∑f[d]-n\*(n+1)/2)/2 减去gcd(d,d)=d的和gcd(i,j)=gcd(j,i)重复的

```cpp
#include<cstdio>
#define re register int
long long n,ans,f[2000010];
int main(){
    scanf("%lld",&n);
    for(re i=n;i;--i){
        f[i]=n/i*(n/i);
        for(re j=i<<1;j<=n;j+=i)f[i]-=f[j];
        ans+=f[i]*i;
    }
    printf("%lld",(ans-n*(n+1)/2)/2);
return 0;
}
```