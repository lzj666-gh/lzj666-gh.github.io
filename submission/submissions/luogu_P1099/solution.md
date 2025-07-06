# P1099 题解

在讨论本题的做法前，有必要先分析一下问题的一些特殊性质。

题解区部分题解在性质分析等方面存在一定欠缺，一定程度上可能会影响读者理解做法。

## 分析

先给出一些记号：

- $P(s,t)$：代表树上两点 $s,t$ 之间的路径（的长度）。
- $D(s,t)$：代表树上两点 $s,t$ 之间的路径（的长度），且这条路径是树的最长简单路径（即树的直径）。

另外，为了方便理解，并使得表意清晰，原题中提到的「树的核」均称为「路径」。

以下引理和定理基于**图上所有边权均为正**这一前提推出。

**引理 1**：对于一棵所有边权均为正的树，如果其存在多条直径，则树上必存在一点 $p$，使得所有直径均经过该点（简单来说，所有直径必交于至少一点）。

**证明**：用反证法。

如果存在两条直径 $D(s,t),D(s^\prime,t^\prime)$ 不相交，则 $\exists a \in D(s,t), b \in D(s^\prime,t^\prime)$，且 $\forall p \in P(a,b) - \{a, b\}$，$p \notin D(s, t)$，$p \notin D(s^\prime, t^\prime)$（即，$P(a,b)$ 除了 $a,b$ 两点之外，其他点均不在这两条直径上）。设 $d_1 = \max \{P(s,a), P(a,t)\}$，$d_2 = \max \{P(s^\prime,b), P(b,t^\prime)\}$，易知 $d_1,d_2 \geq \dfrac{1}{2}D(s, t)$，于是 $d_1 + d_2 + P(a,b) > D(s,t)$，即 $d_1,d_2,P(a,b)$ 这三段拼接成了一条比 $D(s,t), D(s^\prime,t^\prime)$ 这两条直径更长的简单路径，出现了矛盾。$\square$

（啥，你说可能有三条直径两两相交，但不交于一点的情况？画图后马上就发现有环了。）

**定理 1**：对于一棵所有边权均为正的树，如果其存在多条直径，则各直径的中点（不一定恰好是某个节点，可能在某条边的内部）是唯一的。

**证明**：还是用反证法。

设树的两条直径分别为 $D(s, t), D(s^\prime,t^\prime)$，它们的中点分别为 $m, m^\prime$，且两个中点不重合。可以推出，$m^\prime \in D(s, t)$（否则由 **引理 1**，两直径必定存在一个交点 $p$。设 $d_1 = \max \{P(s,p), P(p,t)\}$，$d_2 = \max \{P(s^\prime,p), P(p,t^\prime)\}$，则 $d_1, d_2 > \dfrac{1}{2}D(s, t)$，$d_1 + d_2 > D(s,t)$，与 $D(s,t)$ 是直径矛盾）。

于是实际情况大致如下图所示（略去了树上的其他不必要点，不妨设 $m^\prime$ 位于更靠近 $t$ 的一侧）。

