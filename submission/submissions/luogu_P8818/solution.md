# P8818 题解

[欢迎您在我的博客中阅读本文，谢谢！](https://www.cnblogs.com/crab-in-the-northeast/p/luogu-p8818.html)

本文中 A 和 B 分别代表小 L 和小 Q，而原题中的 $A$，$B$ 两个数组在本题中分别用 $a$ 和 $b$ 表示。

矩阵这个描述就是障眼法。翻译一下题目：

A 在 $a[l_1 \cdots r_1]$ 中选择一个 $x$，然后 B 在 $b[l_2 \cdots r_2]$ 中选择一个 $y$，分数是 $x \times y$，A 想让分数尽可能大，B 想让分数尽可能小。求分数。

肯定先思考 B 再思考 A，因为 A 会思考 B 的思考。

B 的行为就是对于 $x$，找到一个 $b[l_2 \cdots r_2]$ 中的 $y$，使得 $x \times y$ 最小。

具体地：

- $x \ge 0$ 时，B 会选择最小的 $y$；
- $x < 0$ 时，B 会选择最大的 $y$。

那么 A 的行为是什么呢？还是按照正负分类讨论：

如果 A 这次想让 $x \ge 0$，那么 B 会选择最小的 $y$。如果这个 $y \ge 0$，那么 A 一定会选最大的 $x$；如果这个 $y < 0$，那么 A 一定会选最小的非负数 $x$（别忘了当前制约条件 $x \ge 0$）。

如果 A 这次想让 $x < 0$，那么 B 会选择最大的 $y$。如果这个 $y \ge 0$，那么 A 一定会选最大的负数 $x$；如果这个 $y <0$，那么 A 一定会选最小的 $x$。

因此 A 的行为只有四种：选择最大的 $x$；最小的 $x$，最大的负数 $x$，最小的非负数 $x$。

分别讨论 A 选择四种行为时 B 的选择，答案取最大值即可。

然后就变成了静态区间最值的板子。使用 6 个 ST 表分别存储以下信息：

- $a$ 的区间最大值；
- $a$ 的区间最小值；
- $a$ 的负数区间最大值；
    - 具体是把所有满足 $a_i \ge 0$ 的 $a_i$ 全部替换为 $-\infty$ 代表这个位置不存在数，至于为何是 $-\infty$ 请读者自己思考。
- $a$ 的非负数区间最小值；
    - 具体是把所有满足 $a_i < 0$ 的 $a_i$ 全部替换为 $+\infty$ 代表这个位置不存在数。
- $b$ 的区间最大值；
- $b$ 的区间最小值。

时间复杂度 $\mathcal{O}(n\log n + q)$。


```cpp
/*
 * @Author: crab-in-the-northeast 
 * @Date: 2022-10-30 22:49:26 
 * @Last Modified by: crab-in-the-northeast
 * @Last Modified time: 2022-10-30 23:15:25
 */
#include <bits/stdc++.h>
#define int long long
inline int read() {
    int x = 0;
    bool f = true;
    char ch = getchar();
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-')
            f = false;
    for (; isdigit(ch); ch = getchar())
        x = (x << 1) + (x << 3) + ch - '0';
    return f ? x : (~(x - 1));
}
inline int max(int a, int b) {
    return a > b ? a : b;
}
inline bool gmx(int &a, int b) {
    return b > a ? a = b, true : false;
}
inline int min(int a, int b) {
    return a < b ? a : b;
}

const int maxn = (int)1e5 + 5;
const int maxm = (int)1e5 + 5;
const int mlgn = 25;
const int mlgm = 25;

int amx[maxn][mlgn], amn[maxn][mlgn], afx[maxn][mlgn], azn[maxn][mlgn];
int bmx[maxm][mlgm], bmn[maxm][mlgm];

// 6 个 ST 表
// amx：a 的区间最大值，amn：a 的区间最小值，afx：a 的负数区间最大值，azn：a 的非负数区间最小值。
// bmx：b 的区间最大值，bmn：b 的区间最小值。

int lg[maxn];

const int maxinf = LONG_LONG_MAX, mininf = LONG_LONG_MIN;

signed main() {
    int n = read(), m = read(), q = read();
    for (int i = 1; i <= n; ++i) {
        int x = read();
        amx[i][0] = amn[i][0] = x;
        afx[i][0] = (x < 0 ? x : mininf);
        azn[i][0] = (x >= 0 ? x : maxinf);
    }

    for (int i = 1; i <= m; ++i) {
        int x = read();
        bmx[i][0] = bmn[i][0] = x;
    }

    for (int i = 2; i <= max(n, m); ++i)
        lg[i] = lg[i >> 1] + 1;

    for (int j = 1; j <= lg[n]; ++j) {
        for (int i = 1; i + (1 << j) - 1 <= n; ++i) {
            int p = i + (1 << (j - 1));
            amx[i][j] = max(amx[i][j - 1], amx[p][j - 1]);
            afx[i][j] = max(afx[i][j - 1], afx[p][j - 1]);
            amn[i][j] = min(amn[i][j - 1], amn[p][j - 1]);
            azn[i][j] = min(azn[i][j - 1], azn[p][j - 1]);
        }
    }

    for (int j = 1; j <= lg[m]; ++j) {
        for (int i = 1; i + (1 << j) - 1 <= m; ++i) {
            int p = i + (1 << (j - 1));
            bmx[i][j] = max(bmx[i][j - 1], bmx[p][j - 1]);
            bmn[i][j] = min(bmn[i][j - 1], bmn[p][j - 1]);
        }
    }

    while (q--) {
        int la = read(), ra = read(), lb = read(), rb = read();
        int sa = lg[ra - la + 1], sb = lg[rb - lb + 1];
        int pa = ra - (1 << sa) + 1, pb = rb - (1 << sb) + 1;

        int amax = max(amx[la][sa], amx[pa][sa]);
        int amin = min(amn[la][sa], amn[pa][sa]);
        int afmx = max(afx[la][sa], afx[pa][sa]);
        int azmn = min(azn[la][sa], azn[pa][sa]);
        int bmax = max(bmx[lb][sb], bmx[pb][sb]);
        int bmin = min(bmn[lb][sb], bmn[pb][sb]);

        int ans = mininf;

        gmx(ans, amax * (amax >= 0 ? bmin : bmax));
        gmx(ans, amin * (amin >= 0 ? bmin : bmax));
        if (afmx != mininf)
            gmx(ans, afmx * (afmx >= 0 ? bmin : bmax));
        if (azmn != maxinf)
            gmx(ans, azmn * (azmn >= 0 ? bmin : bmax));
        printf("%lld\n", ans);
    }
    return 0;
}
```

如果觉得这篇题解写得好，请不要忘记点赞，谢谢！