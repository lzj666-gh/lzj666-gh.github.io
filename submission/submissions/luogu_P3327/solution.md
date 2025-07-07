# P3327 题解

[$$\Large\texttt{My Blog}$$](https://hydingsy.github.io/)

---
## 写在前面

> 貌似没有题解证明了如下公式：$$d(ij)=\sum\limits_{x\mid i}\sum\limits_{y\mid j} [\gcd(x,y)=1]$$
> 于是在此篇题解的 `Extended` 部分我会给出一种证明！

---

> 题目链接：https://www.lydsy.com/JudgeOnline/problem.php?id=3994

求解（多组数据）

$$\sum\limits_{i=1}^N\sum\limits_{j=1}^M d(ij)$$

数据范围：$1\leqslant N,M,T\leqslant 5\times 10^4$

---

## Solution

首先给出一个公式：

$$d(ij)=\sum\limits_{x\mid i}\sum\limits_{y\mid j} [\gcd(x,y)=1]$$

因此所求为

$$\sum\limits_{i=1}^n\sum\limits_{j=1}^m\sum\limits_{x\mid i}\sum\limits_{y\mid j} [\gcd(x,y)=1]$$

改变求和顺序，先枚举因数 $x$ 和 $y$

$$\sum\limits_{x=1}^n\sum\limits_{y=1}^m \left\lfloor\frac{n}{x}\right\rfloor \left\lfloor\frac{m}{y}\right\rfloor [\gcd(x,y)=1]$$

将 $x,y$ 换成 $i,j$ 吧 QAQ

$$\sum\limits_{i=1}^n\sum\limits_{j=1}^m \left\lfloor\frac{n}{i}\right\rfloor \left\lfloor\frac{m}{j}\right\rfloor[\gcd(i,j)=1]$$

开始莫比乌斯反演！设

$$f(x)=\sum\limits_{i=1}^n\sum\limits_{j=1}^m \left\lfloor\frac{n}{i}\right\rfloor \left\lfloor\frac{m}{j}\right\rfloor[\gcd(i,j)=x]$$

$$g(x)=\sum_{x\mid d} f(d)$$

则有

$$g(x)=\sum\limits_{i=1}^n\sum\limits_{j=1}^m \left\lfloor\frac{n}{i}\right\rfloor \left\lfloor\frac{m}{j}\right\rfloor[x\mid\gcd(i,j)]$$

我们把 $x$ 提出就可以消除 $\gcd$ 的影响

$$g(x)=\sum\limits_{i=1}^{\frac{n}{x}}\sum\limits_{j=1}^{\frac{m}{x}} \left\lfloor\frac{n}{ix}\right\rfloor \left\lfloor\frac{m}{jx}\right\rfloor$$

再根据 $f(x)$ 的定义，得到答案为 $f(1)$

又因为

$$f(n)=\sum\limits_{n\mid d}\mu(\frac{d}{n})g(d)$$

故

$$f(1)=\sum\limits_{1\mid d}\mu(\frac{d}{1})g(d)=\sum_{i=1}^n \mu(i)g(i)$$

接下来再考虑如何求 $g(x)$，我们可以先计算 $s(x)=\sum\limits_{i=1}^{x} \left\lfloor\frac{x}{i}\right\rfloor$，就可以 $\Theta(1)$ 计算 $g(x)$。

**时间复杂度**：$\Theta(T\sqrt{n})$

---

## Code

```cpp
#include <cstdio>
#include <algorithm>
const int N=5e4+5;
int tot,mu[N],p[N];
long long s[N];
bool flg[N];

void init() {
    mu[1]=1;
    for(int i=2;i<=5e4;++i) {
        if(!flg[i]) p[++tot]=i,mu[i]=-1;
        for(int j=1;j<=tot&&i*p[j]<=5e4;++j) {
            flg[i*p[j]]=1;
            if(i%p[j]==0) {
                mu[i*p[j]]=0;
                break;
            } else {
                mu[i*p[j]]=-mu[i];
            }
        }
    }
    for(int i=1;i<=5e4;++i) mu[i]+=mu[i-1];
    for(int x=1;x<=5e4;++x) {
        long long res=0;
        for(int i=1,j;i<=x;i=j+1) j=x/(x/i),res+=1LL*(j-i+1)*(x/i);
        s[x]=res;
    }
}
int main() {
    init();
    int T;
    for(scanf("%d",&T);T--;) {
        int n,m;
        scanf("%d%d",&n,&m);
        if(n>m) n^=m^=n^=m;
        long long ans=0;
        for(int i=1,j;i<=n;i=j+1) {
            j=std::min(n/(n/i),m/(m/i));
            ans+=1LL*(mu[j]-mu[i-1])*s[n/i]*s[m/i];
        }
        printf("%lld\n",ans);
    }
    return 0;
}
```

---

## Extended

如何证明 `Solution` 中的公式？

$$d(ij)=\sum\limits_{x\mid i}\sum\limits_{y\mid j} [\gcd(x,y)=1]$$

我们考虑把每个因子一一映射。

如果 $ij$ 的因子 $k$ 中有一个因子 $p^c$，$i$ 中有因子 $p^a$，$j$ 中有因子 $p^b$。我们规定：

- 如果 $c\leqslant a$，那么在 $i$ 中选择。
- 如果 $c>a$，那么我们把 $c$ 减去 $a$，在 $j$ 中选择 $p^{c-a}$（在 $j$ 中选择 $p^e$ 表示的是 $p^{a+e}$）

对于 $ij$ 的因子 $k$ 的其他因子同理。于是对于任何一个 $k$ 有一个唯一的映射，且每一个选择对应着唯一的 $k$。

通过如上过程，我们发现：对于 $ij$ 的因子 $k=\prod {p_i}^{c_i}$，我们不可能同时在 $i$ 和 $j$ 中选择 $p_i$（优先在 $i$ 中选择，如果不够就只在 $j$ 中选择不够的指数），故 $x$ 和 $y$ 必须互质。

等式得证。