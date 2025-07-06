# P11157 题解

## 题解：P11157 【MX-X6-T3】さよならワンダーランド

### 题意

为了便于分析题意，我们设 $i+j$ 为 $k$。

则问题变成：给定序列 $a_1,\cdots,a_n$，对每个 $i$ 求一个 $k$，使 $k$ 满足：

* $1 \leq k \leq n$
* $a_i \leq k-i \leq a_k$

### 分析

我们可以通过化简式子较严格地确定 $k$ 的上界和下界，首先看下界：

* $1 \leq k$
* 由 $a_i \leq k - i$ 得 $a_i+i \leq k$

所以 $k$ 最小取到 $\max(1,a_i+i)$。

再看上界：

* $k \leq n$
* 由 $k-i \leq a_k$ 得 $k-a_k \leq i$

我们可以用下界来缩小 $k$ 的范围，用上界来判断 $k$ 是否有解。

首先如果 $k$ 取最小仍大于 $n$ 那么无解。

否则我们只需要确定是否有 $k-a_k \leq i$，也就是说只要在 $k$ 的取值范围内有 $(k-a_k)$ 的最小值小于等于 $i$ 就有解，否则无解。

这里 $k$ 的取值范围为 $\max(1, a_i+i) \leq k \leq n$， 所以我们可以 $\mathcal{O(n)}$ 预处理。用 $mn[k]$ 表示 $k \sim n$ 中 $k-a_k$ 的最小值，相应的 $mi[k]$ 表示 $k \sim n$ 中 $k-a_k$ 最小时 $k$ 的取值。

### 代码

没什么好说的了，先 $\mathcal{O(n)}$ 预处理 $mn$ 数组和 $mi$ 数组，再 $\mathcal{O(n)}$ 判断。

```cpp
//P11157 (AC)

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef pair <int, int> pii;

int read()
{
    int res = 0, f = 1;
    char ch = getchar();
    for (; !isdigit(ch); ch = getchar())
        if (ch == '-')
            f = -1;
    for (; isdigit(ch); ch = getchar())
        res = (res << 3) + (res << 1) + (ch - '0');
    return res * f;
}

const int N = 3e5 + 5;
const int INF = 0x3f3f3f3f;

int n;
int a[N];
int mi[N], mn[N];

int main()
{
    int i, k;

    n = read();
    for (i = 1; i <= n; i ++)
        a[i] = read();

    mn[n + 1] = INF;
    for (i = n; i >= 1; i --)
    {
        mn[i] = mn[i + 1];
        mi[i] = mi[i + 1];
        if (i - a[i] < mn[i])
        {
            mn[i] = i - a[i];
            mi[i] = i;
        }
    }

    for (i = 1; i <= n; i ++)
    {
        k = max(a[i] + i, 1);
        if (i >= mn[k] && k <= n)
            printf("1 %d\n", mi[k] - i);
        else
            printf("0\n");
    }

    return 0;
}
```