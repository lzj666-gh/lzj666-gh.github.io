# P1155 题解

## 题意

给你一个长为 $n$ 的序列 $p$ ，问是否能够通过对于两个栈进行 `push, pop(print)` 操作使得最后输出序列单调递增（即为 $1 \cdots n$ ），如果无解输出 $0$ 。

每个操作有个优先级，`push(1) > pop(1) > push(2) > pop(2)` ，输出优先级最大的一组解。

$n \le 1000$

## 题解

有兴趣可以来逛逛 [我的博客](https://www.cnblogs.com/zjp-shadow/p/9831491.html)。

> 洛谷前面大部分题解，对于后面直接模拟的思路肯定是错的，本文介绍一个基于贪心的算法（不知道对不对，因为没有强数据验证）。

首先考虑只有一个栈的时候如何解决这个问题。

就是对于一对位置 $(i, j)$ 是否能共存三个位置 $i < j < k$ 存在 $p_k < p_i < p_j$ 是不可行的，因为 $p_k$ 需要在 $p_i$ 与 $p_j$ 之前出栈，但 $p_i$ 又需要在 $p_j$ 之前出栈，那么这就会产生矛盾。

我们预处理 $\displaystyle f_i = \min_{j = i}^{n} p_j$ ，就可以在 $O(n ^ 2)$ 的时间内判断一对 $i, j$ 是否可以共存了（也就是 $f_{j + 1} < p_i < p_j$ ）

然后对于存在两个栈的情况，我们就需要把 $p$ 划分成两个序列，使得这两个序列之中的数都互不冲突。

这样的话，我们对于一对不能共存的 $i, j$  连边，然后进行二分图染色。如果不可染，那么就是不存在一组合法解。

之后我们只需要解决使得最后解字典序最小的限制。

我们染色的时候 `BFS` 染色，尽量把在前面的放入第一个栈。

然后后面得到操作序列直接模拟肯定是个错的。

> 举个样例：
>
> ```
> 5
> 2 4 1 3 5
> ```
>
> 标准输出：
>
> ```
> a c a b b a b a d b 
> ```
>
> 前面大部分错误的输出：
>
> ```
> a c a b b a b d a b 
> ```

为什么呢，因为你向第二个栈 `push` 后，不一定现在拿出来 `pop` ，第一个栈中能继续 `push` 。

那么我们就贪心一下，我们在 `push` 之后不马上 `pop` ，等到需要 `pop` 的时候再 `pop` 。

哪些时候需要 `pop` 呢，就是这个栈不合法的时候需要 `pop` （也就是这个栈 栈顶到栈底 不单调递增的时候，不满足单调栈性质）

但是注意向第二个栈中 `push` 之前，因为第一个栈的 `pop` 优先级更高，我们看能不能先 `pop` 第一个栈。

这样就应该是最优的了，注意最后要把两个栈按顺序清空。

## 代码

```cpp

#include <bits/stdc++.h>

#define For(i, l, r) for(register int i = (l), i##end = (int)(r); i <= i##end; ++i)
#define Fordown(i, r, l) for(register int i = (r), i##end = (int)(l); i >= i##end; --i)
#define Set(a, v) memset(a, v, sizeof(a))
#define Cpy(a, b) memcpy(a, b, sizeof(a))
#define debug(x) cout << #x << ": " << (x) << endl
#define DEBUG(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back

using namespace std;

template<typename T> inline bool chkmin(T &a, T b) { return b < a ? a = b, 1 : 0; }
template<typename T> inline bool chkmax(T &a, T b) { return b > a ? a = b, 1 : 0; }

inline int read() {
    int x(0), sgn(1); char ch(getchar());
    for (; !isdigit(ch); ch = getchar()) if (ch == '-') sgn = -1;
    for (; isdigit(ch); ch = getchar()) x = (x * 10) + (ch ^ 48);
    return x * sgn;
}

void File() {
#ifdef zjp_shadow
	freopen ("P1155.in", "r", stdin);
	freopen ("P1155.out", "w", stdout);
#endif
}

const int N = 1010, inf = 0x7f7f7f7f;

int n, P[N], minv[N], col[N];

int pos = 1;
stack<int> S[2];

inline void out(char ch) {
	putchar (ch); putchar (' ');
}

inline bool Pop(int id) {
	if (!S[id].empty() && S[id].top() == pos) {
		out(id ? 'd' : 'b'), S[id].pop(), ++ pos;
		return true;
	}
	return false;
}

inline void Push(int cur, int id) {
	if (id == 1) { while(Pop(0)); }
	while (!S[id].empty() && S[id].top() < cur)
		if (!Pop(id)) Pop(id ^ 1);
	if (id == 1) { while(Pop(0)); }
	S[id].push(cur); out(id ? 'c' : 'a');
}

vector<int> G[N];

int main () {

	File(); 
	n = read();

	For (i, 1, n)
		P[i] = read();

	minv[n + 1] = n + 1;
	Fordown (i, n, 1)
		minv[i] = min(minv[i + 1], P[i]);

	For (i, 1, n) For (j, i + 1, n) 
		if (minv[j + 1] < P[i] && P[i] < P[j])
			G[i].pb(j), G[j].pb(i), col[i] = col[j] = -1;

	For (i, 1, n) if (!~col[i]) {
		queue<int> Q; Q.push(i); col[i] = 0;
		while (!Q.empty()) {
			int u = Q.front(); Q.pop();
			for (int v : G[u]) {
				if (~col[v] && col[v] != (col[u] ^ 1)) return puts("0"), 0;
				if (!~col[v]) Q.push(v);
				col[v] = col[u] ^ 1;
			}
		}
	}

	For (i, 1, n)
		Push(P[i], col[i]);

	bool flag = true;
	while (flag) {
		flag = false;
		while(Pop(0)) flag = true;
		while(Pop(1)) flag = true;
	}

	return 0;

}

```

