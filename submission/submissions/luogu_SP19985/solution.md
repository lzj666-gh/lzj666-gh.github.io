# SP19985 题解

## [题目传送门](https://www.luogu.com.cn/problem/SP19985)
## 题目大意：
T 组数据，每组数据给出一个 n，求：
$$\sum_{i=1}^{n}{\sum_{j=i+1}^{n}{\gcd(i,j)}}$$
对 $2^{64}$ 取模！
## 前置芝士：
1.杜教筛（先在这里留个坑，以后再填）

2.莫比乌斯反演（可以看看这个[莫比乌斯反演](https://dpkajj.blog.luogu.org/mobius-J)）

先颓一下式子：
$$\sum_{i=1}^{n}{\sum_{j=i+1}^{n}{\gcd(i,j)}}$$
$$=\sum_{i=1}^{n}{\sum_{j=1}^{i-1}{\gcd(i,j)}}$$
设 d 为$ \gcd(i,j) $

$$=\sum_{d=1}^{n}{
d
\sum_{i=1}^{n}{
\sum_{j=1}^{i-1}{
\left [ \gcd(i,j)=d\right ]}
}
}$$
同时除以 d
$$=\sum_{d=1}^{n}{
d
\sum_{i=1}^{\left \lfloor \frac{n}{d} \right \rfloor}{
\sum_{j=1}^{i-1}{
\left [ \gcd(i,j)=1\right ]}
}
}$$
因为：
$$\sum_{i=1}^{n-1}{\left [ \gcd(i,n)=1 \right ]}=\varphi(n)$$
所以：
$$
\sum_{d=1}^{n}{
d
\sum_{i=1}^{\left \lfloor \frac{n}{d} \right \rfloor}{
\sum_{j=1}^{i-1}{
\left [ \gcd(i,j)=1\right ]}
}
}$$
$$=\sum_{d=1}^{n}{
d
\sum_{i=1}^{\left \lfloor \frac{n}{d} \right \rfloor}{
\varphi(i)
}
}$$
$\varphi(i)$ 的前缀和用杜教筛求出，整除分块即可得出最终答案。

对于取模，开 unsigned long long 即可自动溢出取模。

代码：

```cpp
#include <bits/stdc++.h>
#define int unsigned long long
#define N 10000000
using namespace std;
template <typename T> inline int read() {
    T n = 0, m = 1;
    char c = getchar();

    while (!isdigit(c)) {
        if (c == '-')
            m = -1;

        c = getchar();
    }

    while (isdigit(c)) {
        n = (n << 1) + (n << 3) + c - '0';
        c = getchar();
    }

    return n * m;
}
template <typename T> inline void write(T n) {
    if (n > 9)
        write(n / 10);

    putchar((n % 10) + '0');
}
unordered_map <int, int> mp;
int tot, prime[10000001], phi[10000001];
bool v[10000001];
void get() {
    phi[1] = 1;

    for (int i = 2; i <= N; i++) {
        if (!v[i])
            prime[++tot] = i, phi[i] = i - 1;

        for (int j = 1; j <= tot && prime[j]*i <= N; j++) {
            v[prime[j]*i] = 1;

            if (!(i % prime[j])) {
                phi[i * prime[j]] = phi[i] * prime[j];
                break;
            }

            phi[i * prime[j]] = phi[i] * (prime[j] - 1);
        }
    }

    for (int i = 1; i <= N; i++)
        phi[i] += phi[i - 1];
}
int sum(int n) {
    return ((n & 1) ? (n + 1) / 2 * n : n / 2 * (n + 1));
}
int get_phi(int n) {
    if (n <= N)
        return phi[n];

    if (mp[n])
        return mp[n];

    int ans = sum(n);

    for (int l = 2, r; l <= n; l = r + 1) {
        r = n / (n / l);
        ans -= (r - l + 1) * get_phi(n / l);
    }

    mp[n] = ans;
    return ans;
}
int ans(int n) {
    int ans = 0;

    for (int l = 1, r; l <= n; l = r + 1) {
        r = n / (n / l);
        ans += (get_phi(n / l) - 1) * (sum(r) - sum(l - 1));
    }

    return ans;
}
signed main() {
    get();
    int t = read<int>();

    while (t--)
        write<int>(ans(read<int>())), puts("");

    return 0;
}
```
