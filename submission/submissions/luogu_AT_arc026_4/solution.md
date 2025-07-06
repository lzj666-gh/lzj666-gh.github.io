# AT_arc026_4 题解

根据题目的描述，一条边对 $costperhour'$ 的贡献的多少，可以用 $C/T$ 衡量吗？

---

也许，在一定程度上，是可以对比两条边的贡献。

于是，一开始我便想到一种做法，选择所有 $C_i \le T_i$ 的边，剩余的边再以 $C/T$ 比较跑最小生成树。

能保证正确性的一个显然的结论是：**$C_i \le T_i$ 的所有边总对于贡献为负。**（就是能够让 $costperhour'$ 尽可能小）

但是，这显然是**错**的。反例：对于一条边 $C_i=5, T_i=6$，
$$
\frac{1000}{2000}=0.5<\frac{1005}{2006}\approx0.50009
$$
为什么？有一条式子（不妨 $a/b\le c/d$，等号同时取）：
$$
a/b\le\frac{a+c}{b+d}\le c/d
$$
代入到 $costperhour'$ 的变化，同时设 $costperhour' = c/t$，条件是 $C_i/T_i \le 0$（同 $C_i \le T_i$）。

由于题目并未保证 $c/t \ge 1$，所以有可能有 $c/t < C_i / T_i \le 0$。

所以有：
$$
c/t \le \frac{c + C_i}{t + T_i} \le C_i / T_i
$$
观察到 $costperhour' < costperhour''$（结果变大了，贡献非负）。

所以并不是所有 $C_i \le T_i$ 的边都对贡献为负，还需要判断当前 $costperhour$ 与 $1$ 的大小关系等。

考虑到这不好维护，转换以下思路。

---

不能够通过 $c/t$ 来判断边之间的贡献情况。注意到 $n\le10^4$，可以容下 $n\log^2k$。

如何将判断贡献转换为整式的判断呢？

考虑二分最终 $costperhour$。

但是，我们如何判断一个 $costperhour$（简称为 $cph$） 是否能够被构造出来呢？

由于我们的目标是判断是否能构造 $cph' \le cph$。

$$
cph'= \frac{c'}{t'}
$$
（带 $'$ 表示总和）
$$
\frac{c'}{t'} \le cph
$$
$$
c' \le cph\cdot t'
$$
$$
c' - cph\cdot t'\le 0
$$
那么，处理为整式之后，只需要判断当前选择 $c' - cph \cdot t'$ 之和是否小于等于 $0$ 即可。

通过这个变换可以将判断目标变为正负代价的简单判断。

对于每一条边，我们让 **整合代价** $cph_i' = C_i - cph \cdot T_i$。

若 $cph_i'$ 为负，必然对最终的总代价是好的（目标是非正数嘛）。

那么就可以对边按 $cph_i'$ 排序，选完所有 $cph_i'$ 非正的，最终对正数跑最小生成树即可！

如果跑出的生成树结果与之前选择负数贡献边的贡献之和小于等于 $0$，那么必然可以构造！

注意！这里的判断只能判断对应 $cph$ 能否构造出更小的结果（即只能获得上下界信息），所以才只能二分。

时间复杂度：$O(n\log n \log k), k\to(10^{6})^2 \times 10^4$。（$eps\to10^{-4}$）

```cpp
// Copyright 2022 Lotuses
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#define maxn 114514
struct union_find_set { // 并查集模板
    #define min(x, y) (((x) < (y)) ? (x) : (y))
    int fa[maxn];
    void init(int n) {
        for (int i = 0; i <= min(maxn, n); i++) {
            fa[i] = i;
        }
    }
    int find(int x) {
        return fa[x] == x ? x : (fa[x] = find(fa[x]));
    }
    void uni(int x, int y) {
        fa[find(x)] = find(y);
    }
}ufs;

int n, m;
struct Edge {
    int from, to, cost, time, nxt;
};
std::vector<Edge> G[maxn];
std::vector<Edge> GG;
#define eps 1e-4
#define seps 1e-6

std::pair<double, int> ccph[maxn];

bool check(double cph) {
    for (int i = 0; i < m; i++) {
        ccph[i] = std::make_pair(GG[i].cost - cph * GG[i].time, i);
    }
    std::sort(ccph, ccph + m);
    ufs.init(n); int i = 0; double total = 0;
    for (i = 0; i < m && ccph[i].first <= seps; i++) {
        ufs.uni(GG[ccph[i].second].from, GG[ccph[i].second].to);
        total += ccph[i].first;
    }

    for (i; i < m; i++) {
        int fafrom = ufs.find(GG[ccph[i].second].from),
            fato   = ufs.find(GG[ccph[i].second].to);
        if (fafrom != fato) {
            total += ccph[i].first;
            ufs.uni(fafrom, fato);
        }
    }
    return total <= eps;
}

int main() {
    read(n, m);
    for (int i = 0; i < m; i++) {
        static int a, b, c, t;
        read(a, b, c, t);
        Edge e1 = {a, b, c, t, G[b].size()}, 
             e2 = {b, a, c, t, G[a].size()}; // 提前算好
        G[a].push_back(e1);
        G[b].push_back(e2);
        GG.push_back(e1);
    }

    double l = 0, r = 1e13;
    while (fabs(l - r) > eps) {
        double mid = (l + r) / 2;
        bool resu = check(mid);
        if (resu) {
            r = mid;
        } else {
            l = mid;
        }
    }
    printf("%.3lf", l);
    return 0;
}
```

---

说句闲话，AC 这道题的最好方法是：

```cpp
#include<cstdio>
int main(){puts("nan");}
```

By [/record/73889960](/record/73889960)

update: 改了下 $\LaTeX$，删去了一些无用的代码片段 + 翻译