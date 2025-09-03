# P1314 题解

# P1314 题解

附：建议 [blog](https://www.luogu.com.cn/blog/kimble-blog/p1314-ti-xie) 食用。

~~作者默认读题解的同学以认真读题并思考，不认真读题，你是看不懂地~~


## 题目分析：
### 解释式子
先来研究这一串式子：
$$y_i=\sum\limits_{j=l_i}^{r_i}[w_j \ge W] \times \sum\limits_{j=l_i}^{r_i}[w_j \ge W]v_j$$  

$\sum$ 的意思是：从下面的几循环到上面的几，每一次循环加上左边的数。比如 $\sum\limits_{i=1}^{n}a_i$， 可以看作是：
```cpp
for (int i = 1; i <= n; i++) {
    sum += a[i];
}
```


中括号的含义是如果满足中括号里面的内容，中括号就可以被看作 $1$，否则为 $0$，所以 $[w_j \ge W]$ 的意思是：如果满足 $w_j \ge W$, $[w_j \ge W] = 1$,  否则 $[w_j \ge W] = 0$。

### 思路大意

这道题可以使用二分答案来解决。我们二分 $W$ 后，就可以算出每个区间的检验值 $y_i$，然后计算出它们的和 $y$，将它与 $s$ 比较，更新二分的上下界。

计算区间的检验值可以使用[前缀和](https://www.luogu.com.cn/blog/kimble-blog/yi-wei-er-wei-qian-zhui-hu)，即预处理出数组 $qzh1$ 和 $qzh2$，表示前缀和中括号 和 $v$，然后用 $qzh1_r-qzh1_{l - 1}$ 得到区间 $[l,r]$ 的中括号前缀和，$qzh2_r-qzh2_{l-1}$ 得到区间 $[l,r]$ 的价值和。这样，区间的检验值 $y_i$ 就可以表示为最上面一大串巴拉巴拉的式子啦~



在二分答案时，需要判断 $y$ 和 $s$ 的大小关系来更新二分的上下界，具体方法 ~~可以参考代码实现~~ 听我解释下：如果多了，就说明通过线（$W$）太低了，就往上调，否则就说明通过线高了，往下调。

## 代码：
``` cpp
#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll n, m, s;
ll y, ans;
ll w[200010], v[200010];
ll l[200010], r[200010];
ll qzh1[200010], qzh2[200010];

bool check(ll wq) {
	y = 0;
	memset(qzh1, 0, sizeof(qzh1));  
	memset(qzh2, 0, sizeof(qzh2));
	// 多测不清空，爆零两行泪 
	for (int i = 1; i <= n; i++) {
		if (w[i] > wq)  // > 过了检测通过线 
			qzh1[i] = qzh1[i - 1] + 1, qzh2[i] = qzh2[i - 1] + v[i]; // 前缀和加上 
		else
			qzh1[i] = qzh1[i - 1], qzh2[i] = qzh2[i - 1];  // 承继原来的前缀 
	}
	for (int i = 1; i <= m; i++) {
		int rrrr = r[i];
		int llll = l[i];
		y += (qzh1[rrrr] - qzh1[llll - 1]) * (qzh2[rrrr] - qzh2[llll - 1]);  // 直接照着式子，简单分析，就会发现这跟式子几乎一模一样/doge 
	}
	if (y > s)
		return 1;  // 判断差值大还是小，为了二分的更改做准备 
	else
		return 0;
}

int main() {
	cin >> n >> m >> s;
	for (int i = 1; i <= n; i++)
		cin >> w[i] >> v[i];
	for (int i = 1; i <= m; i++)
		cin >> l[i] >> r[i];
	int lll = 1;
	int rrr = 2000010;  
	ans = s;
	while (lll <= rrr) { // 二分答案 
		int mid = lll + (rrr - lll) / 2;  // 防爆ll， 原式子：(lll + rrr) / 2 
		if (check(mid))
			lll = mid + 1;
		else
			rrr = mid - 1;
			ans = min(ans, llabs(s - y)); // 为了防止爆int， 所以写llabs 
	}
	cout << ans;
}
```


