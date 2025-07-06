# AT_arc084_b 题解



### solution

我们先考虑暴力，把 $K$ 的倍数枚举，每枚举一个取每位求和。  

这肯定超时，关键是循环取每位爆炸，那么我们不妨想，一个数的各个位数和是如何求出的。



先看个位，$1$ 的位和为 $1$，$2$ 就在 $1$ 的前提下 $+1$ 以此类推，就能求出个位位和。  

再看其他位，无非就是 $n$ 个 $10$ 加上若干 $1$，思考 $10$，我们可以用 $1 \times 10$ 来表示，那各位和仍为 $1$。



综上，我们可以整理出两种状态：$+1$ 与 $\times 10$，那么 $+1$ 是各位和 $+1$，可 $\times 10$ 各位和却不便，故可以转换为 **01 bfs**，如图



![](https://cdn.luogu.com.cn/upload/image_hosting/qhejrx3s.png)



但是我们发现还有一个问题，那就是这种方法是会超 $\sf long~long$ 的，难道我们还要用高精吗？  

当然不，我们发现我们欲求 $K$ 的倍数，那么我们在每次 $\times 10$ 是 $\% K$ 就行了，因为这样余数不变，不影响结果。



讲完基本思路，讲一下如何实现。



我们知道 bfs 一般会用队列，那么在 01 bfs 中，我们会用到双向队列 $\rm deque$。  

`#include <queue>` 与 `#include <deque>` 均包含 $\rm deque$，可以用任意一个库。



### Code



```cpp
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <deque>
using namespace std;

const int NR = 1e6 + 5;
int k;
int ans;
bool vis[NR];
struct node {
	int num, w;
};
deque<node> d;

void bfs() {
	d.push_front(node{1, 1});
	vis[1] = true;
	while (!d.empty()) {
		int num = d.front().num, w = d.front().w;
		d.pop_front();
		if (num == 0) {
			cout << w << endl;
			return;
		}
		if (!vis[10 * num % k]) {
			d.push_front(node{10 * num % k, w});
			vis[10 * num % k] = true;
		}
		if (!vis[num + 1]) {
			d.push_back(node{num + 1, w + 1});
		}
	}
	return;
}

int main() {
	cin >> k;
	bfs();
	return 0;
}
```



