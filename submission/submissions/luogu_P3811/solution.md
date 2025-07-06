# P3811 题解

# 乘法逆元小结

> 乘法逆元，一般用于求 $$\frac{a}{b} \pmod p$$ 的值（$p$ 通常为质数），是解决模意义下分数数值的必要手段。

> [有兴趣可以点进我的博客看看啊qwq](https://www.cnblogs.com/zjp-shadow/p/7773566.html)

## 逆元定义

> 若$a*x\equiv1 \pmod {b}$，且$a$与$b$互质，那么我们就能定义:
$x$ 为 $a$ 的逆元，记为$a^{-1}$，所以我们也可以称 $x$ 为 $a$ 在 $\bmod b$ 意义下的倒数，

> 所以对于 $\displaystyle\frac{a}{b} \pmod {p}$ ，我们就可以求出 $b$ 在 $\bmod {p}$ 下的逆元，然后乘上 $a$ ，再 $\bmod {p}$，就是这个分数的值了。


## 求解逆元的方式

### 拓展欧几里得

这个方法十分容易理解，而且对于单个查找效率似乎也还不错，比后面要介绍的大部分方法都要快(尤其对于 $\bmod {p}$ 比较大的时候)。

这个就是利用拓欧求解 线性同余方程 $a*x \equiv c \pmod {b}$ 的$c=1$的情况。我们就可以转化为解 $a*x + b*y = 1$ 这个方程。

求解这个方程的解。不会拓欧可以点[这里](https://www.cnblogs.com/zjp-shadow/p/9267675.html#autoid-3-3-0)~

而且这个做法还有个好处在于，当 $a \bot p$ （互质），但 $p$ 不是质数的时候也可以使用。

代码比较简单：

```cpp
void Exgcd(ll a, ll b, ll &x, ll &y) {
    if (!b) x = 1, y = 0;
    else Exgcd(b, a % b, y, x), y -= a / b * x;
}
int main() {
    ll x, y;
    Exgcd (a, p, x, y);
    x = (x % p + p) % p;
    printf ("%d\n", x); //x是a在mod p下的逆元
}
```

### 快速幂


这个做法要利用 **费马小定理**

> 若$p$为素数，$a$为正整数，且$a$、$p$互质。
则有$a^{p-1} \equiv 1 (\bmod {p})$。

 
这个我们就可以发现它这个式子右边刚好为 $1$ 。


所以我们就可以放入原式，就可以得到：


$$a*x\equiv 1 \pmod p$$


$$a*x\equiv a^{p-1} \pmod p$$


$$x \equiv a^{p-2} \pmod p$$



所以我们可以用快速幂来算出 $a^{p-2} \pmod p$的值，这个数就是它的逆元了


代码也很简单：

```cpp
ll fpm(ll x, ll power, ll mod) {
    x %= mod;
    ll ans = 1;
    for (; power; power >>= 1, (x *= x) %= mod)
    	if(power & 1) (ans *= x) %= mod;
    return ans;
}
int main() {
	ll x = fpm(a, p - 2, p); //x为a在mod p意义下的逆元
}
```

### 线性算法


用于求一连串数字对于一个$\bmod p$的逆元。[洛谷P3811](https://www.luogu.org/problem/show?pid=3811)

只能用这种方法，别的算法都比这些要求一串要慢。


首先我们有一个,$1^{-1}\equiv 1 \pmod p$

然后设 $p=k*i+r,(1<r<i<p)$ 也就是 $k$ 是 $p / i$ 的商，$r$ 是余数 。

再将这个式子放到$\pmod p$意义下就会得到：

$$k*i+r \equiv 0 \pmod p$$

然后乘上$i^{-1}$,$r^{-1}$就可以得到:

$$k*r^{-1}+i^{-1}\equiv 0 \pmod p$$

$$i^{-1}\equiv -k*r^{-1}  \pmod p$$

$$i^{-1}\equiv -\lfloor \frac{p}{i} \rfloor*(p \bmod i)^{-1} \pmod p$$


于是，我们就可以从前面推出当前的逆元了。

代码也很短：

```cpp
inv[1] = 1;
for(int i = 2; i < p; ++ i)
    inv[i] = (p - p / i) * inv[p % i] % p;
```


### 阶乘逆元 $O(n)$ 求

因为有如下一个递推关系。

$\displaystyle inv[i+1]=\frac{1}{(i+1)!}$

$\displaystyle inv[i+1]*(i+1)=\frac{1}{i!}=inv[i]$


所以我们可以求出$n!$的逆元，然后逆推，就可以求出$1...n!$所有的逆元了。


递推式为

$inv[i+1]*(i+1)=inv[i]$

所以我们可以求出 $\displaystyle \forall i, i!,\frac{1}{i!}$ 的取值了。

然后这个也可以导出 $\displaystyle \frac{1}{i} \pmod p$ 的取值，也就是

$$\displaystyle \frac{1}{i!} \times (i - 1)! = \frac{1}{i} \pmod p$$

具体实现可以参考我[这发提交](https://www.luogu.org/record/show?rid=12236223)（卡了常。。）
