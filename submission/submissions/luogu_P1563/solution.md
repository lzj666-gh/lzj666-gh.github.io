# P1563 题解

题目 [ P1563 玩具谜题](https://www.luogu.org/problemnew/show/P1563)

看到那么多人的代码一堆if else 题解写一堆的，我有点眼花，把我的发上来吧
截止发布为止，以下代码是全部AC的

这是一道简单的模拟类型的题，主要注意两点
+ 数据量有点大，int无法表示，用long才能100%AC
+ 朝外向左与朝内向右是一样的方向，反之亦然，因此模拟判断过程可以稍微简化

```c
#include <stdio.h>

#define MAX_N 100000
#define MAX_M 100000

int main()
{
    char er_dir[MAX_N] = {0};       // 存储朝向
    long n, m, i, cur = 0, a, s;
    char er_occ[MAX_N][11] = {{0}};     // 存储职业
    scanf("%ld%ld", &n, &m);
    for (i = 0; i < n; ++i) {
        scanf("%ld%s", er_dir+i, er_occ[i]);
    }
    for (i = 0; i < m; ++i) {
        scanf("%ld%ld", &a, &s);        // 获取左右和序数
        if (er_dir[cur] == a)       // 向外朝左与向内朝右是一致的，反之亦然
        {
            s *= -1;
        }
        cur = (cur + n + s) % n;
    }
    printf("%s", er_occ[cur]);
    return 0;
}
```