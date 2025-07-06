# P1850 题解

# [NOIPTG2016换教室](https://www.luogu.org/problemnew/show/P1850)

## 0x00 [个人博客推广⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄](http://www.vixbob-lwc.pw/)

## 0x01 暴力

直接顺序枚举换几节课，并枚举所有的情况并算出答案，复杂度大概是$O(\sum_i^n(C_n^i) * f(n))$

$C_n^i$ 表示组合数，$f(n)$表示每次算答案的时间，期望得分$60$ ~ $80$ (常数优秀的话)

## 0x02 设计状态

这道题一开始如果往$DP$这个方向思考的话很容易设计出状态，$dp[i][j]$  表示走完前$i$个教室, 换了$j$次的最优方案。然后我再往下思考怎么转移的时候，就想不出来了，因为这样设计状态是没法转移到，因为处理当前走到的教室和上一次走到的教室是有关系的，你不知道上一次的教室就无法转移，因为我们设计的状态没有办法表示上一次的教室选择，所以很自然状态变为$dp[i][j][k]$， 前两维表示的意思没有改变第三维$k$表示处理到第$i$个教室，我有没有选择换教室

## 0x03转移

先考虑不换的情况，即$k = 0$时的情况

$C1 = c[i - 1], C2 = d[i - 1], C3 = c[i], C4 = d[i]$

$mp[i][j]$表示$i,j$间的最短路
	
$dp[i][j][0] =min\begin{cases} dp[i - 1][j][0] + mp[C1][C3]\\dp[i - 1][j][1] + mp[C1][C3] * (1 - k[i - 1]) + mp[C2][C3] * k[i - 1]\end{cases}$


显然如果$i-1$时没有换教室那么，$i - 1$到$i$只有一种情况就是都不换教室，如果$i - 1$时换了教室那么就有两种情况$i - 1$换成功了，或者没换成功所以就是对应的路径长乘上对应的概率

$dp[i][j][1] =min\begin{cases} dp[i - 1][j - 1][0] + mp[C1][C3] * (1 - k[i]) + mp[C1][C4] * k[i]\\dp[i - 1][j - 1][1] + mp[C2][C4] * k[i] * k[i - 1] + mp[C2][C3] * k[i - 1] * (1 - k[i]) + mp[C1][C4] * (1 - k[i - 1]) * k[i] + mp[C1][C3] * (1 - k[i - 1]) * (1 - k[i])\end{cases} $

有上面的经验对于为$k = 1$的情况也很好理解了,显然对于$i - 1$可以是$k = 0 || k = 1$,
对于$k = 0$那么就有两种情况，$k = 1$就有四种情况，就不一一列举了

## 0x04 预处理

对于这道题我们只用预处理出两点之间的最短路就好了又因为只有$300$个点，所以$Floyd$是一个很好的选择

```
for (register int k = 1; k <= v; k++)
    for (register int i = 1; i <= v; i++)
        for (register int j = 1; j <= v; j++)
            mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j]);
```

$PS$ : $mp$初始化的时候不要开太大了，在$Floyd$中会爆$int$

## 0x05 代码

```
#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2e3 + 5;
const double inf = 1e17 + 5;
int n, m, v, e, c[MAXN][2], mp[305][305];
double k[MAXN], dp[MAXN][MAXN][2], ans;
inline int read() {
    char ch = getchar(); int u = 0, f = 1;
    while (!isdigit(ch)) {if (ch == '-')f = -1; ch = getchar();}
    while (isdigit(ch)) {u = u * 10 + ch - 48; ch = getchar();}return u * f;
}
int main(){
    memset(mp, 63, sizeof(mp));
    n = read(); m = read(); v = read(); e = read();
    for (register int i = 1; i <= n; i++)c[i][0] = read();
    for (register int i = 1; i <= n; i++)c[i][1] = read();
    for (register int i = 1; i <= n; i++)scanf("%lf", &k[i]);
    for (register int i = 1; i <= e; i++){
        int x = read(), y = read(), w = read();
        mp[x][y] = mp[y][x] = min(mp[x][y], w);
    }
    for (register int k = 1; k <= v; k++)
        for (register int i = 1; i <= v; i++)
            for (register int j = 1; j <= v; j++)
                mp[i][j] = min(mp[i][j], mp[i][k] + mp[k][j]);
    for (register int i = 1; i <= v; i++)mp[i][i] = mp[i][0] = mp[0][i] = 0;
    for (register int i = 0; i <= n; i++)
        for (register int j = 0; j <= m; j++)dp[i][j][0] = dp[i][j][1] = inf;
    dp[1][0][0] = dp[1][1][1] = 0;
    for (register int i = 2; i <= n; i++){
        dp[i][0][0] = dp[i - 1][0][0] + mp[c[i - 1][0]][c[i][0]];
        for (register int j = 1; j <= min(i, m); j++){
            int C1 = c[i - 1][0], C2 = c[i - 1][1], C3 = c[i][0], C4 = c[i][1];
            dp[i][j][0] = min(dp[i][j][0], min(dp[i - 1][j][0] + mp[C1][C3], dp[i - 1][j][1] + mp[C1][C3] * (1 - k[i - 1]) + mp[C2][C3] * k[i - 1]));
            dp[i][j][1] = min(dp[i][j][1], min(dp[i - 1][j - 1][0] + mp[C1][C3] * (1 - k[i]) + mp[C1][C4] * k[i], dp[i - 1][j - 1][1] + mp[C2][C4] * k[i] * k[i - 1] + mp[C2][C3] * k[i - 1] * (1 - k[i]) + mp[C1][C4] * (1 - k[i - 1]) * k[i] + mp[C1][C3] * (1 - k[i - 1]) * (1 - k[i])));
        }
    }
    ans = inf;
    for (register int i = 0; i <= m; i++)ans = min(ans, min(dp[n][i][0], dp[n][i][1]));
    printf("%.2lf", ans);
    return 0;
}
```