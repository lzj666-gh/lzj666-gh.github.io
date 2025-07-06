# B3614 题解

栈（stack）是一种后进先出的数据结构。

考虑一个容器，一端封死（称为栈底，bottom）。想向容器中加入元素，只能从另一端（称为栈顶，top）逐个加入。因为容器内的元素不能改变顺序，所以在从容器中去除物品只能按照从栈顶到栈底的顺序逐个取出。

数组可以很好的模拟栈。数组的开头（0）一侧可以看作不可移动的栈底，只需要维护一个栈顶指针，表示栈顶的**下一个**位置的下标，就可以轻松的实现插入与删除：

```cpp
struct Stack {
  int st[10000];
  int p;

  Stack() : p(0) {}

  void push(int x) { st[p++] = x; }
  void pop() { --p; }
  int top() { return st[p - 1]; }
  int size() { return p; }
};
```

STL 提供了 `std::stack` 作为封装好的栈，但是其底层内存分配逻辑是 `std::deque`，常数极大。一般而言，如果希望用 STL 实现 stack，可以考虑使用 `std::vector`。不难发现，其函数对应关系如下：

| stack   | vector       |
| ------- | ------------ |
| push(x) | push_back(x) |
| pop()   | pop_back()   |
| top()   | back()       |
| size()  | size()       |

另外需要注意的是，本题中 $x$ 的范围是 $[0, 2^{64} - 1]$，需要使用 unsigned long long int 存储。

以下是本题 std。

```cpp
#include <stack>
#include <string>
#include <iostream>

int main() {
  std::cin.tie(0);
  std::ios::sync_with_stdio(false);
  int T, n;
  for (std::cin >> T; T; --T) {
    std::stack<unsigned long long int> s;
    for (std::cin >> n; n; --n) {
      std::string t;
      std::cin >> t;
      if (t == "push") {
        unsigned long long x;
        std::cin >> x; s.push(x);
      } else if (t == "pop") {
        if (s.empty()) std::cout << "Empty\n";
        else s.pop();
      } else if (t == "query") {
        if (s.empty()) std::cout << "Anguei!\n";
        else std::cout << s.top() << '\n';
      } else {
        std::cout << s.size() << '\n';
      }
		}
	}
  return 0;
}
```

