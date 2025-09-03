# P6835 题解

期望入门题。

这题非常的好，考察了期望的线性性质和选手的推柿子能力，给良心出题人点赞（~~然而我月赛时并没有做出来~~

注：期望的线性性质：在本题中体现为从 $x$ 点到 $y$ 点的期望步数 $E_{x\to y}=E_{x\to x+1}+...+E_{y-1 \to y}=\sum\limits_{i=x}^{y-1}E_{i\to i+1}$。

对于这类在图上随机游走的问题，我们一般会设 $E_{x\to x+1}$ 表示从 $x$ 点到 $x+1$ 点的期望步数，那么答案就是 $\sum\limits_{x=0}^n E_{x\to x+1}$ 的值。

不妨先根据期望的定义列出 $E_{x\to x+1}$ 的转移式（其中 $du_x$ 表示 $x$ 的**返祖边**的条数，而 $E$ 表示 $x$ 的**返祖边**的边集）：

$$
E_{x\to x+1}=\frac{1}{du_x+1}\times1+\frac{1}{du_x+1}\sum_{(x,y)\in E} (E_{y\to x+1}+1)
$$

将 $E_{y\to x+1}=\sum\limits_{i=y}^{x}E_{i\to i+1}$ 代入上式并对上式进行化简：

$$
E_{x\to x+1}=1+\frac{1}{du_x+1}\sum_{(x,y)\in E}\sum_{i=y}^xE_{i\to i+1}
$$

此时记 $E_{x\to x+1}$ 为 $f_x$，记 $sum_x=\sum\limits_{i=0}^x f_i$，则上式可写作：

$$
f_x=1+\frac{1}{du_x+1}\sum_{(x,y)\in E}sum_x-sum_{y-1}
$$

发现等式两边都含有 $E_{x\to x+1}$ ，把 $E_{x\to x+1}$ 全部提到左边（为了让 $f_x$ 能够转移），并消去和式系数 $\frac{1}{du_x+1}$，得：

$$
f_x=(du_x+1)+\sum_{(x,y)\in E}sum_{x-1}-sum_{y-1}
$$

到这里维护一下前缀和，就可以直接转移了。总时间复杂度为 $O(n)$。

上式的化简步骤都是一些常见的状态转移方程的 $\text{Dirty Work}$，本来不想写出来的（

**Show the Code**
```cpp
#include<cstdio>
#define int ll
typedef long long ll;
const int mod=998244353;
int cnt=0;
int h[1000005],to[2000005],ver[2000005];
int f[1000005],sum[1000005],du[1000005];
inline int read() {
	register int x=0,f=1;register char s=getchar();
	while(s>'9'||s<'0') {if(s=='-') f=-1;s=getchar();}
	while(s>='0'&&s<='9') {x=x*10+s-'0';s=getchar();}
	return x*f;
}
inline void add(int x,int y) {to[++cnt]=y;ver[cnt]=h[x];h[x]=cnt;}
signed main() {
	int id=read(),n=read(),m=read();
	for(register int i=1;i<=m;++i) {int x=read(),y=read();add(x,y);++du[x];}
	for(register int x=1;x<=n;++x) {
		f[x]=du[x]+1;
		for(register int i=h[x];i;i=ver[i]) {
			int y=to[i];
			f[x]=((f[x]+(sum[x-1]-sum[y-1])%mod)%mod+mod);
		}
		sum[x]=(sum[x-1]+f[x])%mod;
	}
	printf("%lld\n",sum[n]); 
	return 0;
}
```