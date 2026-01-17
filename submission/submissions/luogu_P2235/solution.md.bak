# P2235 题解

首先，在二进制意义下，$f(n)$为$n$的各位数翻转，即$f((\overline{a_1a_2...a_{x-1}a_x})_2)=(\overline{a_xa_{x-1}...a_2a_1})_2$。

网上好多题解里都没有给出上面命题的具体证明，所以这里就介绍一下证明过程吧（以下的证明过程中的数位全部为二进制意义，$n'$为$n$在二进制意义下的各位数翻转）。

基本思想是数学归纳法。首先，可以发现$n$取$1,2,3$时原命题都成立。

第一个递推式：$f(2n)=f(n)$。

设$n=\overline{a_1a_2...a_{x-1}a_x}$，那么$2n=\overline{a_1a_2...a_{x-1}a_x0}$。显然有$n'=(2n)'$（去掉前导$0$）。所以当$f(n)=n'$时一定有$f(2n)=(2n)'$。

第二个递推式：$f(4n+1)=2f(2n+1)-f(n)$。

设$n=\overline{a_1a_2...a_{x-1}a_x}$，那么$2n+1=\overline{a_1a_2...a_{x-1}a_x1}$，$4n+1=\overline{a_1a_2...a_{x-1}a_x01}$。

显然，

$2(2n+1)'-n'=\overline{1a_xa_{x-1}...a_2a_1}+\overline{1a_xa_{x-1}...a_2a_1}-\overline{a_xa_{x-1}...a_2a_1}$

$=\overline{10a_xa_{x-1}...a_2a_1}=(4n+1)'$。

也就是说，当$f(2n+1)=(2n+1)',f(n)=n'$时，$f(4n+1)=(4n+1)'$。

第三个递推式：$f(4n+3)=3f(2n+1)-2f(n)$。

还是设$n=\overline{a_1a_2...a_{x-1}a_x}$。此时有：

$2n'=\overline{a_xa_{x-1}...a_2a_10}$

$(2n+1)'=\overline{1a_xa_{x-1}...a_2a_1}$

$(4n+3)'=\overline{11a_xa_{x-1}...a_2a_1}$

$3(2n+1)'-2n'=\overline{1a_xa_{x-1}...a_2a_1}+\overline{1a_xa_{x-1}...a_2a_1}+\overline{1a_xa_{x-1}...a_2a_1}-\overline{a_xa_{x-1}...a_2a_10}$

$=\overline{11a_xa_{x-1}...a_2a_1}+\overline{a_xa_{x-1}...a_2a_10}-\overline{a_xa_{x-1}...a_2a_10}$

$=\overline{11a_xa_{x-1}...a_2a_1}=(4n+3)'$。

也就是说，当$f(2n+1)=(2n+1)',f(n)=n'$时，$f(4n+3)=(4n+3)'$。

归纳得出，对于任意一个$n\geq1$，$f(n)=n'$。

也就是说，$f(n)=n$的充分必要条件是$n$在二进制意义下是回文串。

将$m$化为二进制之后数位DP或者乱搞。

代码：

