# CF1842C 题解

题意简述：给定数组 $a$，可选择 $i,j$，$1\le i< j\le |a|$ 且 $a_i = a_j$，删去 $[i, j]$ 的所有数，后面的数（如果有）接上，问最多能删几个数。

考虑 Dp：为了方便，调换题目中 $i,j$ 的大小关系。

令 $f_i$ 表示前 $i$ 个数里面最多能删多少个数，则有：

$$f_i = \max(f_{j - 1} + i - j + 1, f_{i - 1})$$

其中 $1\le j< i\le |a|$ 且 $a_i = a_j$。

观察发现，其中主要的未知量就是 $f_{j - 1} - j + 1$，可以用 $mx_x$ 记录对于数字 $x$，满足 $a_j = x$ 的最大的 $f_{j - 1} - j + 1$，即可在 $O(1)$ 的时间内转移了，时间复杂度 $O(n)$。

```cpp
// 代码省略了不重要的内容。
vector<int> a(n + 1);
vector<int> f(n + 1);
vector<int> mx(n + 1, -INF);
for (int i = 1; i <= n; i++) {
    scanf("%d", &a[i]);
}
for (int i = 1; i <= n; i++) {
    f[i] = max(f[i - 1], i + mx[a[i]]);
    mx[a[i]] = max(mx[a[i]], f[i - 1] - i + 1);
}
printf("%d\n", f[n]);
```