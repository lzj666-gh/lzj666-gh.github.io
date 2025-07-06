# P10253 题解

绝世好题。

赛时写了 $55$ 分，赛后听了讲评过了这题，但感觉讲评讲的太简单了，打算写一篇题解细说。

## 算法 1 25 pts

我会暴力！

暴力枚举 $y$。因为 $x$ 一定不大于 $y$，时间复杂度 $O(Ty)$。

为什么 $x$ 不大于 $y$？

因为考虑到 $\lfloor \dfrac{x}{10} \rfloor \geq 0$，所以 $f(x) \geq x$。题目要求 $f(x) = y$，则有 $y \geq x$。

## 算法 2 35 pts

这是我场上想到的。

因为 $S < 9$，我们首先可以想到假设 $x_i$ 表示 $x$ 从左往右的第 $i$ 位，则 $\displaystyle{\sum_{i=1}^{n}x_i \leq 9}$。然后这就意味着 $y$ 可以分为最多 $10$ 段，每段的所有数都相同，并且 `unique` 去重后递增。

看不懂的话，给一个例子：首先没保证没前导零，那么最极端有类似 $y = 0000111223334445566666677788899$ 的情况，这个时候 $x = 100101001001010000010010010$。

我们记 $a_i$ 表示 $x$ 从左往右第 $i$ 个不为 $0$ 的位的值。那么 $y$ 去掉前导零后，从左往右一定是 $a_1,a_1,\cdots,a_1 + a_2,\cdots,a_1+a_2+a_3,\cdots \displaystyle{\sum_{i = 0}^{k}a_i}$。

$k$ 就是 $y$ 可以分的段数。

或者是我们可以把 $y$ 进行整理，例如 $111223334$ 整理得到 $y = 111111111+111111+1111+1$，会发现每一项都是一个数的重复，每一项重复的数恰巧就是上面讲的 $a_i$！

注意，上面这个很重要，正解就是这玩意。

先放这一部分代码。

```cpp
#include<bits/stdc++.h>
using namespace std;
int t;
int x, y, ans[100005];
string st;
int f(int x) {
	if (!x)
		return 0;
	return x + f(x / 10);
}
int sti(string x) {
	int res = 0;
	for (int i = 0; i < x.size(); i++)
		res = res * 10 + (x[i] - '0');
	return res;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> t;
	while (t--) {
		cin >> st;
		if (st.size() > 9) {
			int cnt = 0;
			ans[++cnt] = st[0] - '0';
			for (int i = 1; i < st.size(); i++)
				if (st[i] != st[i - 1])
					ans[++cnt] = st[i] - '0';
			bool r = 1;
			for (int i = 1; i <= cnt; i++)
				if(ans[i] < ans[i - 1])
					r = 0;
			if (!r) {
				cout << "-1\n";
				continue;
			}
			int ns = ans[1];
			if (ns != 0)
				cout << ans[1];
			for (int i = 1; i < st.size(); i++) {
				if (st[i] == 0)
					continue;
				if (st[i] != st[i - 1]) {
					cout << st[i] - '0' - ns;
					ns = st[i] - '0';
				} else
					cout << st[i] - '0' - ns;
			}
			cout << "\n";
		}
		if (st.size() <= 9) {
			y = sti(st);
			int r = 0;
			x = -1;
			for (int i = 0; i <= y; i++) {
				if (f(i) == y) {
					if (x == -1)
						x = i;
					else
						r = 1;
				}
			}
			if (r == 1)
				cout << "-1\n";
			else
				cout << x << "\n";
		}
	}
}
```

## 算法 3 55pts

可能可以 dfs/bfs 搜出来吧。但是我没写。

我相信玄学。

我没看出来我的代码是怎么做到 $55$ 的。

```cpp
#include<bits/stdc++.h>
using namespace std;
int t;
int x, y;
int f(int x){
	if (!x)
		return 0;
	return x + f(x / 10);
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	cin >> t;
	while (t--){
		cin >> y;
		int r = 0;
		x = -1;
		for (int i = 0; i <= y; i++){
			if (f(i) == y){
				if (x == -1)
					x = i;
				else
					r = 1;
			}
		}
		if (r == 1)
			cout << "-1\n";
		else
			cout << x << "\n";
	}
}
```

