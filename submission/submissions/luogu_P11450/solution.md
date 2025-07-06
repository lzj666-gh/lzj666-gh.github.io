# P11450 题解

# USACO 24Dec Bronze B 题解

## 题意

给定一个三维的正方体奶酪，坐标从 $(0,0,0)$ 延伸到 $(N, N, N)$。有 $Q$ 次询问，每次询问给定三个数 $(x, y, z)$，表示切去由坐标点 $(x,y,z)$ 到坐标点 $(x+1,y+1,z+1)$ 的一个 $1\times 1\times 1$ 立方体奶酪。然后询问，在这个残缺的奶酪中，可以有多少种方式，可以插入一个 $1\times 1\times N$ 的木棒。保证对于 $1\leq i\leq Q$，$(x_i, y_i, z_i)$ 互不相同。

## 分析

可以对题意进行转化。空间中共有 $N\times N\times N$ 个正方体，为了方便，把他们表示为 $\{0,0,0\}$ 到 $\{N-1,N-1,N-1\}$。一个木棒相当与占据了 $n$ 个小正方体，且这 $n$ 个正方体在某一方向是连续的。在坐标上，这种规律呈现为 $x,y,z$ 三种坐标中有两种相同，另外一种构成一个 $1\sim n$ 的排列。比如当 $N=3$ 时，$\{1, 1, 0\},\{1, 1, 1\},\{1, 1, 2\}$ 这三个位置。

## 暴力

很显然当 $N\leq 100$ 时，可以开数组标记是否已经被挖掉。判断那些位置可以插入木棒时，$O(N^2)$ 枚举 $(x,y)$，$(x,z)$ 和 $(y,z)$，然后 $O(N)$ 判断是否可以插入。复杂度 $O(N^3Q)$。

## 对暴力进行优化

因为是在不停的扣奶酪，所以不难发现答案是单调不减的。

发现对于每一组相同的 $(x,y)$ 或 $(x,z)$ 或 $(y,z)$ 坐标，当且仅当这一条被覆盖了 $N$ 次后，才会对答案产生 $+1$ 的贡献。开三个 `map` 记录一下，每次更新的时候判断一下是否满足条件即可。

```cpp
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> PII;
const int Q = 2e5 + 5;
int n, q, x, y, z;
map<PII, int> mapab;
map<PII, int> mapac;
map<PII, int> mapbc;

int main() {
    scanf("%d %d", &n, &q);
    int ans = 0;
    for (int i = 1; i <= q; i ++) {
        scanf("%d %d %d", &x, &y, &z);
        mapab[{x, y}] ++;
        mapac[{x, z}] ++;
        mapbc[{y, z}] ++;
        if (mapab[{x, y}] == n) ans ++;
        if (mapac[{x, z}] == n) ans ++;
        if (mapbc[{y, z}] == n) ans ++;
        printf("%d\n", ans);
    }
    return 0;
}
// 是的，AC 代码比暴力要短
```

那这个题就做完了，撒花。