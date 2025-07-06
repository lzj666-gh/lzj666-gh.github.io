# P2872 题解

每题感悟：

我一定要写这篇题解， 真的太令人智熄了！我交了7遍都不过原因竟是double的问题。一定要写篇题解来帮助和我一样可怜的孩子！

正文：
[题目](https://www.luogu.org/problem/P2872)

首先一起分析一下题目意思， 根据最后一句话使所有农场联通， 求最小和的值， 那么我们会很容易的联想到最小生成树， 是的， 正解之一就是最小生成树（然而我也只会这一个）。

但是现在有几个问题

1.我们只知道点的坐标并不知道各个点之间的距离

解决办法：循环嵌套枚举求出各个点与其后点的距离。 为什么是其后点， 就是比他编号大的点， 因为是双向边，例如从i到j会存一遍那么j从i也会再存一边， 无形之间， 就会变得更复杂

那么怎样写？

```cpp
for(int i = 1; i <= n; i++) {
		for(int j = i + 1; j <= n; j++) {
			double z = juli(i, j);
			add(i, j, z);
		}
	}
```
这样就会保证只加一次边啦！是不是恍然大悟！

2.怎样处理已知边

解决办法：在枚举完所有的边的距离之后， 在读入已知边， 这时两点之间的距离直接存为零即可， 表示从i到j的花费为零。

```cpp
for(int i = 1; i <= m; i++) {
		int x = read(), y = read();
		add(x, y, 0.0);
}
```
这里需要注意一下， 关于add函数中， **最后一个参数必须是double类型的！**

3.关于距离公式：（你们的楼主太差劲了， 专门去查的这个咋写 ， 笑）

$\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} $

但是必须要控制精度

否则#2 #8 #9 #10会挂掉！

别问我怎么知道的我就是知道

![](https://cdn.luogu.com.cn/upload/image_hosting/h8cjsnbo.png?x-oss-process=image/resize,m_lfit,h_170,w_225)

所以你要改成这个亚子：
```cpp
double juli(int x, int y) {
	return (double)(sqrt((double)(E[x].x - E[y].x) * (E[x].x - E[y].x) + (double)(E[x].y - E[y].y) * (E[x].y - E[y].y)));
}
```
所以， 相应的

![](https://cdn.luogu.com.cn/upload/image_hosting/lrd2mjfd.png?x-oss-process=image/resize,m_lfit,h_170,w_225)

好啦， 以上是便是楼主做这道题觉得可以给大家分享借鉴的地方啦！

The Last:
```cpp
#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 5000100;
int n, m, cnt, fa[N], sum;
double ans;
struct Node {
	int x, y;
}E[N];
struct node {
	int from, to;
	double w;
}e[N];
int read() {
	int s = 0, w = 1;
	char ch = getchar();
	while(!isdigit(ch)) {if(ch == '-') w = -1;ch = getchar();}
	while(isdigit(ch)) {s = s * 10 + ch - '0';ch = getchar();}
	return s * w;
}
void add(int x, int y, double z) {
	e[++cnt].from =x;
	e[cnt].to = y;
	e[cnt].w = z;
}
double jl(int x, int y) {
	return (double)(sqrt((double)(E[x].x - E[y].x) * (E[x].x - E[y].x) + (double)(E[x].y - E[y].y) * (E[x].y - E[y].y)));
}
bool cmp(node x, node y) {
	if(x.w == y.w) return x.from < y.from;
	return x.w < y.w;
}
int find(int x) {
	return x == fa[x] ? x : fa[x] = find(fa[x]);
}
int main() {
	n = read(), m = read();
	for(int i = 1; i <= n; i++) 
		E[i].x = read(), E[i].y = read();
	for(int i = 1; i <= n; i++) fa[i] = i;
	for(int i = 1; i <= n; i++) {
		for(int j = i + 1; j <= n; j++) {
			double z = jl(i, j);
			add(i, j, z);
		}
	}
	for(int i = 1; i <= m; i++) {
		int x = read(), y = read();
		add(x, y, 0.0);
	}
	sort(e + 1, e + 1 + cnt, cmp);
	for(int i = 1; i <= cnt; i++) {
		int fx = find(e[i].from), fy = find(e[i].to);
		if(fx != fy) {
			fa[fx] = fy;
			sum++;
			ans += e[i].w;
		}
		if(sum == n - 1) break;
	}
	printf("%.2lf\n", ans);
	return 0;
}
```
ps：你们的楼主太chao了，把图床里的图片删了， 导致题解的图片没了， 卑微...只能重新弄重新提交...（委屈

谢谢收看， 祝身体健康！




