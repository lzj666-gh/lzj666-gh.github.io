# P9749 题解

## [Problem](https://www.luogu.com.cn/problem/P9749)
## Solution
反悔贪心思想。

从左到右考虑，如果行驶到某个加油站，缺油的时候，从之前经过的**最便宜的加油站加油**。

维护变量 $f$ 表示当前的状态。

若 $f < 0$，则代表的是当前还能走多少公里的油。

否则 $f \geq 0$，表示当前需要加油，加的油量为 $\lceil \dfrac{s}{d} \rceil$。

注意本题的数据范围大，需要开 `long long`！

## Code
时间复杂度 $O(n)$。
```cpp
#include <bits/stdc++.h>

using namespace std;

using LL = long long;

const int N = 1e5 + 10;

int v[N], a[N];
int n, d;
int main() {
    scanf("%d%d", &n, &d);
    for (int i = 1; i < n; i++) scanf("%d", &v[i]);
    int mi = INT_MAX;
    LL ans = 0, s = 0;
    for (int i = 1; i < n; i++) {
        scanf("%d", &a[i]);
        s += v[i];
        mi = min(mi, a[i]);
        if (s > 0) {
            ans += (s + d - 1) / d * mi;
            s -= (s + d - 1) / d * d;
        }
    }
    printf("%lld\n", ans);
    return 0;
}
```