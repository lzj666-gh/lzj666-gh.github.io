# P1447 题解

题目大意:给定n和m,求Σ(1<=i<=n)Σ(1<=j<=m)GCD(i,j)\*2-1

i和j的限制不同,传统的线性筛法失效了,这里我们考虑容斥原理

令f[x]为GCD(i,j)=x的数对(i,j)的个数,这个不是很好求

我们令g[x]为存在公因数=x的数对(i,j)的个数(注意不是最大公因数！),显然有g[x]=(n/x)\*(m/x)

但是这些数对中有一些的最大公因数为2d,3d,4d,我们要把他们减掉

于是最终f[x]=(n/x)\*(m/x)-Σ(2\*x<=i\*x<=min(m,n))f[i\*x]

从后向前枚举x即可

时间复杂度O(nlogn)

注意计算g[x]的时候(n/x)\*(m/x)可能会乘爆 会挂掉一个点

```cpp
#include<cstdio>
#define re register int
const int N=100010;
int n,m;long long f[N],ans;
int main(){
    scanf("%d%d",&n,&m);
    if(n>m)n^=m^=n^=m; 
    for(re i=n;i;--i){
        f[i]=(long long)(n/i)*(m/i);
        for(re j=i<<1;j<=n;j+=i)f[i]-=f[j];
        ans+=((i<<1)-1)*f[i];
    }
    printf("%lld",ans);
return 0;
}
```