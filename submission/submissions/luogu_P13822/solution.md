# P13822 题解

### 题目分析
结论：**当序列长度大于 1 时，两个折线序列能够互相转换的必要条件是它们的首元素奇偶性相同**。

- 对于长度为 $1$ 的序列，总是可以通过修改使其与任意序列相同，因此答案一定是 Yes。

- 对于长度大于 $1$ 的序列，由于每次操作必须保持折线性质（相邻差为 $1$）。基于折线序列的定义，我们可以推导出序列中元素的奇偶性是严格交替的。首元素的奇偶性决定了整个序列的奇偶性模式。因此，只有当 $a$ 和 $b$ 的首元素奇偶性相同时，才有可能通过合法操作使两序列相同。

### 代码
```cpp
#include <bits/stdc++.h>
using namespace std;
int t;
int main() {
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int a1;
        scanf("%d", &a1);
        for (int i = 1; i < n; i++) {
            int tmp;
            scanf("%d", &tmp);
        }
        int b1;
        scanf("%d", &b1);
        for (int i = 1; i < n; i++) {
            int tmp;
            scanf("%d", &tmp);
        }
        if (n == 1) {
            printf("Yes\n");
            continue;
        }
        int f1 = (a1 + 1) % 2;
        int f2 = (b1 + 1) % 2;
        if ((f1 == f2)) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }
    return 0;
}
```