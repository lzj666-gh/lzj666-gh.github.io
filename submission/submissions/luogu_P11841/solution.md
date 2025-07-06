# P11841 题解

[题目传送门](https://www.luogu.com.cn/problem/P11841)

赛时 AC 了 T2T3，就差 T1 没调出来（恼。

一道很简单的数学题，可以逆向推回答案。首先目标数量小于初始数量肯定无解，因为操作只能增加数量。如果目标数量等于初始数量则不需要进行操作。否则进行逆向推导，如果第一堆的目标数量大于第二堆的目标数量，就尝试从第一堆中减去若干个第二堆的数量，如果无法实现就是无解。同理，如果第二堆的目标数量大于第一堆的目标数量，就尝试从第二堆中减去若干个第一堆的数量。如果最后目标数量等于初始数量就可以实现，否则无解。

```cpp
#include <iostream>

using namespace std;
using LL = long long;

LL Calc(LL a, LL b, LL c, LL d) {
  if (c < a || d < b) return -1;
  if (c == a && d == b) return 0;
  LL ans = 0;
  while (c > a || d > b) {
    if (c > d) {
      if (d == 0) return -1;
      LL k = (c - a) / d;
      if (k == 0) return -1;
      c -= k * d;
      ans += k;
    } else if (d > c) {
      if (c == 0) return -1;
      LL k = (d - b) / c;
      if (k == 0) return -1;
      d -= k * c;
      ans += k;
    } else return -1;
  } if (c == a && d == b) return ans;
  return -1;
}

int main() {
  ios::sync_with_stdio(false);
  ios_base::sync_with_stdio(false);
  cin.tie(0), cout.tie(0);

  LL T;
  cin >> T;
  while (T--) {
    LL a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << Calc(a, b, c, d) << "\n";
  } return 0;
}
```