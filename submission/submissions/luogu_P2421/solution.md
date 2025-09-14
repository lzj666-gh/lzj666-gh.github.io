# P2421 题解

[$$\Large\texttt{My Blog}$$](https://hydingsy.github.io/articles/problem-NOI-2002-Savage/)

---

## Description

> 题目链接：[Luogu 2421](https://www.luogu.org/problemnew/show/P2421)

克里特岛以野人群居而著称。岛上有排列成环行的 $M$ 个山洞。这些山洞顺时针编号为 $1,2,\dots,M$。岛上住着 $n$ 个野人，一开始依次住在山洞 $C_1,C_2,\dots,C_n$ 中。以后每年，第 $i$ 个野人会沿顺时针向前走 $P_i$ 个洞住下来。每个野人i有一个寿命值 $L_i$，即生存的年数。

奇怪的是，虽然野人有很多，但没有任何两个野人在有生之年处在同一个山洞中，使得小岛一直保持和平与宁静，这让科学家们很是惊奇。他们想知道，至少有多少个山洞，才能维持岛上的和平呢？数据保证有解，$M$ 的值不大于 $10^6$。

数据范围：$1\le n\le 15$，$1\le C_i,P_i\le 100$，$0\le L_i\le 10^6$

------

## Solution

我们形象化地描述题意： 

求最小的 $M$ 使得对于任意的 $i,j$ 使得如下同余方程无解：
$$C_i+xP_i\equiv C_j+xP_j\pmod M\quad (x>\min(L_i,L_j))$$
我们发现题目中保证 $M\le 10^6$，那么我们可以考虑枚举 $M$ 并对这 $n^2$ 个同余方程利用 $\text{exgcd}$ 来求解并判断。

**时间复杂度**：$O(Mn^2\log C_i)$

------

## Code

```cpp
#include <cstdio>
#include <algorithm>

const int N=20;
int n,s[N],p[N],l[N];

int exgcd(int a,int b,int &x,int &y) {
	if(!b) {x=1,y=0;return a;}
	int d=exgcd(b,a%b,y,x);
	y-=a/b*x;
	return d;
}
bool check(int m) {
	for(int i=1;i<=n;++i) for(int j=i+1;j<=n;++j) {
		int a=p[i]-p[j],b=m,c=s[j]-s[i],x,y;
		int d=exgcd(a,b,x,y);
		if(c%d) continue;
		a/=d,b/=d,c/=d;
		if(b<0) b=-b;
		x=(x*c%b+b)%b;
		if(x<=l[i]&&x<=l[j]) return 0;
	}
	return 1;
}
int main() {
	scanf("%d",&n);
	int mx=0;
	for(int i=1;i<=n;++i) scanf("%d%d%d",&s[i],&p[i],&l[i]),mx=std::max(mx,s[i]);
	for(int i=mx;;++i) if(check(i)) return printf("%d\n",i),0;
	return 0;
}

```

