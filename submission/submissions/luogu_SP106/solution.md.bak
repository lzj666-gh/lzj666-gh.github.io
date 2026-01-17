# SP106 题解

给定 $T$ 组 $(n,m)$，求 $S(n,m)$，$S$ 是第二类斯特林数。

如果你不知道第二类斯特林数是啥，可以看看[百度](https://baike.baidu.com/item/%E6%96%AF%E7%89%B9%E6%9E%97%E6%95%B0/4938529?fr=aladdin)：（经过一些修改）

> 第二类斯特林数实际上是集合的一个拆分，表示将 $n$ 个不同的元素拆分成 $m$ 个集合的方案数，记为 $S(n,m)$ 或者 $\begin{Bmatrix}n\\m\end{Bmatrix}$。

看到下面的递推式：$S(n+1,m)=S(n,m-1)+m\times S(n,m)$。

我们对其进行一些变形：

$$
\begin{aligned}
S(n+1,m)=&S(n,m-1)+m\times S(n,m)&\\
S(n,m)=&S(n-1,m-1)+m\times S(n-1,m)&\\
S(n,m)\equiv&\begin{cases}S(n-1,m-1),&m\mod 2=0\\S(n-1,m-1)+S(n-1,m),&\operatorname{otherwise}\end{cases}&\pmod{2}
\end{aligned}
$$

就可以根据上面的表达式大致画出一个转移图：

![](https://cdn.luogu.com.cn/upload/image_hosting/f8gydte6.png)

图中对于一个点 $(n,m)$，从 $(0,0)$ 经过蓝边（向右）和粉边（向右上）到达 $(n,m)$ 的路径条数即为 $S(n,m)$，注意黑边不能经过，蓝边和粉边只能单向经过。因此 $S(n,m)\mod 2$ 就等于路径条数对二取模的余数。

路径条数怎么算呢？我们根据 $0\sim m$ 之间的蓝色边条数来分类讨论，运用一些数学计算就可以得到，发现路径条数的奇偶性与 $\frac{m+1}{2}$ 有关（因为蓝边数量仅与 $m$ 相关）。最后就可以得到结论：

$$
S(n,m)\mod 2=\begin{cases}1,&\left(n=m=0\right)\lor\left(\left(\frac{m+1}{2}-1\right)\operatorname{and}\left(n-m+\frac{m+1}{2}-1\right)=\frac{m+1}{2}-1\right)\\0,&\operatorname{otherwise}\end{cases}
$$

这里我们特判一下几个特殊情况，就可以得到最终结论。

代码：

```cpp
//By: Luogu@rui_er(122461)
#include <bits/stdc++.h>
using namespace std;

#define f(a,b) (\
(a & b) == a\
)

int T, n, m; 

int main() {
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d", &n, &m);
		if(!n && !m) {
			puts("1");
			continue;
		}
		if(!n || !m || n < m) {
			puts("0");
			continue;
		}
		int a = (m + 1) / 2 - 1;
		printf("%d\n", f(a, n-m+a));
	}
	return 0;
}
```