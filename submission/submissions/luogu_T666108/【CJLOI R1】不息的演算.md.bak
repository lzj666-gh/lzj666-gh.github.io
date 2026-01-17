# 【CJLOI R1】不息的演算

## 题目描述

你想要知道今天基础赛的 T3 怎么做，但是你不会，所以你试图向博识尊提问。但是祂不会给予答案，只会用问题回答问题，所以你需要回答祂提出的问题。

博识尊给了你一个 $n\times m$（即 $n$ 行 $m$ 列）的矩阵 $a$。紧接着，博识尊抛出了 $k$ 个问题。

具体的，每个问题有参数 $l_1,r_1,l_2,r_2$，你需要回答 $\displaystyle\prod_{i=l_1}^{r1}\prod_{j=l_2}^{r_2}a_{i,j}\pmod p$，其中 $p$ 是给定的一个正整数。

你觉得这太难了，于是你就以你自己的方式向博识尊提出了抗议。所以博识尊给了你两个限制参数 $x,y$，并保证对于所有的询问，$x<r_1-l_1+1\le 2x;y< r_2-l_2+1\le2y$。

为了 100pts 的 T3，你现在需要求解这个问题。

**由于输入输出量过大，所以我们将使用特殊的输入输出方式。**

## 输入格式

第一行，六个整数，表示 $n,m,k,x,y,p$，含义如题目中所示。

接下来 $n$ 行，每行 $m$ 个整数，表示 $a_{i,j}$。

第 $n+2$ 行，一个随机数种子 $state$ 作为以下代码中变量 $state$ 的初始值（$state < 2^{32}$）。

$$
\begin{aligned}
&\text{函数 } \mathit{next\_random}(): \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \ll 13) \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \gg 17) \\
&\quad \mathit{state} \leftarrow \mathit{state} \oplus (\mathit{state} \ll 5) \\
&\quad While \space \mathit{state}\ge2^{32}:\\
&\quad\quad \mathit{state} \leftarrow \mathit{state} \space - \space 2^{32}\\
&\quad \text{返回 } \mathit{state} \\
&\text{函数 } \mathit{random}(l,r):\\
&\quad \text{返回 } \mathit{next\_random() \bmod (r-l+1) + l}\\
\\
&\mathit{min\_len\_x} \leftarrow x+1 \\
&\mathit{max\_len\_x} \leftarrow \min(2x, n) \\
&\mathit{min\_len\_y} \leftarrow y+1 \\
&\mathit{max\_len\_y} \leftarrow \min(2y, m) \\
\\
&\mathit{len1} \leftarrow random(\mathit{min\_len_\_x},\mathit{max\_len\_x}) \\
&\mathit{len2} \leftarrow random(\mathit{min\_len_\_y},\mathit{max\_len\_y}) \\
&\mathit{x1} \leftarrow random(0,n-len1)\\
&\mathit{y1} \leftarrow random(0,m-len2)\\
&\mathit{x2} \leftarrow x1+len1-1\\
&\mathit{y2} \leftarrow y1+len2-1\\
\end{aligned}
$$

接下来，你需要调用 $k$ 次生成器，每次生成器会给出查询区间 $l_1,r_1,l_2,r_2$，对于每一次的查询请输出答案对 $p$ 取模后的结果。

如果你无法理解输入格式，我们会在文末为你提供一份 c++ 语言的输入输出示例。

## 输出格式

定义最终答案为 $result$，第 $i$ 次查询的答案为 $ans_i$，则 $result=\bigoplus_{i=1}^{k}ans_i$。其中 $\oplus$ 符号表示异或操作，在 C++ 中，你可以使用运算符 `^` 表示。

你只需要输出 $result$ 即可。

## 提示

### 样例解释

样例解码以后的询问如下所示：

```text
1 4 1 3
1 3 1 3
0 2 0 3
0 2 1 4
0 3 1 4
```

它们对应的答案分别为：

```text
3
6
6
1
8
```

### 数据约束

|  测试点编号  |$n$       |$m$       |$k$|特殊性质|每个测试点分数|
|:--:|:--------:|:--------:|:--------:|:-:|:-:|
|$1$|$\le 500$|$\le 500$|$\le 500$|无特殊性质|$10$|
|$2$|$\le 10^3$|$=2$|$\le 10^7$|^|$10$|
|$3$|^|$\le 10^3$|$\le 182375$|^|$10$|
|$4$|^|^|^|$p=10^9+7$|$5$|
|$5$|$\le 500$|$\le 500$|$\le 10^7$|^|$5$|
|$6$|^|^|^|$p=999911658$|$5$|
|$7$|^|^|^|$p=246248468$|$5$|
|$8$|$\le 10^3$|$\le 10^3$|^|$x=1$|$10$|
|$9$|^|^|^|$x\le 10$|$10$|
|$10 \sim 12$|^|^|$\le 10^6$|无特殊性质|$5$|
|$13 \sim 15$|^|^|$\le 10^7$|^|$5$|


以下是输入并生成查询的 C++ 代码，仅供参考理解输入输出格式。

```cpp
#include<bits/stdc++.h>
using namespace std;
int n, m, k, x, y, p, res, ans, a[1005][1005];
unsigned state;
inline unsigned next_random() {
	state = state ^ (state << 13);
	state = state ^ (state >> 17);
	state = state ^ (state << 5);
	return state;
}
inline int random(int l, int r) {
	return next_random() % (r - l + 1) + l;
}
signed main() {
	ios::sync_with_stdio(0);
	cin >> n >> m >> k >> x >> y >> p;
	for (int i = 0; i != n; ++i)
		for (int j = 0; j != m; ++j)
			cin >> a[i][j];
	cin >> state;
	int min_x = x + 1, max_x = min(x * 2, n), min_y = y + 1, max_y = min(y * 2, m);
	while (k--) {
		int len_x = random(min_x, max_x), len_y = random(min_y, max_y);
		int xmin = random(0, n - len_x), ymin = random(0, m - len_y);
		int xmax = xmin + len_x - 1, ymax = ymin + len_y - 1;
		//querying the result in rect x:[xmin,xmax],y:[ymin,ymax] of a[x][y], solve it and save the answer in value "ans".
		res ^= ans;
	}
	cout << res << endl;
}
```

你终于解明了答案，可博识尊给你的回答却只有寥寥十个字：服务器繁忙，请稍后再试。

## 时空限制

时间限制: 5000 ms
内存限制: 512 MB
