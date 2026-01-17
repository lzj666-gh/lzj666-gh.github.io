# P3203 题解

## ~~没人看的~~题意

游戏一开始，Lostmonkey在地上沿着一条直线摆上n个装置，每个装置设定初始弹力系数ki，当绵羊达到第i个装置时，它会往后弹ki步，达到第i+ki个装置，若不存在第i+ki个装置，则绵羊被弹飞。绵羊想知道当它从第i个装置起步时，被弹几次后会被弹飞。为了使得游戏更有趣，Lostmonkey可以修改某个弹力装置的弹力系数，任何时候弹力系数均为正整数。

## 实现

~~LCT裸题但我不会~~

看到这个，一定是用什么数据结构的；但是没有现成的好的方法，怎么办？分块！

设$f[i]$表示从i开始，跳出所在块的步数；$to[i]$表示跳出所在块后到了哪里；

初始化很简单啦，具体看代码吧；

要修改？整个块内暴力重构；

## 代码

```
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f
#define ri register int
#define il inline
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
#define mem0(x) memset((x),0,sizeof(x))
#define mem1(x) memset((x),0x3f,sizeof(x))
#define pb push_back
#define gc getchar
template<class T>void in(T &x) {
    x = 0; bool f = 0; char c = gc();
    while (c < '0' || c > '9') {if (c == '-') f = 1; c = gc();}
    while ('0' <= c && c <= '9') {x = (x << 3) + (x << 1) + (c ^ 48); c = gc();}
    if (f) x = -x;
}
#undef gc
#define N 200010
int k[N];
int block;
int bl[N];
int l[N >> 1];
int f[N], to[N];
int n, m;
il void replace(int p, int w) {
    k[p] = w;
    for (ri i = l[bl[p] + 1] - 1; i >= l[bl[p]]; --i) {
        if (i + k[i] >= l[bl[i] + 1]) {
            f[i] = 1;
            to[i] = i + k[i];
        }
        else {
            f[i] = f[i + k[i]] + 1;
            to[i] = to[i + k[i]];
        }
    }
}
il int query(int p) {
    int ret = 0;
    while (p <= n) {
        ret += f[p];
        p = to[p];
    }
    return ret;
}
signed main() {
    in(n);
    block = sqrt(n);
    for (ri i = 1; i <= n; ++i) {
        in(k[i]);
        bl[i] = (i - 1) / block + 1;
        if (bl[i] != bl[i - 1]) l[bl[i]] = i;
    }
    l[bl[n] + 1] = n + 1;
    //prework
    for (ri i = n; i >= 1; --i) {
        if (i + k[i] >= l[bl[i] + 1]) {
            f[i] = 1;
            to[i] = i + k[i];
        }
        else {
            f[i] = f[i + k[i]] + 1;
            to[i] = to[i + k[i]];
        }
    }
    in(m);
    int op, p, w;
    while (m--) {
        in(op), in(p);
        if (op == 1) {
            printf("%d\n", query(p + 1));
        }
        else {
            in(w);
            replace(p + 1, w);
        }
    }
    return 0;
}

```