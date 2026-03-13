# P5956 题解

#### 题意

有一些 $B$ ($2\le B\le 10^6$) 进制数字，其中数字 $i$ 有 $a_i$ ($a_i\ge 1$) 个。现在要用其中的一些组成一个最大的 $B$ 进制数 $X$ 满足 $X$ 是 $B-1$ 的倍数。之后有 $q$ ($1\le q\le 10^5$) 次询问，第 $i$ 次询问 $X$ 从低位数起的第 $k_i$ 个数字是什么 (如果不存在第 $k_i$ 位则输出 $-1$)。

#### 题解

显然 $X$ 是 $B-1$ 的倍数当且仅当 $X$ 所有位的和是 $B-1$ 的倍数。当选择所有数不满足条件时，由于 $a_i\ge 1$，只需要删除对应的一个数字即可。之后将所有数字从大到小排列就是最大的 $X$。每次询问二分即可。

时间复杂度：$O(B+q\log B)$。

#### 代码

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n, q;
    std::cin >> n >> q;
    std::vector<long long> a(n);
    long long sum = 0;
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
        sum += i * a[i];
    }
    if (sum % (n - 1) != 0)
        --a[sum % (n - 1)];
    for (int i = 1; i < n; ++i)
        a[i] += a[i - 1];
    for (int i = 0; i < q; ++i) {
        long long k;
        std::cin >> k;
        if (k >= a[n - 1]) {
            std::cout << -1 << "\n";
        } else {
            std::cout << std::upper_bound(a.begin(), a.end(), k) - a.begin() << "\n";
        }
    }
    return 0;
}

```

