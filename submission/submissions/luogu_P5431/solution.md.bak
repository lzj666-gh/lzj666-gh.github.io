# P5431 题解

upd on 2025/08/29：这题数据怎么加强了。原来的代码需要加上快读快写才能过，不然最后一个点会超时。

### 前置知识：怎么求逆元

下面摘自 oi-wiki。[不会请点这里](https://oi-wiki.org/math/number-theory/inverse/)。

> 逆元：对于一个线性同余方程 $ax \equiv 1 \pmod p$，$x$ 称为 $a \mod b$ 的逆元，记作 $a^{-1}$。
> 
> [费马小定理](https://oi-wiki.org/math/number-theory/fermat/)：设 $p$ 是素数。对于任意整数 $a$ 且 $p\nmid a$，$a^{p-1}\equiv 1\pmod p$ 都成立。

对线性同余方程 $ax \equiv 1 \pmod p$，根据费马小定理，$ax \equiv a^{p-1} \pmod p$，所以 $x \equiv a^{p-2}$。其中 $p$ 是质数。

由此，我们可以通过快速幂，$O(\log{p})$ 求出 $a$ 模 $p$ 意义下的乘法逆元。

```cpp
#include<iostream>
using namespace std;
int n, p;
long long qpow(long long a, long long b) {
    long long c = 1;
    while(b) {
        if(b % 2) c = c * a % p;
		b /= 2;
		a = a * a % p;
    }
    return c;
}
int main() {
    cin >> n >> p;
    cout << qpow(n, p - 2) << endl;
    return 0;
}
```


### 算法介绍

$O(n + \log{p})$ 求一列数 $a_1,a_2,\cdots,a_n$ 的逆元。

先求出序列 $a_1, a_2, \cdots ,a_n$ 的前缀积 $pre_i$，然后求 $pre_n$ 的逆元，就可以递推出所有 $pre_i$ 的逆元 $ipre_i$。根据我们算出的 $ipre_i$，即可求出 $a_1, a_2, \cdots ,a_n$ 的逆元。

因为

$$\frac{1}{a_i\times a_{i-1}\times\cdots\times a_1}\times a_i\equiv\frac{1}{a_{i-1}\times a_{i-2}\times\cdots\times a_1}\pmod p$$

所以我们得到

$$(pre_{i-1})^{-1} \equiv (pre_i) ^ {-1} \times a_i \pmod p$$

递推代码：
```cpp
ipre[i - 1] = 1ll * ipre[i] * a[i] % p;
```
接下来我们要求出每个 $a_i$ 的逆元。这个很简单，把 $pre_{i-1}$ 乘回去就可以了。

因为

$$a_i \times a_{i-1} \times \cdots \times a_1 \times \frac{1}{a_{i-1} \times a_{i-2} \times \cdots \times a_1} \equiv a_i \pmod p$$

所以

$$a_i^{-1} \equiv ipre_{i} \times pre_{i-1} \pmod p$$

注意最后要乘上 $k^{i}$，递推的时候顺便算一下就可以了。 

### 正确性证明

比较显然。

预处理前缀积是 $O(n)$ 的，快速幂求 $pre_n$ 的逆元是 $O(\log{p})$ 的，递推求出 $pre_i$ 的逆元和 $a_i$ 的逆元是 $O(n)$ 的，所以整个算法复杂度是 $O(n+\log{p})$ 的。

::::success[代码：]
```cpp
#include<iostream>
using namespace std;
#define endl '\n'
int n, p, k;
long long mul;
int a[5000010], pre[5000010], ipre[5000010], sum;
int read() {
	int k = 0, f = 1;
	char c = getchar_unlocked();
	while(c < '0' || c > '9') {
		if(c == '-') f *= -1;
		c = getchar_unlocked();
	}
	while('0' <= c && c <= '9') k = k * 10 + (c - '0'), c = getchar_unlocked();
	return f * k;
}
void write(int x) {
	if(x < 0) putchar('-'), x = -x;
	if(x < 10) putchar(x + '0');
	else write(x / 10), putchar(x % 10 + '0');
}
long long qpow(long long a, long long b) {
    long long c = 1;
    while(b) {
        if(b % 2) c = c * a % p;
        b /= 2;
        a = a * a % p;
    }
    return c;
}
int main() {
    n = read(); p = read(); k = read();
    for(int i = 1; i <= n; i ++) a[i] = read();
    pre[0] = 1;
    for(int i = 1; i <= n; i ++) pre[i] = 1ll * pre[i - 1] * a[i] % p;
    ipre[n] = qpow(pre[n], p - 2);
    for(int i = n ; i >= 1; i --) 
        ipre[i - 1] = 1ll * ipre[i] * a[i] % p;
    mul = k;
	for(int i = 1; i <= n; i ++) {
        long long ans = 1ll * pre[i - 1] * ipre[i] % p;
        sum = (sum + mul * ans) % p;
        mul = mul * k % p;
    }
    write(sum);
    return 0;
}
```
::::