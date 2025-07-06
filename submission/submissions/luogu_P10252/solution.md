# P10252 题解

不懂为什么都写那么长。

若 $a > 1$，则 $ax-b$ 的值为 $x + (a-1)x-b$，如果把 $x$ 换成更大的数，增量更大，反之亦然。

于是特判 $a=1$，否则因为要做乘法，是指数爆炸，直接模拟。单次复杂度 $\log x$。

具体见代码。

```cpp

#include<bits/stdc++.h>
#define int long long
using namespace std;
int t, x, a, b;
signed main(){
	ios::sync_with_stdio(false);
	cin.tie(0);cout.tie(0);
	cin >> t;
	while (t--){
		cin >> x >> a >> b;
		if (a == 1){
			if (b == 0){//这时变换多少次都是 x
				cout << x << "\n";
				continue;
			}
			cout << x % b - b << "\n";//因为 x 每次 -b，减到负数就停了
			continue;
		}
		while (a * x - b < x && x >= 0)
			x = a * x - b; //模拟
		cout << x << "\n";
	}
}
```