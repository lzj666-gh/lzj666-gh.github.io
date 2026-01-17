# 【CJLOI R1】三千万转，响彻这罪业回环

## 题目描述

在翁法罗斯，一次逐火分为 $n$ 个阶段，每个阶段都有 $a_i$ 种不同的方式达成目标，阶段与阶段之间互不干扰，且只能顺次完成。

现在，白厄想请你算一下从第 $l$ 个阶段开始，到第 $r$ 个阶段结束，一共有多少种方案可以达成目标。

白厄经历了 $33550336$ 个轮回，所以他会询问你 $m$ 次。

由于白厄历经了千万次轮回，早已对历史烂熟于心，所以**每个阶段达成目标的方式数不会改变**，且会在程序开始运行时告诉你。

由于方案数可能过多，所以你只需要告诉他方案数对**整数** $p$ 取模的结果就可以了。

由于白厄对于小细节都记得很清楚了，他也就不需要询问你一些细枝末节的东西，所以询问你的区间长度会在 $x$ 到 $2x$ 之间。

### 形式化题意

给定一个长度为 $n$ 的序列 $a$，给定 $m$ 次询问，求区间 $[l,r]$ 的乘积（$x\le r-l+1\le 2x$，取余 $p$）。

## 输入格式

第一行，两个整数，表示 $n,m,x,p$，含义如题目中所示。

接着，我们会给你一个随机数种子 $state$ 作为以下代码中变量 $state$ 的随机值（$state < 2^{32}$）。

$$
\begin{aligned}
&\text{函数 } \mathit{next\_random}(): \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \ll 13) \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \gg 17) \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \ll 5) \\
&\quad While \space \mathit{state}\ge2^{32}:\\
&\quad\quad \mathit{state} \leftarrow \mathit{state} \space - \space 2^{32}\\
&\quad \text{返回 } \mathit{state} \\
\\
&\mathit{min\_len} \leftarrow x \\
&\mathit{max\_len} \leftarrow \min(2x, n) \\
&\mathit{range\_len} \leftarrow \mathit{max\_len} - \mathit{min\_len} + 1 \\
&\mathit{rand} \leftarrow \mathit{next\_random}() \\
&\mathit{len} \leftarrow \mathit{min\_len} + (\mathit{rand} \mod \mathit{range\_len}) \\
\\
&\mathit{low\_l} \leftarrow 1 \\
&\mathit{high\_l} \leftarrow n - \mathit{len} + 1 \\
&\mathit{range\_l} \leftarrow \mathit{high\_l} - \mathit{low\_l} + 1 \\
&\mathit{rand\_l} \leftarrow \mathit{next\_random}() \\
&\mathit{l} \leftarrow \mathit{low\_l} + (\mathit{rand\_l} \mod \mathit{range\_l}) \\
\\
&\mathit{r} \leftarrow l + \mathit{len} - 1 \\
\end{aligned}
$$

然后，你需要调用 $n$ 次 $next\_random$ 函数，第 $i$ 次调用返回的整数表示第 $i$ 个逐火的阶段的方案数 $a_i$。

接下来，你需要调用 $m$ 次生成器，每次生成器会给出查询区间 $l,r$，对于每一次的查询请输出答案对 $p$ 取模后的结果。

## 输出格式

我们定义最终答案为 $result$，第 $i$ 次查询的答案为 $ans_i$，则 $result=(\sum_{i=1}^{m}ans_i\times i)\pmod p$。

你只需要输出 $result$ 即可。

## 提示

对于所有数据 $1\le n\le 10^7,1\le m\le 33550336,1\le x\le n,2\le p\le 10^9+7,1\le state < 2^{32},1\le a_i\le10^9$。

**注意：$p$ 不一定为素数。**

|  测试点编号  |$n$       |$m$       |$p$       |
|:--:|:--------:|:--------:|:--------:|
|$1 \sim 2$|$\le 10^3$|$\le 10^3$|$\le 10^9+7$|
|$3$|$\le 10^6$|$\le 10$|^|
|$4$|$\le 10$|$\le 10^6$|^|
|$5 \sim 8$|$\le 182375$|$\le 182375$|^|
|$9 \sim 10$|$\le 10^7$|$\le 33550336$|$=10^9+7$|
|$11$|^|^|$=999911658$|
|$12$|^|^|$=96841527$|
|$13$|^|^|$=19198101$|
|$14$|^|^|$=246248468$|
|$15 \sim 17$|^|$\le 10^7$|$\le 10^9+7$|
|$18 \sim 20$|^|$\le 33550336$|^|



以下是输入并生成查询的c++代码，仅供参考理解输入输出格式。

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN = 1e7;
int n, m, x, p;
int a[MAXN + 10];
unsigned int state;
inline unsigned int next_random() {
	state = state ^ (state << 13);
	state = state ^ (state >> 17);
	state = state ^ (state << 5);
	return state;
}
int main() {
	cin.tie(0)->sync_with_stdio(false);
	cin >> n >> m >> x >> p >> state;
	for (int i = 1; i <= n; i++) a[i] = next_random() % p;
	unsigned int result = 0;
	int min_len = x, max_len = min(2 * x, n), range_len = max_len - min_len + 1;
	for (int i = 1; i <= m; i++) {
		int len = min_len + (next_random() % range_len);
		int l = 1 + (next_random() % (n - len + 1)), r = l + len - 1;

		int ans = 0;

		// do your things here.

		result ^= ans;
	}
	cout << result << endl;
	return 0;
}
```

## 时空限制

时间限制: 5000 ms
内存限制: 512 MB
