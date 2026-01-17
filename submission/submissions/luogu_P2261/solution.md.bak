# P2261 题解

- 根据题目可以写出$ans=\sum\limits_{i=1}^{n}k\%i$


- 首先知道一点 $a\%b$ 可以表示为 $a-b*\lfloor\frac{a}{b}\rfloor$，写过高精取模的人应该都知道


- 所以 $ans=\sum\limits_{i=1}^{n}k-i*\lfloor\frac{k}{i}\rfloor=n*k-\sum\limits_{i=1}^{n}i*\lfloor\frac{k}{i}\rfloor$


- 然后 $\lfloor\frac{k}{i}\rfloor$ 可以出发分块来做，$\lfloor\frac{k}{i}\rfloor$大约有$\sqrt k$种取值，所以时间复杂度$O(\sqrt k)$


```cpp
#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;

int main() {
    ll n,k;
    scanf("%lld%lld",&n,&k);
    ll ans=n*k;
    for(ll l=1,r;l<=n;l=r+1) {
        if(k/l!=0) r=min(k/(k/l),n); 
        else r=n;
        ans-=(k/l)*(r-l+1)*(l+r)/2;
    }
    printf("%lld",ans);
    return 0;
}
```

无耻的挂一个[blog](http://blog.csdn.net/nuclearsubmarines/article/details/78165951)
