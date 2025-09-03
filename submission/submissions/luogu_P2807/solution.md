# P2807 题解

**upd:2019.4.27（因为洛谷多行LaTeX会挂，所以很多公式是图片）**

好像还是会挂，所以到博客里看好了：<https://heartlessly.github.io/problems/luogu-p2807/>

## Description

$n$ 等分大三角形的每条边，将对应的等分点连接起来（连接线分别平行于三条边），求有多少个三角形。


## Source

**[[Luogu]P2807](https://www.luogu.org/problemnew/show/P2807)**

## Solution

看似很简单的数学题，实际上让人摸不着头发（？？？

不妨设$\triangle  ABC$ 的边长为 $n$，这样 $n$ 等分每一条边后，每个小三角形的边长为 $1$ 。

先考虑头朝上的三角形（$\triangle$）：

边长为 $1$ 的三角形有多少个呢？

![Eu7ej1.png](https://s2.ax1x.com/2019/04/27/Eu7ej1.png)

（如图）显然第一层有 $1$ 个，第二层有 $2$ 个，一直到第 $n$ 层有 $n$ 个，共
$$
1 + 2 + \cdots + n = \frac{n\left( n + 1\right)}{2}
$$
那边长为 $2$ 的三角形呢？

![Eu7ZcR.png](https://s2.ax1x.com/2019/04/27/Eu7ZcR.png)

（如图）我们可以数它左下角那个边长为 $1$ 的三角形，因为有大小限制，最右侧一列就不能数了，所以问题变为求边长为 $n - 1$ 的三角形中有几个边长为 $1$ 的三角形，与上面的求法一样，共
$$
1 + 2 + \cdots + n - 1 = \frac{n \left( n - 1\right)}{2}
$$
同理，边长为 $i\ \left(1 \leq i \leq n\right)$ 的三角形共
$$
1 + 2 + \cdots + n - i + 1 = \frac{\left(n - i + 1 \right)\left( n - i + 2 \right)}{2}
$$
由此可以得出结论，边长 $1 \sim n$ 头朝上的三角形共
$$
\frac{\sum\limits_{i = 1}^n\left(n - i + 1 \right)\left( n - i + 2 \right)}{2} = 
\frac{\sum\limits_{i = 1}^n i\left( i + 1\right)}{2} = \frac{n \left( n + 1\right)\left(n + 2 \right)}{6}
$$
至于第 $2$ 步到第 $3$ 步怎么得出来的，这里给出详细解释。

**定理：** 
$$
\sum\limits_{i = 1}^n i^2 = 1^2+2^2+ \cdots + n^2 = \frac{n\left( n + 1 \right) \left( 2n + 1\right)}{6}
$$
**证明：**

首先需要知道
$$
\left( n + 1 \right)^3 = n^3 + 3n^2 + 3n + 1
$$
那么
$$
\left( n + 1 \right)^3 - n^3 = 3n^2 + 3n + 1
$$
因此我们可以列出 $n$ 个式子

![EuLVIK.png](https://s2.ax1x.com/2019/04/27/EuLVIK.png)

把这 $n$ 个式子相加，得到

$$
\left( n + 1\right)^3 - 1^3 = 3\sum\limits_{i=1}^n i^2 + 3\sum\limits_{i=1}^n i + n
$$

化简

$$
n^3 + 3n^2 + 2n = 3\sum\limits_{i = 1}^ni^2 + \frac{3n\left(n + 1\right)}{2}
$$

$$
2n^3 + 6n^2 + 4n = 6\sum\limits_{i = 1}^ni^2 + 3n^2 + 3n
$$

$$
\sum\limits_{i = 1}^ni^2 = \frac{2n^3 + 3n^2 + n}{6}
$$

因式分解，得
$$
\sum\limits_{i = 1}^ni^2 = \frac{2n^3 + 3n^2 + n}{6} = \frac{n\left(2n^2 + 3n + 1 \right)}{6} = \frac{n\left( n + 1 \right) \left( 2n + 1\right)}{6}
$$
证毕。

于是乎，我们就可以推出

![EuLcJU.png](https://s2.ax1x.com/2019/04/27/EuLcJU.png)

再考虑头朝下的三角形（$\bigtriangledown $）：

![Eu7nnx.png](https://s2.ax1x.com/2019/04/27/Eu7nnx.png)

（如图）边长为 $1$ 的三角形第 $1$ 行没有，第二行有 $1$ 个，第三行有 $2$ 个，一直到第 $n$ 行有 $n - 1$ 个，所以共
$$
1 + 2 + \cdots + n - 1 = \frac{n \left( n - 1\right)}{2}
$$

接下来数边长为 $2$ 的三角形。

![Eu7V39.png](https://s2.ax1x.com/2019/04/27/Eu7V39.png)

（如图）我们考虑数它下方的三角形。前三行没有，第 $4$ 行有 $1$ 个，第 $5$ 行有 $2$ 个，一直到第 $n$ 行有 $n - 3$ 个，共
$$
1 + 2 + \cdots + n - 3 = \frac{\left( n - 2 \right)\left( n - 3 \right)}{2}
$$
同理，边长为 $3$ 的三角形共
$$
1 + 2 + \cdots + n - 5 = \frac{\left( n - 4 \right)\left( n - 5 \right)}{2}
$$
边长为 $i\ \left( 2 \leq 2i \leq n \right)$ 的三角形共
$$
1 + 2 + \cdots + n - 2 i + 1 = \frac{\left( n - 2i + 1 \right)\left( n - 2i + 2 \right)}{2}
$$

头朝下的三角形共（第一行式子表示 $n$ 是奇数，第二行式子表示 $n$ 是偶数）

![EuXFN6.png](https://s2.ax1x.com/2019/04/27/EuXFN6.png)

推导一下。

先考虑 $n$ 是奇数的情况。

![EuXnud.png](https://s2.ax1x.com/2019/04/27/EuXnud.png)

$n$ 为偶数也是同样的道理。

![EuXuDA.png](https://s2.ax1x.com/2019/04/27/EuXuDA.png)
把头朝上和头朝下的三角形加起来，得到

![EuXG8S.png](https://s2.ax1x.com/2019/04/27/EuXG8S.png)

这就是最后的答案，每次都可以 $O(1)$ 求了，总时间复杂度为 $O(T)$ 。

## Code

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

template <class T>
inline void read(T &x) {
    x = 0;
    char c = getchar();
    bool f = 0;
    for (; !isdigit(c); c = getchar()) f ^= c == '-';
    for (; isdigit(c); c = getchar()) x = x * 10 + (c ^ 48);
    x = f ? -x : x;
}

template <class T>
inline void write(T x) {
    if (x < 0) {
        putchar('-');
        x = -x;
    }
    T y = 1, len = 1;
    for (; y <= x / 10; y *= 10) ++len;
    for (; len; --len, x %= y, y /= 10) putchar(x / y + 48);
}

int t, n;

int main() {
    for (read(t); t; --t) {
        read(n);
        if (n & 1) write((n + 1) * (2 * n * n + 3 * n - 1) / 8);//奇数 
        else write(n * (n + 2) * (2 * n + 1) / 8);//偶数 
        putchar('\n');
    }
    return 0;
}
```