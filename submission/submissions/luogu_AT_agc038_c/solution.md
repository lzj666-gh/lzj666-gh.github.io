# AT_agc038_c 题解

---
title: [AGC038C] LCMs
tags: [数学, 莫比乌斯反演]


---

[题目来源](https://atcoder.jp/contests/agc038/tasks/agc038_c)

##### 前言

因为这道题中包含了比较多的常见套路所以写了这篇题解，给想学习数论的人，下文中如果出现比较常见的套路，都会着重说明

### 题面描述

- 给定一个长度为 $N$ 的数列 $A_1, A_2, A_3, \dots, A_N$。
- 请你求出 $\sum_{i=1}^{N}\sum_{j=i+1}^{N}\mathrm{lcm}(A_i,A_j)$ 的值模 $998244353$ 的结果。
- $1 \leq N \leq 2 \times 10^5$，$1 \leq A_i \leq 10^6$。

### 题目解答

首先$\sum_{i=1}^{N}\sum_{j=i+1}^{N}\mathrm{lcm}(A_i,A_j)$ 第二个 $\sum$ 不是从 $1$ 开始的这让我们很难受，所以：
$$
\sum_{i=1}^{N}\sum_{j=i+1}^{N}\mathrm{lcm}(A_i,A_j)=\frac{\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)-\sum_{i=1}^{N}{A_i}}{2}
$$
现在我们的就是要算 $\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)$，之后的过程就比较套路了。（下文中会使用 $(A_i,A_j)$ 表示 $A_i$ 和 $A_j$ 的最大公约数）
$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{i=1}^{N}\sum_{j=1}^{N}{\frac{A_i \times A_j}{(A_i, A_j)}} \\
&=\sum_{i=1}^{N}\sum_{j=1}^{N}\sum_{d=1}^{Max}{\frac{A_i \times A_j}{d}[(A_i,A_j)=d]}
\end{aligned}
$$
然后是数论题的常见处理方法，把后面的 $\sum$ 提到前面，至于如何判断什么时候能向前提，下面会简单的说以下：

+ 我们发现 $\frac{A_i \times A_j}{d}[(A_i,A_j)=d]$ 。这个式子中 $\frac{1}{d}$ 这一项只和 $d$ 有关，而和 $i,j$ 无关，但是我们是在最后一个 $\sum$ 处枚举的 $d$ ，那么这个时候我们就可以考虑把最后一个 $\sum$ 向前提取。

$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{i=1}^{N}\sum_{j=1}^{N}\sum_{d=1}^{Max}{\frac{A_i \times A_j}{d}[(A_i,A_j)=d]} \\
&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [(A_i,A_j)=d]}
\end{aligned}
$$

我们看到了 $[(A_i,A_j)=d]$ 这种式子，这个时候就要多加注意了，因为当我们看到形如 $[k=1]$ 这种式子时我们就可以进行反演了，方法如下。
$$
[k=1]=\sum_{d|k}\mu(d)
$$
但是 $[(A_i,A_j)=d]$ 这个式子，后面的是 $d$ 而不是 $1$ ，那我们考虑一下怎么把它转化成 $1$。
$$
[(A_i,A_j)=d][d|A_i][d|A_j]=[(\frac{A_i}{d},\frac{A_j}{d})=1][d|A_i][d|A_j]
$$
因为我们发现 $d|A_i,d|A_j$ 所以就有上面的转化。
$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [(A_i,A_j)=d]} \\
&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j][(\frac{A_i}{d},\frac{A_j}{d})=1]}
\end{aligned}
$$
之后进行反演
$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j][(\frac{A_i}{d},\frac{A_j}{d})=1]} \\
&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j]\sum_{t|(\frac{A_i}{d},\frac{A_j}{d})}}{\mu(t)}
\end{aligned}
$$
还是和上面一样，最后的式子之和 $t$ 有关，和 $i,j,d$没有关系，所以我们也把它往前提。（这个地方可以放在 $d$ 的前面也可以放在后面）
$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{d=1}^{Max}\frac{1}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j]\sum_{t|(\frac{A_i}{d},\frac{A_j}{d})}}{\mu(t)} \\
&=\sum_{d=1}^{Max}\sum_{t=1}^{\lfloor \frac{Max}{d} \rfloor}\frac{\mu(t)}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j][t|A_i][t|A_j]} \\
&=\sum_{d=1}^{Max}\sum_{t=1}^{\lfloor \frac{Max}{d} \rfloor}\frac{\mu(t)}{d}\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [dt|A_i][dt|A_j]}
\end{aligned}
$$
我们来观察后面这个式子 $\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [d|A_i][d|A_j]}$ ，对于任何一个 $d|A$ 都会对任何一个 $d|B$ ，包括 $A$ 和 $B$ 是一个数的时候。

