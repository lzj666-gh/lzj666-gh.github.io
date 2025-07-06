# P7589 题解

[题目链接](https://www.luogu.com.cn/problem/T169952?contestId=41599)

前置知识：[Nim 游戏](https://zhuanlan.zhihu.com/p/52931007)

本题的底层博弈模型为 Nim 游戏。将每条直线上黑棋和白棋之间的间距视为一个石子堆（准确地说，石子堆的石子数目等于黑棋和白棋间的距离减去一，因为棋子不能重叠），在不考虑后退操作的情况下，相当于 Alice 和 Bob 在玩一个 $n$ 个石子堆的 Nim 游戏。

现在考虑后退操作的影响。如果 Alice 具有必胜策略，Bob 仍“负隅顽抗”，不停地执行后退操作，那么 Alice 可以通过“反向操作”（reversible move）将 Bob 造成的影响消除，即 Bob 后退多少距离，Alice 就前进多少距离，这样就能将局面恢复到 Bob 后退之前的状态。由于规则的限制，不能无限执行后退操作，因此局面的胜负状态不会改变。

参考代码：
```cpp
#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[])
{
    int cases;
    cin >> cases;
    for (int cs = 1; cs <= cases; cs++)
    {
        int n, k, d, y, b, w, nim = 0;
        cin >> n >> k >> d;
        for (int i = 0; i < n; i++)
        {
            cin >> y >> b >> w;
            nim ^= abs(b - w) - 1;
        }
        cout << (nim ? "Yes" : "No") << '\n';
    }
    return 0;
}

```

