# P3199 题解

对于这个东西，有一个结论（Karp1977年的论文）：

我们新建一个节点，从它到每个点连一条权值任意的边（比如都是0），再令$F_j(i)$表示从新建的点到$i$点恰好经过$j$条边的最短路，那么有

$$ans=\min_{1\leq i\leq n, F_{n+1}(i)\neq\infty}\max_{j=1}^{n}\left[\frac{F_{n+1}(v)-F_k(v)}{n+1-k}\right]$$

具体证明请看[我的博客](http://www.cnblogs.com/y-clever/p/7043553.html)

虽然代码不是跑的最快的但是理论复杂度低（没办法，数据不卡SPFA），是$O(nm)$的（而且代码也是最短的，只有0.71KB，不比Dijkstra难写）

```cpp
#include <algorithm>
#include <cstdio>
const int N = 3050;
const int M = 10050;
const double INF = 1e12;
double F[N][N], w[M];
int u[M], v[M];
int main() {
  int n, m, i, j;
  scanf("%d%d", &n, &m);
  for (i = 0; i < m; ++i)
    scanf("%d%d%lf", &u[i], &v[i], &w[i]);
  for (i = 0; i <= n; ++i)
    for (j = 1; j <= n; ++j)
      F[i][j] = i ? INF : 0;
  for (i = 0; i < n; ++i)
    for (j = 0; j < m; ++j)
      F[i + 1][v[j]] = std::min(F[i + 1][v[j]], F[i][u[j]] + w[j]);
  double ans = 1e7, ans1;
  for (i = 1; i <= n; ++i) if (F[n][i] < 1e11) {
    ans1 = -INF;
    for (j = 0; j < n; ++j)
      ans1 = std::max(ans1, (F[n][i] - F[j][i]) / (n - j));
    ans = std::min(ans, ans1);
  }
  printf("%.8lf\n", ans);
  return 0;
}

```
下面还有一个空间复杂度极低（70MB->1.9MB），稍长一点（0.71KB->0.98KB），稍慢一点（3936ms->4468ms）的实现，算了两遍，滚动数组（实际上，上面的代码在BZOJ上MLE，因为BZOJ这题空间64M）

```cpp
#include <algorithm>
#include <cstdio>
const int N = 3050;
const int M = 10050;
const double INF = 1e12;
double _F[2][N], Fn[N], w[M], maxv[N];
int u[M], v[M];
int main() {
  int n, m, i, j;
  scanf("%d%d", &n, &m);
  for (i = 0; i < m; ++i)
    scanf("%d%d%lf", &u[i], &v[i], &w[i]);
  double *F = _F[0], *G = _F[1];
  for (i = 1; i <= n; ++i)
    G[i] = 0;
  for (i = 0; i < n; ++i, std::swap(F, G)) {
    for (j = 1; j <= n; ++j) F[j] = INF;
    for (j = 0; j < m; ++j)
      F[v[j]] = std::min(F[v[j]], G[u[j]] + w[j]);
  }
  for (i = 1; i <= n; ++i) Fn[i] = G[i];
  double ans = 1e7;
  for (i = 1; i <= n; ++i)
    maxv[i] = Fn[i] / n, G[i] = 0;
  for (i = 0; i < n; ++i, std::swap(F, G)) {
    for (j = 1; j <= n; ++j) F[j] = INF;
    for (j = 0; j < m; ++j)
      F[v[j]] = std::min(F[v[j]], G[u[j]] + w[j]);
    for (j = 1; j <= n; ++j) maxv[j] = std::max(maxv[j], (Fn[j] - F[j]) / (n - i - 1));
  }
  for (i = 1; i <= n; ++i) if (Fn[i] < 1e11) ans = std::min(ans, maxv[i]);
  printf("%.8lf\n", ans);
  return 0;
}
```