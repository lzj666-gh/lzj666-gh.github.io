# P4054 题解

本~~蒟蒻~~第四篇题解，上次提交写得太少了，这次望管理给过！

~~貌似是个树状数组模板题~~

## 写在前面
$Q$：树状数组是什么？

$A$：~~是一种数据结构。~~

定义原一维数组为 $A$ ，则树状数组 $C$ 的值为：
$$C_1=A_1$$
$$C_2=A_1+A_2$$
$$C_3=A_3$$
$$C_4=A_1+A_2+A_3+A_4$$
$$C_5=A_5$$
$$C_6=A_5+A_6$$
$$C_7=A_7$$
$$C_8=A_1+A_2+A_3+A_4+A_5+A_6+A_7+A_8$$
以此类推。

介绍一下著名的 $lowbit$ 函数吧。

### lowbit
$Q$：$lowbit$ 求的是什么？

$A$：整数转为二进制后，最后一位 $1$ 及之后的所有 $0$ 所构成的数值。

$lowbit$ 看似麻烦，一看代码，发现也只有一行就解决了：
```cpp
int lowbit(int x) {
	return x & -x;
}
```
这里涉及到了二进制补码的知识。

回到本题，你会豁然开朗！

## 思路
- 数据结构：树状数组
- 变化：多记一维 $color$
- 就没有其他改动了

## CODE
```cpp
#include <stdio.h>
int n, m;
int a[301][301];
int c[301][301][101];
inline void add(int x, int y, int k, int color) {
	for (int i = x; i <= n; i += i & -i)
		for (int j = y; j <= m; j += j & -j)
			c[i][j][color] += k;
}
inline int query(int x, int y, int color) {
	int ret = 0;
	for (int i = x; i; i -= i & -i)
		for (int j = y; j; j -= j & -j)
			ret += c[i][j][color];
	return ret;
}
int main(void) {
	scanf("%d %d", &n, &m);
	int Q, x1, y1, x2, y2, color;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf("%d", &color);
			a[i][j] = color;
			add(i, j, 1, color);
		} 
	for (scanf("%d", &Q); Q--; ) {
		int op;
		scanf("%d", &op);
		if (op == 1) {
			scanf("%d %d %d", &x1, &y1, &color);
			add(x1, y1, -1, a[x1][y1]);
			a[x1][y1] = color;
			add(x1, y1, 1, color);
		}
		else {
			scanf("%d %d %d %d %d", &x1, &x2, &y1, &y2, &color);
			printf("%d\n", query(x2, y2, color) - query(x1 - 1, y2, color) - query(x2, y1 - 1, color) + query(x1 - 1, y1 - 1, color));
		}
	}
	return 0;
}
```

## 推荐树状数组题单
### 官方精选
- [【数据结构2-2】线段树与树状数组](https://www.luogu.com.cn/training/206)

### 用户分享
- [树状数组模板题](https://www.luogu.com.cn/training/3079)

- [CMの树状数组](https://www.luogu.com.cn/training/1143)

## The end. Thanks.

~~（走过路过一定要赞过啊~~