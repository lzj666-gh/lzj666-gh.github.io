# P9621 题解

## 思路

不妨令 $p_i$ 表示圆圈 $i$ MISS 的概率，$e_i$ 为圆圈 $i$ 的期望得分．下文称“强制退出游戏”为“寄”．

先考虑固定起点为 $1$ 怎么做．

设 $f_i$ 表示点击圆圈 $i$ 后寄了的概率，$g_i$ 表示点击完前 $i$ 个圆圈后没寄的概率．

考虑计算 $f$，此时 $(i - K, i]$ 这一段圆圈必须全都 MISS，而圆圈 $i - K$ 不能 MISS，且点击 $i - K$ 前没寄．所以有：

$$
f_i = \left((1 - p_{i - K}) \prod_{j \in (i - K, i]} p_j\right) g_{i - K - 1}
$$

考虑计算 $g$，此时对于前 $i$ 个圆圈，点击后都不能寄，有：

$$
g_i = 1 - \sum_{j = 1}^i f_j
$$

此时期望得分为

$$
e_1 + \sum_{i = 1}^{n - 1} g_i e_{i + 1}
$$

现在考虑对于 $1 \sim n$ 中所有位置作为起点时，计算答案．不妨先算出期望分数的和，然后乘 $\frac{1}{n}$．

类似地，设 $f_{s, i}$ 表示从圆圈 $s$ 开始游玩，点击圆圈 $i$ 后寄了的概率，$g_{s, i}$ 表示从圆圈 $1$ 开始游玩，点击完圆圈 $i$ 后继续游玩的概率，特别地，令 $g_{s, s - 1} = 1$．那么期望和为：

$$
\begin{aligned}
  \sum_{s = 1}^n \left(e_s + \sum_{i = s}^{n - 1} g_{s, i} e_{i + 1}\right)
  &= \sum_{i = 1}^n e_i \left(1 + \sum_{s = 1}^{i - 1} g_{s, i - 1}\right) \\
\end{aligned}
$$

不妨令 $h_i = \sum\limits_{s = 1}^i g_{s, i} = i - \sum\limits_{j = 1}^i \sum\limits_{s = 1}^j f_{s, j}$，考虑对每个 $i$ 快速计算 $\sum\limits_{s = 1}^i f_{s, i}$．

$$
\begin{aligned}
  \sum_{s = 1}^i f_{s, i}
  &= \sum_{s = 1}^i \left((1 - p_{i - K}) \prod_{j \in (i - K, i]} p_j\right) g_{s, i - K - 1} \\
  &= \left((1 - p_{i - K}) \prod_{j \in (i - K, i]} p_j\right) \sum_{s = 1}^i g_{s, i - K - 1}  \\
  &= \left((1 - p_{i - K}) \prod_{j \in (i - K, i]} p_j\right) h_{i - K - 1}
\end{aligned}
$$

预处理前缀积和及其逆元即可 $O(n)$ 计算．注意 $p_i$ 可以等于 $0$，std 的处理方式是使用 $1$ 作为占位，然后特判 $(i - K, i]$ 中有 $0$ 的情况．

## 代码

```cpp
#include <cstdio>
#define debug(...) fprintf(stderr, __VA_ARGS__)

using i64 = long long;

inline i64 rd() {
	i64 x = 0, f = 1, c = getchar();
	while (((c - '0') | ('9' - c)) < 0)
		f = c != '-', c = getchar();
	while (((c - '0') | ('9' - c)) > 0)
		x = x * 10 + c - '0', c = getchar();
	return f ? x : -x;
}

struct Gen {
	using ull = unsigned long long;
	ull rand_num;
	inline void init(ull seed) { rand_num = seed; }
	inline ull next() {
		ull z = (rand_num += 0x9e3779b97f4a7c15);
		z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9;
		z = (z ^ (z >> 27)) * 0x94d049bb133111eb;
		return z ^ (z >> 31);
	}
	inline int rnr(int l, int r) { return l + (int)(next() % (r - l + 1)); }
	inline void get(int &a, int &b, int &c, int &d) {
		int divpart = rnr(0, 100);
		a = rnr(0, divpart), b = divpart - a;
		c = rnr(0, 100 - divpart), d = 100 - divpart - c;
	}
} Ge;

const int N = 5e6;
const i64 P = 998244353;
inline i64 fpow(i64 b, i64 p) {
	i64 res = 1;
	for (; p; b = b * b % P, p >>= 1) {
		if (p & 1) res = res * b % P;
	}
	return res;
}
i64 I[101];

int type;
int n, k;
i64 e[N + 5], p[N + 5], ip[N + 5];
i64 pr[N + 5], ipr[N + 5];
int fl[N + 5];
i64 f[N + 5];

int main() {
	for (int i = 1; i <= 100; i++) I[i] = fpow(i, P - 2);

	type = rd(), Ge.init(rd());
	n = rd(), k = rd();
	for (int i = 1, p1, p2, p3, p4; i <= n; i++) {
		if (!type) p1 = rd(), p2 = rd(), p3 = rd(), p4 = rd();
		else Ge.get(p1, p2, p3, p4);
		e[i] = (300 * p1 + 100 * p2 + 50 * p3) % P * I[100] % P;
		p[i] = p4 * I[100] % P, ip[i] = 100 * I[p4] % P;
	}

	pr[0] = ipr[0] = 1;
	for (int i = 1; i <= n; i++) {
		pr[i] = pr[i - 1] * (p[i] ? p[i] : 1) % P;
		ipr[i] = ipr[i - 1] * (ip[i] ? ip[i] : 1) % P;
		fl[i] = fl[i - 1] + !p[i];
	}

	i64 sum = 0;
	for (int i = 1; i <= n; i++) {
		i64 ct = 0;

		if (i >= k) {
			i64 c1 = (fl[i] - fl[i - k]) ? 0 : (pr[i] * ipr[i - k] % P);
			i64 c2 = (1 + P - p[i - k]) % P;

			(ct += c1) %= P;
			if (i > k) (ct += c1 * c2 % P) %= P;
			if (i > k + 1) (ct += c1 * c2 % P * f[i - k - 1] % P) %= P;
		}

		(sum += ct) %= P;
		f[i] = (i + P - sum) % P;
	}

	i64 ans = 0;
	for (int i = 1; i <= n; i++) (ans += (1 + f[i - 1]) * e[i] % P) %= P;
	(ans *= fpow(n, P - 2)) %= P;

	printf("%lld\n", ans);
	return 0;
}
```

## 参考

edisnimorF, [_下次再见 题解_](https://www.luogu.com.cn/blog/edisnimorF/xia-ci-zai-jian-ti-xie)
