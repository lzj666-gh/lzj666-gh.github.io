# P5711 题解

- 公历年份是 $4$ 的倍数，且不是 $100$ 的倍数。
- 如果这是 $100$ 的倍数，必须是 $400$ 的倍数才是闰年。
- 其他情况就是平年。

（代码是按照分析原模原样的写的）

```cpp
#include<bits/stdc++.h>
using namespace std;
int n;
int main() {
	cin >> n;
	if ( (n % 4 == 0 && n % 100 != 0) || n % 400 == 0) cout << 1;// || 表示或者，&& 表示且。
	else cout << 0;
}
```