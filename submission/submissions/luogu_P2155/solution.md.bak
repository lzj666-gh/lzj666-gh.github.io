# P2155 题解

本题在 [/discuss/show/338087](/discuss/show/338087) 加强数据前的题解有一些是错误的，具体原因下面会说明。

错误的题解存在的问题是，当 $n \ge R$ 时就直接输出 $0$，在原数据下是能 AC 的。

实际上并不是这样的，可以试试这个数据：

```plain
1 3
4 3
```

输出应该是 $2$。但是我见到的大部分题解输出都是 $0$。

为什么呢？

我们先看看这题的公式：$\displaystyle \mathrm{ans} = \frac{n!}{m!} \cdot \varphi(m!)$，其中 $\varphi(x)$ 代表 $x$ 的欧拉函数。

化简：

$$ \begin{aligned} \mathrm{ans} &= \frac{n!}{m!} \cdot \varphi(m!) \\ &= \frac{n!}{m!} \cdot m! \prod_{p \mid m!} \frac{p - 1}{p} \\ &= n! \cdot \frac{\displaystyle \prod_{p \in \mathbb{P} \mathbin{\&} p \le m} (p - 1)}{\displaystyle \prod_{p \in \mathbb{P} \mathbin{\&} p \le m} p} \end{aligned} $$

那么，我们只要处理 $\displaystyle \prod p$ 对 $R$ 的逆元吗？

错了，因为 $n!$ 中的因子 $R$ 还有可能和 $\displaystyle \prod p$ 中的 $R$ 消掉。

正解应该是对 $n \ge R$ 的 $n!$ 消去一个 $R$，对 $m \ge R$ 的 $\displaystyle \prod p$ 同时消去一个 $R$ 才对。

由于 $\displaystyle \prod p$ 中最多含有一个 $R$ 所以不需要多做消去。

代码：

```cpp
#include<cstdio>
#define F(i,a,b) for(int i=(a);i<=(b);++i)
#define F2(i,a,b) for(int i=(a);i<(b);++i)
int T,Mod,n,m;
int primes[664580], pnum=0;
bool isn_prime[10000001];
int pi[664580],inv[10000001];
int in[664580],fct[10000001];
int pos[10000001];
void init(){
	isn_prime[0]=isn_prime[1]=1;
	F(i,2,10000000){
		if(!isn_prime[i]) primes[++pnum]=i;
		for(int j=1;j<=pnum&&primes[j]*i<=10000000;++j){
			isn_prime[primes[j]*i]=1;
			if(i%primes[j]==0) break;
		}
	}
	inv[1]=1; for(int i=2;i<Mod&&i<=10000000;++i)
		inv[i]=1ll*(Mod-Mod/i)*inv[Mod%i]%Mod;
	pi[0]=1; F(i,1,pnum) pi[i]=1ll*pi[i-1]*(primes[i]-1)%Mod;
	in[0]=1; F(i,1,pnum) if(primes[i]!=Mod) in[i]=1ll*in[i-1]*inv[primes[i]%Mod]%Mod; else in[i]=in[i-1];
	fct[0]=1; F(i,1,10000000) if(i!=Mod) fct[i]=1ll*fct[i-1]*i%Mod; else fct[i]=fct[i-1];
	F(i,2,10000000) if(isn_prime[i]) pos[i]=pos[i-1]; else pos[i]=pos[i-1]+1; 
}
int main(){
	scanf("%d%d",&T,&Mod);
	init();
	while(T--){
		scanf("%d%d",&n,&m);
		if(n>=Mod&&m<Mod) puts("0");
		else printf("%d\n",1ll*fct[n]*pi[pos[m]]%Mod*in[pos[m]]%Mod);
	}
	return 0;
}
```