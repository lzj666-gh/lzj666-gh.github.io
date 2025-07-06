# P9343 题解

容易想到当对于 $x$ 号酒，假如输入数据出现了 `1 x` 和 `2 x`，那么就可以做到每杯酒都至少有 $1$。同时还要考虑到假如到最后都没有这种情况出现，有两种情况也是可以的：$o = 1$ 时 $x$ 的种类假如等于 $n$ 或者 $o = 2$ 时 $x$ 的种类大于 $1$。

实现这个并不难，开桶分别记录 $o = 1$ 和 $o = 2$ 的 $x$，然后处理就十分简单了，更新需要的计数器并判断是否能满足题意即可。注意要多测清空以及小心不要读入到一半就把 `solve` 结束了。

```cpp
void solve() {
    int cnt1 = 0, cnt2 = 0;
    memset(vis1, false, sizeof vis1);
    memset(vis2, false, sizeof vis2);
    scanf ("%d%d", &n, &m);
    for (int i = 1; i <= m; i++) scanf ("%d%d", &o[i], &x[i]);
    for (int i = 1; i <= m; i++) {
        if (o[i] == 1) {
            if (vis2[x[i]]) {
                cout << i << '\n';
                return;
            }
            if (!vis1[x[i]]) cnt1++, vis1[x[i]] = true;
        }
        if (o[i] == 2) {
            if (vis1[x[i]]) {
                cout << i << '\n';
                return;
            }
            if (!vis2[x[i]]) cnt2++, vis2[x[i]] = true;
        }
        if (cnt2 > 1 || cnt1 == n) {
            cout << i << '\n';
            return;
        }
    }
    puts("-1");
}
```