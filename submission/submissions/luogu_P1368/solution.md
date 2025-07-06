# P1368 题解

> 怎么没人用 Lyndon 分解求最小表示法呢？它这么冷门的嘛...

## Lyndon 串

对于一个字符串，若其本身就是其最小后缀，则称它为 Lyndon 串。

形式化地，对于长度为 $n$ 的字符串 $s$，若满足对于 $i \in [2,n]$，都有 $s < s[i:n]$，则称其为 Lyndon 串。

## Lyndon 分解

任意一个字符串都可以被唯一的分解成若干个字典序非严格递减的 Lyndon 串。

形式化地，对于长度为 $n$ 的字符串 $s$，存在唯一的若干个 Lyndon 串 $t_{1\dots m}$，满足 $s=t_1 + t_2 + \cdots + t_m$ 且 $t_1 \ge t_2 \ge \cdots \ge t_m$。

## Duval 算法

Duval 算法可以在 $\mathcal O(n)$ 的时间求出一个字符串的 Lyndon 分解。

维护三个指针 $i,j,k$，这三个指针将整个字符串分成了四个部分 $s[1:i-1], s[i,k-1], s[j,k-1], s[k,n]$：

- $s[1,i-1]$：这部分的 Lyndon 分解已经完成。
- $s[i,k-1]$：这部分可以被表示成 $t^c + v$，其中 $t$ 是一个 Lyndon 串，$t^c$ 表示 $t$ 循环 $c$ 次，$v$ 是 $t$ 的一个可空真前缀。
- $s[j,k-1]$：注意这部分是包含在上一个部分中的，其中 $j = k - |t|$。
- $s[k,n]$：这部分还未处理，此时正在考虑 $k$。

考虑 $k$ 有三种情况：

- $s_j = s_k$：可以将 $t$ 继续循环下去，因此 $j$ 往后移一位，考虑下一个 $k$。
- $s_j < s_k$：可以将 $t^c + v + s_k$ 合并为一个 Lyndon 串，因此 $j$ 设为 $i$，考虑下一个 $k$。
- $s_j > s_k$：可以将 $t$ 单独作为 Lyndon 分解中的一个串，然后从 $v$ 的开头开始重新考虑，因此 $i$ 设为 $v$ 的开头，$j,k$ 对应设为 $i,i+1$。

#### 【模板】[P6114 【模板】Lyndon 分解](https://www.luogu.com.cn/problem/P6114)

```cpp
const int N = 5e6 + 7;
int n, ans;
char s[N];

int main() {
	rds(s, n);
	int i = 1;
	while (i <= n) {
		int j = i, k = i + 1;
		while (k <= n && s[j] <= s[k]) j = s[j] == s[k++] ? j + 1 : i;
		while (i <= j) i += k - j, ans ^= i - 1;
	}
	print(ans);
	return 0;
}
```

## 最小表示法

一个字符串的**最小表示**定义为其所有循环同构中字典序最小的串。

形式化地，对于长度为 $n$ 的字符串 $s$，若 $p \in [1,n]$ 满足对于 $i \in [1, n]$，都有 $s[p:n] + s[1:p-1] \le s[i:n] + s[1:i-1]$，则称 $s[p:n] + s[1:p-1]$ 为 $s$ 的最小表示。

最小表示法可以使用 Lyndon 分解求出。

对于长度为 $n$ 的字符串 $s$，设 $t = s + s$，对 $t$ 进行 Lyndon 分解，找到首字符位置 $\le n$ 且最大的 Lyndon 串，这个串的首字符即最小表示法的首字符。

#### 【模板】[P1368 工艺 /【模板】最小表示法](https://www.luogu.com.cn/problem/P1368)

```cpp
const int N = 6e5 + 7;
int n, ans, s[N];

int main() {
	rd(n);
	for (int i = 1; i <= n; i++) rd(s[i]), s[i+n] = s[i];
	int i = 1;
	while (i <= n) {
		int j = i, k = i + 1;
		while (k <= n * 2 && s[j] <= s[k]) j = s[j] == s[k++] ? j + 1 : i;
		while (i <= j) i += k - j, ans = i <= n ? i : ans;
	}
	if (ans == 0) ans = n;
	for (int i = 1; i <= n; i++) print(s[ans-1+i], " \n"[i==n]);
	return 0;
}
```

#### 【例题】[UVA719 Glass Beads](https://www.luogu.com.cn/problem/UVA719)

与上一题不同的是，这题要求位置最靠前。

只有一种情况下两道题的答案不一样，那就是字符串恰好为一个循环串的时候。

那么我们换一个写法即可。

```cpp
const int N = 2e4 + 7;
int n, ans;
char s[N];

inline void solve() {
	rds(s, n);
	for (int i = 1; i <= n; i++) s[i+n] = s[i];
	int i = 1;
	while (i <= n) {
		ans = i;
		int j = i, k = i + 1;
		while (k <= n * 2 && s[j] <= s[k]) j = s[j] == s[k++] ? j + 1 : i;
		while (i <= j) i += k - j;
	}
	print(ans);
}

int main() {
	int T;
	rd(T);
	while (T--) solve();
	return 0;
}
```

## 参考资料

- OI Wiki [Lyndon 分解](https://oi-wiki.org/string/lyndon/#finding-the-smallest-cyclic-shift)
- wucstdio [题解 P6127 【【模板】Lyndon 分解】](https://www.luogu.com.cn/blog/wucstdio/solution-p6127)