回忆一下我们在初中学习过的公式：

+ $$
  (a+b)^2=a^2+b^2+2ab
  $$

+ $$
  (a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca
  $$

+ $$
  \dots\dots
  $$

注意到 $(A_1+A_2+A_3+A_4+\dots+A_k)^2$ 刚好就是 $A_x (x \in [1,k])$ 对于所有 $A_y(y \in [1,k])$ 都有贡献，所以：
$$
\sum_{i=1}^{N}\sum_{j=1}^{N}{A_i\times A_j\times [dt|A_i][dt|A_j]}=(\sum_{i=1}^{N}A_i\times [dt|A_i])^2
$$

$$
\begin{aligned}
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)&=\sum_{d=1}^{Max}\sum_{t=1}^{\lfloor \frac{Max}{d} \rfloor}\frac{\mu(t)}{d}(\sum_{i=1}^{N}A_i\times [dt|A_i])^2
\end{aligned}
$$

我们发现 $A_i$ 的值域只有 $10^6$ ，所以我们可以用 $c_i$ 表示有多少个 $i$，这样就有：
$$
\sum_{i=1}^{N}A_i\times [dt|A_i]=\sum_{dt|i}^{Max}i\times c_i
$$
$\sum_{T|i}^{Max}i\times c_i$显然可以用类似筛法的一个东西用 $O(nlog(n))$的方法求出对于每一个 $T$ 的值，具体的时间复杂度证明大概就是（虽然极为不严谨）：
$$
\int_{1}^{n}\frac{n}{x}\ dx \sim n\times\ln(n)
$$
当然如果你做过[这道题](https://www.luogu.com.cn/problem/P5495)，并掌握了 $4$ 种卷集，那么你也可以用 $O(nloglog(n))$ 的时间复杂度解决它。

现在我们的式子变成了：
$$
\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)=\sum_{d=1}^{Max}\sum_{t=1}^{\lfloor \frac{Max}{d} \rfloor}\frac{\mu(t)}{d}(\sum_{dt|i}^{Max}i\times c_i)^2
$$
那么我们只需要枚举 $d$ 再枚举 $t$ 就可以利用 $O(nlog(n))$ 的时间算出答案。
既然我们已经计算出了 $\sum_{i=1}^{N}\sum_{j=1}^{N}\mathrm{lcm}(A_i,A_j)$ 的值，我们把它减去 $\sum_{i=1}^{N}{A_i}$ ，再除 $2$，就可以算出答案了。

写的时候注意一下常数，少一点除法 QAQ

```cpp
int n, m, a[N], p[M], c, f[M], mu[M];
modint C[M], Ans, Mu[M];

int main() {
	read(n), Build_Mod(998244353);
	for (int i = 1; i <= n; i++) read(a[i]), m = max(m, a[i]);
	mu[1] = 1;
	for (int i = 2; i <= m; i++) {
		if (!f[i]) p[++c] = i, f[i] = 1, mu[i] = -1;
		for (int j = 1; j <= c && i * p[j] <= m; j++) {
			f[i * p[j]] = 1, mu[i * p[j]] = -mu[i];
			if (i % p[j] == 0) {mu[i * p[j]] = 0; break;}
		}
	}
	for (int i = 1; i <= n; i++) C[a[i]] += a[i];
	for (int j = 1; j <= c; j++)
		for (int i = m / p[j]; i >= 1; i--)
			C[i] += C[i * p[j]];
	for (int i = 1; i <= m; i++) Mu[i] = Ch(mu[i]), C[i] = C[i] * C[i];
	for (int i = 1; i <= m; i++) {
		modint t = (modint)1 / i;
		for (int j = 1; j <= m / i; j++)
			Ans += Mu[j] * C[i * j] * t;
	}
	for (int i = 1; i <= n; i++) Ans -= a[i];
	print(Ans / 2);
	return 0;
}
```

