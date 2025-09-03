# P2440 题解

$\boxed{\text{前言}}$

由于这道题有一名神仙选手@[yummy](https://www.luogu.com.cn/user/101694)重造了毒瘤数据并且撤下了 **24** 篇题解，我来义无反顾的填补这个巨大的坑!

这里很多题解都是几年前写的，思路不够完善、清晰，很多都是只放了一个代码就完事，我来注射一下新鲜血液。

$\boxed{\text{思路}}$

首先我们输入 n 和 k 并且运用二分找到合适的尺寸，而l 必须要足够小，r 必须要足够的大。题中写道数组中的数最大不会超过 100000000 ，所以我们设 100000001 就可以了。

现在就走到了判断的环节，我们如何判断 mid 是太小还是太大呢？我们需要编写一个新函数 -- f。

在函数 f 中，我们依次要判断 a 中的每一个数并计算出能切出多少个 mid ，还要用一个变量  ans 储存他们，如果 ans 分的分数比 k 多或者正好等于，返回真。如果是小于 k ，返回假。

当 f 返回的是真的时候，我们就要试试还能不能把 mid 调大一点，就要 

```
l = mid;
```

如果返回的是假，我们就加的太大了，就要把 $mid$ 调小一点，就要

```
r = mid;
```

一直到结束，输出 l 就可以了。

$\boxed{\text{完整代码区}}$

```cpp
// #include <bits/stdc++.h>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

long long n, k;
long long a[1000005];

bool f(long long x) {
	long long ans = 0;
	for (int i = 1; i <= n; i++) {
		ans += a[i] / x;
	}
	return ans >= k;
}

int main() {
	cin >> n >> k;
	for (int i = 1; i <= n; i++) cin >> a[i];
	
	long long l = 0, r = 100000001;
	long long mid;
	
	while (l + 1 < r) {
		mid = (l + r) / 2;
		if (f(mid)) l = mid;
		else r = mid;
	}
	cout << l << endl;
	return 0;
} 
```

$\boxed{\text{祈祷区}}$

管理员求过，路过人求赞，希望能给你一点点小小的帮助呢~