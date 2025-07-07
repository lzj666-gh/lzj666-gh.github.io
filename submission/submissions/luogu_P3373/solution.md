# P3373 题解

### update 2020.3.5 修改后符合了洛谷题解规范

[传送门](https://www.luogu.org/problemnew/show/P3373)

我又来发教科书般的代码了。

看看其他题解，发现线段树写的好乱啊，于是发了篇福利文。

相比较于P3372，此题多了个区间乘法。

一个 `tag` 似乎应付不了了，那么来两个 `tag` 啊： `add` 和 `mul` 。

##### 前置知识：通过 P3372【模板】线段树1

## 1. 区间加法

还是一样。

```cpp
s[pos].add = (s[pos].add + k) % mod;
s[pos].sum = (s[pos].sum + k * (s[pos].r - s[pos].l + 1)) % mod;
```

## 2. 区间乘法

这里就有点不一样了。

先把 `mul` 和 `sum` 乘上 `k` 。

对于之前已经有的 `add` ，把它乘上 `k` 即可。**在这里，我们把乘之后的值直接更新add的值。**

你想， `add` 其实应该加到 `sum` 里面，所有乘上 `k` 后，运用乘法分配律， `(sum + add) * k == sum * k + add * k` 。

这样来实现 `add` 和 `sum` 有序进行。

```cpp
s[pos].add = (s[pos].add * k) % mod;
s[pos].mul = (s[pos].mul * k) % mod;
s[pos].sum = (s[pos].sum * k) % mod;
```

## 3. pushdown的维护

现在要下传两个标记： `add` 和 `mul` 。

`sum` ：因为 `add` 之前已经乘过，所以在子孩子乘过 `mul` 后直接加就行。

`mul` ：直接乘。

`add` ：因为 `add` 的值是要包括乘之后的值，所以子孩子要先乘上 `mul` 。

```cpp
s[pos << 1].sum = (s[pos << 1].sum * s[pos].mul + s[pos].add * (s[pos << 1].r - s[pos << 1].l + 1)) % mod;

s[pos << 1].mul = (s[pos << 1].mul * s[pos].mul) % mod;

s[pos << 1].add = (s[pos << 1].add * s[pos].mul + s[pos].add) % mod;
```


## 代码

在此注释： `<<` 和 `|` 是位运算，`n << 1 == n * 2`，`n << 1 | 1 == n * 2 + 1`（再具体的自己百度）。


```cpp
#include <bits/stdc++.h>

#define MAXN 100010
#define ll long long

using namespace std;

int n, m, mod;
int a[MAXN];

struct Segment_Tree {
	ll sum, add, mul;
	int l, r;
}s[MAXN * 4];

void update(int pos) {
	s[pos].sum = (s[pos << 1].sum + s[pos << 1 | 1].sum) % mod;
    return;
}

void pushdown(int pos) { //pushdown的维护
	s[pos << 1].sum = (s[pos << 1].sum * s[pos].mul + s[pos].add * (s[pos << 1].r - s[pos << 1].l + 1)) % mod;
	s[pos << 1 | 1].sum = (s[pos << 1 | 1].sum * s[pos].mul + s[pos].add * (s[pos << 1 | 1].r - s[pos << 1 | 1].l + 1)) % mod;
	
	s[pos << 1].mul = (s[pos << 1].mul * s[pos].mul) % mod;
	s[pos << 1 | 1].mul = (s[pos << 1 | 1].mul * s[pos].mul) % mod;
	
	s[pos << 1].add = (s[pos << 1].add * s[pos].mul + s[pos].add) % mod;
	s[pos << 1 | 1].add = (s[pos << 1 | 1].add * s[pos].mul + s[pos].add) % mod;
		
	s[pos].add = 0;
	s[pos].mul = 1;
	return; 
}

void build_tree(int pos, int l, int r) { //建树
	s[pos].l = l;
	s[pos].r = r;
	s[pos].mul = 1;
	
	if (l == r) {
		s[pos].sum = a[l] % mod;
		return;
	}
	
	int mid = (l + r) >> 1;
	build_tree(pos << 1, l, mid);
	build_tree(pos << 1 | 1, mid + 1, r);
	update(pos);
	return;
}

void ChangeMul(int pos, int x, int y, int k) { //区间乘法
	if (x <= s[pos].l && s[pos].r <= y) {
		s[pos].add = (s[pos].add * k) % mod;
		s[pos].mul = (s[pos].mul * k) % mod;
		s[pos].sum = (s[pos].sum * k) % mod;
		return;
	}
	
	pushdown(pos);
	int mid = (s[pos].l + s[pos].r) >> 1;
	if (x <= mid) ChangeMul(pos << 1, x, y, k);
	if (y > mid) ChangeMul(pos << 1 | 1, x, y, k);
	update(pos);
	return;
}

void ChangeAdd(int pos, int x, int y, int k) { //区间加法
	if (x <= s[pos].l && s[pos].r <= y) {
		s[pos].add = (s[pos].add + k) % mod;
		s[pos].sum = (s[pos].sum + k * (s[pos].r - s[pos].l + 1)) % mod;
		return;
	}
	
	pushdown(pos);
	int mid = (s[pos].l + s[pos].r) >> 1;
	if (x <= mid) ChangeAdd(pos << 1, x, y, k);
	if (y > mid) ChangeAdd(pos << 1 | 1, x, y, k);
	update(pos);
	return;
}

ll AskRange(int pos, int x, int y) { //区间询问
	if (x <= s[pos].l && s[pos].r <= y) {
		return s[pos].sum;
	}
	
	pushdown(pos);
	ll val = 0;
	int mid = (s[pos].l + s[pos].r) >> 1;
	if (x <= mid) val = (val + AskRange(pos << 1, x, y)) % mod;
	if (y > mid) val = (val + AskRange(pos << 1 | 1, x, y)) % mod;
	return val;
}

int main() {
	scanf("%d%d%d", &n, &m, &mod);
	
	for (int i = 1; i <= n; i++) {
		scanf("%d", &a[i]);
	}
	
	build_tree(1, 1, n);
	
	for (int i = 1; i <= m; i++) {
		int opt, x, y;
		scanf("%d%d%d", &opt, &x, &y);
		if (opt == 1) {
			int k;
			scanf("%d", &k);
			ChangeMul(1, x, y, k);
		}
		if (opt == 2) {
			int k;
			scanf("%d", &k);
			ChangeAdd(1, x, y, k);
		}
		if (opt == 3) {
			printf("%lld\n", AskRange(1, x, y));
		}
	}
    
	return 0;
}
```

> 日拱一卒，功不唐捐