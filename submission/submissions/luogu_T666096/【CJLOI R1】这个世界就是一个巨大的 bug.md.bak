# 【CJLOI R1】这个世界就是一个巨大的 bug

## 题目描述

具体的来说，我们认为在地球表面和真正危险的外界隔着 $n$ 个不同的层。

每一个层上都只有一个空洞，为了精确的描述他们的位置，我们将这些层纵向等分为 $m$ 个区间。第 $i$ 个层的空洞位于 $[l_i,r_i]$ 区间内。

我们认为真正的 bug 会降临，当且仅当存在一条路径，只经过空洞对应的区间，就可以从最上面的第 $1$ 层的某一个位置开始，下降到第 $n$ 层。需要注意的是，真正的 bug 可以从第 $i$ 层下降到第 $i+1$ 层，当且仅当存在一个位置 $x$，满足 $x\in[l_i,r_i]$ 且 $x\in[l_{i+1},r_{i+1}]$。

不过层与层间界限不分明，这意味着不同的层之间可以自由的交换顺序。这是防止真正的 bug 降临的重要防线！

然而，界限不分明的副作用是相邻的层可能会发生合并。具体的来说，如果第 $L$ 至 $R$ 层发生了合并，那么这个大层的空洞位置是 $\cup_{i=L}^R[l_i,r_i]$。也就是说原先各个层的空洞都会成为真正的 bug 可以经过的位置。

好在你具有一些特殊的超能力：你可以随意地控制层与层之间的顺序，也可以随意的合并相邻的层。

合并过后的层算作一层，但是一旦合并，你就不能够分开他们了。

你的目标是保证真正的 bug 无法降临的前提下，将层数合并到最小。

如果无论你怎么重新排列，都无法保证真正的 bug 无法降临，请输出 `1145141919810`。

为了防止“不可以，总司令”一类的情况出现，你需要多次回答这个问题。

### 形式化

有 $n$ 个集合，第 $i$ 个集合 $S_i$ 初始状态下为 $[l_i,r_i]\cap\mathbb{Z}$。第 $i$ 个与第 $i+1$ 个相邻。

定义两个相邻的集合 $A,B$ 合并后的结果为 $A\cup B$。定义其可达为 $A\cap B\neq\emptyset$。定义 $S_l$ 和 $S_r$ 可达当且仅当 $\forall i\in[l,r-1],S_l$ 和 $S_{l+1}$ 可达。

你可以任意多次的重排集合的顺序，或者合并两个集合。请问最少剩下多少个集合才能保证第一个集合与最后一个集合不可达？

如果一定可达，输出 `1145141919810`。

## 输入格式

第一行一个整数 $t$，表示询问组数。

对于每组数据，第一行两个整数 $n,m$。

接下来 $n$ 行，每行两个整数 $l_i,r_i$。

## 输出格式

共 $t$ 行，每行一个整数，表示最少剩余的层数。

## 提示

### 样例解释

对于第一组询问，无论怎么排布与合并，$2$ 总是可达的，因此你无法保证真正的 bug 无法降临。

对于第二组询问，两种可行的方案如图所示：

![](https://cdn.luogu.com.cn/upload/image_hosting/vjjs952v.png)

对于第三组询问，一种可行的方案如图所示：

![](https://cdn.luogu.com.cn/upload/image_hosting/mj5u3yi8.png)

### 数据范围

对于所有数据，保证 $t\le10^3,n,m\le5\times 10^3,1\le l_i\le r_i\le m$。具体范围如下：

| Subtask | $n\le$ | $m\le$ | 分值 |
|:-:|:-:|:-:|:-:|
| $0$ | $4$ | $5$ | $20$ |
| $1$ | $10^3$ | $10^3$ | $60$ |
| $2$ | $5\times10^3$ | $5\times10^3$ | $20$ |

特别的，因为本题输入量偏大，我们提供快读快写模板。你可以使用 `io.read()` 读入一个整数，使用 `io.write` 输出一个整数，`io.puts` 输出一个字符串。

```cpp
#define sipt
#define sopt
struct IO {
#define mxsz (1 << 21)
	char buf[mxsz], * p1, * p2;
	char pbuf[mxsz], * pp; bool acc[128];
	IO() : p1(buf), p2(buf), pp(pbuf) {}
	~IO() { fwrite(pbuf, 1, pp - pbuf, stdout); }
	inline char gc() {
		if (p1 == p2) p2 = (p1 = buf) + fread(buf, 1, mxsz, stdin);
		return p1 == p2 ? ' ' : *p1++;
	}
	inline void setacc(const char* c) { while (*c) acc[*c++] = 1; }
	inline char getc() { char c; while (!acc[c = gc()]); return c; }
#ifndef sipt
	inline int read() {
		int r = 0; char c = gc(); while (c < '0' || c>'9') c = gc();
		while (c >= '0' && c <= '9') r = r * 10 + (c ^ 48), c = gc();
		return r;
	}
#else
	inline int read() {
		int r = 0; char c = gc(); bool rev = 0;
		while (c < '0' || c>'9') rev |= (c == '-'), c = gc();
		while (c >= '0' && c <= '9') r = r * 10 + (c ^ 48), c = gc();
		return rev ? ~r + 1 : r;
	}
#endif
	inline void push(const char& c) {
		if (pp - pbuf == mxsz) fwrite(pbuf, 1, mxsz, stdout), pp = pbuf;
		*pp++ = c;
	}
	inline void write(int x) {
		static char sta[22]; int top = 0;
		do sta[top++] = x % 10, x /= 10; while (x);
		while (top) push(sta[--top] ^ 48);
	}
	inline void write(int x, char opc) {
#ifdef sopt
		if (x < 0) push('-'), x = ~x + 1;
#endif
		write(x), push(opc);
	}
	inline void puts(const char* c) { while (*c) push(*c++); }
} io;
```

## 时空限制

时间限制: 1000 ms
内存限制: 512 MB
