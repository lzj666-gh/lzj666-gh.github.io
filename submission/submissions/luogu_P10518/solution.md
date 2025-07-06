# P10518 题解

### [题目传送门](https://www.luogu.com.cn/problem/P10518)

### 解题思路

签到题，简单来说就是求 $a + b + 2 \times c + 3 \times d$，依题意模拟即可。

### code

```cpp
# include <bits/stdc++.h>
using namespace std;
int main() {
	int a, b, c, d;
	cin >> a >> b >> c >> d;
	cout << a + b + 2 * c + 3 * d;
	return 0;
}
```