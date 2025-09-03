# P10096 题解

[P10096 [ROIR 2023 Day 1] 扫地机器人
](https://www.luogu.com.cn/problem/P10096)

### 题目分析

注意到要求路径所覆盖的面积，我们可以考虑将路径分解为若干个矩形的面积并。

记扫地机器人的左下角为 $(x,y)$。

- `N`，向上：矩形的左下角为 $(x, y)$，右上角为 $(x+k, y+k+d)$

- `S`，向下：矩形的左下角为 $(x, y-d)$，右上角为 $(x+k, y+k)$

- `W`，向左：矩形的左下角为 $(x-d, y)$，右上角为 $(x+k, y+k)$

- `E`，向右：矩形的左下角为 $(x, y)$，右上角为 $(x+k+d, y+k)$

接下来就是矩形面积并了，运用扫描线即可，不会的转[P5490](https://www.luogu.com.cn/problem/P5490)。

code:

```cpp
#include <bits/stdc++.h>
#define int long long
#define ls p<<1
#define rs p<<1|1
#define fi first
#define se second
#define pb push_back
#define mk make_pair
#define ll long long
#define space putchar(' ')
#define enter putchar('\n')
using namespace std;

typedef pair <int, int> pii;
typedef vector <int> vi;

template <typename T> inline T rd(T& x) {
    x = 0; int f = 1;
	char c = getchar();
    while (!isdigit(c)) f = c == '-' ? -1 : f, c = getchar();
    while (isdigit(c)) x = (x<<3)+(x<<1)+(c^48), c = getchar();
    return x *= f;
}

template <typename T> inline void write(T x) {
	if (x < 0) x = -x, putchar('-');
	if (x > 9) write(x/10);
	putchar('0'+x%10);
}

const int N = 1e5+5;
struct node { int x, l, r, k; } e[N<<1];
int n, k, x, y, tot, ans, b[N<<1], len[N<<3], cnt[N<<3];

void add(int x1, int y1, int x2, int y2) {
	b[tot+1] = x1, b[tot+2] = x2;
	e[tot+1] = {y1, x1, x2, 1}, e[tot+2] = {y2, x1, x2, -1};
	tot += 2;
}

bool cmp(node a, node b) { return a.x < b.x; }

void pushup(int p, int l, int r) {
	if (cnt[p]) len[p] = b[r+1]-b[l];
	else len[p] = len[ls]+len[rs];
}

void modify(int p, int l, int r, int ql, int qr, int x) {
	if (qr < l || r < ql) return;
	if (ql <= l && r <= qr) return cnt[p] += x, pushup(p, l, r), void();
	int mid = l+r>>1;
	modify(ls, l, mid, ql, qr, x), modify(rs, mid+1, r, ql, qr, x);
	pushup(p, l, r);
}

signed main() {
	rd(k), rd(n);
	for (int i = 1; i <= n; ++i) {
		char c; cin >> c; int d = rd(d);
		if (c == 'N') add(x, y, x+k, y+k+d), y += d;
		else if (c == 'S') add(x, y-d, x+k, y+k), y -= d;
		else if (c == 'W') add(x-d, y, x+k, y+k), x -= d;
		else add(x, y, x+k+d, y+k), x += d;
	}
	n <<= 1;
	sort(e+1, e+n+1, cmp); sort(b+1, b+n+1); tot = unique(b+1, b+n+1)-b-1;
	for (int i = 1; i < n; ++i) {
		e[i].l = lower_bound(b+1, b+tot+1, e[i].l)-b;
		e[i].r = lower_bound(b+1, b+tot+1, e[i].r)-b;
		modify(1, 1, tot, e[i].l, e[i].r-1, e[i].k);
		ans += 1ll*len[1]*(e[i+1].x-e[i].x);
	}
	cout << ans;
	return 0;
}
```