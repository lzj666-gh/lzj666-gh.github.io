# SP3105 题解

## 简介

$ A^x=B(mod C) $ 已知ABC，求x；

如果互质 $ O(sqrt(phi(C)) $ 大步小步算法（分块）

## 方法

![](https://cdn.luogu.com.cn/upload/pic/28471.png)

先利用剩余系的性质，提出几个A，约去约数，使AC互质；

假设提出了k个A，因为要求最小正整数解，ans-k可能为负数，被舍去，所以暴力判断[0,k]；

先判特解：B==1，则x==0；

注意判无解：B不能整除gcd(A,C)（一定要在上一步之后）；

然后由欧拉定理可知，答案在[0,phi(c))之间，所以分块，一块一块用map判断；

## 注意事项

**WTF**，调了一晚上；

1.一定要把
```
(b *= inv(a2, c)) %= c;
    if (b == 1) {
        ans = k;
        return 1;
    }
```
放在它的前边：
```
if (b % gcd(a, c))  return 0;
```

因为当b==1时的情况要提前特判；

2.此题卡常，必须用扩展欧几里得；

3.一定要记得每次清空block；

## 代码


```cpp
//%:pragma GCC optimize(2)
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<stack>
#include<bitset>
#include<deque>
using namespace std;
#define ll long long
#define inf 0x3f3f3f3f
#define ri register int
#define il inline
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
#define mem0(x) memset((x),0,sizeof (x))
#define mem1(x) memset((x),0x3f,sizeof (x))
il char gc() {
    static const int BS = 1 << 22;
    static unsigned char buf[BS], *st, *ed;
    if (st == ed) ed = buf + fread(st = buf, 1, BS, stdin);
    return st == ed ? EOF : *st++;
}
#define gc getchar
template<class T>void in(T &x)
{
    x = 0; bool f = 0; char c = gc();
    while (c < '0' || c > '9') {if (c == '-') f = 1; c = gc();}
    while ('0' <= c && c <= '9') {x = (x << 3) + (x << 1) + (c ^ 48); c = gc();}
    if (f) x = -x;
}
#undef gc
void out(int x) {
    if (x < 0) putchar('-'), x = -x;
    if (x > 9) out(x / 10);
    putchar(x % 10 + '0');
}
#define int ll
il int getphi(int x) {
    int res = 1;
    for (int i = 2, mi = sqrt(x); i <= mi; ++i)
        if (x % i == 0) {
            res *= i - 1, x /= i;
            while (x % i == 0) res *= i, x /= i;
        }
    if (x > 1) res *= x - 1;
    return res;
}
il int qpow(int a, int b, int md) {  // calc a^b%md
    int ret = 1;
    for (; b; b >>= 1, (a *= a) %= md) if (b & 1) (ret *= a) %= md;
    return ret;
}
il void exgcd(int a, int b, int &x, int &y) {
    if (b == 0) {
        x = 1, y = 0;
        return;
    }
    exgcd(b, a % b, y, x);
    y -= a / b * x;
}
il int inv(int a, int md) {
    int x, y;
    exgcd(a, md, x, y);
    return x < 0 ? x + md : x;
}
il int gcd(ri a, ri b) {
    ri t;
    while (b) {
        t = a, a = b, b = t % a;
    }
    return a;
}
#define N 100000
map<int, int>block;
il bool bigsmall(int a, int b, int c, int &ans) { // calc a^x==b(mod c)
    int k = 0, a2 = 1, bb = b, cc = c;
    ri t;
    while ((t = gcd(a, c)) > 1 && !(b % t)) {
        b /= t, c /= t, ++k, (a2 *= a / t) %= c;
    }
    (b *= inv(a2, c)) %= c;
    if (b == 1) {
        ans = k;
        return 1;
    }
    if (b % gcd(a, c))  return 0;
    t = 1;
    for (ri i = 0; i <= k; ++i, (t *= a) %= cc) {
        if (t == bb) {
            ans = i;
            return 1;
        }
    }
    ri sq = (int)ceil(sqrt((double)getphi(c)));
    t = 1;
    for (ri i = 0; i <= sq; ++i, (t *= a) %= c)
        if (!block.count(t)) block[t] = i;
    for (ri i = 0, pow = qpow(a, sq, c), ta = 1; i <= sq; ++i, (ta *= pow) %= c) {
        if (block.count(t = (b * inv(ta, c) % c))) {
            ans = i * sq + block[t] + k;
            return 1;
        }
    }
    return 0;
}
int a, b, c, ans;
signed main() {
    while (in(a), in(c), in(b), a || b || c) {
        b %= c;
        if (bigsmall(a, b, c, ans)) printf("%lld\n", ans);
        else puts("No Solution");
        block.clear();
    }
    return 0;
}

```