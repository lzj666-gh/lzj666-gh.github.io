# P5681 题解

## 思路

前置知识：正方形、长方形的面积公式

$Alice$的正方形的面积公式：

$$S = a^2$$

$Bob$的长方形的面积公式：

$$S = b \times c$$

现在给你$a, b, c$的值，那么代入计算即可

注意数据范围：$1\le a,b,c \le 10^9$

$int$最大只可以存$2^{31} - 1$，差不多是$2 \times 10^9$，算面积时会爆$int$，但是$long long$可以存下$2^{63} - 1$的数据，差不多是$10^{19}$，而算出来的面积最大也就是$10^9 \times 10^9 = 10^{18}$了

所以使用$longlong$就可以存下面积的值了

但是算的过程中会爆$int$，所以要乘上$1ll$，相当于强制转换成$longlong$

```cpp
#include <bits/stdc++.h>

#define ll long long

using namespace std;

int a, b, c;//题目给出的a,b,c
ll S1, S2;//Alice的面积和Bob的面积

int main() {
	scanf("%d%d%d", &a, &b, &c);//输入
	
	S1 = 1ll * a * a;	
    S2 = 1ll * b * c;//算出两者的面积，注意强制转换
	if (S1 > S2) cout << "Alice" << endl;//比较，并输出
			else cout << "Bob" << endl;
	
	return 0;//结束
}
```

> 日拱一卒，功不唐捐
