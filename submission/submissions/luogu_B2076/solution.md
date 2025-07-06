# B2076 题解

## 思路

水一篇打表题解。

首先第十次弹跳的高度很简单，是 $h\div1024$。

接下来看共经过的米数：

首先球从 $h$ 米下落，之后弹起来 $\frac h2$ 米，再下落 $\frac h2$ 米，这样子第九次弹起来在 $\frac h{2^9}$ 米，再落下 $\frac h{2^9}$ 米。

可以列出总弹跳高度的式子：

$$
h\times(1+2\times\frac{1}{2}+2\times\frac{1}{2^2}+...+2\times\frac1{2^9})
$$

$$
=h\times(1+1+\frac{1}{2}+\frac{1}{2^2}+...+\frac1{2^8})
$$
右边那串东西可以按按计算器，也可以套等比数列求和公式（$q$ 为公比）：

$$
S=1+\frac{a_1-a_n\times q}{1-q}=1+\frac{1-\frac1{256}\times\frac12}{\frac12}=\frac{767}{256}
$$

所以经过的米数为 $h\times\frac{767}{256}$ 米。

## 代码
```cpp
#include<bits/stdc++.h>
using namespace std;
double h;
int main(){
	scanf("%lf",&h);//输入h
	printf("%lf %lf",h*767.0/256.0,h/1024.0);//代式子 输出所经过米数和第十次弹跳高度 
	return 0;
}
```