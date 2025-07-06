# P11769 题解

### 分析

题意不难理解，挺字面的。

这个题是贪心，根据我们正难则反的原则，这里应该倒过来跑。因为有负贡献，我们可以把它向前合并，把两个一起算。

设当前练习日（负贡献的）和前一天时间分别为 $t$ 和 $t_p$，贡献分别为 $w$ 和 $w_p$。

那么，两天的总贡献为：
$$
t \times w + \min\{t, t_p\} \times w_p
$$
由题意得：$t \ge t_p$

且 $w < 0$

所以易得在 $t = t_p$ 时，原式取得最大值为：
$$
\min\{t, t_p\} \times (w + w_p)
$$
但是呢，这里的时间不能比之后的日子练习时间长，所以设目前时间最小值为 $mint$ （欸怎么是薄荷），则原式最大值为：
$$
\min\{t, t_p, mint\} \times (w + w_p)
$$
那么，只要用这个式子一直往前推，计算 $w$ 的后缀和直到总贡献为正时，再照贡献为正的情况来算就是最优情况力。

哦对了，贡献为正时，计算方式为：
$$
\min\{t, mint\} \times w
$$
剩下小的事项在代码里标出来力。

### Code!

```cpp
// Author: albertting
// Time: 2025/06/26 20:35:22
#include <bits/stdc++.h>
#define __Made return
#define in 0
#define China__ ;
using namespace std;

int n;
int t[1000005], w[1000005];

void init() {
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    cin >> n;
    for(int i = 1; i <= n; i++) cin >> t[i];
    for(int i = 1; i <= n; i++) cin >> w[i];
}

void solve() {
    long long ans = 0; // 十年 OI 一场空
    int mint = 1e9 + 1;
    for(int i = n; i >= 1; i--) {
        if(w[i] < 0) {
            w[i - 1] += w[i];
            t[i - 1] = min(t[i - 1], t[i]);
        } else {
            mint = min(mint, t[i]); // 这里要更新吼
            ans += 1ll * w[i] * mint;
        }
    }
    cout << ans;
}

int main() {
    init();
    solve();
    __Made in China__
}
```