# P5410 题解

---
### [【模板】扩展 KMP（Z 函数）](https://www.luogu.com.cn/problem/P5410)
---
### 前言
做这题时我还不会扩展 KMP，看了奆佬 [$\text{qzz33554432}$](https://www.luogu.com.cn/user/365118) 的笔记才学会。

现在我已取得了奆佬的授权，于是本篇题解将会结合这位奆佬的笔记与我自己的理解和绘图来展现给大家，如有错漏敬请指出！

希望这篇题解能对你有帮助 ヾ(◍ ╹ ∇ ╹ ◍)ﾉﾞ！

---
### 修正
2021.07.12 感谢 [$\text{jwggg}$](https://www.luogu.com.cn/user/330714) 指出求 $nxt$ 时， $k = 1$ 的原因与 $nxt[1]$ 的求法讲述有错误，已修正并补充说明！

2021.07.26 感谢 [$\text{遮云壑}$](https://www.luogu.com.cn/user/284715) 指出最后求答案的公式有错误，已修正！

2022.05.12 感谢 [$\text{zuishuai}$](https://www.luogu.com.cn/user/515001) 指出对图 3 讲解时的公式有错误，已修正！


2022.11.05 感谢 [$\text{xubozheng}$](https://www.luogu.com.cn/user/735171) 指出的观感疏漏，~~可恶的博客竟然无法正常显示表格边框，可恶~~，已将例子换为图片！

---
### 扩展 KMP
扩展 KMP（exKMP），能在 $O(|a|+|b|)$ 的时间内处理出文本串 $a$ 的所有后缀和模式串 $b$ 的最长公共前缀。

我会分两部分来讲解 exKMP，分别为 $nxt(next)$ 和 $ext(extend)$ 数组。

---
### $nxt(next)$
类似于 KMP，exKMP 也需要一个 $nxt$ 数组。我们对模式串 $b$ 构建 $nxt$ 数组，$nxt[i]$ 表示“模式串 $b$” 与 “模式串 $b$ 以 $b[i]$ 开头的后缀” 的 “最长公共前缀” 的长度。

举个例子 :

![图片 0](https://cdn.luogu.com.cn/upload/image_hosting/pd9np4oo.png)

我们先不管 $nxt$ 数组的用处，先来思考一下如何求得 $nxt$ 数组。

假设 $nxt[i](0\leqslant i<x)$ 的值都均已求出，现在我们要求 $nxt[x]$ 的值。

对于所有的 $0 < i < x$，我们找到 $i + nxt[i] - 1$ 的最大值，设 $k$ 为这个最大值对应的 $i$。定义 $p$ 为 $k + nxt[k] - 1$，$p$ 就是我们目前匹配到的最大下标。

细心的你一定会发现我们没有算入 $i=0$ 时 $i + nxt[i] - 1$ 的值，这是因为无论模式串 $b$ 是怎样的，模式串 $b$ 以 $b[0]$ 开头的后缀就是 $b$ 本身，也就是说 $nxt[0]$ 的值为 $|b|$，那如果最大值赋值成了它，我们就无法达到算法优化的效果啦。所以在下面的代码实现中，我们会将 $k$ 的初值赋值为 $1$。

根据以上定义我们可以得到，在模式串 $b$ 中，$[0,nxt[k]-1]$ 和 $[k,p]$ 两段是相等的。如下图所示，蓝方框是相等的：

![图片 1](https://cdn.luogu.com.cn/upload/image_hosting/u2mgbtds.png)

现在我们要求模式串 $b$ 中 $[x,n-1]$ 与 $[0,n-1]$ 的最长公共前缀。

前面我们知道，$b[0,nxt[k]-1]$ 和 $b[k,p]$ 是相等的，所以我们可以推出，$b[x-k,nxt[k]-1]$ 和 $b[x,p]$ 也是相等的。如下图所示，绿方框是相等的，剩余的蓝方框也是相等的：

![图片 2](https://cdn.luogu.com.cn/upload/image_hosting/r9daq72e.png)

我们定义 $l$ 为 $nxt[x - k]$，可以得到：$[0,l-1] = [x-k,x-k+l-1] = [x,x+l-1]$。所以下图的灰方框是相等的。

此时，如下图所示，如果图中的灰方框小于初始的绿方框，也就是 $l<p-x+1$，即 $x+l\leqslant p$，那么我们可以确定 $nxt[x]=l$。

![图片 3](https://cdn.luogu.com.cn/upload/image_hosting/ucdfcu9v.png)

否则，如下图所示，灰方框大于初始的绿方框。此时的 $b[0,l-1]$、$b[x-k,x-k+l-1]$、$b[x,x+l-1]$ 三个灰方框的大小是相等的，但字符不一定是相等的，就需要逐位比较了。这里有些方框覆盖在了一起，要自己分辨哟。ヽ( ･ω･ヽ）

![图片 4](https://cdn.luogu.com.cn/upload/image_hosting/5uha4tcj.png)

因为 $p$ 已是我们处理过的最大下标，那我们就直接从 $p-x+1$ 和 $p+1$ 进行逐位比较，从而求出 $nxt[x]$ 的值，此时的 $x + nxt[x] - 1$ 一定刷新了最大值，于是我们要重新赋值 $k$。在这整个过程中，$p$ 是单调递增的，所以这部分的复杂度为 $O(n)$。

那么我们现在就能写出求 $nxt$ 的代码啦：

```cpp
void qnxt(char *c)
{
	int len = strlen(c);
	int p = 0, k = 1, l; //我们会在后面先逐位比较出 nxt[1] 的值，这里先设 k 为 1
	//如果 k = 0，p 就会锁定在 |c| 不会被更改，无法达成算法优化的效果啦
	nxt[0] = len; //以 c[0] 开始的后缀就是 c 本身，最长公共前缀自然为 |c|
	while(p + 1 < len && c[p] == c[p + 1]) p++;
	nxt[1] = p; //先逐位比较出 nxt[1] 的值
	for(int i = 2; i < len; i++)
	{
		p = k + nxt[k] - 1; //定义
		l = nxt[i - k]; //定义
		if(i + l <= p) nxt[i] = l; //如果灰方框小于初始的绿方框,直接确定 nxt[i] 的值
		else
		{
			int j = max(0, p - i + 1);
			while(i + j < len && c[i + j] == c[j]) j++; //否则进行逐位比较
			nxt[i] = j;
			k = i; //此时的 x + nxt[x] - 1 一定刷新了最大值，于是我们要重新赋值 k
		}
	}
}
```

---
### $ext(extend)$
我们用 $ext[i]$ 表示“模式串 $b$” 与 “文本串 $a$ 以 $a[i]$ 开头的后缀” 的 “最长公共前缀” 的长度。

假设 $ext[i](0\leqslant i<x)$ 的值均已求出，现在我们要求 $ext[x]$ 的值。

跟上文求 $nxt$ 数组很类似，我们找到 $i + ext[i] - 1$ 的最大值 , 设 $k$ 为这个最大值对应的 $i$，$p$ 为 $k+ext[k] - 1$，$l$ 为 $nxt[x-k]$。我们绘成图，会发现与 $nxt$ 的十分相似。

![图片 5](https://cdn.luogu.com.cn/upload/image_hosting/15yya06u.png)

根据 $nxt$ 相同的推导方式，我们就能写出 $ext$ 的代码啦：

```cpp
void exkmp(char *a, char *b)
{
	int la = strlen(a), lb = strlen(b);
	int p = 0, k = 0, l;
	while(p < la && p < lb && a[p] == b[p]) p++; //先算出初值用于递推
	ext[0] = p;
	for(int i = 1; i < la; i++) //下面都是一样的逻辑啦
	{
		p = k + ext[k] - 1;
		l = nxt[i - k];
		if(i + l <= p) ext[i] = l;
		else
		{
			int j = max(0, p - i + 1);
			while(i + j < la && j < lb && a[i + j] == b[j]) j++;
			ext[i] = j;
			k = i;
		}
	}
}
```

---

### 代码
在处理完 $nxt$ 和 $ext$ 数组后，答案就显而易见啦！

我的代码里下标是从 $0$ 开始的，所以只需要输出 $\text{xor}^{|b|-1}_{i=0}(i+1)\times(nxt[i]+1)$  和 $\text{xor}^{|a|-1}_{i=0}(i+1)\times(ext[i]+1)$就好了。

下面放出完整代码：

```cpp
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N = 2e7 + 10;
ll nxt[N], ext[N];
void qnxt(char *c)
{
	int len = strlen(c);
	int p = 0, k = 1, l; //我们会在后面先逐位比较出 nxt[1] 的值，这里先设 k 为 1
	//如果 k = 0，p 就会锁定在 |c| 不会被更改，无法达成算法优化的效果啦
	nxt[0] = len; //以 c[0] 开始的后缀就是 c 本身，最长公共前缀自然为 |c|
	while(p + 1 < len && c[p] == c[p + 1]) p++;
	nxt[1] = p; //先逐位比较出 nxt[1] 的值
	for(int i = 2; i < len; i++)
	{
		p = k + nxt[k] - 1; //定义
		l = nxt[i - k]; //定义
		if(i + l <= p) nxt[i] = l; //如果灰方框小于初始的绿方框,直接确定 nxt[i] 的值
		else
		{
			int j = max(0, p - i + 1);
			while(i + j < len && c[i + j] == c[j]) j++; //否则进行逐位比较
			nxt[i] = j;
			k = i; //此时的 x + nxt[x] - 1 一定刷新了最大值，于是我们要重新赋值 k
		}
	}
}
void exkmp(char *a, char *b)
{
	int la = strlen(a), lb = strlen(b);
	int p = 0, k = 0, l;
	while(p < la && p < lb && a[p] == b[p]) p++; //先算出初值用于递推
	ext[0] = p;
	for(int i = 1; i < la; i++) //下面都是一样的逻辑啦
	{
		p = k + ext[k] - 1;
		l = nxt[i - k];
		if(i + l <= p) ext[i] = l;
		else
		{
			int j = max(0, p - i + 1);
			while(i + j < la && j < lb && a[i + j] == b[j]) j++;
			ext[i] = j;
			k = i;
		}
	}
}
int la, lb;
char a[N], b[N];
ll ans;
int main()
{
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
	cin >> a >> b;
	qnxt(b);
	exkmp(a, b);
	la = strlen(a), lb = strlen(b), ans = 0;
	for(int i = 0; i < lb; i++) //要注意下标从 0 开始
	{
		ans ^= (i + 1) * (nxt[i] + 1);
	}
	cout << ans << "\n";
	ans = 0;
	for(int i = 0; i < la; i++)
	{
		ans ^= (i + 1) * (ext[i] + 1);
	}
	cout << ans;
	return 0;
}
```

---
### 后记
感谢你的阅读，希望这篇题解能对你有帮助！

加油吧！✧\*٩( ◕ ᗜ ◕ )و✧\*