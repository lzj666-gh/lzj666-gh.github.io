# P3243 题解

看到题目，可以想到拓扑排序。但是如果要求字典序最小的排列，那就错了。

可以举出反例：$4$种菜肴，限制为$<2,4><3,1>$，

那么字典序最小的是$2,3,1,4$，但题目要求的最优解是$3,1,2,4$。

继续考虑，可以发现，如果最后一个数字在合法范围内尽可能大，那么这样是绝对有利的。

因为如果设最后一个数字是$x$，那么除了$x$之外的所有数都不会被放到最后一个位置。

而这样就可以让前面所有小于$x$的数都尽量靠前（大于$x$的数，虽然也能靠前，但由于$x$的位置已经固定，因此没有用），达到题目的目标。

因此，最优解就是符合条件的排列中，**反序列**的字典序**最大**的排列。

所以，在反图上跑拓扑排序，求最大字典序。在实现上，由于需要多次找出队列中的最大值，因此用堆代替队列。

代码：

```cpp
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
inline int read() {
    int res = 0; bool bo = 0; char c;
    while (((c = getchar()) < '0' || c > '9') && c != '-');
    if (c == '-') bo = 1; else res = c - 48;
    while ((c = getchar()) >= '0' && c <= '9')
        res = (res << 3) + (res << 1) + (c - 48);
    return bo ? ~res + 1 : res;
}
const int N = 3e5 + 5;
priority_queue<int> Hea;
int n, m, ecnt, nxt[N], adj[N], go[N], cnt[N], ans[N];
void add_edge(int u, int v) {
    nxt[++ecnt] = adj[u]; adj[u] = ecnt; go[ecnt] = v; cnt[v]++;
}
void work() {
    int i, x, y, tot = 0; ecnt = 0; memset(adj, 0, sizeof(adj));
    memset(cnt, 0, sizeof(cnt)); n = read(); m = read(); bool flag = 0;
    for (i = 1; i <= m; i++) {
        x = read(); y = read();
        add_edge(y, x); if (x == y) flag = 1;
    }
    if (flag) return (void) puts("Impossible!");
    for (i = 1; i <= n; i++) if (!cnt[i]) Hea.push(i);
    while (!Hea.empty()) {
        int u = Hea.top(); Hea.pop(); ans[++tot] = u;
        for (int e = adj[u], v; e; e = nxt[e])
            if (!(--cnt[v = go[e]])) Hea.push(v);
    }
    if (tot < n) return (void) puts("Impossible!");
    for (i = n; i; i--) printf("%d ", ans[i]);
    printf("\n");
}
int main() {
    int T = read();
    while (T--) work();
    return 0;
}
```