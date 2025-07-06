# P5142 题解

under 题解 [P5142](https://www.luogu.org/problemnew/show/P5142)

------------

题目要求维护模意义下的区间方差，显然是数据结构题。

考虑方差公式：

$ \begin{aligned} \sigma^2 &= \frac{1}{n} \sum \limits_{i = 1}^n (x_i - \bar{x})^2 \\ &= \frac{1}{n} (\sum \limits_{i = 1}^n x_i^2 - 2 \bar{x} \sum \limits_{i = 1}^nx_i + n \bar{x}^2) \\ &= \frac{1}{n} (\sum \limits_{i = 1}^n x_i^2 - 2 \bar{x} \times n \bar{x} + n \bar{x}^2) \\ &= \frac{1}{n} \sum \limits_{i = 1}^n x_i^2 - \bar{x}^2 \\ \end{aligned} $

而算术平均数

$ \begin{aligned} \bar{x} &= \frac{1}{n} \sum \limits_{i = 1}^n x_i \end{aligned} $


可以发现，只要维护序列的**区间和**和**区间平方和**，就可以维护平均数和方差。

**区间和**和**区间平方和**都**满足结合律**，因此可以用**线段树**维护。

------------

题目要求对 $ 1e9+7 $ 取模，而 $ 1e9+7 < \frac{INT \_ MAX}{2} $，完全可以不使用 `long long` 变量维护。

于是写了一发代码，看看~~毒瘤~~真正的取模和强制类型转换~~的大常数~~是什么样子的：

代码(c++11) 含注释：

```cpp
#include<cstdio>

using namespace std;
typedef long long ll;

constexpr int mod = 1e9+7;

int N, M, op, x, y, s1, s2, inv, ave, ans, a[100003];

int qpow(int b, int p = mod - 2, int m = mod) {
	// 快速幂用于费马小定理求逆元 
	b %= m;
	int s = 1 % m;
	for(; p; p >>= 1, b = (ll)b * b % m)
		if(p & 1) s = (ll)s * b % m;
	return s;
}

namespace SGT {
	#define ls p<<1
	#define rs p<<1|1
	#define sr(x) ((ll)(x)*(x)%mod) // 注意这个宏 

	int L[400003], R[400003], s1[4000003], s2[400003];
    	// s1[] 存储区间和，s2[] 存储区间平方和 
        // 由于无区间修改，不需要 lazytag 和 pushdown 操作 

	inline void pushup(int p) {
		s1[p] = (s1[ls] + s1[rs]) % mod;
		s2[p] = (s2[ls] + s2[rs]) % mod;
	}

	void build(int p, int l, int r) {
		L[p] = l, R[p] = r;
		if(l == r) {
			s1[p] = a[l] % mod;
			s2[p] = sr(a[l]) % mod;
			return;
		}
		int m = (l + r) >> 1;
		build(ls, l, m);
		build(rs, m + 1, r);
		pushup(p);
	}

	void modify(int p, int k, int v) {
    	// 单点修改 
		if(L[p] == R[p]) {
			s1[p] = v % mod;
			s2[p] = sr(v) % mod;
			return;
		}
		int m = (L[p] + R[p]) >> 1;
		if(k <= m) modify(ls, k, v);
		else modify(rs, k, v);
		pushup(p);
	}

	int query1(int p, int l, int r) {
		// 询问区间和 
		if(l == L[p] && r == R[p]) return s1[p] % mod;
		int m = (L[p] + R[p]) >> 1;
		if(r <= m) return query1(ls, l, r) % mod;
		if(l > m) return query1(rs, l, r) % mod;
		return (query1(ls, l, m) + query1(rs, m + 1, r)) % mod;
	}

	int query2(int p, int l, int r) {
		// 询问区间平方和 
		if(l == L[p] && r == R[p]) return s2[p] % mod;
		int m = (L[p] + R[p]) >> 1;
		if(r <= m) return query2(ls, l, r) % mod;
		if(l > m) return query2(rs, l, r) % mod;
		return (query2(ls, l, m) + query2(rs, m + 1, r)) % mod;
	}
}

int main() {
	scanf("%d%d", &N, &M);
	for(int i = 1; i <= N; ++i) scanf("%d", &a[i]);
	SGT::build(1, 1, N);
	
	while(M--) {
		scanf("%d%d%d", &op, &x, &y);
		if(op == 1) SGT::modify(1, x, y % mod);
		else {
			// 以下各变量均在模意义下 
			// 强制类型转换 (ll) 一个也不能少！ 
			s1 = SGT::query1(1, x, y) % mod;	// 区间和 
			s2 = SGT::query2(1, x, y) % mod;	// 区间平方和 
			inv = qpow(y - x + 1);				// 区间长度（分母）的逆元 
			ave = (ll)s1 * inv % mod;			// 区间算术平均数 
			ans = (ll)s2 * inv % mod - (ll)ave * ave % mod;
			ans = (ans % mod + mod) % mod;
				// 区间方差，前文有减法操作，防止出现负数
				// 现有题解在这里都给 $ans 加了 3 个 $mod 才 AC 
				// 但考试中怎么知道加上几个才不会被卡呢？ 
				
			printf("%d\n", ans);
		}
	}
	return 0;
}

```


------------

后记：

故意不开 `long long` 并不是为了毒瘤，而是为了磨炼自己的基本功。

在平常的练习中把刀磨锋利，才能在考试中得心应手地使用。

~~（寓言故事草）~~

如果有错误或不懂的地方，请在私信或评论中告知我。**谢谢大家！**
