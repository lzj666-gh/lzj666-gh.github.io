# P7913 题解

让我们先忽略廊桥数量的限制来安排航班。我们维护一个空闲的廊桥队列，每到达一架航班，就给它安排编号最小的廊桥供其使用。

现在加上廊桥数量的限制。容易发现刚才的廊桥分配方法直接就帮我们解决了廊桥限制的问题：如果当前有 $n$ 个廊桥可供使用，则分配到 $n+1$ 号及以后的廊桥实质上就是分配到远机位了，不需要再做任何额外的处理。

到这里做法就很清晰了：我们按照开头提到的分配方法来安排航班的停靠位置，记录各廊桥停靠的航班数，做一个前缀和，最后枚举分配给某个区的廊桥数，算出各情况下两区实际使用廊桥的航班数总和，即可解决本题。

```cpp
// Problem: P7913 [CSP-S 2021] 廊桥分配（洛谷民间数据）
// Contest: Luogu
// URL: https://www.luogu.com.cn/problem/P7913
// Memory Limit: 512 MB
// Time Limit: 1000 ms
//
// Powered by CP Editor (https://cpeditor.org)

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
struct range {
  int x, y;
} a[100005], b[100005];
int res1[100005], res2[100005];
int n;
bool cmp(const range& a, const range& b) { return a.x < b.x; }
void calc(range* t, int m, int* res) {
  priority_queue<pii, vector<pii>, greater<pii> > lq; // 等待离港航班队列
  priority_queue<int, vector<int>, greater<int> > wq; // 空闲廊桥队列
  for (int i = 1; i <= n; i++) wq.push(i);
  for (int i = 1; i <= m; i++) {
    while (!lq.empty() && t[i].x >= lq.top().first) {
      wq.push(lq.top().second);
      lq.pop();
    }
    if (wq.empty()) continue;
    int dest = wq.top();
    wq.pop();
    res[dest]++;
    lq.push(make_pair(t[i].y, dest));
  }
  for (int i = 1; i <= n; i++) res[i] += res[i - 1];
}
int main() {
  int m1, m2;
  cin >> n >> m1 >> m2;
  for (int i = 1; i <= m1; i++) cin >> a[i].x >> a[i].y;
  for (int i = 1; i <= m2; i++) cin >> b[i].x >> b[i].y;
  sort(a + 1, a + m1 + 1, cmp);
  sort(b + 1, b + m2 + 1, cmp);
  calc(a, m1, res1);
  calc(b, m2, res2);
  int ans = 0;
  for (int i = 0; i <= n; i++) {
    ans = max(ans, res1[i] + res2[n - i]);
  }
  cout << ans << endl;
  return 0;
}
```