## 算法 4 70pts

我们考虑到算法 2 中那个变形。

$\lfloor \dfrac{x}{10}\rfloor$ 实际上是十进制右移，于是那个变形得以推广。

我们会发现，这构成了一个等比数列。

一个数 $x$ 重复 $k$ 次就是 $x + 10x +\dots +10^{k-1}x$。

我们发现，这构成了一个等比数列。

我们知道，等比数列有求和公式。如果不会，可以参考赵思林老师的《初等代数研究》（一本好书）或者直接翻人教 A 版选修二第一章（如果课本重修了请联系我）。

**下面我们的原数用 $X$ 表示。**

反正公式是 $S_n = \dfrac{a_1(1 - q^n)}{1-q}$。

$q$ 为公比， $a_1$ 为首项，$S_n$ 为前 $n$ 项和。

因为我们知道了 $q = 10$ 所以 $S_n = \dfrac{a_1(1-10^n)}{-9}$。

我们用一下分配律：$S_n = \dfrac{a_1-10^na_1}{-9}$。

分子和分母同时乘上 $-1$ 得 $S_n = \dfrac{10^n a_1 - a_1}{9}$。

把 $n = k, a_1 = x$ 代进去得到 $S_n = \dfrac{10^kx-x}{9}$。然后这只是其中的一项，我们把每一项加起来。

把所有的 $-x$ 加起来就是数字根（意思就是一个数每一位加起来的和）的相反数 $-S$。

把所有的 $10^kx$ 加起来得到 $10X$。因为原来从右往左第 $i$ 位在 $10^{i-1}$ 量级。没错吧。

那么得到 $f(x) = \dfrac{10X - S}{9}$。也就是 $9y=10X-S$。

然后就好写了。我们考虑从 $9y$ 开始枚举 $10X$。因为 $X$ 为整数，我们只要枚举 $10$ 的倍数。

因为 $10X-9y$ 每次加 $10$，每次把 $10X$ 加上 $10$ 只要边进位边维护 $S$ 即可，所以空间复杂度是 $O(\log_{10}y)$。这里为了更直观，把底数写上了。下面底数都为 $10$。我就省略了。

