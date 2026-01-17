# P5017 题解

### 前言

听说今年普及组难度堪比提高 $Day\ 1$，作为一名~~半退役~~提高选手，心血来潮，特地来接受这道经典好题的洗礼。

---

### 正文

这是一道题意简明的题，论解法却无比多样。我个人喜欢先把题意抽象化。

我们不妨认为时间是一条**数轴**，每名同学按照到达时刻分别对应数轴上**可能重合的点**。安排车辆的工作，等同于将数轴分成若干个**左开右闭**段，每段的长度 $\geqslant m$。原本的等车时间之和，自然就转换成所有点到各自**所属段右边界**的**距离之和**。

如果您无法理解复杂的文字描述，试图结合下面的这幅图思考：

![](https://i.loli.net/2018/11/13/5bead5ac2c9c8.png)

这不就有个鲜明的线性 $dp$ 模型了吗？设 $f_i$ 表示对数轴上 $(-\infty,\ i]$ 分段，且最后一段的右边界是 $i$，位于 $(-\infty,\ i]$ 内的点到各自所属段右边界的距离之和最小值。转移式：

$$f_i = \min_{j \leqslant i-m}\{ f_j+ \sum_{j < t_k \leqslant i} i-t_k \}$$

设最后一段对应 $(j,\ i]$，既然它的长度 $\geqslant m$，则有 $j \leqslant i - m$。我们知道 $j < t_k \leqslant i$，意味着第 $k$ 个点在这段中，它到右端的距离 $= i - t_k$，因而产生这么多的贡献。累加贡献，与 $j$ 以前的最优答案 $f_j$，即可推出转移式。

另外，特判 $(-\infty,\ i]$ 单独作为一段的**边界情况**，即 $f_i = \sum\limits_{t_k \leqslant i}i - t_k$。

然而我们对 $\sum\limits_{j < t_k \leqslant i} i-t_k$ 束手无策，如何快速求出呢？这时**前缀和**有了重大用途。拆，拆，拆！

$$\sum_{j < t_k \leqslant i} i-t_k = (\sum_{j < t_k \leqslant i}i)-(\sum_{j < t_k \leqslant i}t_k)=(cnt_i - cnt_j) \times i - (sum_i - sum_j)$$

其中，$cnt_i$ 表示 $(-\infty,\ i]$ 中点的个数，$sum_i$ 表示 $(-\infty,\ i]$ 中点的位置之和。顺便改写下刚才的转移式：

$$f_i = \min_{j \leqslant i-m}\{ f_j +  (cnt_i - cnt_j) \times i - (sum_i - sum_j)\}$$

这里令 $t = \max\limits_{1\leqslant i \leqslant n}\{t_i\}$，最终答案只需在 $i \geqslant t$ 找最小的 $f_i$ 即可。实际上，$[t,\ t + m)$ 包含了所有可能的答案。

至此，我们有了 $50$ 分的优秀做法，时间复杂度为 $O(t^2)$。代码如下：

```cpp
#include <cstdio>
#include <algorithm>

const int maxT = 4000105;

int n, m, t, ti, ans = 1e9, cnt[maxT], sum[maxT], f[maxT];

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &ti); t = std::max(t, ti);
        cnt[ti]++; sum[ti] += ti;
    }
    for (int i = 1; i < t + m; i++) { cnt[i] += cnt[i - 1]; sum[i] += sum[i - 1]; } // 前缀和.
    for (int i = 0; i < t + m; i++) {
        f[i] = cnt[i] * i - sum[i]; // 特判边界情况.
        for (int j = 0; j <= i - m; j++) { f[i] = std::min(f[i], f[j] + (cnt[i] - cnt[j]) * i - (sum[i] - sum[j])); }
    }
    for (int i = t; i < t + m; i++) { ans = std::min(ans, f[i]); }
    printf("%d\n", ans);
    return 0;
}
```

时间复杂度爆炸，怎么办？使用 $dp$ **优化法宝一：剪去无用转移**！

这是原来的转移式：

$$f_i = \min_{j \leqslant i-m}\{ f_j +  (cnt_i - cnt_j) \times i - (sum_i - sum_j)\}$$

实际上只需要：

$$f_i = \min_{i - 2m < j \leqslant i-m}\{ f_j +  (cnt_i - cnt_j) \times i - (sum_i - sum_j)\}$$

不知你是否看到了区别？仍然考虑 $(j,\ i]$ 段的长度，由于分的段数不会增大答案，当它的长度 $\geqslant 2m$ 时，我们完全可以再给它切一刀，得到**不劣**的答案。通过此性质，可剪去大量无用转移。

时间复杂度降至 $O(tm)$，按照写法常数可获得 $70$ ~ $100$ 不等的成绩，并不排除在 $CCF$ 少爷机上超时的可能。

```cpp
#include <cstdio>
#include <algorithm>

const int maxT = 4000105;

int n, m, t, ti, ans = 1e9, cnt[maxT], sum[maxT], f[maxT];

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &ti); t = std::max(t, ti);
        cnt[ti]++; sum[ti] += ti;
    }
    for (int i = 1; i < t + m; i++) { cnt[i] += cnt[i - 1]; sum[i] += sum[i - 1]; } // 前缀和.
    for (int i = 1; i < t + m; i++) {
        f[i] = cnt[i] * i - sum[i]; // 特判边界情况.
        for (int j = std::max(i - m - m + 1, 0)/*剪去无用转移*/; j <= i - m; j++) { f[i] = std::min(f[i], f[j] + (cnt[i] - cnt[j]) * i - (sum[i] - sum[j])); }
    }
    for (int i = t; i < t + m; i++) { ans = std::min(ans, f[i]); }
    printf("%d\n", ans);
    return 0;
}
```

不稳，很虚，怎么办？使用 $dp$ **优化法宝二：剪去无用状态**！

举个例子，假设正在求 $f_i$，但在 $(i-m,\ i]$ 中没有任何点，这个 $f_i$ 相对来说就是 **“无用”** 的。原因是若最后一段长度恰好 $= m$，这里面又没有任何点，不分割也罢。长度 $>m$ 时，完全可以把这一段的右边界往左“拖”，产生**不劣**的答案。

然而直接扔掉这个状态，会与上一个优化缩小转移范围起冲突，故**无用**的位置令 $f_i = f_{i-m}$，防止漏解。

可以证明**“有用”**的位置 $\leqslant nm$ 个，故时间复杂度再次优化成 $O(nm^2 + t)$。期望得分 $100$ 分。代码：

```cpp
#include <cstdio>
#include <algorithm>

const int maxT = 4000105;

int n, m, t, ti, ans = 1e9, cnt[maxT], sum[maxT], f[maxT];

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &ti); t = std::max(t, ti);
        cnt[ti]++; sum[ti] += ti;
    }
    for (int i = 1; i < t + m; i++) { cnt[i] += cnt[i - 1]; sum[i] += sum[i - 1]; } // 前缀和.
    for (int i = 0; i < t + m; i++) {
        if (i >= m && cnt[i - m] == cnt[i]) { f[i] = f[i - m]; continue; } // 剪去无用状态.
        f[i] = cnt[i] * i - sum[i]; // 特判边界情况.
        for (int j = std::max(i - m - m + 1, 0)/*剪去无用转移*/; j <= i - m; j++) { f[i] = std::min(f[i], f[j] + (cnt[i] - cnt[j]) * i - (sum[i] - sum[j])); }
    }
    for (int i = t; i < t + m; i++) { ans = std::min(ans, f[i]); }
    printf("%d\n", ans);
    return 0;
}
```

这样写毫无逼格，怎么办？使用 $dp$ **优化法宝三：利用单调性质**！

移除前两个优化，转变画风，$j$ 是 $i$ 的决策点，满足：

$$f_i = f_j +  (cnt_i - cnt_j) \times i - (sum_i - sum_j)$$

还是拆，拆，拆！

$$f_i = f_j +  cnt_i \times i - cnt_j \times i - sum_i + sum_j$$

把只跟 $j$ 有关的项移到左边，跟 $i,\ j$ 有关的乘积放在中间，只跟 $i$ 有关的项移到最右边：

$$\underline{f_j + sum_j}_{\ y} = \underline{i_{_{}}}_{\ k} \times \underline{cnt_j}_{\ x} + \underline{(f_i - cnt_i \times i + sum_i)}_{\ b}$$

这不是**斜率优化**裸题吗！斜率 $i$ 单调上升，维护下凸壳。对于 $i$ 把 $i - m$ 推入队列，即可保证决策点 $j \leqslant i - m$。

每个状态点最多进出队列一次，时间复杂度 $O(t)$，仍能拿到 $100$ 分。

```cpp
#include <cstdio>
#include <algorithm>

const int maxT = 4000105;

int n, m, t, ti, ans = 1e9, l = 1, r, cnt[maxT], sum[maxT], q[maxT], f[maxT];

inline double getSlope(int u, int v) { return (double) (f[v] + sum[v] - f[u] - sum[u]) / (cnt[u] == cnt[v] ? 1e-9 : cnt[v] - cnt[u]); }

int main() {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &ti); t = std::max(t, ti);
        cnt[ti]++; sum[ti] += ti;
    }
    for (int i = 1; i < t + m; i++) { cnt[i] += cnt[i - 1]; sum[i] += sum[i - 1]; } // 前缀和.
    for (int i = 0; i < t + m; i++) {
        if (i - m >= 0) {
        	while (l < r && getSlope(q[r - 1], q[r]) >= getSlope(q[r], i - m)) { r--; }
        	q[++r] = i - m; // 把可能成为最优解的推入队列. 
        }
    	while (l < r && getSlope(q[l], q[l + 1]) <= i) { l++; } // 把不可能成为最优解的弹出队列. 
        f[i] = cnt[i] * i - sum[i]; // 特判边界情况.
        if (l <= r) { f[i] = std::min(f[i], f[q[l]] + (cnt[i] - cnt[q[l]]) * i - (sum[i] - sum[q[l]])); } // 斜率优化转移. 
    }
    for (int i = t; i < t + m; i++) { ans = std::min(ans, f[i]); }
    printf("%d\n", ans);
    return 0;
}
```

教练加强了这题，$t \leqslant 10^9$，复杂度依赖 $t$ 的做法都挂了，怎么办？

掌握前两个优化的核心思想后，不难发现**最优情况**下，每个点到所属段右边界的距离 $< 2m$。令 $g_{i,\ j}$ 表示对 $t_{1..n}$ **排序**后（$0 \leqslant j < 2m$），第 $i$ 个点距离所属段右边界 $j$ 个单位时，第 $1..i$ 个点距离之和的最小值。

理论上，想要得到 $g_{i,\ j}$，我们需要枚举 $k,\ l$，用 $g_{k,\ l}$ 转移。可有趣的是，当前的第 $i$ 个点，要么和第 $i - 1$ 个点在**同一段内**，要么抛弃第 $i - 1$ 个点，**新开了一段**，而自己是里面的第一个。

总而言之，只要枚举一个 $k$，用 $g_{i-1,\ k}$ 转移得到 $g_{i,\ j}$，两者没有区别的。

在同一段内的情况很简单，不用枚举 $k$ 就可以直接转移：

$$g_{i,\ j} = g_{i - 1,\ t_i + j - t_{i-1}} + j$$

新开一段的情况，同样要保证段长 $\geqslant m$：

$$g_{i,\ j} = \min\limits_{t_{i-1} + k + m \leqslant t_i + j} \{ g_{i - 1,\ k} \} + j $$

易知，随着 $j$ 的增大，能够转移的 $k$ 的上限也不断增大，故使用**前缀最小值**维护可以转移的 $g_{i-1,\ k}$。

时间复杂度为 $O(n\ \log\ n + nm)$，即 $O(nm)$，目前看应该是最快的 $dp$ 做法了。注意边界细节，$AC$ 代码如下：

```cpp
#include <cstdio>
#include <algorithm>

const int maxN = 505, maxM = 205;

int n, m, mm, ans = 1e9, t[maxN], g[maxN][maxM];

int main() {
    scanf("%d%d", &n, &m); mm = m + m;
    for (int i = 1; i <= n; i++) { scanf("%d", &t[i]); }
    std::sort(t + 1, t + n + 1); // 排序. 
    for (int i = 1; i <= n; i++) {
    	g[i][0] = 1e9; // 先特判 j = 0 的情况. 
    	for (int j = 0; j <= std::min(t[i] - t[i - 1] - m, m - 1); j++) { g[i][0] = std::min(g[i][0], g[i - 1][j]); }
    	for (int j = 1; j < mm; j++) { g[i][j] = std::min(g[i][j - 1], t[i] + j - t[i - 1] - m >= 0 && t[i] + j - t[i - 1] - m < mm ? g[i - 1][t[i] + j - t[i - 1] - m] : (int) 1e9); } // 前缀最大值维护新开一段的情况. 
    	for (int j = 0; j < mm; j++) { g[i][j] = std::min(g[i][j], t[i] + j - t[i - 1] < mm ? g[i - 1][t[i] + j - t[i - 1]] : (int) 1e9) + j; } // 分在同一段内的情况, 加上 j 的贡献. 
    }
    for (int i = 0; i < m; i++) { ans = std::min(ans, g[n][i]); }
    printf("%d\n", ans);
    return 0;
}
```

听同学说，他有一个 $O(n)$ 的做法，怎么办？

很抱歉，作者菜得可怜，把 $dp$ 用到极致也只有 $O(nm)$，但**不清楚**贪心或乱搞是否能在 $O(n)$ 内解决本题。

---

### 尾注

或许您发现了，我给出的代码都特别短。是的，这道题考验的就是 $dp$ 的灵活运用，合理剪枝优化，利用好其性质，甚至能够用更加优美的做法暴踩标算。至于代码，只有会敲和懒得敲。