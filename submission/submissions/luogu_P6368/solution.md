# P6368 题解

### Analysis

简单的字符串处理，首先左右镜面对称相当于把一个字符串翻转以后接在原串的后面。`algorithm` 库提供的函数 `std::reverse(begin, end)` 可以将给定容器翻转，其中 `begin` 表示容器头指针，`end` 表示尾指针，左闭右开。`string` 库提供的 STL `std::string` 通过重载 `+` 和 `+=` 运算符来支持两个字符串的拼接。将 $b$ 接到 $a$ 后面可以使用 `a += b` 实现。

上下的镜面对称相当于直接把上面的第 $i$ 行赋值给下面的第 $2r - i + 1$ 行即可。

注意 `std::string` 在存储字符串时下标是从 $0$ 开始的，所以 $y$ 读入后要减一。

### Code

```cpp
#include <string>
#include <iostream>
#include <algorithm>

const int maxn = 105;

int n, m, x, y;
std::string ans[maxn];

int main() {
  std::cin >> n >> m;
  for (int i = 1; i <= n; ++i) {
    std::cin >> ans[i];
    std::string tmp = ans[i];
    std::reverse(tmp.begin(), tmp.end());
    ans[i] += tmp;
  }
  for (int i = n << 1, j = 1; i > n; --i) {
    ans[i] = ans[j++];
  }
  std::cin >> x >> y;
  --y;
  ans[x][y] = (ans[x][y] == '#') ? '.' : '#';
  for (int i = 1, dn = n << 1; i <= dn; ++i) {
    std::cout << ans[i] << std::endl;
  }
  return 0;
}
```