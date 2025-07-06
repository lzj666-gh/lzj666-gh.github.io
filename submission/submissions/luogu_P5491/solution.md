# P5491 题解

[blog](https://kewth.github.io/2019/10/21/二次剩余/)

二次剩余，~~俗称模意义开根~~。  
也就是对于常数 $n$ 解这样一个方程：

$$x^2 \equiv n \pmod{p}$$

这里只介绍模数 $p$ 为奇素数的解法，也就是 Cipolla 算法。

以下运算皆指模 $p$ 意义下的运算。

## 解的数量

严格来讲，非 0 数 $n$ 是二次剩余当且仅当方程 $x^2 \equiv n$ 有解，也就是能开根。  
上述方程无解的非 0 数 $n$ 称作非二次剩余。

对于二次剩余 $n$ ，$x^2 \equiv n$ 有多少解？

假设有多组解，对于任意两个不相等的解 $x_0, x_1$ ，有 $x_0^2 \equiv x_1^2$ 。  
移项后平方差，得到 $(x_0 - x_1)(x_0 + x_1) \equiv 0$ 。

由于 $p$ 是奇素数，且 $x_0 \ne x_1$ ， $x_0 - x_1$ 在模 $p$ 意义下是不会为 0 的。  
故有 $x_0 + x_1 \equiv 0$ ，也就是说两个不相等的解一定是相反数，  
换言之，该方程只有两个解，且它们互为相反数。  
而当 $p$ 为奇素数时模意义的两个相反数不会相等，因为奇偶性不同。

还可以知道，任意一对相反数都对应一个二次剩余，而且这些二次剩余是两两不同的。  
也就说二次剩余的数量恰为 $\frac{p-1}{2}$ ，其他的非 0 数都是非二次剩余，数量也是 $\frac{p-1}{2}$ 。

## 欧拉准则

如何快速判断一个数 $n$ 是否为二次剩余？

以下讨论假定 n 不为 0 。

观察费马小定理 $n^{p-1} \equiv 1$ ，由于 $p$ 是奇素数，可以得到 $n^{2(\frac{p-1}{2})} - 1\equiv 0$ ，  
也就是说 $n^{\frac{p-1}{2}}$ 是 1 开根的结果，根据上面所说， 1 开根只有两个解 1 和 -1 。  
那么 $n^{\frac{p-1}{2}}$ 只能是 1 或 -1 。

若 $n$ 是二次剩余，则有 $n^{\frac{p-1}{2}} \equiv (x^2)^{\frac{p-1}{2}} \equiv x^{p-1} \equiv 1$ 。

若 $n^{\frac{p-1}{2}} \equiv 1$ ，将 $n$ 表示为 $g^k$ ， 其中 $g$ 是模 $p$ 意义下的原根。  
那么有 $g^{k\frac{p-1}{2}} \equiv 1$ 由于 $g$ 是原根，必有 $p-1|k\frac{p-1}{2}$ ，  
也就是说 $k$ 一定是偶数，那么令 $x \equiv g^{\frac{k}{2}}$ 即是 $n$ 开根的结果，这说明 $n$ 是二次剩余。

也就是说 $n^{\frac{p-1}{2}} \equiv 1$ 与 $n$ 是二次剩余是等价的，  
由于 $n^{\frac{p-1}{2}}$ 不为 1 是只能是 -1 ，那么 $n^{\frac{p-1}{2}} \equiv -1$ 与 $n$ 是非二次剩余等价。

*ps: 网上一堆伪证（包括楼下一篇题解）说若 $n$ 是非二次剩余，不存在 $x$ 使得上式为 1 ，但这只能说明上式为 -1 时 $n$ 是非二次剩余，并不能推翻“当 $n$ 是非二次剩余时上式为 1”*

## Cipolla

对于二次剩余解方程 $x^2 \equiv n$ 。

找到一个 $a$ 满足 $a^2 - n$ 是非二次剩余，由于非二次剩余的数量接近 $\frac{p}{2}$ ，  
通过随机 + 检验的方式期望约 2 次可以找到这样一个 $a$ 。

接下来定义 $i^2 \equiv a^2 - n$ 。  
但是 $a^2 - n$ 不是二次剩余，怎么找得到这样一个 $i$ ？

类比实数域到复数域的推广，定义这样一个 $i$ ，然后可以将所有数表示为 $A+Bi$ 的形式，  
其中 $A, B$ 都是模 $p$ 意义下的数，类似于实部和虚部。

那么 $(a + i)^{p+1} \equiv n$ ，考虑证明。

**引理 1** ： $i^p \equiv -i$ 。

证明： $i^p \equiv i(i^2)^{\frac{p-1}{2}} \equiv i(a^2 - n)^{\frac{p-1}{2}} \equiv -i $

**引理 2** ： $(A + B)^p \equiv A^p + B^p$ 。

证明：二项式定理展开后，由于 $p$ 是质数，除了 $C_p^0, C_p^p$ 外的组合数分子上的阶乘没法消掉，模 $p$ 都会为 0 ，剩下来的就是 $C_p^0 A^0 B^p + C_p^p A^p B^0$ 。

现在证明上述结论：

$$(a + i)^{p+1} \equiv (a^p + i^p) (a + i) \equiv (a - i) (a + i) \equiv a^2 - i^2 \equiv n$$

那么 $(a + i)^{\frac{p+1}{2}}$ 即是一个解，其相反数是另一个解。

然而还剩最后一个问题， $(a + i)^{\frac{p+1}{2}}$ 的“虚部”一定为 0 吗？

幸运的是，的确如此，假设存在 $(A + Bi)^2 \equiv n$ 且 $B \ne 0$ ，  
那么有 $A^2 + B^2i^2 + 2ABi \equiv n$ ，即 $A^2 + B^2(a^2 - n) - n \equiv -2ABi$ 。  
式子的左边“虚部”为 0 ，那么式子右边的虚部也一定为 0 ，也就是说 $AB \equiv 0$ 。  
既然假设了 $B \ne 0$ 那么一定是 $A \equiv 0$ ，也就是说 $(Bi)^2 \equiv n$ 。  
也就是 $i^2 \equiv nB^{-2}$ ，由于 $B^2$ 是个二次剩余，其逆元 $B^{-2}$ 一定也是二次剩余，乘上二次剩余 $n$ 后一定还是二次剩余，这与 $i^2$ 是个非二次剩余产生矛盾。

## 实现

实现的时候弄个“复数”类（据说也可以不用）即可。

参考实现：

```cpp
#include <cstdio>
#include <cstdlib>
typedef long long lolong;

int mod;
lolong I_mul_I; // 虚数单位的平方

struct complex {
	lolong real, imag;
	complex(lolong real = 0, lolong imag = 0): real(real), imag(imag) { }
};
inline bool operator == (complex x, complex y) {
	return x.real == y.real and x.imag == y.imag;
}
inline complex operator * (complex x, complex y) {
	return complex((x.real * y.real + I_mul_I * x.imag % mod * y.imag) % mod,
			(x.imag * y.real + x.real * y.imag) % mod);
}

complex power(complex x, int k) {
	complex res = 1;
	while(k) {
		if(k & 1) res = res * x;
		x = x * x;
		k >>= 1;
	}
	return res;
}

bool check_if_residue(int x) {
	return power(x, (mod - 1) >> 1) == 1;
}

void solve(int n, int p, int &x0, int &x1) {
	mod = p;

	lolong a = rand() % mod;
	while(!a or check_if_residue((a * a + mod - n) % mod))
		a = rand() % mod;
	I_mul_I = (a * a + mod - n) % mod;

	x0 = int(power(complex(a, 1), (mod + 1) >> 1).real);
	x1 = mod - x0;
}
```
