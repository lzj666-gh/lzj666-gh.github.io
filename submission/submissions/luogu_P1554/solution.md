# P1554 题解

## 普通做法
枚举序列中的每个数字，用数位分离法统计每一个数码出现次数。

### 代码
```cpp
#include <bits/stdc++.h>
#define ll long long
//#define rw() ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#ifndef rw()
#ifdef __linux__
#define getchar getchar_unlocked
#define putchar putchar_unlocked
#endif

namespace FX {
	template<typename T> inline void r(T &in) {
		in = 0;
		bool bo = 0;
		char ch = getchar();
		while (!isdigit(ch)) {
			bo ^= (ch == '-');
			ch = getchar();
		}
		while (isdigit(ch))
			in = (in << 1) + (in << 3) + (ch ^ 48), ch = getchar();
		if (bo) {
			in = -in;
		}
	}
	template<typename T> inline void w(T out) {
		static char op[25];
		int top = 0;
		if (out < 0) {
			putchar('-');
			do {
				op[++top] = -(out % 10) + 48, out /= 10;
			} while (out);
		} else {
			do {
				op[++top] = out % 10 + 48, out /= 10;
			} while (out);
		}
		while (top)
			putchar(op[top--]);
		putchar(' ');
	}
	template<typename T, typename... Ts> inline void r(T &in, Ts &... ins) {
		r(in), r(ins...);
	}
	template<typename T, typename... Ts> inline void w(T out, Ts... outs) {
		w(out), w(outs...);
	}
	inline void w(const char *p) {
		while (*p) {
			putchar(*p++);
		}
	}
}
#undef getchar
#undef putchar
using namespace FX;
#endif
using namespace std;
ll n,m,ans[16];
int main() {
	r(m,n);
	for (ll i=m;i<=n;i++){
		for (ll u=i;u>0;u/=10){
			ans[u%10]++;
		}
	}
	for (ll i=0;i<10;i++){
		w(ans[i]);
	}
	return 0;
}
```

## 进阶做法
用记忆化搜索统计每个数码在序列 $[1, 2, \ldots, M - 2, M - 1]$ 和序列 $[1, 2, \ldots, N - 1, N]$ 中出现次数，它们的差就是这个数码在序列 $[M, M + 1, M + 2, \ldots, N - 1, N]$ 出现次数，记忆化搜索的讲解看代码注释。

### 代码
```cpp
#include <bits/stdc++.h>
#define ll long long
//#define rw() ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#ifndef rw()
#ifdef __linux__
#define getchar getchar_unlocked
#define putchar putchar_unlocked
#endif

namespace FX {
	//里面的代码与之前给出的相同
}
#undef getchar
#undef putchar
using namespace FX;
#endif
using namespace std;
ll n, m, num[16], p, cnt, f[16][16][2][2], ans[16];
/*
x是当前为从高到低第几位，p是正在统计的数码，y是当前p出现的次数。
bo是判断之前的是不是前导零，bl是判断之前的是否达到上限。
*/
ll dfs(ll x, ll y, bool bo, bool bl) {
	if (f[x][y][bo][bl] != -1) {
		return f[x][y][bo][bl];
	}
	if (!x) {
		return y;
	}
	ll maxx = (bl ? num[x] : 9), sum = 0;
	for (ll i = 0; i <= maxx; i++) {
		if (!p) {//注意前导零不能被算在内
			sum += dfs(x - 1, y + (!i && !bo), !i && bo, bl && i == maxx);
		} else {
			sum += dfs(x - 1, y + (i == p), !i && bo, bl && i == maxx);
		}
	}
	return f[x][y][bo][bl] = sum;
}

int main() {
	r(m,n);
	m--;
	while (m) {
		num[++cnt] = m % 10;
		m /= 10;
	}
	for (p = 0; p <= 9; p++) {
		memset(f, -1, sizeof f);
		ans[p] = dfs(cnt, 0, 1, 1);
	}
	cnt = 0;
	while (n) {
		num[++cnt] = n % 10;
		n /= 10;
	}
	for (p = 0; p <= 9; p++) {
		memset(f, -1, sizeof f);
		w(dfs(cnt, 0, 1, 1) - ans[p]);
	}
	return 0;
}
```