代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
int t;
int x, y;
string st;
int ans[514514];
int f(int x) {
	if (!x)
		return 0;
	return x + f(x / 10);
}
int sti(string x) {
	int res = 0;
	for (int i = 0; i < x.size(); i++)
		res = res * 10 + (x[i] - '0');
	return res;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> t;
	while (t--) {
		cin >> st;
		if (st == "0"){
			cout << st << "\n";
			continue;
		}
		int n = st.size(), fnd = 0;
		for (int i = n; i <= n + 10; i++)
			ans[i] = 0;
		for (int i = 1; i <= n; i++)
			ans[i] = st[i - 1] - '0';
		for (int i = 1; i <= n / 2; i++)
			swap(ans[i], ans[n - i + 1]);
		int jw = 0;
		for (int i = 1; i <= n; i++) {
			ans[i] = (ans[i] - jw) * 9 + jw;
			ans[i + 1] += ans[i] / 10;
			jw = ans[i] / 10;
			ans[i] %= 10;
			if (ans[n + 1])
				n++;
		}
		long long sum = 0, cha = 0;
		while (ans[1] != 0) {
			ans[1] ++;
			ans[2] += ans[1] / 10;
			ans[1] %= 10;
			cha++;
		}
		for (int i = 1; i <= n; i++)
			if (ans[i] >= 10) {
				ans[i + 1] += ans[i] / 10;
				ans[i] %= 10;
			}
		for (int i = 1; i <= n; i++)
			sum += ans[i];
		if (sum == cha) {
			bool qd = 0;
			for (int i = n; i >= 2; i--) {
				if (ans[i] != 0)
					qd = 1;
				if (ans[i] != 0 || qd == 1)
					cout << ans[i];
			}
			fnd = 1;
			cout << "\n";
			continue;
		}
		while (1) {
			if (cha > 9 * n)
				break;
			cha += 10;
			sum++;
			ans[2]++;
			for (int i = 2; i <= n; i++)
				if (ans[i] >= 10) {
					sum -= 9;
					ans[i] %= 10;
					ans[i + 1] ++;
				}
			//	cout << "\n:::\n";
			//	cout << cha << " " << sum << "\n\n\n";
			if (sum == cha) {
				bool qd = 0;
				for (int i = n; i >= 2; i--) {
					if (ans[i] != 0)
						qd = 1;
					if (ans[i] != 0 || qd == 1)
						cout << ans[i];
				}
				fnd = 1;
				cout << "\n";
				break;
			}
		}
		if (!fnd)
			cout << "-1\n";
	}
}
```

TLE 了， $70$ 分。为什么呢？

因为进位要扫一遍，实际上这样是 $O(T\log^2y)$ 的。我们知道 $\log y$ 在 $5 \times 10^5$ 左右，于是过不了。

## 最终算法 100pts

考虑到进位没必要扫一遍，我们只要不断进位，直到特定的一位没法进位了我们就不用进位了。

加上这个优化就变成了 $O(T\log y)$，当然可以通过。

```cpp
#include<bits/stdc++.h>
using namespace std;
int t;
int x, y;
string st;
int ans[514514];
int f(int x) {
	if (!x)
		return 0;
	return x + f(x / 10);
}
int sti(string x) {
	int res = 0;
	for (int i = 0; i < x.size(); i++)
		res = res * 10 + (x[i] - '0');
	return res;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cin >> t;
	while (t--) {
		cin >> st;
		if (st == "0"){
			cout << st << "\n";
			continue;
		}
		int n = st.size(), fnd = 0;
		for (int i = n; i <= n + 10; i++)
			ans[i] = 0;
		for (int i = 1; i <= n; i++)
			ans[i] = st[i - 1] - '0';
		for (int i = 1; i <= n / 2; i++)
			swap(ans[i], ans[n - i + 1]);
		int jw = 0;
		for (int i = 1; i <= n; i++) {
			ans[i] = (ans[i] - jw) * 9 + jw;
			ans[i + 1] += ans[i] / 10;
			jw = ans[i] / 10;
			ans[i] %= 10;
			if (ans[n + 1])
				n++;
		}
		long long sum = 0, cha = 0;
		while (ans[1] != 0) {
			ans[1] ++;
			ans[2] += ans[1] / 10;
			ans[1] %= 10;
			cha++;
		}
		for (int i = 1; i <= n; i++)
			if (ans[i] >= 10) {
				ans[i + 1] += ans[i] / 10;
				ans[i] %= 10;
			}
		for (int i = 1; i <= n; i++)
			sum += ans[i];
		if (sum == cha) {
			bool qd = 0;
			for (int i = n; i >= 2; i--) {
				if (ans[i] != 0)
					qd = 1;
				if (ans[i] != 0 || qd == 1)
					cout << ans[i];
			}
			fnd = 1;
			cout << "\n";
			continue;
		}
		while (1) {
			if (cha > 9 * n)
				break;
			cha += 10;
			sum++;
			ans[2]++;
			int i = 2;
			while (ans[i] >= 10) {
				sum -= 9;
				ans[i] %= 10;
				ans[i + 1] ++;
				i++;
			}
			if (sum == cha) {
				bool qd = 0;
				for (int i = n; i >= 2; i--) {
					if (ans[i] != 0)
						qd = 1;
					if (ans[i] != 0 || qd == 1)
						cout << ans[i];
				}
				fnd = 1;
				cout << "\n";
				break;
			}
		}
		if (!fnd)
			cout << "-1\n";
	}
}
```

## 一些其他的话

写了那么多，求管理通过，求大家点赞。

我写 $\LaTeX$ 的时候一直把“floor”写成“florr”，警示后人。

通过记录 rid 为 $151541554$，真吉利。