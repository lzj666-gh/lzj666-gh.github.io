# AT_agc016_d 题解

在博客园食用更佳：[https://www.cnblogs.com/PinkRabbit/p/AGC016.html](https://www.cnblogs.com/PinkRabbit/p/AGC016.html)。

令初始的异或和为 $x$，拿在手中，相当于每次用手中的数把 $a$ 中的一个值顶掉，然后把原来的值拿在手里。

那么可以先判一下 $b$ 是否一定能被得到：只需判 $b$ 的可重集是否包含于 $a \cup \{x\}$ 即可。

然后我们考虑一个过程，用 $x$ 替换了 $a_p$，然后用 $a_p$ 替换了 $a_q$，循环下去。

其实最终一定是要用 $b_i$ 替换 $a_i$ 的，而上面的过程又是从 $x$ 出发走了一条路。

这启发我们从 $b_i$ 向 $a_i$ 连边（不同位置上相同的数值对应同一个点），然后尝试从 $x$ 出发遍历每条边。

注意如果图是一个包含 $x$ 的连通块，则一定可以找到一条欧拉路径（不一定是回路）覆盖所有边。

如果图不连通，或 $x$ 不在连通块内（$x$ 是孤立点），则答案就是边数再加上连通块数再减去 $1$（如果 $x$ 是孤立点就不用减 $1$）。

```cpp
#include <cstdio>
#include <vector>
#include <map>

const int MN = 100005;

int N, A[MN], B[MN], X, cnt, M, Ans;
std::map<int, int> mp;

int vis[MN];
std::vector<int> G[MN];
void DFS(int u) {
	vis[u] = 1;
	for (int v : G[u]) if (!vis[v]) DFS(v);
}

int main() {
	scanf("%d", &N);
	for (int i = 1; i <= N; ++i) scanf("%d", &A[i]), ++mp[A[i]], X ^= A[i];
	for (int i = 1; i <= N; ++i) scanf("%d", &B[i]), --mp[B[i]];
	++mp[X];
	for (auto p : mp) if (p.second < 0) return puts("-1"), 0;
	for (auto &p : mp) p.second = ++cnt;
	for (int i = 1; i <= N; ++i) if (A[i] != B[i]) {
		int u = mp[B[i]], v = mp[A[i]];
		G[u].push_back(v);
		G[v].push_back(u);
		++M;
	}
	for (int i = 1; i <= cnt; ++i) if (!G[i].empty())
		if (!vis[i]) ++Ans, DFS(i);
	if (!G[mp[X]].empty()) --Ans;
	printf("%d\n", M + Ans);
	return 0;
}
```