# P3388 题解

- Update on 2023.6.26：重构题解，原题解见 [剪贴板](https://www.luogu.com.cn/paste/8tek61w5)。
- Update on 2024.8.9：修改题解。

摘自笔记 [图论 I](https://www.luogu.com.cn/article/amxn9li0)。

#### 无向图 DFS 树

给定无向连通图 $G$，从点 $r$ 开始 DFS，取出进入每个点 $i$ 时对应的边 $(fa_i, i)$ 并定向为 $fa_i\to i$，得到一棵以 $r$ 为根的树。称 $(fa_i, i)$ 为 **树边**，其它边为 **非树边**。

给每个点标号为它被访问到的次序，称为 **时间戳**，简称 dfn。DFS 得到的结点序列称为 **DFS 序**，时间戳为 $i$ 的结点在 DFS 序中的位置为 $i$。

![](https://cdn.luogu.com.cn/upload/image_hosting/9ljfysuq.png)

上图是一个可能的 DFS 树以及对应的时间戳。

无向图 DFS 树的性质（**非常重要**）：

- 祖先后代性：任意非树边两端具有祖先后代关系。
- 子树独立性：结点的每个儿子的子树之间没有边（和上一条性质等价）。
- 时间戳区间性：子树时间戳为一段区间。
- 时间戳单调性：结点的时间戳小于其子树内结点的时间戳。

### Tarjan 求割点

**前置知识**：DFS 树，DFS 序。

注意区分：DFS 序表示对一张图 DFS 得到的结点序列，而时间戳 dfn 表示每个结点在 DFS 序中的位置。

记 $x$ 的子树为 $x$ 在 DFS 树上的子树，包含 $x$ 本身，记作 $T(x)$。记 $T'(x) = V\backslash T(x)$，即整张图除了 $T(x)$ 以外的部分。

不妨认为 $G$ 是无向连通图。对于非连通图，对每个连通分量分别求割点。

笔者希望提出一种新的理解 Tarjan 算法的方式。网上大部分博客讲解 Tarjan 算法时 `low` 数组凭空出现，抽象的定义让很多初学者摸不着头脑，从提出问题到解决问题的逻辑链的不完整性让我们无法感受到究竟是怎样的灵感启发了这一算法的诞生。

#### 非根结点的割点判定

设 $x$ 不为 DFS 树的根，则 $T'(x)$ 非空。

若 $x$ 是割点，则删去 $x$ 之后，对于 $z\in T'(x)$，存在 $y$ 和它不连通。而删去 $x$ 之后 $T'(x)$ 通过树边仍然连通，所以 $y\in T(x)$。而如果 $y$ 和 $z$ 不连通，又因为 $T'(x)$ 连通，那么 $y$ 和所有 $T'(x)$ 的点均不连通。

反之，若删去 $x$ 之后存在 $y\in T(x)$ 和 $T'(x)$ 的点均不连通，那么 $x$ 显然是割点。这说明 $x$ 是割点当且仅当存在 $y\in T(x)$ 不经过 $x$ 能到达的所有点均属于 $T(x)$。

现在要刻画 “不经过 $x$ 能到达的所有点均属于 $T(x)$”。

注意到，如果 $y\in T(x)$ 不经过 $x$ 就和 $T'(x)$ 连通，那么存在 $y$ 到 $v\in T'(x)$ 的路径，满足 $v$ 是路径上第一个属于 $T'(x)$ 的结点。设路径上倒数第二个点为 $u$，则 $u\in T(x)$。如果 $(u, v)$ 是树边，那么 $u = x$，矛盾。因此 $(u, v)$ 是非树边，那么 $v$ 是 $u$ 的祖先（祖先后代性）。又因为 $x$ 是 $u$ 的祖先且 $v$ 在 $x$ 的子树外，所以 $v$ 是 $x$ 的祖先。如下图。

![](https://cdn.luogu.com.cn/upload/image_hosting/kolj8ax0.png)

进一步地，因为 $x$ 的不同儿子子树之间没有非树边（子树独立性），设 $x$ 的儿子 $y'$ 的子树包含 $y$，那么 $u\in T(y')$。

因此，如果 $y$ 不经过 $x$ 和 $T'(x)$ 连通，即 $x$ 不是割点，那么存在 $u\in T(y')$ 使得 $u$ 可以通过一条非树边到达 $x$ 的祖先。设 $f_x$ 表示与 $x$ 通过 **非树边** 相连的所有点的时间戳的最小值，则条件可写为 $f_u < d_x$。

- 对于 $T(y')$，如果存在 $u\in T(y')$ 满足 $f_u < d_x$，那么删去 $x$ 后 $T(y')$ 的每个点和 $T'(x)$ 均连通：$T(y')$ 内所有点通过树边连通，且 $u$ 和 $T'(x)$ 某点直接相连。

- 反之，如果 $T(y')$ 内所有点的 $f$ 值均不小于 $d_x$，那么删去 $x$ 后 $T(y')$ 的每个点和 $T'(x)$ 均不连通。因为如果连通，那么总得有一个点能一步连通。

这样，我们得到了非根结点的割点判定法则：

> $x$ 是割点当且仅当存在树边 $x\to y'$，使得 $y'$ 子树 **不存在** 点 $u$ 使得 $f_u < d_x$。
>
> 这等价于存在 $x$ 的儿子 $y'$，满足 $\min_{u\in T(y')} f_u \geq d_x$。

设 $g_x$ 表示 $x$ 的子树内所有点 $u\in T(x)$ 的 $f_u$ 的最小值（`low` 的真正含义），根据树形 DP，有
$$
g_x = \min\left(\min_{y'\in \mathrm{son}(x)} g_{y'}, \min_{(x, y) \in E\land (x, y)\notin T} d_y\right)
$$

对于后半部分，忽略 $(x, y)$ 必须是非树边的条件不会导致错误：如果用儿子更新，显然没有问题。如果用父亲更新，即用 $d_x$ 更新 $g_y$，也不会导致错误，因为判定是 $g_y\geq d_x$，有等号。但注意求解割边时不能忽略，因为判定是 $g_y > d_x$。

**说明**：将 $g_x$ 初始化为 $d_x$ 显然不会导致错误。

**应用**：研究删去 $x$ 后整张图的形态。删去 $x$ 后，每个判定 $x$ 为割点的 $y'$ 的 $T(y')$ 单独形成一个连通块，剩余部分（其它所有 $T(y')$ 和 $T'(x)$）形成一个连通块。因为判定割点的准则就是删去 $x$ 后 $y'$ 是否与 $T'(x)$ 连通。

#### 根的割点判定与代码

设 $x$ 为 DFS 树的根。

若 $x$ 在 DFS 树上有大于一个儿子，根据子树独立性，删去 $x$ 后各儿子子树不连通，所以 $x$ 是割点。反之删去 $x$ 后剩余部分通过树边连通，$x$ 不是割点。

综上，使用 Tarjan 算法求无向图 $G$ 的所有割点的时间复杂度为 $\mathcal{O}(n + m)$。

再次强调，以下代码仅在求解割点时正确。求解割边需要额外的特判。

[模板题](https://www.luogu.com.cn/problem/P3388) 代码。

```cpp
#include <bits/stdc++.h>
using namespace std;
constexpr int N = 1e5 + 5;
int n, m, R;
int dn, dfn[N], low[N], cnt, buc[N]; // dfn 是时间戳 d, low 是 g
vector<int> e[N];
void dfs(int id) {
  dfn[id] = low[id] = ++dn; // 将 low[id] 初始化为 dn 不会导致错误, 且一般都这么写
  int son = 0;
  for(int it : e[id]) {
    if(!dfn[it]) {
      son++, dfs(it), low[id] = min(low[id], low[it]);
      if(low[it] >= dfn[id] && id != R) cnt += !buc[id], buc[id] = 1;
    }
    else low[id] = min(low[id], dfn[it]);
  }
  if(son >= 2 && id == R) cnt += !buc[id], buc[id] = 1;
}
int main() {
  cin >> n >> m;
  for(int i = 1; i <= m; i++) {
    int u, v;
    cin >> u >> v;
    e[u].push_back(v), e[v].push_back(u);
  }
  for(int i = 1; i <= n; i++) if(!dfn[i]) R = i, dfs(i);
  cout << cnt << endl;
  for(int i = 1; i <= n; i++) if(buc[i]) cout << i << " ";
  return 0;
}
```

#### [P3469 [POI2008] BLO-Blockade](https://www.luogu.com.cn/problem/P3469)

一道 Tarjan 求割点的练手题。

设删去与结点 $u$ 相连的所有边之后形成的连通块大小分别为 $s_{1\sim k}$，则答案为 $\sum_{i = 1} ^ k s_i (n - s_i)$。注意，不要忘记 $u$ 没有被删去，它本身是一个大小为 $1$ 的连通块。

因为 $v$ 判定 $u$ 为割点当且仅当封锁 $u$ 之后 $v$ 及其子树与整张图剩余部分不连通，所以考虑所有判定 $x$ 为割点的 $y_i$，它们的子树分别单独形成连通块。除去这些结点后，还有一个大小为 $n - 1 - \sum size(y_i)$ 的连通块（可能为空，但不影响答案）。

时间复杂度 $\mathcal{O}(n)$。

```cpp
#include <bits/stdc++.h>
using namespace std;
constexpr int N = 1e5 + 5;
int n, m, dfn[N], low[N], dn;
long long ans[N], sz[N];
vector<int> e[N];
void dfs(int id) {
  dfn[id] = low[id] = ++dn;
  long long r = n - 1;
  ans[id] = r, sz[id] = 1;
  for(int it : e[id]) {
    if(!dfn[it]) {
      dfs(it), low[id] = min(low[id], low[it]), sz[id] += sz[it];
      if(low[it] >= dfn[id]) ans[id] += sz[it] * (n - sz[it]), r -= sz[it];
    }
    else low[id] = min(low[id], dfn[it]);
  }
  ans[id] += r * (n - r);
}
int main() {
  cin >> n >> m;
  for(int i = 1; i <= m; i++) {
    int u, v;
    cin >> u >> v;
    e[u].push_back(v), e[v].push_back(u);
  }
  dfs(1);
  for(int i = 1; i <= n; i++) cout << ans[i] << endl;
  return 0;
}
```