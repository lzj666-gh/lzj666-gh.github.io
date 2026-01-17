# P2398 题解

$ans=\sum_{k=1}^nk*f[k]$

$f[k]$表示$gcd(i,j)=k$的个数 

$g[k]$表$k|gcd(i,j)$的个数

显然$g[k]=f[k]+f[2k]+...+f[mk]$

而$g[k]=\lfloor\frac nk\rfloor^2$($i$有$\lfloor\frac nk\rfloor$种选择$j$一样所以相乘就是$\lfloor\frac nk\rfloor^2$)

所以$f[k]=\lfloor\frac nk\rfloor^2-(f[2k]+f[3k]+....)$

复杂度是$n*(1+\frac12+\frac13+...+\frac1n)$


所以总复杂的为$O(nH(n)),H(n)$为调和级数

因为$n$不大,这个算法常数小,所以就比算$\sum_{d=1}^n\phi(d)*\lfloor\frac nd\rfloor^2$要快一些

什么你说杜教筛?那玩意常数更大.做杜教筛不如去做[这个](https://www.luogu.org/problemnew/show/P4213)

```cpp
#include<cstdio>
#define re register int
long long n,ans,f[100010];
int main(){
    scanf("%lld",&n);
    for(re i=n;i;--i){
        f[i]=n/i*(n/i);
        for(re j=i<<1;j<=n;j+=i)f[i]-=f[j];
        ans+=f[i]*i;
    }
    printf("%lld",ans);
return 0;
}
```