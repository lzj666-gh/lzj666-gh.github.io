# P6003 题解

[更好的阅读体验请点这里](https://www.cnblogs.com/BrianPeng/p/12284076.html)

## 在这里解释一下二分内judge()的操作方式

首先一定是二分$x$，不必多说

但是如果真的一天天扫过去，每次judge()是$O(k)$的，明显超时

所以在judge()时会使用类似**除法分块**的方法

假设现在剩下了$r$的欠债，还剩$t$天

循环退出条件：$r\leqslant0||t==0$，这时直接通过$r\leqslant0$的成立与否判断$x$的成立与否

那么$y=\lfloor\frac{r}{x}\rfloor$

如果$y<=m$，那么直接就以$m$为每天的还债量，于是$r-=tm,t=0$

否则就计算一下会有连续多少天的每日还债量是$y$，假设这种情况持续$a$天，那么可以知道在$a-1$天之后的还债量$=y$，而$a$天之后的还债量$<y$

于是有方程$\lfloor\frac{r-(a-1)y}{x}\rfloor=y,\lfloor\frac{r-ay}{x}\rfloor<y$

改为不等式：$\frac{r-(a-1)y}{x}\geqslant y,\frac{r-ay}{x}<y$

变形：$a\leqslant\frac r y-x+1,a>\frac r y-x$

因为$a$是正整数，所以$a=\lfloor\frac r y-x+1\rfloor$

于是在之后的连续$a$天，花费都是$y$

那么就可以快速把答案“跳”出来了

**Time complexity: $O(n^\frac{1}{2}\log n)$**（后面有证明）

**Memory complexity: $O(1)$**

细节请见代码（代码中用$rm$代替$r$）

```cpp
//This program is written by Brian Peng.
#pragma GCC optimize("Ofast","inline","no-stack-protector")
#include<bits/stdc++.h>
using namespace std;
#define int long long
#define Rd(a) (a=read())
#define Gc(a) (a=getchar())
#define Pc(a) putchar(a)
int read(){
	register int x;register char c(getchar());register bool k;
	while(!isdigit(c)&&c^'-')if(Gc(c)==EOF)exit(0);
	if(c^'-')k=1,x=c&15;else k=x=0;
	while(isdigit(Gc(c)))x=(x<<1)+(x<<3)+(c&15);
	return k?x:-x;
}
void wr(register int a){
	if(a<0)Pc('-'),a=-a;
	if(a<=9)Pc(a|'0');
	else wr(a/10),Pc((a%10)|'0');
}
signed const INF(0x3f3f3f3f),NINF(0xc3c3c3c3);
long long const LINF(0x3f3f3f3f3f3f3f3fLL),LNINF(0xc3c3c3c3c3c3c3c3LL);
#define Ps Pc(' ')
#define Pe Pc('\n')
#define Frn0(i,a,b) for(register int i(a);i<(b);++i)
#define Frn1(i,a,b) for(register int i(a);i<=(b);++i)
#define Frn_(i,a,b) for(register int i(a);i>=(b);--i)
#define Mst(a,b) memset(a,b,sizeof(a))
#define File(a) freopen(a".in","r",stdin),freopen(a".out","w",stdout)
int n,k,m,l(1),r,md;
bool jdg(int x);
signed main(){
	r=Rd(n),Rd(k),Rd(m);
	while(l<=r)jdg(md=(l+r)>>1)?l=md+1:r=md-1;
	wr(l-1),exit(0);
}
bool jdg(int x){
	int y,a,rm(n),t(k);
	while(t&&rm>0){
		y=rm/x;
		if(y>m)a=min(rm/y-x+1,t),rm-=a*y,t-=a;
		else rm-=t*m,t=0;
	}
	return rm<=0;
}
```

---

## 现在是复杂度证明

每次judge()的时间消耗就是不同$y$值的数量，假设是$d$

那么最坏情况就是不同的$y$值分别是$1,2,\cdots,d$，而且每个只出现一次

那么就有$\sum_{i=1}^d i\geqslant n$，此时使$d$最小

利用等差数列求和公式：$\frac{d(d+1)}{2}\geqslant n$

当$d=\lceil (2n)^\frac{1}{2}\rceil$时就满足不等式

所以$d=O(n^\frac{1}{2})$

于是最终时间复杂度$O(d\log n)=O(n^\frac{1}{2}\log n)$，可以AC