```cpp
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 605;
struct cyx {
    int n, a[N];
    cyx() {}
    cyx(int _n) :
        n(_n) {memset(a, 0, sizeof(a));}
} a, b, f[N], g[N];
cyx read() {
    int i = 1, j; cyx res = cyx(0); char c; bool flag = 0;
    while ((c = getchar()) < '0' || c > '9');
    if (c - 48) res.a[res.n = 1] = c - 48, flag = 1;
    while ((c = getchar()) >= '0' && c <= '9') {
        if (c - 48) flag = 1;
        if (flag) res.a[++res.n] = c - 48;
    }
    if (!res.n) res.a[res.n = 1] = 0;
    for (j = res.n; i < j; i++, j--) swap(res.a[i], res.a[j]);
    return res;
}
void write(cyx num) {
    int i; for (i = num.n; i; i--) putchar(num.a[i] + 48);
    putchar('\n');
}
cyx div2(cyx a) {
    int i; cyx b = a;
    for (i = b.n; i; i--) {
        if (b.a[i] & 1) b.a[i - 1] += 10;
        b.a[i] >>= 1;
    }
    while (b.n > 1 && !b.a[b.n]) b.n--;
    return b;
}
cyx add(cyx a, cyx b) {
    int i; cyx c = cyx(max(a.n, b.n));
    for (i = 1; i <= c.n; i++) {
        c.a[i] += a.a[i] + b.a[i];
        if (c.a[i] > 9) c.a[i + 1]++, c.a[i] -= 10;
    }
    if (c.a[c.n + 1]) c.n++; return c;
}
cyx pow2(int x) {
    int i, j, tmp; cyx res = cyx(1); res.a[1] = 1;
    for (i = 1; i <= x; i++) {
        tmp = 0;
        for (j = 1; j <= res.n; j++) {
            res.a[j] <<= 1; res.a[j] += tmp;
            if (res.a[j] > 9) res.a[j] -= 10, tmp = 1;
            else tmp = 0;
        }
        if (tmp) res.a[++res.n] = 1;
    }
    return res;
}
cyx plus1(cyx x) {
    int i = 1;
    while (i <= x.n && x.a[i] == 9) x.a[i++] = 0;
    if (i > x.n) x.a[++x.n] = 1; else x.a[i]++;
    return x;
}
cyx trans(cyx x) {
    int i; cyx res = cyx(1);
    for (i = 1; i <= x.n; i++)
        if (x.a[i]) res = add(res, pow2(i - 1));
    return res;
}
cyx solve(cyx v) {
    if (v.n == 1 && v.a[1] == 1) return pow2(0);
    f[0] = pow2(0);
    int i, j, k, h, n = v.n; for (i = 1; i <= v.n; i++)
        f[i] = pow2(i & 1 ? (i >> 1) + 1 : i >> 1),
        g[i] = i == 1 ? pow2(0) : f[i - 2];
    if (v.n & 1) {
        for (i = j = (v.n >> 1) + 1; j <= v.n; i--, j++)
            if (v.a[i] != v.a[j]) break;
        if (i) {
            if (v.a[i] > v.a[j]) for (k = h = (v.n >> 1) + 1; h <= v.n; k--, h++)
                v.a[k] = v.a[h];
            else {
                if (v.a[(v.n >> 1) + 1]) {
                    v.a[(v.n >> 1) + 1] = 0;
                    for (k = h = (v.n >> 1) + 1; h <= v.n; k--, h++)
                        v.a[k] = v.a[h];
                }
                else {
                    bool flag = 1;
                    for (k = 1; k < v.n; k++) if (v.a[k]) {flag = 0; break;}
                    if (flag) {
                        v.a[v.n--] = 0;
                        for (k = 1; k <= v.n; k++) v.a[k] = 1;
                    }
                    else {
                        k = (v.n >> 1) + 1;
                        while (!v.a[k]) v.a[k++] = 1; v.a[k]--;
                        for (i = 1; i <= (v.n >> 1); i++)
                            v.a[i] = v.a[v.n - i + 1];
                    }
                }
            }
        }
    }
    else {
        for (i = (v.n >> 1), j = (v.n >> 1) + 1; j <= v.n; i--, j++)
            if (v.a[i] != v.a[j]) break;
        if (i) {
            if (v.a[i] > v.a[j])
            for (k = (v.n >> 1), h = (v.n >> 1) + 1; h <= v.n; k--, h++)
                v.a[k] = v.a[h];
            else {
                bool flag = 1;
                for (k = 1; k < v.n; k++) if (v.a[k]) {flag = 0; break;}
                if (flag) {
                    v.a[v.n--] = 0;
                    for (k = 1; k <= v.n; k++) v.a[k] = 1;
                }
                else {
                    k = (v.n >> 1) + 1;
                    while (!v.a[k]) v.a[k++] = 1; v.a[k]--;
                    for (i = 1; i <= (v.n >> 1); i++)
                        v.a[i] = v.a[v.n - i + 1];
                }
            }
        }
    }
    cyx res = cyx(1); for (i = 1; i < n; i++) res = add(res, g[i]);
    if (n != v.n) return res; int mid = (n & 1) ? (n >> 1) + 1 : (n >> 1);
    cyx uu = cyx(0); for (i = mid; i >= 2; i--) uu.a[++uu.n] = v.a[i];
    while (uu.n > 1 && !uu.a[uu.n]) uu.n--; cyx vv = plus1(trans(uu));
    return add(res, vv);
}
int main() {
    a = read(); b = cyx(0);
    while (a.n != 1 || a.a[1]) b.a[++b.n] = a.a[1] & 1,
        a = div2(a); write(solve(b));
    return 0;
}
```