![](https://cdn.luogu.com.cn/upload/image_hosting/oaiyl6ql.png)

则 $P(s,s^\prime) = P(s, m^\prime) + P(m^\prime + s^\prime) > \dfrac{1}{2}D(s, t) + \dfrac{1}{2}D(s^\prime, t^\prime) = D(s,t)$，与 $D(s,t)$ 是直径矛盾。$\square$

**引理 2.1**：若两条直径有重叠的部分，则于重叠部分同一端点引出的两条直径的非重叠的部分的长度相等。

**证明**：设两条直径分别为 $D(a, c)$，$D(b, d)$，重叠部分为 $P(s,t)$，如下图所示（$P(s,t)$ 可能是一个点，即 $s = t$）：

![](https://cdn.luogu.com.cn/upload/image_hosting/f587t21u.png)

如果 $P(a,s) \neq P(b,s)$（此时容易得到 $P(c,t) \neq P(d,t)$），则取 $P(a, s)$ 和 $P(b,s)$ 中较长的一条（长度设为 $d_1$），$P(c, t)$ 和 $P(d,t)$ 中较长的一条（长度设为 $d_2$），则由于 $d_1$ 和 $d_2$ 不在同一条直径上（否则推出 $D(a,c) > D(b,d)$，出现矛盾）则 $d_1 + P(s,t) + d_2 > D(a,c)$，出现了矛盾。$\square$

**引理 2.2**：若路径存在不位于直径上的部分，这条路径对应的偏心距一定不会比全部位于直径上的路径的偏心距的**最小值**更小。

**证明**：原命题等价于，对于任意一条不完全位于（或者完全不位于）直径上的路径 $F$，都存在一条完全位于直径上的路径 $F^\prime$，使得 $\operatorname{ECC}(F) \geq \operatorname{ECC}(F^\prime)$。下面是一个构造性的证明。

简单来说，我们采用如下方法构造：对于一条不完全位于（或者完全不位于）直径上的路径 $F$，找到该路径与直径的一个交点 $m$（必要时通过延长 $F$ 来找到交点），然后再证明 $P(m,m)$ 这条路径至少不会比 $F$ 更劣。

沿用 **引理 2.1** 中出现的记号，构建下图（树上的部分节点略去）：

![](https://cdn.luogu.com.cn/upload/image_hosting/9iwxoi6p.png)

注：

1. 加粗的点一定位于树的某条直径上，未加粗的点一定不位于树的任意一条直径上，即 $P(p,v)$ 这条路径不是树的直径。
2. 其实原图有多少条直径对本引理证明没有影响，~~图上保留多条直径只是忘记删了~~。

现在开始讨论。

1. 考虑 $P(p,u)$ 这条路径。距离 $P(p,u)$ 最远的点是哪个点，是 $v$ 吗？因为，$P(b,m) + P(m,v) < P(b,m) + P(m,d) = D(b,d)$，即 $P(m,v) < P(m,d)$，因此距离 $u$ 最远的点，是直径的端点，不是 $v$ 这样一个不在直径上的点。
2. 现在考虑 $P(u,v)$ 这条路径。距离 $P(u,v)$ 最远的点是哪个点，是 $p$ 吗？如果 $P(p,u) \geq P(a,m)$（其余情况同理），则 $D(a,c) = P(a,m) + P(m,c) \leq P(p,u) + P(m,c) < P(p,u) + P(u,m) + P(m,c) = P(p,c)$，与 $D(a,c)$ 是直径矛盾。因此距离 $P(u,v)$ 最远的点，仍然是直径的端点。
3. 最后考虑 $P(m,m)$ 这条路径。距离 $P(m,m)$ 最远的点是哪个点，是 $p$ 或者 $v$ 吗？注意到 $p,v$ 均不在直径上，于是 $P(b,m) + P(m,p) < P(b,m) + P(m,d) = D(b,d)$，即 $P(m,p) < P(m,d)$（这里只举了 $p$ 的情况，$v$ 同理），因此距离 $P(m,m)$ 最远的点，仍然是直径的端点。

（由于直径是树上最长简单路径这一性质，距离上述三条路径最远的点一定不会在从直径上 $m$ 之外的其他点引出的支链上取得，因此这些支链没有画出。）

对于 2 和 3 两种情况，偏心距显然为 $\max\{P(a,m), P(m,c)\}$，对于 1 这种情况，偏心距为 $\max\{P(a,m), P(m,c)\} + P(u,m)$。综上，1 和 2 这两种路径不完全位于（或者完全不位于）直径上的方案，不会比 3 这种完全位于直径上的方案更优。$\square$

因此，虽然原题限制路径只能在直径上取得，但可以忽略这一限制考虑所有满足长度限制的路径，而求得的最小偏心距不变。

**定理 2**：设在所有满足长度限制的路径中，取得最小偏心距的路径得到的偏心距为 $\textrm{minBCC}$，则对于任意一条直径，都存在一条长度不超过 $s$ 的路径 $F$，使得 $\operatorname{BCC}(F) = \mathrm{minBCC}$。

**证明**：

沿用 **引理 2.1** 中出现的记号，构建下图：

![](https://cdn.luogu.com.cn/upload/image_hosting/mjb8pfen.png)

注：加粗的点一定位于树的某条直径上，未加粗的点一定不位于树的任意一条直径上，即 $P(p,z)$ 这条路径不是树的直径。

如果我们取 $P(c,y)$ 这条路径，距离该路径最远的点，容易发现不是 $p$。可能是 $z$ 吗？定理 1 告诉我们，$P(t,z) < \dfrac{1}{2}D(a,c)$，从而得到 $P(x,z) < \dfrac{1}{2}D(a,c)$。而 $P(a,y) \geq \dfrac{1}{2} D(a,c)$，因此排除 $z$ 是最远点的可能性。

（$d$ 是最远点时，$P(c,d)$ 也是树的直径，为了不影响 $P(s,t)$ 是直径重合部分这一前提，这里假定 $P(c,d)$ 不是树的直径。）

综上，这条路径的偏心距 $\operatorname{ECC}(P(c,y)) = P(a,y)$。简单比较后容易发现，$P(t,t)$ 这条路径偏心距（容易看出是 $P(a,t)$）一定会更小。

由此得出，当所选路径不包含直径的重合部分时，这条路径一定不是最优路径。

现在考虑所选路径包含直径重合部分的情况。以 $P(s,t)$ 为例，这时候的偏心距 $\operatorname{ECC}(P(s,t)) = \max\{P(m,p), P(s,a), P(t,c)\}$，如果将 $P(s,t)$ 延伸成 $P(s,y)$ 或者 $P(s,q)$，偏心距的表达式没有发生变化（仍然存在 $P(t,c)$ 项）。因此，在所选路径包含直径重合部分的时候，直径的选择对答案没有影响。$\square$

由 **定理 2**，我们不用在树上的每条直径上都找到取得最小偏心距的路径，只需要在其中一条直径上找即可。

## 解法

### 解法一：枚举

先求出树的任意一条直径，然后在直径上枚举路径的端点。 

（由 **引理 2.2**，也可以不用求出树的直径，直接枚举树上的所有路径。）

接下来 DFS 遍历整棵树，按定义求出其他点到路径的距离，从而得到该路径的偏心距。

枚举的时间复杂度 $O(n^2)$，遍历的时间复杂度为 $O(n)$，总时间复杂度为 $O(n^3)$，已经可以通过本题。

### 解法二：双指针优化枚举

注意到，在固定路径的一端 $s$ 的前提下，随着路径长度的增加，偏心距不会变大。

于是可以考虑枚举路径的一端 $s$，用双指针的技巧找到距离 $s$ 最远，且不超过路径长度上限的点 $t$，从而减少候选的最优路径数量。

枚举的过程时间复杂度降到了 $O(n)$，总时间复杂度为 $O(n^2)$。

### 解法三：二分

考虑二分偏心距，将最优化问题变成存在性问题。

定义一端是直径上的点，且只有该点在直径上，其他点都不在直径上的一条链为直径的**支链**。设 $d_i$ 为从 $i$ 点引出的最长支链的长度。

分析偏心距的可能情况。

![](https://cdn.luogu.com.cn/upload/image_hosting/pzx0c11u.png)

以路径 $P(2,4)$ 为例，距离该路径最远的点，可能是 $1$，$5$，$p$。由于 $P(1,5)$ 是直径，$q$ 到 $P(2,4)$ 的距离一定不会比 $1$ 到 $P(2,4)$ 更远，因此在计算偏心距的时候不用考虑 $q$ 点。$1,5$ 是直径的端点，而 $p$ 是路径上的点（除了路径端点）引出的支链的最远点。

归纳一下，设直径上的点分别为 $a_1,a_2,\ldots,a_k$，取的路径为 $P(a_i,a_j)$（$i \leq j$），则所求的偏心距为：$\max \{\max_{i < p < j} d_{a_p}, P(a_1,a_i), P(a_j, a_k)\}$。

$d_i$ 可以在求出直径后通过一次 DFS 求出。在二分偏心距 $e$ 后，先找到直径的两端点 $i$，$j$，使得 $P(a_1,a_i), P(a_j,a_k) \leq e$，再判断路径长度是否超过限制，以及 $\max_{i < p < j} d_{a_p} < e$ 是否满足。如果以上条件均满足，则找到一条可行的路径。

时间复杂度 $O(n \log \sum w)$。可以通过 [P2491](https://www.luogu.com.cn/problem/P2491)。

### 解法四：双指针+前缀和

考虑将解法二的双指针引入解法三。

解法二低效的原因主要在于每次双指针求出最优区间后都要 DFS 一遍，在解法三分析了偏心距的组成后，我们发现没有必要再进行重复的 DFS，只需要在双指针过程中，动态更新 $\max_{i < p < j} d_{a_p}, P(a_1,a_i), P(a_j, a_k)$ 即可。

第一项区间最大值是经典的滑动窗口，可以用单调队列计算，其余两项前缀和即可。

时间复杂度 $O(n)$。

到这里就完了吗？时间复杂度确实到达了下限（输入就需要同样的时间复杂度），但是代码实现还能更简单。

注意到一个性质：$\forall l \in [1,i]$，$d_{a_l} \leq P(a_1, a_i)$，同样地，$\forall l \in [j,k]$，$d_{a_l} \leq P(a_j, a_k)$。

**证明**：由直径是树上最长简单路径的性质，可以得到 $d_{a_j} + P(a_j, a_i) \leq P(a_1,a_i)$，再结合 $P(a_j, a_i) > 0$，从而原命题得证。$\square$

于是我们将偏心距的表达式替换为 $\max \{\max_{1 \leq p \leq k} d_{a_p}, P(a_1,a_i), P(a_j, a_k)\}$，这一过程中我们加入的项都是不大于 $P(a_1,a_i), P(a_j, a_k)$ 的项，在取 $\max$ 后不会影响结果。

$\max_{1 \leq p \leq k} d_{a_p}$ 是定值，因此不必再使用单调队列！实现难度也相应简单了不少。

## 参考实现

把四个解法的代码都贴了出来，不同解法之间使用 `namespace` 进行隔离，可以通过对比阅读以观察优化点。

```cpp
// Problem: P1099 [NOIP2007 提高组] 树网的核
// Contest: Luogu
// URL: https://www.luogu.com.cn/problem/P1099
// Memory Limit: 128 MB
// Time Limit: 1000 ms
//
// Powered by CP Editor (https://cpeditor.org)

#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
struct edge {
  int v, w;
  edge(int v = 0, int w = 0) {
    this->v = v;
    this->w = w;
  }
};
const int maxn = 300000 + 5;
vector<edge> e[maxn];
int dep[maxn], f[maxn], c;
int dia[maxn], cnt, pres[maxn], posts[maxn];
bool vis[maxn];
int n, s;
void dfs(int u, int fa) {
  f[u] = fa;
  for (auto ed : e[u]) {
    if (ed.v == fa || vis[ed.v]) continue;
    dep[ed.v] = dep[u] + ed.w;
    if (dep[ed.v] > dep[c]) c = ed.v;
    dfs(ed.v, u);
  }
}
void get_diameter() {
  dfs(1, 0);
  dep[c] = 0;
  dfs(c, 0);
  for (int u = c; u; u = f[u]) {
    dia[++cnt] = u;
    pres[cnt] = dep[u];
  }
  reverse(dia + 1, dia + cnt + 1);
  reverse(pres + 1, pres + cnt + 1);
  for (int i = cnt; i > 0; i--) posts[i] = pres[cnt] - pres[i];
}
namespace sub1 {
void solve() {
  int minecc = 1 << 30;
  for (int i = 1; i <= cnt; i++)
    for (int j = i; j <= cnt; j++) {
      if (pres[j] - pres[i] <= s) {
        memset(vis, 0, sizeof(vis));
        for (int k = i; k <= j; k++) vis[dia[k]] = true;
        int ecc = 0;
        for (int k = i; k <= j; k++) {
          dep[dia[k]] = 0, c = 0;
          dfs(dia[k], 0);
          ecc = max(ecc, dep[c]);
        }
        minecc = min(minecc, ecc);
      }
    }
  cout << minecc << endl;
}
}  // namespace sub1
namespace sub2 {
void solve() {
  int minecc = 1 << 30;
  int l = 1, r = 1;
  for (; l <= cnt; l++) {
    while (r <= cnt && pres[r + 1] - pres[l] <= s) r++;
    memset(vis, 0, sizeof(vis));
    for (int k = l; k <= r; k++) vis[dia[k]] = 1;
    int ecc = 0;
    for (int k = l; k <= r; k++) {
      dep[dia[k]] = 0, c = 0;
      dfs(dia[k], 0);
      ecc = max(ecc, dep[c]);
    }
    minecc = min(minecc, ecc);
  }
  cout << minecc << endl;
}
}  // namespace sub2
namespace sub3 {
int maxd[maxn];
bool check(int ecc) {
  int l = 1, r = cnt;
  while (l < cnt && pres[l + 1] <= ecc) l++;
  while (r > l && posts[r - 1] <= ecc) r--;
  if (pres[r] - pres[l] > s) return false;
  int d = 0;
  for (int i = l + 1; i < r; i++) d = max(d, maxd[i]);
  return d <= ecc;
}
void solve() {
  for (int i = 1; i <= cnt; i++) vis[dia[i]] = true;
  for (int i = 1; i <= cnt; i++) {
    dep[dia[i]] = 0, c = 0;
    dfs(dia[i], 0);
    maxd[i] = dep[c];
  }
  int l = 0, r = 1 << 30, ans = 0;
  while (l <= r) {
    int mid = (l + r) >> 1;
    if (check(mid))
      ans = mid, r = mid - 1;
    else
      l = mid + 1;
  }
  cout << ans << endl;
}
}  // namespace sub3
namespace sub4 {
void solve() {
  for (int i = 1; i <= cnt; i++) vis[dia[i]] = true;
  int maxd = 0;
  for (int i = 1; i <= cnt; i++) {
    dep[dia[i]] = 0, c = 0;
    dfs(dia[i], 0);
    maxd = max(dep[c], maxd);
  }
  int l = 1, r = 1;
  int minecc = 1 << 30;
  for (; l <= cnt; l++) {
    while (r <= cnt && pres[r + 1] - pres[l] <= s) r++;
    minecc = min(max(maxd, max(pres[l], posts[r])), minecc);
  }
  cout << minecc << endl;
}
}  // namespace sub4
int main() {
  ios::sync_with_stdio(false);
  cin >> n >> s;
  for (int i = 1; i < n; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    e[u].emplace_back(v, w);
    e[v].emplace_back(u, w);
  }
  get_diameter();
  sub4::solve();
  return 0;
}
```