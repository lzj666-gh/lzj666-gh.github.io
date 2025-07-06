# P3901 题解

这题其实可以做到$O(n)$预处理，每次$O(1)$查询

根本没有那么复杂……（似乎原来的题不同）


- 问题抽象为在一个序列中是否存在一个数，它的上一个和它相等数是否在序列中。

- 我们就可以用一个$Left$数组记录它上个和它相等的数出现的位置

- 所以我们就可以记录到$i$之前所有$Left$的最大值（$MaxLeft$），因为这个最有可能改变答案。（贡献最大）

- 每次询问$l$到$r$是否存在相同的。我们只要询问$MaxLeft[r]$是否$<$ $l$。如果是，那么答案就是$Yes$否则就是$No$。

- 对于$\le l$的$Left$对答案根本不会产生贡献

附代码：

```cpp
#include <bits/stdc++.h>
#define For(i, l, r) for(int i = (l), _end_ = (int)(r); i <= _end_; ++i)
#define Fordown(i, r, l) for(int i = (r), _end_ = (int)(l); i >= _end_; --i)
#define Set(a, v) memset(a, v, sizeof(a))
using namespace std;

bool chkmin(int &a, int b) {return b < a ? a = b, 1 : 0;}
bool chkmax(int &a, int b) {return b > a ? a = b, 1 : 0;}

inline int read() {
    int x = 0, fh = 1; char ch = getchar();
    for (; !isdigit(ch); ch = getchar() ) if (ch == '-') fh = -1;
    for (; isdigit(ch); ch = getchar() ) x = (x<<1) + (x<<3) + (ch ^ '0');
    return x * fh;
}

const int N = 1e5 + 1e2;
int n, q;
int a[N], Left[N];
int last[N], Max_Left[N];
void input() {
    n = read(); q = read();
    For (i, 1, n)
        a[i] = read();

    For (i, 1, n) {
        Left[i] = last[a[i]];
        last[a[i]] = i;
        chkmax(Max_Left[i], Left[i]);
        chkmax(Max_Left[i], Max_Left[i-1]);
    }
}

void solve() {
    while (q--) {
        int l = read(), r = read();
        puts(Max_Left[r] >= l ? "No" : "Yes");
    }
}

int main () {
    input();
    solve();
    return 0;
}
```
> PS:实测60ms,好像是最快的