# P11230 题解

容易发现是图论题，建模就是每个位置往他能接的位置连边，于是不妨先考虑给定一个一般的有向图怎么做。简单的想法是预处理出所有答案，你可以用一个类似广搜的东西，从 $1$ 开始每次向外拓展一层，记录可达性即可，复杂度是 $O(nr)$ 的。

但是这题的图边数特别多，那我们干脆不建边了，直接去判断每个点能否被当前的点到达。每次记录的就是当前接龙的最后一个数。

题目有个很烦的限制，一个人不能接两次。但是可以发现，如果当前这一层的某个数 $x$ 同时在至少两个人的序列里，那么所有人的数 $x$ 都能接到下一个了。所以只要考虑只有一个人有 $x$ 的情况。开个数组记录这一层的每个数在谁手上，没有为 $-1$，有一个人 $i$ 有就设为 $i$，两个人及以上有设为 $0$。这样处理后就可以快速找出可以接到哪些位置上了。

然后再通过这些新接的头找出所有能接的尾巴。先对所有头打标记，然后遍历每一个位置，如果他距离上一个标记（不含自己）的距离 $\le k$ 就加入下一层的队列。重复做这个就好了，单组数据复杂度 $O(nr+q)$。

# AC 代码

```cpp
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int MAXN = 2e5 + 10;
const int MAXM = 1e2 + 10;

inline 
void read(int &x) {
	x = 0; char c = getchar();
	for (; isspace(c); c = getchar());
	for (; isdigit(c); c = getchar()) x = x * 10 + c - '0';
}

int T, n, m, q; int cnt[MAXN]; bool ans[MAXM][MAXN];

int a[MAXN]; bool vis[MAXN]; int pos[MAXN];

inline 
void init() {
	vector<pair<int, int>> f, g;
	for (int i = 1; i <= n; i++) {
		for (int j = pos[i], p = -1e9; j < pos[i + 1]; j++) {
			if (j - p < m) f.emplace_back(i, j), ans[1][a[j]] = 1;
			if (a[j] == 1) p = j;
		}
	}
	for (int t = 2; t <= 100; t++) {
		memset(cnt, 0xff, sizeof cnt);
		for (pair<int, int> x : f) {
			int y = a[x.second];
			if (cnt[y] == -1) cnt[y] = x.first;
			else if (cnt[y] != x.first) cnt[y] = 0;
		}
		for (int i = 1; i <= n; i++) {
			for (int j = pos[i]; j < pos[i + 1]; j++) {
				if (~cnt[a[j]] && cnt[a[j]] != i) g.emplace_back(i, j);
			}
		}
		f.clear();
		for (pair<int, int> x : g) vis[x.second] = 1;
		for (int i = 1; i <= n; i++) {
			for (int j = pos[i], p = -1e9; j < pos[i + 1]; j++) {
				if (j - p < m) f.emplace_back(i, j), ans[t][a[j]] = 1;
				if (vis[j]) p = j;
			}
		}
		for (pair<int, int> x : g) vis[x.second] = 0;
		g.clear();
	}
}

int main() {
	freopen("chain.in", "r", stdin);
	freopen("chain.out", "w", stdout);
	for (read(T); T--; ) {
		read(n), read(m), read(q);
		memset(ans, 0, sizeof ans);
		memset(vis, 0, sizeof vis);
		for (int i = 1, k; i <= n; i++) {
			read(k), pos[i + 1] = pos[i] + k;
			for (int j = pos[i]; j < pos[i + 1]; j++) read(a[j]);
		}
//		clock_t st = clock();
		init();
//		fprintf(stderr, "init time: %.3lfs\n", (double)(clock() - st) / CLOCKS_PER_SEC);
		for (int r, c; q--; read(r), read(c), printf("%d\n", ans[r][c]));
	}
}

```