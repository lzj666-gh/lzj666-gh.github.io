# P8654 题解

[题目传送门](https://www.luogu.com.cn/problem/P8654)

一道并查集模板题。

没什么好说的，先给个并查集模板，神犇可以直接跳过。

查找根：

```cpp
int find_root(int n) {
    if (fa[n] == n) return n;
    return fa[n] = find_root(fa[n]);
}
```
合并：

```cpp
void merge(int x, int y) { 
    int sx = find_root(x), sy = find_root(y);
    if (sx != sy) fa[sx] = sy;
}
```

预处理：

```cpp
for (int i = 1; i <= n; i++) fa[i] = i;
```
题目要求有多少个集合，也就是有多少个根。简单判断即可。

```cpp
if (fa[i] == i) ans++;
```
### Code

```cpp
#include <bits/stdc++.h>
#define ll long long
#define INF 1e9
using namespace std;
int m, n, k, ans;
int fa[1000005];
int find_root(int n) { // 查找根
    if (fa[n] == n) return n;
    return fa[n] = find_root(fa[n]);
}
void merge(int x, int y) { // 合并
    int sx = find_root(x), sy = find_root(y);
    if (sx != sy) fa[sx] = sy;
}
signed main() {
    ios :: sync_with_stdio(0);
    cin >> m >> n >> k;
    for (int i = 1; i <= m * n; i++) fa[i] = i; // 预处理
    for (int i = 1; i <= k; i++) {
        int u, v;
        cin >> u >> v;
        merge(u, v);
    }
    for (int i = 1; i <= m * n; i++) {
        if (fa[i] == i) ans++; // 如果是根，答案增加
    }
    cout << ans;
    return 0;
}
```

