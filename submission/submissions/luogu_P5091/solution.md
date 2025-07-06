# P5091 题解

### 费马小定理：

当 $a,p\in \mathbb{Z}$ 且 $p$ 为质数，且 $a\not\equiv 0\pmod{p}$ 时有：  
$a^{p-1}\equiv 1\pmod{p}$。

所以 $a^b\equiv a^{b\bmod (p-1)}\pmod p$。

### 欧拉定理：

当 $a,m\in \mathbb{Z}$，且 $\gcd(a,m)=1$ 时有：  
$a^{\varphi(m)}\equiv 1\pmod{m}$。

这里 $\varphi(x)$ 是数论中的欧拉函数。

所以 $a^b\equiv a^{b\bmod \varphi(m)}\pmod m$。

### 扩展欧拉定理：

当 $a,m\in \mathbb{Z}$ 时有：  
$a^b\equiv\left\{\begin{matrix}a^b&,b<\varphi(m)\\a^{b\bmod\varphi(m)+\varphi(m)}&,b\ge\varphi(m)\end{matrix}\right.\pmod m$。

证明略。

### 题解：

套公式即可。

```cpp
#include <cstdio>

int a, m, phi = 1;
int bm, flag;

int qPow(int b, int e) {
	int a = 1;
	for (; e; e >>= 1, b = (long long)b * b % m)
		if(e & 1) a = (long long)a * b % m;
	return a;
}

int main() {
	scanf("%d%d", &a, &m);
	a %= m;
	int mm = m;
	for (int i = 2; i * i <= mm; ++i) {
		if (mm % i) continue;
		phi *= i - 1;
		mm /= i;
		while (mm % i == 0)
			phi *= i,
			mm /= i;
	} if (mm > 1) phi *= mm - 1;
	char ch;
	while ((ch = getchar()) < '0' || ch > '9') ;
	while (bm = bm * 10ll + (ch ^ '0'), (ch = getchar()) >= '0' && ch <= '9')
		if (bm >= phi) flag = 1, bm %= phi;
	if (bm >= phi) flag = 1, bm %= phi;
	if (flag) bm += phi;
	printf("%d", qPow(a, bm));
	return 0;
}
```