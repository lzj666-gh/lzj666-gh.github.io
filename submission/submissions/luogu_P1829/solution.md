# P1829 题解

[$$\Large\texttt{My Blog}$$](https://hydingsy.github.io/)

---

> 题目链接：https://www.luogu.org/problemnew/show/P1829

求解（对 $20101009$ 取模）

$$\sum\limits_{i=1}^n\sum\limits_{j=1}^m\operatorname{lcm}(i,j)$$

数据范围：$n,m\leqslant 10^7$

---

## Solution

易知原式等价于

$$\sum\limits_{i=1}^n\sum\limits_{j=1}^m\frac{i\cdot j}{\gcd(i,j)}$$

枚举最大公因数 $d$，显然两个数除以 $d$ 得到的数互质

$$\sum\limits_{i=1}^n\sum\limits_{j=1}^m\sum\limits_{d|i,d|j,\gcd(\frac{i}{d},\frac{j}{d})=1}\frac{i\cdot j}{d}$$

非常经典的 $\gcd$ 式子的化法

$$\sum\limits_{d=1}^n d\cdot\sum\limits_{i=1}^{\lfloor\frac{n}{d}\rfloor}\sum\limits_{j=1}^{\lfloor\frac{m}{d}\rfloor}[\gcd(i,j)=1]\cdot i\cdot j$$

后半段式子中，出现了互质数对之积的和，为了让式子更简洁就把它拿出来单独计算。于是我们记

$$\operatorname{sum}(n,m)=\sum\limits_{i=1}^n\sum\limits_{j=1}^m [\gcd(i,j)=1]\cdot i\cdot j$$

接下来对 $\operatorname{sum}(n,m)$ 进行化简。首先枚举约数，并将 $[\gcd(i,j)=1]$ 表示为 $\varepsilon(\gcd(i,j))$

$$\sum\limits_{d=1}^n\sum\limits_{d|i}^n\sum\limits_{d|j}^m\mu(d)\cdot i\cdot j$$

设 $i=i'\cdot d$，$j=j'\cdot d$（其中 $i',j'$ 指上式中的 $i,j$ ），显然式子可以变为

$$\sum\limits_{d=1}^n\mu(d)\cdot d^2\cdot\sum\limits_{i=1}^{\lfloor\frac{n}{d}\rfloor}\sum\limits_{j=1}^{\lfloor\frac{m}{d}\rfloor}i\cdot j$$

观察上式，前半段可以预处理前缀和；后半段又是一个范围内数对之和，记

$$g(n,m)=\sum\limits_{i=1}^n\sum\limits_{j=1}^m i\cdot j=\frac{n\cdot(n+1)}{2}\times\frac{m\cdot(m+1)}{2}$$

可以 $\Theta(1)$ 求解

至此

$$\operatorname{sum}(n,m)=\sum\limits_{d=1}^n\mu(d)\cdot d^2\cdot g(\lfloor\frac{n}{d}\rfloor,\lfloor\frac{m}{d}\rfloor)$$

我们可以 $\lfloor\frac{n}{\lfloor\frac{n}{d}\rfloor}\rfloor$ 数论分块求解 $\operatorname{sum}(n,m)$ 函数。

在求出 $\operatorname{sum}(n,m)$ 后，回到定义 $\operatorname{sum}$ 的地方，可得原式为

$$\sum\limits_{d=1}^n d\cdot\operatorname{sum}(\lfloor\frac{n}{d}\rfloor,\lfloor\frac{m}{d}\rfloor)$$

可见这又是一个可以数论分块求解的式子！

本题除了推式子比较复杂、代码细节较多之外，是一道很好的莫比乌斯反演练习题！（上述过程中，默认 $n\leqslant m$）

**时间复杂度**：$\Theta(n+m)$（两次数论分块）

---

## Code

```cpp
#include <cstdio>
#include <algorithm>
using std::min;

const int N=1e7;
const int mod=20101009;
int n,m,mu[N+5],p[N/10+5],sum[N+5];
bool flg[N+5];

void init() {
    mu[1]=1;
    int tot=0,k=min(n,m);
    for(int i=2;i<=k;++i) {
        if(!flg[i]) p[++tot]=i,mu[i]=-1;
        for(int j=1;j<=tot&&i*p[j]<=k;++j) {
            flg[i*p[j]]=1;
            if(i%p[j]==0) {mu[i*p[j]]=0;break;}
            mu[i*p[j]]=-mu[i];
        }
    }
    for(int i=1;i<=k;++i) sum[i]=(sum[i-1]+1LL*i*i%mod*(mu[i]+mod))%mod;
}
int Sum(int x,int y) {
    return (1LL*x*(x+1)/2%mod)*(1LL*y*(y+1)/2%mod)%mod;
}
int func(int x,int y) {
    int res=0;
    for(int i=1,j;i<=min(x,y);i=j+1) {
        j=min(x/(x/i),y/(y/i));
        res=(res+1LL*(sum[j]-sum[i-1]+mod)*Sum(x/i,y/i)%mod)%mod;
    }
    return res;
}
int solve(int x,int y) {
    int res=0;
    for(int i=1,j;i<=min(x,y);i=j+1) {
        j=min(x/(x/i),y/(y/i));
        res=(res+1LL*(j-i+1)*(i+j)/2%mod*func(x/i,y/i)%mod)%mod;
    }
    return res;
}
int main() {
    scanf("%d%d",&n,&m);
    init();
    printf("%d\n",solve(n,m));
}
```