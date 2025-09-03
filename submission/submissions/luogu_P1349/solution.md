# P1349 题解

#### 解题思路

既然广义斐波那契，而且数据范围这么大，那么我们使用矩阵快速幂来进行求解。大家都知道斐波那契的初始矩阵如下

$$\begin{bmatrix}1&1\\1&0\end{bmatrix}$$

那么这道题我们怎么推矩阵呢？先确定目标矩阵如下

$$\begin{bmatrix} F_n & F_{n-1}\end{bmatrix}$$

然后推导过程如下：

$$F_n = p\times F_{n-1} + q\times F_{n-2}$$
$$\downarrow$$
$$\begin{bmatrix}F_{n-1}&F_{n-2}\end{bmatrix}\times\begin{bmatrix}p&1\\q&0\end{bmatrix}$$
$$\downarrow$$
$$\begin{bmatrix}(p\times F_{n-1}+q\times F_{n-2})&(F_{n-1}\times 1+F_{n-2}\times0)\end{bmatrix}$$
$$\downarrow$$
$$\begin{bmatrix} F_n & F_{n-1}\end{bmatrix}$$

#### 吐槽一下

你谷的公式渲染不咋地，我写的老长老长的公式自己默认换行，无法显示QAQ

建议你谷更新一下QWQ

#### 附上代码

```cpp
#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

typedef long long LL;
LL n, Mod, p, q, a1, a2, ans;
struct mat{
	LL m[4][4];
}Ans, base;
inline void init() {
	Ans.m[1][1] = a2, Ans.m[1][2] = a1;
	base.m[1][1] = p, base.m[2][1] = q, base.m[1][2] = 1;
}
inline mat mul(mat a, mat b) {
	mat res;
	memset(res.m, 0, sizeof(res.m));
	for(int i=1; i<=2; i++) {
		for(int j=1; j<=2; j++) {
			for(int k=1; k<=2; k++) {
				res.m[i][j] += (a.m[i][k] % Mod) * (b.m[k][j] % Mod);
				res.m[i][j] %= Mod;
			}
		}
	}
	return res;
}
inline void Qmat_pow(int p) {
	while (p) {
		if(p & 1) Ans = mul(Ans, base);
		base = mul(base, base);
		p >>= 1;
	}
}

int main() {
	scanf("%lld%lld%lld%lld%lld%lld", &p, &q, &a1, &a2, &n, &Mod);
	if(n == 1) {
		cout<<a1;
		return 0;
	}
	if(n == 2) {
		cout<<a2;
		return 0;
	}
	init();
	Qmat_pow(n-2);
	ans = Ans.m[1][1];
	ans %= Mod;
	printf("%lld", ans);
}
```