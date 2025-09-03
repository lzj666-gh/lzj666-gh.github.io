# P2466 题解

##对一类动态规划问题的研究
###(摘自)湖南省长沙市第一中学 徐源盛 论文  By Bartholomew
当前决策对未来“行动”的费用影响只与当前决策有关
**好久没有写博客了,最近准备攻一波集训队论文(慌**


>**引自论文:**
>在常规动态规划问题中，我们面临当前状态时“行动”造成的花费往往与这个
状 态 是 同 时 计 算 的 。 例 如 在 经 典 的 石 子 合 并 问 题 中 ， 规 划 方 程 为
$$f[i][j]=max{f[i][k]+f[k+1][j]}+w(i,j)$$当我们计算 $f[i][j]$时，才会把将 i 到 j 的石子全部
合并到一起这一“行动”的费用加进去。这很符合我们的思维习惯。
然而近年来频繁出现一类动态规划问题，在这类问题中，当前“行动”的费用
的一部分需要在之前决策时被计算并以状态的形式对当前状态造成影响。造成这
一独特的计算的原因就是当前的决策会对未来的“行动”费用造成影响。这类问题
构造方程往往比较困难，需要仔细分析原题，找到矛盾所在。

那么简单来说就是**现在的决策内容会对之后的计算价值产生影响**

那么我们怎么办:简单,如果这个影响是我们能够求的,那么我们就**当前计算**就好了!

##题解
$1.$
先把所有的点包括起点按 $x$ 值排序，这样题目就变成从起点出发，每次可以
向左或向右走到最近的某个彩蛋，将其射落，设每个彩蛋第一次走到的时刻为 $t_i$，
答案就是 $$∑(y_i-t_i*v_i)max$$

$2.$
很容易想到用 $f[1][i][j]$、$f[2][i][j]$分别表示从起点出发已射落 i 到 j 这一段彩蛋，当前停留在 i 点、j 点的最大得分.
考虑 $f[1][i][j]$,即点 i 是当前射击的彩蛋，射击的得分与当前时刻挂钩，但
是当前的时刻是不能从 $f[1][i][j]$的状态中表示出来的。
我们发现上述方法的矛盾其实就在于**曾经的行走花费的时间会对当前的得分产生影响**，
我们可以进一步考虑 $f[1][i][j]$的求解，由于射击 i 的得分是 $yi-t*vi$，而 t
等于之前**每一步决策移动的时间总和**，这样我们就可以把$t*v_i$在之前的移动中就计算，也就是说每次移动都要把**未来会减少的得分计算在内**。
比如说从 $f[1][i][j]$推到 $f[1][i-1][j]$，即从 i 走到 i-1 时除了 i 到 j 这一段彩蛋
外，其它的彩蛋都在下落，将这丢失的分数一并计算到从 i 走到 i-1 中。由于-t*vi
已经在之前决策时计算，所以射击时加上 yi 即可。

用 $$w[i][j]=\sum_{i=0}^n v_i - \sum_{k=i}^jv_k$$

即除了 i 到 j 这一段的彩蛋外的
所有彩蛋下落速度和，那么很容易得到方程：

$$f1[i][j]=y[i]+max(f1[i+1][j]-(xi+1-xi)*w[i+1][j],f2[i+1][j]-(xj-xi)*w[i+1][j])$$
$$f2[i][j]=y[j]+max(f2[i][j-1]-(xj-xj-1)*w[i][j-1],f1[i][j-1]-(xj-xi)*w[i][j-1])$$
答案就是$$\frac{max(f1[1][n],f2[1][n])}{1000}$$
算法的时间复杂度为 $O(n^2)$。至此问
题已得到完全解决。

所以我们应该记住：对于当前决策影响未来的问题->就是现在算将来的影响再进行DP


```cpp
#pragma GCC optimize(3)
#pragma GCC optimize("Ofast")
#pragma GCC optimize("inline")
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#define N 1005
#define INF 0x3f3f3f3f
using namespace std;

int n, leftn, rightn;
double m, f[2][N][N], w[N][N], sum[N], getn;

struct node
{
    double x, y, v;
} a[N];

inline bool cmp(node A, node B)
{
    return A.x < B.x;
}

int main(int argc, char const *argv[])
{
    scanf("%d%lf", &n, &m);
    a[1] = node{m, 0.0, 0.0};
    for(int i = 2; i <= n + 1; i++)
        scanf("%lf", &a[i].x);
    for(int i = 2; i <= n + 1; i++)
        scanf("%lf", &a[i].y);
    for(int i = 2; i <= n + 1; i++)
        scanf("%lf", &a[i].v), getn += a[i].v;
    sort(a + 1, a + 2 + n, cmp);
    for(int i = 1; i <= n + 1; i++)
    {
        sum[i] = sum[i - 1] + a[i].v;
        if(fabs(a[i].x - m) <= 1e-15 && fabs(a[i].y - 0.0) <= 1e-15)
        {
            leftn = rightn = i;
        }
    }
    memset(f, -INF, sizeof f);
    f[0][leftn][leftn] = f[1][rightn][rightn] = 0.00;
    for(register int k = 1; k <= n + 1; ++k)
    {
        for(register int i = 1; i + k <= n + 1; ++i)
        {
            int j = i + k;
            f[0][i][j] = a[i].y + max(f[0][i + 1][j] - (a[i + 1].x - a[i].x) * (sum[n + 1] + sum[i] - sum[j]),
                                      f[1][i + 1][j] - (a[j].x - a[i].x) * (sum[n + 1] + sum[i] - sum[j]));
            f[1][i][j] = a[j].y + max(f[1][i][j - 1] - (a[j].x - a[j - 1].x) * (sum[n + 1] + sum[i - 1] - sum[j - 1]) ,
                                      f[0][i][j - 1] - (a[j].x - a[i].x) * (sum[n + 1] + sum[i - 1] - sum[j - 1]));
        }
    }
    printf("%.3lf\n", max(f[1][1][n + 1], f[0][1][n + 1]) / 1000.0);
    return 0;
}

```

