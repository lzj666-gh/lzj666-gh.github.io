# P4097 题解

欢迎来看 [OI Wiki](https://oi-wiki.org/ds/li-chao-tree/) 上李超树的教程，其中有一部分是我写的，所以可能在内容上会~~被包含~~有所重合。

---

李超树：插入直线/线段，支持查询单点极值。

用线段树对于每个区间维护在 $m=\frac{l+r}{2}$ 处取值最大的直线的信息。

现在我们需要插入一条线段 $f$，在这条线段完整覆盖的线段树节点代表的区间中，某些区间的最优线段可能发生改变。

考虑某个被新线段 $f$ 完整覆盖的区间，若该区间无最优线段，则该线段可以直接成为最优线段。

否则，设该区间的中点为 $m$，我们拿新线段 $f$ 在中点处的值与原最优线段 $g$ 在中点处的值作比较。

如果新线段 $f$ 更优，则将 $f$ 和 $g$ 交换。那么现在考虑在中点处 $f$ 不如 $g$ 优的情况：

1. 若在左端点处 $f$ 更优，那么 $f$ 和 $g$ 必然在左半区间中产生了交点，递归到左儿子中进行插入；
2. 若在右端点处 $f$ 更优，那么 $f$ 和 $g$ 必然在右半区间中产生了交点，递归到右儿子中进行插入。
3. 若在左右端点处 $g$ 都更优，那么 $f$ 不可能成为答案，不需要继续下传。

由于仅有一个交点，所以两边子区间最多会递归一个。复杂度 $\mathcal{O}(\log n)$．

> 这个做法比大部分分类讨论做法简洁，不需要对斜率正负等信息进行冗长的分类讨论，更容易记忆。

查询 $x=k$ 答案时，从根走到 $[x,x]$ 节点记录的所有最优直线在 $x=k$ 时取值的答案极值即为所求。这里是运用了**标记永久化**的思想。

一些基本的扩展：

- 如果是**插入线段**，需要定位到线段横坐标区间在李超树上的拆分出的区间，然后一个个递归修改下去，复杂度是 $\mathcal{O}(\log^2n)$ 的。
- 李超树的经典应用是斜率优化，[这里是关于此我之前写过的总结](https://www.cnblogs.com/do-while-true/p/15404389.html)。

```cpp
#include <iostream>
#include <string>
#define MOD1 39989
#define MOD2 1000000000
#define MAXT 40000
using namespace std;
typedef pair<double, int> pdi;

const double eps = 1e-9;

int cmp(double x, double y) {
  if (x - y > eps) return 1;
  if (y - x > eps) return -1;
  return 0;
}

struct line {
  double k, b;
} p[100005];

int s[160005];
int cnt;

double calc(int id, int d) { return p[id].b + p[id].k * d; }

void add(int x0, int y0, int x1, int y1) {
  cnt++;
  if (x0 == x1)  // 特判直线斜率不存在的情况
    p[cnt].k = 0, p[cnt].b = max(y0, y1);
  else
    p[cnt].k = 1.0 * (y1 - y0) / (x1 - x0), p[cnt].b = y0 - p[cnt].k * x0;
}

void upd(int root, int cl, int cr, int u) {  // 对线段完全覆盖到的区间进行修改
  int &v = s[root], mid = (cl + cr) >> 1;
  int bmid = cmp(calc(u, mid), calc(v, mid));
  if (bmid == 1 || (!bmid && u < v)) swap(u, v);
  int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
  if (bl == 1 || (!bl && u < v)) upd(root << 1, cl, mid, u);
  if (br == 1 || (!br && u < v)) upd(root << 1 | 1, mid + 1, cr, u);
}

void update(int root, int cl, int cr, int l, int r,
            int u) {  // 定位插入线段完全覆盖到的区间
  if (l <= cl && cr <= r) {
    upd(root, cl, cr, u);
    return;
  }
  int mid = (cl + cr) >> 1;
  if (l <= mid) update(root << 1, cl, mid, l, r, u);
  if (mid < r) update(root << 1 | 1, mid + 1, cr, l, r, u);
}

pdi pmax(pdi x, pdi y) {  // pair max函数
  if (cmp(x.first, y.first) == -1)
    return y;
  else if (cmp(x.first, y.first) == 1)
    return x;
  else
    return x.second < y.second ? x : y;
}

pdi query(int root, int l, int r, int d) {  // 查询
  if (r < d || d < l) return {0, 0};
  int mid = (l + r) >> 1;
  double res = calc(s[root], d);
  if (l == r) return {res, s[root]};
  return pmax({res, s[root]}, pmax(query(root << 1, l, mid, d),
                                   query(root << 1 | 1, mid + 1, r, d)));
}

int main() {
  ios::sync_with_stdio(false);
  int n, lastans = 0;
  cin >> n;
  while (n--) {
    int op;
    cin >> op;
    if (op == 1) {
      int x0, y0, x1, y1;
      cin >> x0 >> y0 >> x1 >> y1;
      x0 = (x0 + lastans - 1 + MOD1) % MOD1 + 1,
      x1 = (x1 + lastans - 1 + MOD1) % MOD1 + 1;
      y0 = (y0 + lastans - 1 + MOD2) % MOD2 + 1,
      y1 = (y1 + lastans - 1 + MOD2) % MOD2 + 1;
      if (x0 > x1) swap(x0, x1), swap(y0, y1);
      add(x0, y0, x1, y1);
      update(1, 1, MOD1, x0, x1, cnt);
    } else {
      int x;
      cin >> x;
      x = (x + lastans - 1 + MOD1) % MOD1 + 1;
      cout << (lastans = query(1, 1, MOD1, x).second) << endl;
    }
  }
  return 0;
}
```