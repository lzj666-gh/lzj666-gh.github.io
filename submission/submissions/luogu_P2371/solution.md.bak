# P2371 题解

## Description

对于等式 $a_1x_1 + a_2x_2 + \cdots + a_nx_n = B\ \left(B \in \left[l,r \right] \right)$，已知 $n\ (1 \leq n \leq 12)$，$a_i\ (0 \leq a_i \leq 5 \times 10^5)$，$l, r\ (1 \leq l \leq r \leq 10^{12})$，求有多少 $B$ 可以使该等式存在非负整数解。

## Solution

很容易想到 **完全背包**，用 $f_i$ 表示 $B$ 的值能否为 $i$，那么转移方程为

$$\large {f_j = f_j \mid f_{j - a_i}}$$

还可以用 $\rm bitset$ 优化，时间复杂度为 $O(\frac{nr}{w})$ 。

$l, r$ 很大，上述方法显然行不通。

我们可以分别求出 $0 \sim r$ 中符合条件的 $B$ 的数量 和 $0 \sim l - 1$ 中符合条件的 $B$ 的数量，前者减去后者即是答案。现在假设 $mn$ 是 $a_i$ 中的一个数，那么对于 $a_1x_1 + a_2x_2 + \cdots + a_nx_n = i$，都满足 $a_1x_1 + a_2x_2 + \cdots + a_nx_n = i + k \times mn\ (k \in \rm N)$ 。在这个式子中，显然 $i$ 越小，符合条件的数就会越多。

我们可以用 $dis_i$ 表示 $B$ 模 $mn$ 等于 $i$ 时的最小值。接下来连有向边 $i \to (i + a_j) \bmod mn$，其中 $0 \leq i < mn$，边权为 $a_j$，表示从 $i$ 变为 $i + a_j$ 所花费的代价是 $a_j$ 。$0$ 到 $i$ 的最短路即是 $B$ 模 $mn$ 等于 $i$ 时的最小值。假定现在要求 $0 \sim x$ 中符合条件的 $B$ 的数量，若这个最小值不大于 $x$，则所有的 $i + k \times mn\ (i + k \times mn \leq x,k \in \rm N)$ 都符合条件，一共有 $\left \lfloor \frac{x - dis_i}{mn} \right \rfloor + 1$ 个。

所以枚举 $i$，累加就能得到答案。同时 $mn$ 取所有 $a_i$ 的最小值最优，因为这样边数最少。时间复杂度为 $O(kn\max\limits_{i = 1}^n\{ a_i \})$ 。由于特殊的连边，$\rm SPFA$ 不会被卡，可以放心使用。

我们一般称这种算法为 **同余最短路** 。

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

template <class T>
inline void read(T &x) {
    x = 0;
    char c = getchar();
    bool f = 0;
    for (; !isdigit(c); c = getchar()) f ^= c == '-';
    for (; isdigit(c); c = getchar()) x = x * 10 + (c ^ 48);
    x = f ? -x : x;
}

template <class T>
inline void write(T x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    T y = 1;
    int len = 1;
    for (; y <= x / 10; y *= 10) ++len;
    for (; len; --len, x %= y, y /= 10) putchar(x / y + 48);
}

const int MAXN = 5e5, MAXM = 6e6;
const LL INF = 1e12;
int n, m, mn = MAXN + 5, tot, a[MAXN + 5], head[MAXN + 5];
LL l, r, dis[MAXN + 5];
bool vis[MAXN + 5];
struct Edge {
    int next, to, dis;
} e[MAXM + 5];

inline void addEdge(int u, int v, int w) {
    e[++tot] = (Edge) { head[u], v, w };
    head[u] = tot;
}

inline void spfa(int s) {
    for (int i = 0; i < mn; ++i) dis[i] = INF + 1;//初始化 
    queue<int> q;
    dis[s] = 0;//满足模 mn 等于 0 的最小的 B 是 0
    q.push(s);
    for (; !q.empty(); ) {
        int u = q.front();
        q.pop();
        vis[u] = 0;
        for (int v, w, i = head[u]; v = e[i].to, w = e[i].dis, i; i = e[i].next)
            if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                if (!vis[v]) {
                    q.push(v);
                    vis[v] = 1;
                }
            }
    }
}

inline LL query(LL x) {//求出 0 ~ x 中符合条件的 B 的数量 
    LL res = 0;
    for (int i = 0; i < mn; ++i)
        if (dis[i] <= x)
            res += (x - dis[i]) / mn + 1;//累加答案 
    return res;
}

int main() {
    read(n), read(l), read(r);
    for (int x, i = 1; i <= n; ++i) {
        read(x);
        if (x) {//a[i] = 0 可以跳过，因为没有贡献 
            a[++m] = x;
            mn = min(mn, x);//求出最小且非 0 的 a[i] 作为 mn 的值 
        }
    }
    n = m;
    for (int i = 0; i < mn; ++i)
        for (int j = 1; j <= n; ++j)
            if (a[j] != mn)//自己向自己没必要连边 
                addEdge(i, (i + a[j]) % mn, a[j]);//连有向边 
    spfa(0);//从 0 开始
    write(query(r) - query(l - 1));
    putchar('\n');
    return 0;
}
```