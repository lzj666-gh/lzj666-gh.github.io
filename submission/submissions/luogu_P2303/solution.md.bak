# P2303 题解

前几篇题解都是暴力 $\displaystyle \sum d \cdot \varphi(n / d)$。

这里我有一种更优的方法。

推导过程有点复杂，这里只能略提一二，若要了解详细过程，请访问我的博客[题解](http://www.cnblogs.com/PinkRabbit/p/8278728.html)。

前几篇题解都提到的：

$$ \begin{aligned} \sum \gcd(i,n) &= \sum_{j = 1}^{n} j \sum_{i = 1}^{n} [\gcd(i, n) = j] \\ &= \sum_{j \mid n} j \cdot \varphi(n / j) \end{aligned} $$

我进一步把 $\varphi$ 拆开算：

$$ \begin{aligned} &= \sum_{j \mid n} \frac{n}{j} \varphi(j) \\ &= \sum_{j \mid n} \frac{n}{j} \!\left( j \cdot \prod_{p \mid j} \frac{p - 1}{p} \right) \\ &= n \sum_{j \mid n} \prod_{p | j} \frac{p - 1}{p} \end{aligned} $$

这里 $p$ 是质数。

那么令 $n = p_1^{b_1} p_2^{b_2} p_3^{b_3} \cdots p_k^{b_k}$。

那么 $j = p_1^{c_1} p_2^{c_2} p_3^{c_3} \cdots p_k^{c_k}$，满足$0 \le c_i \le b_i$。

根据相同的 $p$ 在不同的 $j$ 中出现的条件，可以推出贡献一定时的 $j$ 在答案中的贡献次数。

总之，总贡献为 $\displaystyle \prod_{i}^{k} \left( \frac{p_i - 1}{p_i} \text{ , (if } c_i > 0 \text{)} \right)$。

这里 $c_i = 0$ 的话，就把这一项变成 $1$（不产生贡献）。

再经过对最终结果的归纳和化简（因式分解），得出答案：

$$n \prod_{i = 1}^{k} \frac{b_i p_i - b_i + p_i}{p_i}$$

时间复杂度为 $\mathcal O(\sqrt{n})$，代码：

```cpp
#include<cstdio>
long long n;
long long f(){
    long long ans=n; long long i;
    for(i=2;i*i<=n;++i) if(n%i==0){
        int b=0;
        while(n%i==0) ++b,n/=i;
        ans/=i;
        ans*=b*i-b+i;
    } if(n>1) ans/=n, ans*=n+n-1; 
    return ans;
}
int main(){
    scanf("%lld",&n);
    printf("%lld",f());
    return 0;
}
```