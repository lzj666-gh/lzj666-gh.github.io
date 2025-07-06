# P9777 题解

# 题意
 
 已知 $x+x^{-1}=k$，求 $(x^{n}+x^{-n})\bmod M$。
 
# 思路

我们先考虑 $n$ 很小的情况：

当 $n$ 等于 $2$ 时，我们发现这就是一个完全平方公式，即 $x^{2}+x^{-2}=(x+x^{-1})^2-2$，所以我们可以通过 $n=1$ 推出 $n=2$ 时的结果。

当 $n$ 等于 $3$ 时，我们突然想到自己背过立方和公式，即 $x^{3}+x^{-3}=(x+x^{-1})(x^2+x^{-2}-2)$，所以我们也可以通过 $n=2$ 推出 $n=3$ 时的结果。

当 $n$ 等于 $4$ 的时候，我们发现我们不会背公式了，但是由前面的分析可知，$n=4$ 是一定可以由 $n=3$ 推出的。那我们直接对 $x^{3}+x^{-3}$ 乘上一个 $x+x^{-1}$ ，发现结果为 $x^{4}+x^{-4}+x^{2}+x^{-2}$ ，移项一下我们惊奇的发现： 
$x^{4}+x^{-4}=(x^{3}+x^{-3})×(x+x^{-1})-(x^{2}+x^{-2})$ 。

如果我们用 $F_n$ 记录结果，那我们可以得到是不是 $F_4=F_1×F_3-F2$，那我们可以大胆地猜想，是不是 $F_n=F_1×F_{n-1}-F_{n-2}$,然后我们按照上面相同的方法一验证，果然是这样。

这时候我们想到我还是个蒟蒻时曾经写过斐波那契数列这道题，但我们发现这题的 $n$ 的范围非常大，不能直接递推求解。然后我又想到了我在机房垫底时学到的矩阵快速幂优化斐波那契数列，所以我们构造出矩阵：

$\begin{bmatrix}
F_n & F_{n-1}  \\
\end{bmatrix}×\begin{bmatrix}
k & 1\\
-1 & 0\\
\end{bmatrix}$

然后套矩阵快速幂模板即可，时间复杂度 $O(\log{N})$。

# 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
long long n,k,mod;
struct Matrix {
  long long a[3][3];

  Matrix() { memset(a, 0, sizeof a); }

  Matrix operator*(const Matrix &b) const {
    Matrix res;
    for (register int i = 1; i <= 2; ++i)
      for (register int j = 1; j <= 2; ++j)
        for (register int k = 1; k <= 2; ++k)
          res.a[i][j] = (res.a[i][j] + a[i][k] * b.a[k][j]) % mod;
    return res;
  }
} ans, base;

inline void init() {
  base.a[1][1] = k;
  base.a[1][2] = 1;
  base.a[2][1] =-1;
  ans.a[1][1] = (k*k-2)%mod;
  ans.a[1][2] = k%mod;
}

inline void qpow(long long b) {
  while (b) {
    if (b & 1) ans = ans * base;
    base = base * base;
    b >>= 1;
  }
}
long long read(){
    long long a=0;int op=1;char ch=getchar();
    while(ch<'0'||'9'<ch){if(ch=='-')op=-1;ch=getchar();}
    while('0'<=ch&&ch<='9'){a=(a<<3)+(a<<1)+(48^ch);ch=getchar();}
    return a*op;
}
int main() {
  mod=read();
  k=read();
  n=read();
  if (n == 0) {
  	printf("2");
	return 0;
  } 
  if (n == 1) {
  	printf("%lld",k%mod);
  	return 0;
  }
  if (n == 2) {
  	printf("%lld",(k*k-2)%mod);
  	return 0;
  }
  init();
  qpow(n - 2);
  printf("%lld",(ans.a[1][1] +mod)% mod);
}
```
## 后记
赛时这题给我整破防了，写题解的时候也在破防。(怎么有人不考虑 $n=0$ 的情况啊）。