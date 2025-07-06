# P10520 题解

思路：按题意模拟即可。转换得到的平面直角坐标 $x'$ 就是 $\frac{1}{2}x$ 加上 $\frac{1}{2}y$，$y'$ 就是 $\frac{\sqrt{3}}{2}x$ 减去 $\frac{\sqrt{3}}{2}y$。最后输出保留 $6$ 位小数即可。

上代码：
```
#include <bits/stdc++.h>
using namespace std;

double x,y;
int main(){
	cin>>x>>y;
	printf("%.6lf\n",x / 2 + y / 2);
	printf("%.6lf\n",x / 2 * sqrt(3) - y / 2 * sqrt(3));
	return 0;
}
```