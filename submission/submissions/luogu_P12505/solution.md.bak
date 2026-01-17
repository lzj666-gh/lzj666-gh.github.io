# P12505 题解

神秘模拟赛 T1。同学在洛谷上测 50pts，在 lemon 上跑了 100pts。

### solution

我们可以举例考虑什么时候会产生贡献。

- 第一种情况是 $0010100$，此时将中间的 $0$ 改为 $1$ 会产生 $3$ 的贡献，记为 $add_3$。
- 第二种情况是 $0001000$，此时将 $1$ 某一边的 $0$ 改掉会提供 $2$ 的贡献，记为 $add_2$。
- 第三种情况是 $0011100$，此时我们从 $1$ 的连通块向两边扩展，每次会产生 $1$ 的贡献，就是剩下的 $0$ 的点。

我们统计出每种贡献出现的次数，把询问离线下来，从大向小加贡献即可。

具体实现的时候我对询问挂在 $k$ 上，做了个扫描线。

### code
```cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1e5 + 5;
int n, a[N], q, ans[N], pos[N], cnt, cnt_0, add_2, add_3;
vector<int> que[N];
string s;
signed main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    cin >> n >> q >> s; s = " " + s;
    for (int i = 1; i <= q; i ++ ) {
        int k; cin >> k;
        que[k].push_back(i);
    }
    int res = 0;
    for (int i = 1; i <= n; i ++ ) {
        if (s[i] == '1') {
            int j = i;
            while (j < n && s[j + 1] == '1') j ++ ;
            if (j - i + 1 >= 2) res += j - i + 1; 
            else if (j == i) pos[++ cnt] = i;
            i = j;
        } else cnt_0 ++ ;
    }
    for (int i = 1; i <= cnt; i ++ ) {
        if (pos[i] == pos[i + 1] - 2) add_3 ++ , i ++ ;
        else if (s[pos[i] + 1] != '1' && s[pos[i] - 1] != '1') add_2 ++ ;
    }
    for (auto it : que[0]) ans[it] = res;
    for (int i = 1; i <= cnt_0; i ++ ) {
        if (add_3) add_3 -- , res += 3;
        else if (add_2) add_2 -- , res += 2;
        else res += 1;
        for (auto it : que[i]) ans[it] = res;
        if (cnt_0 == n && i == 1) for (auto it : que[i]) ans[it] = 0; 
    }
    for (int i = cnt_0 + 1; i <= n; i ++ )
        for (auto it : que[i]) ans[it] = res;
    for (int i = 1; i <= q; i ++ ) cout << ans[i] << '\n';
    return 0;
}
```