# P10412 题解

考查内容：

- 【3】贪心法。
- 一维的前缀和与差分技巧。（可能算【3】递推法？）

首先试图找到**周期**数列 $b$ 美妙的充要条件。

注意到，当且仅当 $\sum a_i\ge 0$ 时，数列 $b$ 美妙。下面给出证明：

（一）先证当 $\sum a_i < 0$ 时，数列 $b$ 不美妙。

显然，对于任意自然数 $k_0$，令 $k=k_0+n-1$，则 $\sum_{i=k_0}^kb_i=\sum a_i<0$。

（二）再证当 $\sum a_i\ge 0$ 时，数列 $b$ 美妙。

设数列 $b$ 的前缀和为 $s$，特别地，$s_{-1}=0$。取 $k_0\in[0,n-1]$ 使得 $s_{k_0-1}$ 取到最小值符合题意。

任取 $k\ge k_0$，则 $\sum_{i=k_0}^kb_i=s_k-s_{k_0-1}=s_{k\bmod n}+\lfloor\frac{k}{n}\rfloor\sum a_i-s_{k_0-1}\ge s_{k\bmod n}-s_{k_0-1}\ge 0$。

综上，当且仅当 $\sum a_i\ge 0$ 时，数列 $b$ 美妙。$\square$

至此，问题转化为最少花费多少代价，使得 $\sum a_i\ge 0$。我们也终于发现交换两个数的操作是没有用的。当 $\sum a_i\ge 0$ 时答案显然为 $0$，以下讨论 $\sum a_i < 0$ 的情况。

将 $a_i$ 升序排序，之后依次考虑每个 $a_i$，判断使用加一操作和删除操作哪个更优，就采用更优的方法，直到 $\sum a_i\ge 0$ 为止。需要注意 $a_i$ 不能被删空。

```cpp
const ll N = 1e5 + 5;
ll n, p, q, r, a[N];
cin >> n >> p >> q >> r;
for(ll i = 1; i <= n; ++i) cin >> a[i];
sort(a + 1, a + 1 + n);
ll sum = accumulate(a + 1, a + 1 + n, 0LL);
if(sum >= 0) cout << 0 << endl;
else {
    ll ans = 0;
    for(ll i = 1; i < n; ++i) {
        if(a[i] >= 0) break;
        ll now = min(-a[i], -sum);
        ll cost = min(p * now, q);
        ans += cost;
        sum += -a[i];
        if(sum >= 0) break;
    }
    if(sum < 0) ans += p * (-sum);
    cout << ans << endl;
}
```