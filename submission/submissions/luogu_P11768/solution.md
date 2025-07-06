# P11768 题解

## 思路
首先当一次移动距离等于 $0$ 就直接输出 $a+b$。  
因为天依如果不用自行车的话一个时间单位只能向上下左右走一个，所以如果不用的话，就是走 $a+b$ 个时间单位。  
然后考虑使用自行车，一次走 $l$ 个格子，一定是向下使用 $x$ 次，向右使用 $y$ 次，最后一格一格走到 $(a ,b)$，注意考虑她冲刺到了后面在倒退回来的情况，以及卡了我半小时的，**注意其优化步数多的要优先考虑**。
## 代码
```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
inline int read() {
	int x = 0 ,f = 1;
	char ch = getchar();
	while('0' > ch || ch > '9'){
		if(ch == '-') f = -1;
		ch = getchar();
	}
	while('0' <= ch && ch <= '9') {
		x = (x << 1) + (x << 3) + (ch & 15);
		ch = getchar();
	}
	return x * f;
}
int T ,a ,b ,k ,l ,x ,y ,ans1 ,ans2;
signed main() {
	T = read();
	while(T --) {
		a = read(); b = read(); k = read(); l = read();
		if(l == 0) {
			cout << a + b << '\n';
			continue;
		}
		x = b / l ,y = a / l;
		if(k >= x)k -= x ,ans1 = b - x * l;
		else ans1 = b - k * l ,k = 0ll;
		if(k >= y)k -= y ,ans2 = a - y * l;
		else ans2 = a - k * l ,k = 0ll;
		if(k > 0ll) {
			if(ans1 > (l / 2) && ans2 > (l / 2) && ans2 > ans1) {
				ans2 = l - ans2;
				-- k;
			}
			if(k > 0 && ans1 > (l / 2)) {
				ans1 = l - ans1;
				-- k;
			}
			if(k > 0 && ans2 > (l / 2)) {
				ans2 = l - ans2;
				-- k;
			}
		}
		cout << ans1 + ans2 << '\n';
	}
	return 0;
}
```
###### 完结撒花(记得点赞)