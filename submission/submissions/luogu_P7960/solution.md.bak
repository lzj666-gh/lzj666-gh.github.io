# P7960 题解

谨以此题解来纪念我七年的 OI 生涯（退役了，再见了 OI）

像今年 T1 这种几年不遇的水题你是不可能再遇见第二次的。

这道题提前预处理单纯地筛一筛就可以了，没有别的任何操作。

需要注意的是，在预处理时要合理的剪枝，保证时间复杂度控制在  $O(10^7+T)$（$10^7$ 是数据范围，$T$是询问数）。

我们用 $f$ 数组表示该数是否被标记。如果一个数 $i$ 被标记过了，就直接跳过；如果 $i$ 含有数字 $7$，我们就将 $i$ 的所有倍数（包括 $i$ 本身）全部标记。

我们用 $nx$ 数组（也就是 $next$ 的缩写）来记录该数的下一个报的数是多少。在处理的时候，我们需要记录上一个报的数 $ls$（$last$ 的缩写，也就是没有标记的数）。如果 $i$ 没有标记过也不含有数字 $7$，那么 $nx_{ls}$ 就是 $i$，然后将 $ls$ 更新为 $i$。

预处理的好处就是保证询问的时候每次询问都是 $O(1)$。如果询问的 $x$ 被标记了，就输出 $-1$；反之，输出 $nx_x$。

还要注意一点，考场上一定要用上读入优化和输出优化，小心可能会被卡。

代码非常的好写，看看就可以了：

```cpp
#include <bits/stdc++.h>
using namespace std;
inline int read()//读入优化
{
    int x = 0, f = 1;
    char ch = getchar();
    while (!isdigit(ch))
    {
        f = ch != '-';
        ch = getchar();
    }
    while (isdigit(ch))
    {
        x = (x << 1) + (x << 3) + (ch ^ 48);
        ch = getchar();
    }
    return f ? x : -x;
}
inline void write(int x)//输出优化
{
    if (x >= 10)
        write(x / 10);
    putchar(x % 10 + 48);
}
const int N = 1e7 + 100;
int T, x, ls;
int f[N], nx[N];
bool check(int x)//判断是否含有数字7
{
    while (x)
    {
        if (x % 10 == 7)
            return 1;
        x /= 10;
    }
    return 0;
}
void init()//预处理部分
{
    for (int i = 1; i <= N - 10; i++)
    {
        if (f[i])//如果被标记过，就跳过
            continue;
        if (check(i))//如果含有数字7，标记其倍数
        {
            for (int j = i; j <= N - 10; j += i)
                f[j] = 1;
            continue;
        }
        nx[ls] = i;//记录i
        ls = i;//更新ls
    }
}
int main()
{
    init();//先预处理
    T = read();
    while (T--)
    {
        x = read();
        if (f[x])//被标记了输出-1，否则输出nx
            puts("-1");
        else
            write(nx[x]), putchar('\n');
    }
    return 0;
}
```

T1 太水了，导致其他三道很难，拉不开差距。今年 NOIP 直接爆炸，直接宣告了我的退役 QwQ。

总之，再见了 OI，感谢陪伴的七年，祝一切顺利。