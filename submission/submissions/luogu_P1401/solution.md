# P1401 题解

## P1401 [入门赛 #18] 禁止在 int 乘 int 时不开 long long 题解

### 思路分析

~~题目说的不是我吗？~~

题目要求在 `int` 乘 `int` 溢出时输出 $\texttt{long long int}$，否则输出 $\texttt{int}$，这里有个小技巧，我们可以利用 C++ 的数据自然溢出解题。

首先我们记 `int ix, iy, ia, ib;` 为对应数据在 `int` 类型下的储存，`long long x, y, a, b;` 为在 `long long` 类型下的储存。比较连个相乘的结果即可。

一种常见的错误：

```cpp
#include <cstdio>
int ix, iy;
int ia, ib;
long long x, y;
long long a, b;
int main()
{
    scanf("%lld%lld", &x, &y);
    scanf("%lld%lld", &a, &b);
    ix = x;
    iy = y;
    ia = a;
    ib = b;
    if (x * a != ix * ia || y * b != iy * ib)
    {
        printf("long long int\n");
    }
    else
    {
        printf("int\n");
    }
    return 0;
}
```

显而易见的 Hack 数据：

```plain
-1000000 1
-1 1000000
```

因为我们只相乘了左右端点，但如果其交叉相乘溢出则无法判断。

所以我们需要判断 $4$ 种情况。

### 代码实现

```cpp
#include <cstdio>
int ix, iy;
int ia, ib;
long long x, y;
long long a, b;
int main()
{
    scanf("%lld%lld", &x, &y);
    scanf("%lld%lld", &a, &b);
    ix = x;
    iy = y;
    ia = a;
    ib = b;
    if (x * a != ix * ia || x * b != ix * ib || y * a != iy * ia || y * b != iy * ib)
    {
        printf("long long int\n");
    }
    else
    {
        printf("int\n");
    }
    return 0;
}
```