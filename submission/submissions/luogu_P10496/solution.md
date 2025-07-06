# P10496 题解

upd：修改了时间复杂度。

这是一道数论好题，我介绍一下蓝书的做法。

不难发现，$x$ 个 $8$ 连起来的正整数等价于 $8 \times \frac{10^x-1}{9}$，那么题目转换为，给出 $L$，让我们求一个最小的正整数 $x$，使得：
$$
L\mid8\times \frac{10^x-1}{9}
$$

我们先把两边乘上 $9$，得：
$$
9L\mid8 \times (10^x-1)
$$

我们不妨再设 $d=\gcd(L,8)$，又可以把原式化为：
$$
\frac{9L}{d}\mid10^x-1
$$

再改写为同余式：
$$
10^x \equiv 1\pmod{\frac{9L}{d}}
$$

此时，我们再引入一个引理：若 $a,n$ 互质，则满足 $a^x \equiv 1\pmod{n}$ 的最小正整数解为 $\varphi(n)$ 的约数。

证明过程（摘录自蓝书）：

反证法。假设满足 $a^x \equiv 1 \pmod{n}$ 的最小正整数解 $x_0$ 不能整除 $\varphi(n)$。

设 $\varphi(n)=qx_0+r(0 < r < x_0)$。因为 $a^{x_0} \equiv 1 \pmod{n}$，所以 $a^{qx_0} \equiv 1 \pmod{n}$。根据欧拉定理，有 $a^{\varphi(n)} \equiv 1 \pmod{n}$，所以 $a^r \equiv 1 \pmod{n}$。这与 $x_0$ 最小矛盾，故假设不成立，原命题成立。

证毕。

那么我们就可以轻松地解决这道题了，根据引理，我们先求出 $\varphi(\frac{9L}{d})$，然后枚举它的所有约数 $x$，当 $10^x \equiv 1 \pmod{\frac{9L}{d}}$ 时，直接输出即可。

如何判断无解呢？只需判断 $\gcd(10,\frac{9L}{d})$ 是否不等于 $1$ 即可。

这样，我们就完成了这道题目，时间复杂度 $O(\sqrt{n}\log n)$（排序后）。

主体部分代码如下：
```cpp
vector <ll> t;
ll phi(ll x) {
	ll ans = x;
	for (int i = 2; i * i <= x; i++) {
		if (x % i == 0) {
			ans = ans * (i - 1) / i;
			while (x % i == 0) x /= i;
		}
	}
	if (x > 1) ans = ans * (x - 1) / x;
	return ans;
}
int main() {
	ll n;
	int cnt = 0;
	while (read(n), n) {
		t.clear();
		n = 9 * n / gcd(n, 8ll);
		cout << "Case " << ++cnt << ": ";
		if (gcd(n, 10ll) != 1) {
			cout << "0\n";
		}
		else {
			ll x = phi(n);
			for (ll i = 1; i * i <= x; i++) {
				if (x % i == 0) {
					t.push_back(i);
					if (x / i != i) {
						t.push_back(x / i);
					}
				}
			}
			sort(t.begin(), t.end());
			int i;
			for (i = 0; i < t.size(); i++) {
				if (quick_pow(10ll, t[i], n) == 1) {
					break;
				}
			}
			writeln(t[i]);
		}
	}
}
```