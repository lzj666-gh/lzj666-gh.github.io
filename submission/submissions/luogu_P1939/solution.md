# P1939 题解

#### 解题思路

这道题目的关键之处在于构造初始矩阵，题目都告诉我们了要用矩阵加速。所以矩阵快速幂是核心所在。

#### 如何构造

我们首先要确定目标矩阵。下面这个矩阵就是我想要的矩阵.
$$\begin{bmatrix}F[i]\\F[i-1]\\F[i-2]\end{bmatrix}$$

那么这个矩阵要怎样算出来。根据题目给出的递推式可以得到下面三个式子
$$f[i] = f[i-1] \times 1 + f[i-2] \times 0 + f[i-3] \times 1$$
$$f[i-1] = f[i-1] \times 1 + f[i-2] \times 0 + f[i-3] \times 0$$
$$f[i-2] = f[i-1] \times 0 + f[i-2] \times 1 + f[i-3] \times 0$$

通过每一项的系数可以得出初始矩阵为
$$\begin{bmatrix}1&0&1\\1&0&0\\0&1&0\end{bmatrix}$$

然后我们就可以通过矩阵快速幂进行求解。

值得注意的是，这个矩阵的$N$次方算出来的第一个元素是$F[N+1]$,这样的话我们可以直接在输出的时候输出第二行第一个元素。

#### 附上代码

```cpp
#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long LL;
const int Mod = 1e9+7;
int T, n;
struct mat{
	LL m[5][5];
}Ans, base;
inline void init() {
	memset(Ans.m, 0, sizeof(Ans.m));
	for(int i=1; i<=3; i++) Ans.m[i][i] = 1;
	memset(base.m, 0, sizeof(base.m));
	base.m[1][1] = base.m[1][3] = base.m[2][1] = base.m[3][2] = 1;
}
inline mat mul(mat a, mat b) {
	mat res;
	memset(res.m, 0, sizeof(res.m));
	for(int i=1; i<=3; i++) {
		for(int j=1; j<=3; j++) {
			for(int k=1; k<=3; k++) {
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
	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		if(n <= 3) {
			printf("1\n");
			continue;
		}
		init();
		Qmat_pow(n);
		printf("%lld\n", Ans.m[2][1]);
	}
}
/*
f[i-1]       f[i]
f[i-2] ----> f[i-1]
f[i-3]       f[i-2]
f[i] = f[i-1] * 1 + f[i-2] * 0 + f[i-3] * 1
f[i-1] = f[i-1] * 1 + f[i-2] * 0 + f[i-3] * 0
f[i-2] = f[i-1] * 0 + f[i-2] * 1 + f[i-3] * 0
so
1 0 1
1 0 0
0 1 0
*/
```