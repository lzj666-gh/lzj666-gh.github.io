# B3845 题解

## 思路分析
枚举 $a,b$，那么我们定 $c$ 为 $\lfloor\sqrt{a^2+b^2}\rfloor$。

接下来我们需要判断一下 $c$ 是否满足以下条件：
- $c\le n$：判断 $c$ 是否在 $n$ 的范围内。
- $c^2=a^2+b^2$：由于 $c$ 已经向下取整，所以这样判断即可确定 $\sqrt{a^2+b^2}$ 是否为整数。

判断成功后累加即可，时间复杂度 $\mathcal O(n^2)$，可以通过。
## 代码实现
```cpp
#include <iostream>
#include <cmath>

int main() {
	int n, ans = 0; std::cin >> n;
	for (int a = 1; a <= n; ++a)
		for (int b = a; b <= n; ++b) {
			int c = sqrt(a * a + b * b);
			if (c > n || c * c != a * a + b * b) continue;
			++ans;
		}
	std::cout << ans;
	return 0;
}
```
